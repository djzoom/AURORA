# Realtime Core

> **Status:** planned. Part of the Aurora architecture.

OpenAI Realtime-style loop: mic -> ASR -> LLM -> TTS -> reply, with end-to-end
latency under 500 ms. This is the integration target after the course's ASR,
LLM, and TTS building blocks are in place.

**Principle:** no API wrappers — build / train / run the models here.
See the top-level [`ROADMAP.md`](../../../ROADMAP.md) for the timeline.
