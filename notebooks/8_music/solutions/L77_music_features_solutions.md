# 参考实现 — L77_music_features

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def chroma_vector(power_spectrum, sr, n_fft):
    n_bins = len(power_spectrum)
    freqs = np.arange(n_bins) * sr / n_fft
    chroma = np.zeros(12)
    for k, (f, p) in enumerate(zip(freqs, power_spectrum)):
        if f <= 0:
            continue
        midi = 12 * np.log2(f / 440) + 69
        pc = int(round(midi)) % 12
        chroma[pc] += p
    chroma /= (chroma.max() + 1e-8)
    return chroma
```

## 参考实现 2

```python
def rms_envelope(x, frame_len=2048, hop=512):
    n_frames = 1 + (len(x) - frame_len) // hop
    frames = np.array([x[i*hop : i*hop+frame_len] for i in range(n_frames)])
    return np.sqrt(np.mean(frames ** 2, axis=1))
```

