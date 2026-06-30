"""aurora.music.embed — from-scratch contrastive learning for music embeddings.

Public API
----------
MusicEncoder   — CNN encoder: mel spectrogram → fixed-length embedding vector
triplet_loss   — Triplet Loss: same-song pairs close, different-song pairs far
nt_xent_loss   — NT-Xent / SimCLR Loss: batch-wide contrastive objective

No external ML libraries beyond torch are used for the core math.
"""

from __future__ import annotations

try:
    import torch
    import torch.nn as nn
    import torch.nn.functional as F
except ImportError as _err:
    raise ImportError(
        "torch is required for aurora.music.embed. "
        "Install it with:  pip install 'aurora[music]'"
    ) from _err


class MusicEncoder(nn.Module):
    """CNN encoder that maps variable-length mel spectrograms to fixed-dim vectors.

    Architecture::

        Conv2d(1→16, k=3) → ReLU → MaxPool(2,2)
        Conv2d(16→32, k=3) → ReLU → AdaptiveAvgPool2d((1, n_mels//4))
        Flatten → Linear(32*(n_mels//4), embed_dim)

    The AdaptiveAvgPool2d handles variable-length time axis T, always producing
    a (B, embed_dim) output regardless of the input duration.

    Parameters
    ----------
    n_mels : int
        Number of mel bins in the input spectrogram (default 64).
    embed_dim : int
        Output embedding dimension (default 128).
    """

    def __init__(self, n_mels: int = 64, embed_dim: int = 128) -> None:
        super().__init__()
        self.cnn = nn.Sequential(
            nn.Conv2d(1, 16, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),                         # T//2, n_mels//2
            nn.Conv2d(16, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.AdaptiveAvgPool2d((1, n_mels // 4)),     # 1, n_mels//4
        )
        self.fc = nn.Linear(32 * (n_mels // 4), embed_dim)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Forward pass.

        Parameters
        ----------
        x : torch.Tensor
            Shape ``(B, 1, T, n_mels)`` — batch of mel spectrograms.

        Returns
        -------
        torch.Tensor
            Shape ``(B, embed_dim)`` — one embedding vector per clip.
        """
        h = self.cnn(x)    # (B, 32, 1, n_mels//4)
        h = h.flatten(1)   # (B, 32 * n_mels//4)
        return self.fc(h)  # (B, embed_dim)


def triplet_loss(
    anchor: torch.Tensor,
    positive: torch.Tensor,
    negative: torch.Tensor,
    margin: float = 0.2,
) -> torch.Tensor:
    """Triplet Loss for metric learning.

    Pushes ``anchor`` closer to ``positive`` (same song) and farther from
    ``negative`` (different song) by at least ``margin``.

    .. math::

        L = \\frac{1}{B} \\sum_{i} \\max(d_{pos,i} - d_{neg,i} + m,\\; 0)

    where :math:`d` is the L2 (Euclidean) distance.

    Parameters
    ----------
    anchor, positive, negative : torch.Tensor
        Shape ``(B, d)`` — one embedding per row.
    margin : float
        Safety margin :math:`m` (default 0.2).

    Returns
    -------
    torch.Tensor
        Scalar loss value.
    """
    d_pos = torch.norm(anchor - positive, dim=-1)   # (B,)
    d_neg = torch.norm(anchor - negative, dim=-1)   # (B,)
    loss = torch.clamp(d_pos - d_neg + margin, min=0.0).mean()
    return loss


def nt_xent_loss(
    z1: torch.Tensor,
    z2: torch.Tensor,
    temperature: float = 0.07,
) -> torch.Tensor:
    """NT-Xent / SimCLR Normalized Temperature-Scaled Cross-Entropy Loss.

    Each pair ``(z1[i], z2[i])`` is a positive pair (two augmented views of
    the same clip). All other ``2B - 2`` samples in the batch serve as
    negatives — including both the other ``z1`` and ``z2`` entries.

    .. math::

        L = -\\frac{1}{2B} \\sum_{i} \\log
            \\frac{\\exp(s_{i,j}/\\tau)}{\\sum_{k \\neq i} \\exp(s_{i,k}/\\tau)}

    where :math:`j` is the positive partner of :math:`i` and :math:`s` is
    cosine similarity. The inputs should already be L2-normalized.

    Parameters
    ----------
    z1, z2 : torch.Tensor
        Shape ``(B, d)`` — L2-normalized embedding pairs.
    temperature : float
        Softmax temperature :math:`\\tau` (default 0.07).

    Returns
    -------
    torch.Tensor
        Scalar loss value.
    """
    B = z1.shape[0]
    z = torch.cat([z1, z2], dim=0)          # (2B, d)
    sim = (z @ z.T) / temperature           # (2B, 2B) cosine similarities
    sim.fill_diagonal_(float("-inf"))        # exclude self-similarity
    # z1[i] positively pairs with z2[i] at index B+i, and vice versa
    labels = torch.cat([
        torch.arange(B, 2 * B),
        torch.arange(0, B),
    ]).to(z.device)
    return F.cross_entropy(sim, labels)
