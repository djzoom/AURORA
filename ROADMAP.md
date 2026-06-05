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

## Month 1 — Audio Core  ·  *Audio Analysis Engine*
Code is already written (`src/aurora/audio/`); the goal is to **understand it to
the point you could re-derive every line from a blank file**. Weekly detail in
`docs/week-NN-checklist.md`.
- [x] FFT / DFT / IFFT from scratch (radix-2 Cooley-Tukey), validated vs numpy
- [x] Windows (Hann/Hamming/Blackman), STFT, magnitude & power spectrograms
- [x] Mel scale + triangular filterbank, log-mel, MFCC (own DCT-II)
- [x] WAV I/O from scratch, signal generators, test suite, CI
- [ ] **W1** Signals, sampling, complex numbers / Euler; read `io.py`, `windows.py`
- [ ] **W2** Re-implement `transforms.py` from blank; blog: "Writing the FFT from scratch"
- [ ] **W3** Re-implement `stft.py`/`mel.py`; spectrogram visualization CLI (real heatmaps)
- [ ] **W4** MFCC/DCT; MFCC on real LibriSpeech audio (cross-checked vs librosa); add a feature

## Month 2 — ML / Deep-Learning Foundations  ·  *First Trained Model*
- [ ] From-scratch autograd + MLP, backprop by hand (Karpathy "Zero to Hero")
- [ ] PyTorch fundamentals; CNN / RNN / attention basics
- [ ] Train a keyword-spotting classifier on Speech Commands using **your own mel features**
- [ ] Blog: from linear regression to backprop, in your own words

## Month 3 — Speech Core (ASR)  ·  *Caption Engine*
- [ ] CTC loss + attention internals; WER evaluation harness
- [ ] Whisper-small fine-tune on LibriSpeech (cloud GPU)
- [ ] (stretch) streaming ASR with chunked / causal attention

## Month 4 — Music Core  ·  *Music Intelligence Engine*  (your strength area)
- [ ] Music embedding model (song → vector), à la Spotify
- [ ] Recommendation: user likes → neighbors → recommendations
- [ ] (stretch) MusicGen fine-tune

## Month 5 — LLM + RAG + Agent  ·  *Podcast Intelligence Engine*
- [ ] Local inference: Llama / Qwen / Mistral (no GPT API)
- [ ] Transformer/attention internals, LoRA fine-tuning
- [ ] RAG over audiobooks / music theory / podcasts (FAISS)
- [ ] Podcast Agent

## Month 6 — Integration + Cloud + MLOps  ·  *Aurora v1*
- [ ] Polish **one** end-to-end demo (e.g. mic → ASR → LLM response)
- [ ] Docker, CI/CD, Weights & Biases experiment tracking, basic monitoring
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
