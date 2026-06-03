# AURORA — Six-Month Roadmap

The objective: in six months, hold an evidence chain — not a single app — that
demonstrates Senior Research Engineer potential to interviewers at audio/voice/
music AI teams. Every milestone produces a **working artifact**, a **blog
post**, and (where relevant) a **reproduced paper**.

## Anti-pattern

This is explicitly **not** an API-wrapper project. The following does **not**
count: `Whisper API + OpenAI API + ElevenLabs + Next.js`. No model, no
training, no DSP, no systems — that has near-zero interview value.

---

## Month 1 — Audio Core  ·  *Audio Analysis Engine*
- [x] FFT / DFT / IFFT from scratch (radix-2 Cooley-Tukey), validated vs numpy
- [x] Windows (Hann/Hamming/Blackman), STFT, magnitude & power spectrograms
- [x] Mel scale + triangular filterbank, log-mel, MFCC (own DCT-II)
- [x] WAV I/O from scratch, signal generators, test suite, CI
- [ ] Spectrogram visualization CLI + blog: "Writing the FFT from scratch"
- [ ] PyTorch fundamentals warm-up

## Month 2 — Speech Core  ·  *Realtime Caption Engine*
- [ ] Whisper-small fine-tune on LibriSpeech
- [ ] Conformer ASR encoder (from scratch where instructive)
- [ ] Streaming ASR with chunked / causal attention
- [ ] WER evaluation harness

## Month 3 — TTS Core  ·  *Voice Studio*
- [ ] FastSpeech2 / VITS training loop
- [ ] Voice cloning on a personal voice dataset
- [ ] Vocoder + alignment, MOS-style eval (not an ElevenLabs call)

## Month 4 — Music Core  ·  *Music Intelligence Engine*
- [ ] Music embedding model (song → vector), à la Spotify
- [ ] Recommendation: user likes → neighbors → recommendations
- [ ] MusicGen fine-tune; "Run Baby Run" and "Sleep" generators

## Month 5 — LLM + RAG + Agent  ·  *Podcast Intelligence Engine*
- [ ] Local inference: Llama / Qwen / Mistral (no GPT API)
- [ ] Transformer/attention internals, LoRA fine-tuning, RLHF basics
- [ ] RAG over Bible / audiobooks / music theory / podcasts (FAISS → Qdrant)
- [ ] Podcast Agent

## Month 6 — Realtime + Cloud + MLOps  ·  *Aurora v1*
- [ ] Realtime agent: mic → ASR → LLM → TTS, end-to-end **< 500 ms**
- [ ] Docker, Kubernetes, CI/CD, MLflow, Weights & Biases, monitoring
- [ ] Aurora v1 deployed; live demos

---

## Research Core (parallel, all six months)
Reproduce one paper per week — target **24 papers**, each with code, an
experiment, and a write-up. Directions: **Whisper, AudioLM, MusicLM, VALL-E,
SoundStorm, VoiceBox**.

## Final deliverables
- Active GitHub history with a real commit trail
- 50+ technical blog posts
- 20+ reproduced papers
- 100+ real users
- Full stack: Docker · AWS · GPU · CI/CD · monitoring
- Live demos: realtime voice assistant · voice cloning · music recommendation ·
  music generation · podcast generation · multimodal analysis

## Status legend
`[x]` done · `[ ]` todo · `▢` core not yet started
