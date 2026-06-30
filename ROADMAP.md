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
> live in [`docs/current/course/LEARNING_PLAN.md`](docs/current/course/LEARNING_PLAN.md) and
> [`docs/current/course/week-01-checklist.md`](docs/current/course/week-01-checklist.md).

## Anti-pattern

This is explicitly **not** an API-wrapper project. The following does **not**
count: `Whisper API + OpenAI API + ElevenLabs + Next.js`. No model, no
training, no DSP, no systems — that has near-zero interview value.

---

## Phase 0 — Foundation + Math Prep  `notebooks/0_foundation/` + `1–4_*/` L01–L31
- [x] 99-lesson course written, audited, and corrected (all pass `validate_pipeline.py`)
- [x] All 91 content notebooks upgraded to A-/B+ (popular-science narrative + whiteboard + self-eval) — 2026-07-01
- [x] L01–L03 Foundation: Aurora motivation, sound digitisation, spectrogram intuition
- [x] L04–L08 Trig/complex: sine waves, complex numbers, Euler's formula, Fourier intuition
- [x] L09–L21 Linear algebra: vectors → matrices → SVD → visual transforms
- [x] L22–L26 Calculus: derivatives, gradients, chain rule, gradient descent
- [x] L27–L31 Probability: distributions, softmax, cross-entropy

## Phase 1 — Audio Core  ·  *Audio Analysis Engine*  `notebooks/5_audio_dsp/` L32–L53
Daily detail in [`docs/current/course/week-01-checklist.md`](docs/current/course/week-01-checklist.md).
- [x] FFT / DFT / IFFT from scratch (radix-2 Cooley-Tukey), validated vs numpy
- [x] Windows (Hann/Hamming/Blackman), STFT, magnitude & power spectrograms
- [x] Mel scale + triangular filterbank, log-mel, MFCC (own DCT-II)
- [x] WAV I/O from scratch, signal generators, test suite, CI
- [x] **L32–L53** All Audio DSP notebooks corrected and audited
- [ ] MFCC on real LibriSpeech audio (cross-checked vs librosa) — practical exercise
- [ ] Blog: "Writing the FFT from scratch"

## Phase 2 — ML / Deep-Learning Foundations  ·  *First Trained Model*  `notebooks/6_deep_learning/` L54–L65
- [x] From-scratch autograd + MLP, backprop by hand (Karpathy "Zero to Hero") → L54–L58
- [x] PyTorch fundamentals; CNN / attention basics → L59–L61
- [x] KWS Dataset + DataLoader (shape bug fixed: mel.T gives CNN-ready (40, T)) → L62
- [x] CNN keyword-spotting model defined → L63
- [ ] Train KWS classifier on Speech Commands (cloud GPU run)
- [ ] Blog: from linear regression to backprop, in your own words

## Phase 3 — Speech Core (ASR)  ·  *Caption Engine*  `notebooks/7_asr/` L66–L75
- [x] Edit distance from scratch (Levenshtein DP) → L67; WER evaluation → L73
- [x] CTC alignment intuition + forward algorithm (pure NumPy) → L68–L69
- [x] Whisper architecture + decoding strategies (greedy / beam search) → L70–L71
- [ ] Whisper-small fine-tune on LibriSpeech (cloud GPU) → L72
- [x] ASR error analysis: substitution / deletion / insertion patterns → L74
- [ ] (stretch) streaming ASR with chunked / causal attention

## Phase 4 — Music Core  ·  *Music Intelligence Engine*  `notebooks/8_music/` L76–L82
- [x] Music theory primer: pitch classes, chroma wheel, MIDI ↔ Hz → L76
- [x] From-scratch features: chromagram, onset envelope, beat tracking (aurora.music) → L77–L78
- [x] Music embedding model skeleton (MusicEncoder, triplet_loss, NT-Xent) → L79
- [x] Similarity search + recommendation: pure NumPy k-NN → L80–L81
- [ ] (stretch) MusicGen fine-tune

## Phase 5 — LLM + RAG + Agent  ·  *Podcast Intelligence Engine*  `notebooks/9_llm/` L83–L91
- [x] All 91 content notebooks upgraded to A-/B+ grade (popular-science narrative, structured task intros, whiteboard challenges, self-evals) — 2026-07-01
- [x] Transformer from scratch; LoRA low-rank adaptation → L83–L84
- [x] KV-Cache from scratch (pure NumPy) → L85; sampling strategies (top-k/top-p) → L86
- [x] INT8 quantization from scratch; HuggingFace local inference → L87
- [x] TF-IDF retrieval from scratch (no faiss, no sentence-transformers) → L88
- [x] RAG pipeline: chunk → TF-IDF index → cosine retrieve → prompt → generate → L89
- [x] Conversational RAG agent → L90

## Phase 6 — Integration + Cloud + MLOps  ·  *Aurora v1*  `notebooks/10_integration/` L92–L99
- [x] End-to-end pipeline notebook (mic → ASR → LLM) → L92
- [x] MLOps: W&B tracking, Docker, CI/CD → L93
- [x] Aurora v1 demo + evidence chain → L94
- [x] Research skills, whiteboard practice, interview prep → L95–L97
- [x] Retrospective + next steps → L98–L99
- [ ] Aurora v1 deployed to cloud; live demo URL

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
