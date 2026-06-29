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
