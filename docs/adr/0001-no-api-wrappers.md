# ADR 0001 — No API wrappers; build from first principles

- **Status:** accepted
- **Date:** 2026-06-03

## Context

Aurora's purpose is to serve as an evidence chain for Senior Research Engineer
potential at audio/voice/music AI teams. A project that merely composes hosted
APIs (`Whisper API + OpenAI API + ElevenLabs + Next.js`) carries near-zero
signal in those interviews: it shows no model, no training, no DSP, no systems
design, no research.

## Decision

Every core capability is built, trained, or run locally rather than delegated
to a third-party API:

- **Audio Core:** FFT, STFT, mel filterbank, DCT, MFCC, and WAV I/O are
  hand-written. NumPy is permitted only as an array/arithmetic primitive; the
  *algorithms* are ours and are validated against `numpy.fft` and reference
  formulas in tests.
- **Speech / TTS / Music / LLM:** models are trained or fine-tuned and run with
  local inference — not called as a hosted service.
- **RAG / Realtime / Multimodal:** the retrieval, streaming, and orchestration
  logic is implemented, not outsourced.

## Consequences

- **Positive:** strong, verifiable interview signal across DSP, ML, systems and
  research; full control over performance and behavior; deep learning by doing.
- **Negative / cost:** more upfront engineering than gluing APIs; heavier
  compute (GPU) for training; correctness now requires its own test harness.
- **Mitigation:** keep the Audio Core dependency-light (numpy only) and gate
  heavy stacks (torch, transformers, faiss) behind optional-dependency extras
  so the foundation stays fast to install and test.
