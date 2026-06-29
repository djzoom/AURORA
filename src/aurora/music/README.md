# Music Core

> **Status:** implemented. `features.py` (chromagram, onset, beat tracking) and `similarity.py` (cosine k-NN) are built.

Music intelligence: song embeddings (song -> vector, Spotify-style), a
recommendation model (likes -> neighbors -> recommendations), and MusicGen
fine-tuning for generation (e.g. 'Run Baby Run', 'Sleep').

**Principle:** no API wrappers — build / train / run the models here.
See the top-level [`ROADMAP.md`](../../../ROADMAP.md) for the timeline.
