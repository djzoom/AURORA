# 参考实现 — L51_real_audio

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1（练习 1：10 ms 帧移，验证帧数）

```python
hop_10ms = 160  # 10 ms @ 16 kHz

coeffs_10ms = mfcc(samples, sr, n_mfcc=13, n_fft=1024,
                   hop_length=hop_10ms, n_mels=80)
print(f"hop=256 帧数: {coeffs.shape[0]}")
print(f"hop=160 帧数: {coeffs_10ms.shape[0]}  （center=True → 1 + N//hop ≈ duration/0.01）")
```

## 参考实现 2（练习 2：n_mels=40 vs 80，对比 MFCC）

```python
coeffs_mel40 = mfcc(samples, sr, n_mfcc=13, n_fft=1024, hop_length=256, n_mels=40)
coeffs_mel80 = mfcc(samples, sr, n_mfcc=13, n_fft=1024, hop_length=256, n_mels=80)

print("n_mels=40 前 3 帧:\n", coeffs_mel40[:3].round(3))
print("n_mels=80 前 3 帧:\n", coeffs_mel80[:3].round(3))

fig, axes = plt.subplots(1, 2, figsize=(12, 3.5), sharey=True)
for ax, c, n_mels in zip(axes, [coeffs_mel40, coeffs_mel80], [40, 80]):
    im = ax.imshow(c.T, aspect="auto", origin="lower", cmap="RdBu_r")
    ax.set_title(f"n_mels={n_mels}  shape={c.shape}")
    ax.set_xlabel("帧"); ax.set_ylabel("MFCC 系数")
plt.tight_layout(); plt.show()
```

## 参考实现 3（练习 3：可调基频的 V-C-V 信号）

```python
def make_vcv_f0(f0: float = 220, sr: int = 16000) -> np.ndarray:
    """合成与 make_vcv_signal 相同结构的 V-C-V，但元音 /a/ 基频可调。"""
    t_a = np.arange(int(0.4 * sr)) / sr
    vowel_a = sum(
        (1.0 / k) * np.sin(2 * np.pi * f0 * k * t_a)   # 基频 120 → 参数 f0
        for k in range(1, 9)
    )
    vowel_a /= np.max(np.abs(vowel_a)) + 1e-9

    n_burst = int(0.1 * sr)
    burst = np.random.default_rng(42).standard_normal(n_burst) * 0.3

    t_i = np.arange(int(0.5 * sr)) / sr
    harmonic_weights = [1.0, 0.4, 0.8, 0.2, 0.6, 0.1, 0.5, 0.15]
    vowel_i = sum(
        w * np.sin(2 * np.pi * 150 * k * t_i)
        for k, w in enumerate(harmonic_weights, start=1)
    )
    vowel_i /= np.max(np.abs(vowel_i)) + 1e-9

    return np.concatenate([vowel_a, burst, vowel_i])
```

信号总时长 0.4 + 0.1 + 0.5 = 1.0 s 不变，所以 MFCC 形状与原始 `coeffs` 一致；
频谱图上元音 /a/ 段的谐波条纹间距从 ~120 Hz 变为 ~220 Hz（整体上移）。
