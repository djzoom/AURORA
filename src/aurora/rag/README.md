# RAG

> **Status:** planned. Part of the Aurora architecture.

The current retrieval primitives live in `aurora.llm.retrieve`: pure NumPy
TF-IDF indexing, cosine similarity, and lightweight document lookup.

This package is the future home for higher-level retrieval orchestration:
chunking, citation, answer synthesis, and application-specific adapters once
the course moves beyond notebook demos.

**Principle:** no API wrappers — build / train / run the models here.
See the top-level [`ROADMAP.md`](../../../ROADMAP.md) for the timeline.
