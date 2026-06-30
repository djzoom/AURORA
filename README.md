# AURORA

**Audio Understanding, Reasoning and Orchestration Research Architecture**

A from-scratch audio-AI research system spanning DSP, speech recognition,
speech synthesis, music intelligence, LLMs, retrieval, agents, realtime
inference, and MLOps.

> **Guiding principle — no API wrappers.** Aurora is not "Whisper API + OpenAI
> API + ElevenLabs + Next.js." Every core is built to demonstrate
> first-principles understanding: the DSP layer is hand-written, the speech and
> music models are trained, the inference is run locally. The goal is a
> portfolio that reads as *Senior Research Engineer*, not *API integrator*.

---

## What it does

A user uploads **speech, music, video, or a podcast**, and Aurora can:

> understand · analyze · transcribe · summarize · retrieve · generate · converse · recommend · synthesize

It is, in spirit, a fusion of **OpenAI Voice + Spotify + NotebookLM Audio +
Suno + Apple Siri**.

## Why this project

It exercises the entire stack interviewers at audio/voice/music AI teams
actually probe: **DSP · ML · Speech · Music · LLM · RAG · Agents · System
Design · Cloud · Research.**

---

## System architecture

```
Aurora
├── aurora.audio      FFT / STFT / Mel / MFCC / WAV — fully implemented ✅
├── aurora.llm        KV-Cache / sampling / TF-IDF / RAG — implemented  ✅
├── aurora.music      features / similarity / embed — implemented        ✅
├── aurora.speech     metrics (WER) — partial; ASR training planned      ▷
├── aurora.realtime   mic → ASR → LLM → TTS pipeline — planned          ▢
└── aurora.mlops      Docker / W&B / CI — planned                       ▢
```

See [`ROADMAP.md`](ROADMAP.md) for the full six-month plan.

---

## Audio Core (implemented)

The foundation. Everything is written from first principles and validated
against reference implementations — **no librosa, no SciPy DSP.**

| Primitive | Module | Notes |
|---|---|---|
| DFT / FFT / IFFT | `aurora.audio.transforms` | iterative radix-2 Cooley-Tukey, validated against `numpy.fft` |
| Windows | `aurora.audio.windows` | Hann / Hamming / Blackman, periodic & symmetric |
| STFT & spectrograms | `aurora.audio.stft` | framing, magnitude & power |
| Mel scale & filterbank | `aurora.audio.mel` | HTK mel, triangular filters, log-mel (dB) |
| MFCC & DCT-II | `aurora.audio.mfcc` | orthonormal DCT from scratch |
| WAV I/O & generators | `aurora.audio.io` | PCM WAV read/write, sine/chirp |

### Quick start

```bash
pip install -e ".[dev]"
pytest                      # 38 tests, FFT validated against numpy
python scripts/demo_audio.py
```

```python
from aurora.audio import sine, mfcc, mel_spectrogram

x = sine(440.0, duration=1.0, sample_rate=16000)
M = mel_spectrogram(x, sample_rate=16000, n_mels=80)   # (frames, 80)
C = mfcc(x, sample_rate=16000, n_mfcc=13)              # (frames, 13)
```

---

## Learning track (`notebooks/`)

99 interactive lessons, L01 → L99, taking the full project from scratch through
10 phases: foundation → trig/complex → linear algebra → calculus → probability
→ audio DSP → deep learning → ASR → music → LLM/RAG → integration.

Each lesson: read the explanation, fill in the `✏️ TODO`, watch the `✅`
checker pass. See [`notebooks/README.md`](notebooks/README.md) for the full
course map and [`docs/current/course/LEARNING_PLAN.md`](docs/current/course/LEARNING_PLAN.md)
for the week-by-week study plan.

```bash
pip install -e ".[notebooks]" && jupyter lab   # start at notebooks/0_foundation/L01_motivation.ipynb
```

All 99 notebooks pass `python scripts/validate_pipeline.py` (JSON integrity +
Python syntax + audio pipeline shape assertions).

## Repository layout

```
src/aurora/              # the package, one sub-package per core
tests/                   # pytest suite (DSP validated against numpy)
notebooks/               # 99-lesson interactive course (L01–L99)
docs/current/            # active audit, standards, course materials
docs/current/audit/      # per-lesson audit + professor review
docs/archive/            # historical snapshots
scripts/                 # runnable demos and validation tools
.github/workflows/       # CI
```

## Development

```bash
make install                        # editable install with dev deps
make test                           # run pytest
make lint                           # ruff
make format                         # black
python scripts/validate_pipeline.py # notebook acceptance gate (JSON + syntax + pipeline)
```

## License

MIT — see [`LICENSE`](LICENSE).
