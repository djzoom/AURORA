Model: `base.en` · 200 LibriSpeech test-clean utterances (1800 s of audio), greedy decoding, CPU.

| Front end | Corpus WER |
|---|---|
| Whisper's own (`torch.stft` + librosa mel) | 3.08 % |
| Aurora (`aurora.audio.log_mel_whisper`) | 3.08 % |

Identical transcripts: 200 / 200. Max feature error across all utterances: 2.90e-05 (mean of per-utterance max: 1.19e-05).
