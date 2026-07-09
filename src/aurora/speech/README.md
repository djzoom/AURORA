# Speech Core

> **Status:** partially implemented. `metrics.py` provides edit distance, WER,
> and corpus-level WER; the broader ASR stack lives in the course notebooks and
> roadmap.

Automatic speech recognition. The current learning track covers edit distance,
CTC, Whisper architecture, decoding, WER, and error analysis (L66–L75). The
next stages are Whisper fine-tuning and streaming (real-time) ASR with chunked,
causal attention.

**Principle:** no API wrappers — build / train / run the models here.
See the top-level [`ROADMAP.md`](../../../ROADMAP.md) for the timeline.
