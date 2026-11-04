# notebooks/ — a 99-lesson interactive audio-AI course

[中文版 · Chinese](README.md)

> **Language note.** The lessons themselves are currently written in **Chinese**,
> with every technical term glossed in English on first use — e.g.
> 采样（sampling）, 梅尔滤波器（mel filterbank）. The code, function names,
> docstrings, tests and the research report ([`REPORT.md`](../REPORT.md)) are in
> English. This page is an English map of the whole course so you can see what
> it covers. An English translation of the lessons is planned; contributions
> are very welcome (see [Contributing a translation](#contributing-a-translation)).

All 99 lessons are free and open source under the MIT licence — no paywall, no
"first lesson free", nothing to sign up for. See [`OPENNESS.md`](../docs/current/OPENNESS.md).

## Getting started

```bash
cd AURORA
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev,notebooks]"
python -m ipykernel install --user --name aurora --display-name "Python (AURORA)"
jupyter lab
```

Pick the `Python (AURORA)` kernel in the top-right corner. If it isn't listed, do L01 first.

## How each lesson works

Run cells one by one with `Shift+Enter`. A **✏️ TODO** cell is code for you to
write; run it, and the check cell below turns ✅ or raises an error. Every
lesson follows the same shape: a plain-language introduction → a demo → TODO
exercises → a closed-book whiteboard derivation with an answer cell → a
self-review gate. Reference solutions live in `solutions/` next to each phase,
never inside the notebooks.

Lessons marked 🎨 are visual lessons: no coding task, you build intuition by
changing parameters and watching plots.

Stuck? The [video library](../docs/current/course/VIDEO_LIBRARY.md) maps 92
YouTube lectures (Karpathy, 3Blue1Brown, Valerio Velardo, Hung-yi Lee, MIT…)
to lesson numbers L01–L99: watch the intuition lecture, then the
implementation lecture, then come back and write it yourself.

---

## The course (L01 → L99)

### 🏁 Phase 0 · Foundations  `0_foundation/`  L01–L03

| # | Lesson |
|---|---|
| L01 | What Aurora is — from a sine wave to Whisper: the six-month roadmap and why build from scratch |
| L02 | Sound as numbers — sampling, PCM arrays, your first audible sine wave |
| L03 | Spectrogram intuition — reading the three axes of a time–frequency plot before learning the FFT |

### 📐 Phase 1 · Complex numbers & trigonometry  `1_complex_trig/`  L04–L08

| # | Lesson |
|---|---|
| L04 | The three parameters of a sine — frequency sets pitch, amplitude sets loudness, phase sets the starting point |
| L05 | The geometry of complex numbers — real/imaginary → polar form; multiplication = rotation + scaling |
| L06 | Euler's formula e^{iθ} = cos θ + i sin θ — the twiddle factor at the heart of the FFT |
| L07 | Everything is a sine — building a square wave from harmonics; Fourier intuition in one picture |
| L08 🎨 | Visualising the complex plane — unit-circle rotation, conjugates and phase, animated |

### 🔢 Phase 2 · Linear algebra  `2_linear_algebra/`  L09–L21

| # | Lesson |
|---|---|
| L09 | Vector algebra — addition, scalar multiplication and linear combinations, in NumPy and geometrically |
| L10 | Dot products and projection — a·b = \|a\|\|b\| cos θ, and why similarity = dot product ÷ norms |
| L11 | Vector norms — L1 / L2 / ∞: computation, geometry and what they mean for regularisation |
| L12 | Matrix multiplication — a matrix is a linear map, multiplication is composition; a 2×2 worked by hand |
| L13 | Special matrices — orthogonal matrices preserve length, symmetric = mirror, testing positive-definiteness |
| L14 | Eigenvalues and SVD — the geometry of Ax = λx; SVD as the universal decomposition |
| L15 | Gaussian elimination — solving Ax = b, row-echelon form, when solutions exist |
| L16 | Determinants and inverses — det(A) as area scaling; inverting, and when you can't |
| L17 | Eigendecomposition A = PDP⁻¹ — changing basis turns a matrix product into scalar multiplication |
| L18 | Invertibility and rank — rank = information, null space = the directions that get crushed, diagnosing singular matrices |
| L19 🎨 | Matrix transformations illustrated — rotation, scaling and shear, animated |
| L20 🎨 | A map of decompositions — LU / QR / SVD compared geometrically |
| L21 🎨 | Matrices as filters — the DFT matrix and the mel matrix: audio processing is matrix multiplication |

### ∂ Phase 3 · Calculus  `3_calculus/`  L22–L26

| # | Lesson |
|---|---|
| L22 | Derivatives — tangent slope, the limit definition, numerical vs analytical differentiation |
| L23 | Gradients — the direction of steepest ascent; partial derivatives and the gradient vector |
| L24 | The chain rule — differentiating nested functions, the maths behind backpropagation |
| L25 | Gradient descent — fitting a line to data, from loss function to weight-update rule |
| L26 🎨 | Calculus visualised — tangents, contour lines and gradient-descent trajectories |

### 🎲 Phase 4 · Probability & statistics  `4_probability/`  L27–L31

| # | Lesson |
|---|---|
| L27 | Probability basics — events, conditional probability, independence and the law of large numbers |
| L28 | Mean, variance, standardisation — descriptive statistics, z-scores and comparing distributions |
| L29 | Common distributions — uniform, Gaussian, Bernoulli: PDF / CDF and sampling |
| L30 | Softmax and cross-entropy — the output layer and loss of a classifier, gradient derived by hand |
| L31 🎨 | Distributions visualised — PDF, CDF and the cross-entropy loss surface |

### 🔊 Phase 5 · Audio DSP  `5_audio_dsp/`  L32–L53

| # | Lesson |
|---|---|
| L32 | NumPy for signals — `np.arange` / `linspace`, building a one-second 16 kHz time axis |
| L33 | Generating a sine — `x[n] = A·sin(2πfn/sr)`, implemented and checked against `aurora.audio.sine` |
| L34 | Nyquist and aliasing — what a 6 kHz sine becomes when sampled at 8 kHz |
| L35 | Euler meets the FFT — what `e^{-2πikn/N}` is; visualising twiddle factors |
| L36 | Window functions — spectral leakage from the rectangular window; Hann / Hamming / Blackman compared |
| L37 | The brute-force DFT — `X[k] = Σ x[n] e^{-2πikn/N}`, an O(N²) double loop verified against NumPy |
| L38 | The FFT butterfly — even/odd split, `E[k] + W^k·O[k]`, from O(N²) to O(N log N) |
| L39 | Writing the FFT from scratch — recursive Cooley–Tukey, error < 1e-10 vs `numpy.fft` |
| L40 | Spectrum analysis in practice — magnitude and phase spectra, frequency resolution, a 440 Hz + 880 Hz mix |
| L41 | The windowed-FFT pipeline — signal → window → FFT → magnitude spectrum, end to end |
| L42 🎨 | The FFT drawn — butterfly diagram; spectra of a pure tone, a chord and noise |
| L43 | How the STFT works — putting timestamps on a spectrum; the time–frequency resolution trade-off |
| L44 | Writing the STFT — framing + windowing + FFT, checked against `aurora.audio.stft` |
| L45 | Making spectrograms — `magnitude_spectrogram`, `pcolormesh` heatmaps, reading a time–frequency plot |
| L46 | The mel scale — logarithmic pitch perception, mel = 2595·log₁₀(1 + f/700), triangular filters |
| L47 | Writing the mel filterbank — `mel_filterbank` from formula to NumPy, checked against the library |
| L48 🎨 | Time–frequency plots compared — linear vs mel vs log-mel spectrograms |
| L49 | The DCT-II — why it decorrelates; a pure-NumPy replacement for `scipy.fft.dct` |
| L50 | The full MFCC pipeline — signal → STFT → mel → log → DCT, checking the shape at every step |
| L51 | MFCCs on real audio — extracting features from a real WAV file, with librosa as the answer key |
| L52 | Audio Core complete — wrapping up feature engineering, the unit tests all green, assembling the evidence |
| L53 🎨 | MFCCs illustrated — waveform → spectrogram → mel spectrogram → cepstral coefficients, layer by layer |

### 🧠 Phase 6 · Deep learning  `6_deep_learning/`  L54–L65

| # | Lesson |
|---|---|
| L54 | A `Value` computation graph — scalar autodiff: forward values and backward gradients, hand-written add / mul nodes |
| L55 | Completing the operators — `__pow__`, ReLU, tanh, exp nodes; the full computation graph |
| L56 | Backpropagation by hand — the chain rule layer by layer: gradient = local gradient × upstream gradient |
| L57 | An MLP from scratch — fully connected layers, activations, the complete forward and backward pass |
| L58 | The training loop — loss, `optimizer.step`, convergence curves, fitting `make_moons` |
| L59 | PyTorch tensors — converting to and from NumPy, devices, `requires_grad` |
| L60 | How autograd works — `grad_fn` graphs, `backward()`, `retain_graph` |
| L61 | `nn.Module` in practice — Linear / ReLU / Sequential, managing parameters, saving models |
| L62 | `Dataset` and `DataLoader` — a custom `__getitem__`, batching audio data |
| L63 | An audio classifier — CNN on mel features, defining the network for Speech Commands |
| L64 | Training and evaluation — train loop + validation loop, accuracy, confusion matrix, diagnosing overfitting |
| L65 🎨 | Training visualised — loss / accuracy curves, gradient norms, weight histograms |

### 🎙️ Phase 7 · Speech recognition  `7_asr/`  L66–L75

| # | Lesson |
|---|---|
| L66 | ASR end to end — acoustic model → language model → decoder; end-to-end vs classical pipelines |
| L67 | Edit distance from scratch — Levenshtein dynamic programming, the maths of WER |
| L68 | How CTC alignment works — the blank symbol, monotonic paths and label collapsing |
| L69 | The CTC forward algorithm — summing over all paths, O(T×2L) in pure NumPy |
| L70 | Inside Whisper — log-mel input, Transformer encoder–decoder, multitask heads |
| L71 | Whisper decoding — greedy decoding and beam search, from principle to implementation |
| L72 | Fine-tuning Whisper — LoRA low-rank adapters vs full fine-tuning, adapting to Chinese / dialect data |
| L73 | Evaluating with WER — insertions / deletions / substitutions, sentence-level analysis compared with jiwer |
| L74 | ASR error analysis — substitution / deletion / insertion patterns, from a WER number to what to fix |
| L75 🎨 | The ASR pipeline drawn — waveform → spectrogram → tokens → text |

### 🎵 Phase 8 · Music understanding  `8_music/`  L76–L82

| # | Lesson |
|---|---|
| L76 | Music theory crash course — pitch, intervals, the chroma wheel and equal temperament |
| L77 | Music features — chroma, RMS energy, zero-crossing rate, implemented in `aurora.music` |
| L78 | Beat tracking from scratch — onset envelope, autocorrelation and tempo (BPM) estimation |
| L79 | Music embeddings — contrastive learning: pull similar styles together, push genres apart |
| L80 | Vector similarity search — cosine vs dot product vs L2, a pure-NumPy k-NN |
| L81 | A music recommender — user taste → embeddings → nearest neighbours → a playlist |
| L82 🎨 | Music features visualised — chromagrams, beat grids, similarity heatmaps |

### 💬 Phase 9 · LLMs & retrieval  `9_llm/`  L83–L91

| # | Lesson |
|---|---|
| L83 | A Transformer from scratch — multi-head attention + positional encoding + feed-forward |
| L84 | LoRA — W = W₀ + BA: fine-tuning a GPT-style model with 0.1 % of the parameters |
| L85 | A KV cache from scratch — updating the key/value cache, O(seq²) → O(seq) per step |
| L86 | Sampling strategies from scratch — temperature / top-k / top-p in pure NumPy |
| L87 | Quantisation and local inference — how INT8 quantisation works; lightweight inference with Hugging Face |
| L88 | TF-IDF retrieval from scratch — term frequency × inverse document frequency, vector search in NumPy |
| L89 | A complete RAG pipeline — chunking + TF-IDF retrieval + prompt construction + generation |
| L90 | Conversational RAG and a tool-using agent (ReAct) — session memory, source attribution, Thought/Action/Observation |
| L91 🎨 | Attention illustrated — multi-head attention heatmaps, the low-rank structure of LoRA |

### 🚀 Phase 10 · Integration  `10_integration/`  L92–L99

| # | Lesson |
|---|---|
| L92 | The end-to-end pipeline — microphone → ASR → LLM → text answer, assembled |
| L93 | MLOps basics — experiment tracking with W&B, model versioning, Docker packaging and deployment scripts |
| L94 | Aurora v1 demo — every capability in one showcase; assembling the evidence |
| L95 | Reading research papers — the three-pass method, paper structure, submission and collaboration |
| L96 | Whiteboard practice — deriving the DFT / FFT / attention out loud |
| L97 | Presenting your work — a 30-second summary, the GitHub evidence chain, mapping skills to a CV |
| L98 | Retrospective — six months of milestones, what worked, measuring the learning curve |
| L99 | What next — research directions, open-source contribution, the next milestone |

---

## Companion material

- Learning plan: [`docs/current/course/LEARNING_PLAN.md`](../docs/current/course/LEARNING_PLAN.md) *(Chinese)*
- Roadmap: [`ROADMAP.md`](../ROADMAP.md) *(English)*
- Bilingual glossary and knowledge graph: [`docs/current/obsidian/INDEX.md`](../docs/current/obsidian/INDEX.md)
- Per-lesson audit reports: [`docs/current/audit/INDEX.md`](../docs/current/audit/INDEX.md) *(Chinese)*
- Report a problem in a lesson: [dev@0xGarfield.com](mailto:dev@0xGarfield.com) — please include the lesson number, file name, steps to reproduce and a screenshot.

## Acceptance gate

All 99 notebooks pass the automated gate:

```bash
python scripts/validate_pipeline.py   # JSON + syntax + audio pipeline + structural checks
```

## Contributing a translation

English versions are welcome one lesson at a time. The convention:

- Put the translation next to the original as `L##_<name>.en.ipynb`.
- Translate markdown cells only; leave code cells, cell tags and the ✏️ TODO
  placeholders exactly as they are, so the acceptance gate and the answer keys
  keep working.
- Start the first markdown cell with `# Lesson N · <title>` (e.g. `# Lesson 1 · …`),
  and title the whiteboard section **Closed-book derivation** — the gate checks both.
- Keep the English glosses that already appear in the Chinese text as the
  canonical term.
- Run `python scripts/validate_pipeline.py` before opening a pull request.
