# Speech Core

> **Status:** planned. Part of the Aurora architecture.

Automatic speech recognition. Stage 1: Conformer / Whisper-small fine-tune on
LibriSpeech. Stage 2: streaming (real-time) ASR with chunked, causal
attention. Core to OpenAI Voice / Anthropic Audio roles.

**Principle:** no API wrappers — build / train / run the models here.
See the top-level [`ROADMAP.md`](../../../ROADMAP.md) for the timeline.
