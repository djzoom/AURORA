"""Aurora Music Core — from-scratch music feature extraction and similarity search.

Public API
----------
chromagram, chroma_vector   — time-varying 12-bin chroma (aurora.audio.stft based)
rms_envelope                — per-frame RMS energy
zero_crossing_rate          — per-frame ZCR
onset_envelope              — spectral flux for beat detection
beat_track                  — BPM estimation via autocorrelation

cosine_similarity           — similarity between two vectors
pairwise_cosine             — (n,d) → (n,n) similarity matrix
knn_search / find_similar    — top-k retrieval by cosine similarity (two names, same function)

MusicEncoder                — CNN encoder: mel spectrogram → fixed-length embedding (L79)
triplet_loss                — Triplet Loss for metric learning (L79)
nt_xent_loss                — NT-Xent / SimCLR contrastive loss (L79)
"""
from aurora.music.features import (
    chromagram,
    chroma_vector,
    rms_envelope,
    zero_crossing_rate,
    onset_envelope,
    beat_track,
)
from aurora.music.similarity import cosine_similarity, pairwise_cosine, knn_search, find_similar

__all__ = [
    "chromagram",
    "chroma_vector",
    "rms_envelope",
    "zero_crossing_rate",
    "onset_envelope",
    "beat_track",
    "cosine_similarity",
    "pairwise_cosine",
    "knn_search",
    "find_similar",
]

# torch-dependent embedding API (requires pip install aurora[music])
try:
    from aurora.music.embed import MusicEncoder, triplet_loss, nt_xent_loss
    __all__ += ["MusicEncoder", "triplet_loss", "nt_xent_loss"]
except ImportError:
    pass  # torch not available; install with: pip install aurora[music]
