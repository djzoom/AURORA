# LLM Core

> **Status:** implemented. `kvcache.py`, `retrieve.py`, `sample.py` are built and usable.

Local LLM inference and adaptation — Llama / Qwen / Mistral run locally (no
GPT API). Transformer & attention internals, LoRA fine-tuning, RLHF basics.
Hosts the Podcast Agent.

**Principle:** no API wrappers — build / train / run the models here.
See the top-level [`ROADMAP.md`](../../../ROADMAP.md) for the timeline.
