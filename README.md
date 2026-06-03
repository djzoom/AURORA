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
├── Audio Core        DSP from scratch: FFT, STFT, mel, MFCC          ✅ implemented
├── Speech Core       ASR (Conformer / Whisper fine-tune), streaming  ▢ planned
├── TTS Core          VITS / FastSpeech2, voice cloning               ▢ planned
├── Music Core        embeddings, recommendation, MusicGen            ▢ planned
├── LLM Core          local Llama/Qwen/Mistral, LoRA, agents          ▢ planned
├── RAG               FAISS/Qdrant knowledge system                   ▢ planned
├── Multimodal Core   audio+video: transcript, chapters, summary      ▢ planned
├── Realtime Core     mic → ASR → LLM → TTS, <500ms                    ▢ planned
├── Research Core     one paper reproduced per week                    ▢ planned
└── MLOps Core        Docker, K8s, CI/CD, MLflow, W&B                  ▢ planned
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

## Repository layout

```
src/aurora/        # the package, one sub-package per core
tests/             # pytest suite (DSP validated against numpy)
docs/              # design notes, ADRs, blog drafts
scripts/           # runnable demos
.github/workflows/ # CI
```

## Development

```bash
make install   # editable install with dev deps
make test      # run pytest
make lint      # ruff
make format    # black
```

## License

MIT — see [`LICENSE`](LICENSE).
