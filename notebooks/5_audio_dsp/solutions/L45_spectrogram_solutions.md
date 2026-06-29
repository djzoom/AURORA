# 参考实现 — L45_spectrogram

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def plot_spectrogram(x, sr, win_len=1024, hop=256):
    S = stft(x, n_fft=win_len, hop_length=hop)       # (n_frames, F)
    A = np.abs(S).T                                    # (F, n_frames)
    dB = 20 * np.log10(A + 1e-8)
    dur = len(x) / sr

    fig, ax = plt.subplots(figsize=(10, 4))
    im = ax.imshow(
        dB,
        origin="lower",
        aspect="auto",
        extent=[0, dur, 0, sr / 2],
        cmap="inferno",
    )
    fig.colorbar(im, ax=ax, label="幅度 (dB)")
    ax.set_xlabel("时间 (s)")
    ax.set_ylabel("频率 (Hz)")
    ax.set_title("频谱图 (dB 幅度)")
    plt.tight_layout()
    plt.show()
```

