# 参考实现 — L46_mel

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def hz_to_mel(f):
    return 2595 * np.log10(1 + np.asarray(f, dtype=float) / 700)
```

## 参考实现 2

```python
def mel_filterbank(n_mels, n_fft, sr):
    mel_min = 0.0
    mel_max = hz_to_mel(sr / 2)
    mel_points = np.linspace(mel_min, mel_max, n_mels + 2)
    hz_points = 700 * (10 ** (mel_points / 2595) - 1)
    bin_idx = np.floor((n_fft + 1) * hz_points / sr).astype(int)

    n_bins = n_fft // 2 + 1
    fb = np.zeros((n_mels, n_bins))
    for m in range(n_mels):
        lo, ctr, hi = bin_idx[m], bin_idx[m+1], bin_idx[m+2]
        for k in range(lo, ctr):
            fb[m, k] = (k - lo) / (ctr - lo) if ctr != lo else 0
        for k in range(ctr, hi):
            fb[m, k] = (hi - k) / (hi - ctr) if hi != ctr else 0
    return fb
```

