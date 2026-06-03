# Realtime Core

> **Status:** planned. Part of the Aurora architecture.

OpenAI Realtime-style loop: mic -> ASR -> LLM -> TTS -> reply, with end-to-end
latency under 500 ms.

**Principle:** no API wrappers — build / train / run the models here.
See the top-level [`ROADMAP.md`](../../../ROADMAP.md) for the timeline.
