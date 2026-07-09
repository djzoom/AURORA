# Music Core

> **Status:** implemented. `features.py` (chromagram, onset, beat tracking) and
> `similarity.py` (cosine k-NN) are built; `embed.py` adds an optional
> torch-based music embedding stack for the notebook course.

Music intelligence for the current course path: feature extraction, song
embeddings, and recommendation (L76–L82). MusicGen fine-tuning is still a
roadmap stretch goal, not part of the present notebook sequence.

**Principle:** no API wrappers — build / train / run the models here.
See the top-level [`ROADMAP.md`](../../../ROADMAP.md) for the timeline.
