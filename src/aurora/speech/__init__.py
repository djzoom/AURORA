"""Aurora Speech Core — evaluation metrics (from scratch).

Currently provides edit distance and word error rate. ASR model training is
tracked in ROADMAP.md; the Whisper-compatible front end lives in
:mod:`aurora.audio.whisper_frontend`.
"""

from .metrics import corpus_wer, edit_distance, wer

__all__ = ["edit_distance", "wer", "corpus_wer"]
