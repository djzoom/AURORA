"""aurora.llm.kvcache — key-value cache for autoregressive Transformer inference."""
import numpy as np


class KVCache:
    """Key-value cache that stores past K and V tensors per Transformer layer.

    Why it exists
    -------------
    In autoregressive generation, at step t we need attention over tokens 0..t.
    Without cache: recompute K,V for all past tokens at every step → O(T²) per step.
    With cache: append one new K/V slice per step → O(seq) work per step.
    Total FLOPs are the same asymptotically, but we skip ~T× redundant projections.

    Shape convention
    ----------------
    K, V tensors: (n_heads, seq_len, head_dim).
    Each call to update() appends along the seq_len axis.
    """

    def __init__(self, n_heads: int, head_dim: int, max_seq_len: int = 2048):
        self.n_heads = n_heads
        self.head_dim = head_dim
        self.max_seq_len = max_seq_len
        self._k: dict = {}  # layer_id → np.ndarray (n_heads, seq, head_dim)
        self._v: dict = {}

    def update(self, layer: int, new_k: np.ndarray, new_v: np.ndarray):
        """Append new K/V for one token and return the full cached K/V.

        Args:
            layer: integer layer index.
            new_k, new_v: (n_heads, 1, head_dim) — single new token projections.

        Returns:
            (k_full, v_full): (n_heads, seq_so_far, head_dim) tensors.
        """
        if layer not in self._k:
            self._k[layer] = new_k
            self._v[layer] = new_v
        else:
            self._k[layer] = np.concatenate([self._k[layer], new_k], axis=1)
            self._v[layer] = np.concatenate([self._v[layer], new_v], axis=1)
        return self._k[layer], self._v[layer]

    def seq_len(self) -> int:
        """Current sequence length stored in the cache."""
        if not self._k:
            return 0
        return next(iter(self._k.values())).shape[1]

    def clear(self):
        """Reset the cache (call between independent sequences)."""
        self._k.clear()
        self._v.clear()

    def flops_saved(self, d_model: int) -> int:
        """Approximate FLOPs saved vs naive recomputation at current seq length."""
        T = self.seq_len()
        # each past token's K/V projection costs 2 * d_model² FLOPs; we avoided T of them
        return 2 * T * d_model * d_model
