# AURORA — Six-Month Roadmap

The objective: in six months, hold an **evidence chain** — not a single app —
that demonstrates research-engineer fundamentals and a steep learning curve to
interviewers at audio/voice/music AI teams. Every milestone produces a
**working artifact** and a **short technical write-up**; some reproduce a paper.

> **Reality check.** Starting from a beginner foundation, six full-time months
> build a credible *junior/new-grad research-engineer* evidence chain and lay
> genuine senior-track groundwork — not a finished senior. The signal is
> **depth, not volume**: a few correct, hand-implemented, well-explained
> artifacts beat a pile of API glue. Personal study plan and daily checklists
> live in [`docs/LEARNING_PLAN.md`](docs/LEARNING_PLAN.md) and
> [`docs/week-01-checklist.md`](docs/week-01-checklist.md).

## Anti-pattern

This is explicitly **not** an API-wrapper project. The following does **not**
count: `Whisper API + OpenAI API + ElevenLabs + Next.js`. No model, no
training, no DSP, no systems — that has near-zero interview value.

---

## Phase 1 — Audio Core  ·  *Audio Analysis Engine*  `notebooks/5_audio_dsp/` L32–L53
Code is already written (`src/aurora/audio/`); the goal is to **understand it to
the point you could re-derive every line from a blank file**.
Daily detail in `docs/week-01-checklist.md` (L32–L42) and `docs/week-02-checklist.md` (L37–L42).
- [x] FFT / DFT / IFFT from scratch (radix-2 Cooley-Tukey), validated vs numpy
- [x] Windows (Hann/Hamming/Blackman), STFT, magnitude & power spectrograms
- [x] Mel scale + triangular filterbank, log-mel, MFCC (own DCT-II)
- [x] WAV I/O from scratch, signal generators, test suite, CI
- [ ] **L32–L36** Signals, sampling, complex numbers / Euler; read `io.py`, `windows.py`
- [ ] **L37–L42** Re-implement `transforms.py` from blank; blog: "Writing the FFT from scratch"
- [ ] **L43–L48** Re-implement `stft.py`/`mel.py`; spectrogram visualization CLI (real heatmaps)
- [ ] **L49–L53** MFCC/DCT; MFCC on real LibriSpeech audio (cross-checked vs librosa); add a feature

## Phase 2 — ML / Deep-Learning Foundations  ·  *First Trained Model*  `notebooks/6_deep_learning/` L54–L65
- [ ] From-scratch autograd + MLP, backprop by hand (Karpathy "Zero to Hero")  → L54–L58
- [ ] PyTorch fundamentals; CNN / RNN / attention basics  → L59–L61
- [ ] Train a keyword-spotting classifier on Speech Commands using **your own mel features**  → L62–L64
- [ ] Blog: from linear regression to backprop, in your own words

## Phase 3 — Speech Core (ASR)  ·  *Caption Engine*  `notebooks/7_asr/` L66–L75
- [ ] Edit distance from scratch (Levenshtein DP) → L67; WER evaluation harness → L73
- [ ] CTC alignment intuition + forward algorithm (pure NumPy) → L68–L69
- [ ] Whisper architecture + decoding strategies (greedy / beam search) → L70–L71
- [ ] Whisper-small fine-tune on LibriSpeech (cloud GPU) → L72
- [ ] ASR error analysis: substitution / deletion / insertion patterns → L74
- [ ] (stretch) streaming ASR with chunked / causal attention

## Phase 4 — Music Core  ·  *Music Intelligence Engine*  `notebooks/8_music/` L76–L82
- [ ] Music theory primer: pitch classes, chroma wheel, MIDI ↔ Hz → L76
- [ ] From-scratch features: chromagram, onset envelope, beat tracking (aurora.music) → L77–L78
- [ ] Music embedding model (song → vector), contrastive learning → L79
- [ ] Similarity search + recommendation: pure NumPy k-NN (no faiss) → L80–L81
- [ ] (stretch) MusicGen fine-tune

## Phase 5 — LLM + RAG + Agent  ·  *Podcast Intelligence Engine*  `notebooks/9_llm/` L83–L91
- [ ] Transformer from scratch; LoRA low-rank adaptation → L83–L84
- [ ] KV-Cache from scratch (pure NumPy) → L85; sampling strategies (top-k/top-p) → L86
- [ ] INT8 quantization from scratch; optional HuggingFace local inference → L87
- [ ] TF-IDF retrieval from scratch (no faiss, no sentence-transformers) → L88
- [ ] RAG pipeline: chunk → TF-IDF index → cosine retrieve → prompt → generate → L89
- [ ] Conversational RAG: session memory, source attribution, Podcast Q&A → L90

## Phase 6 — Integration + Cloud + MLOps  ·  *Aurora v1*  `notebooks/10_integration/` L92–L99
- [ ] Polish **one** end-to-end demo (e.g. mic → ASR → LLM response) → L92–L94
- [ ] Docker, CI/CD, Weights & Biases experiment tracking, basic monitoring → L93
- [ ] Research skills: three-pass reading, paper structure, submission & academic collaboration → L95
- [ ] Whiteboard practice + interview prep → L96–L97
- [ ] Retrospective + next steps → L98–L99
- [ ] Aurora v1 deployed; package the evidence chain for interviews

> **Deferred** (not realistic at depth in six months from a beginner start):
> TTS voice-cloning training, full realtime **< 500 ms** pipeline, large-scale
> paper reproduction. Revisit once the four cores above are solid.

---

## Research Core (parallel)
Reproduce **3-5 papers properly** — each with code, an experiment, and a
write-up — rather than skimming many. Priority: **Whisper**, then one music
paper (e.g. **MusicGen**) once the Music Core lands.

## Final deliverables (quality over count)
- Consistent GitHub history of **meaningful** commits (not commit-count farming)
- ~1-2 short technical write-ups per week — clarity over quantity
- 3-5 papers genuinely reproduced
- 4 cores at real depth: Audio · Speech · Music · LLM/RAG
- One polished live demo + Docker · cloud GPU · CI/CD · experiment tracking

## Status legend
`[x]` done · `[ ]` todo · `▢` core not yet started
