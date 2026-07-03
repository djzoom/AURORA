# 参考实现 — L78_beat_tracking

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

`my_onset_envelope` — 谱通量（Spectral Flux）onset 包络：相邻帧幅度谱的正差值之和。
`stft` 返回形状 `(n_frames, n_fft//2+1)`，在 `axis=0`（时间轴）做差分，`axis=1`（频率轴）求和，
因此输出长度为 `n_frames - 1`（差分少一帧），且半波整流保证非负。

```python
def my_onset_envelope(signal, sample_rate, n_fft=N_FFT, hop_length=HOP):
    """谱通量 onset 包络：相邻帧幅度谱正差值之和。"""
    S = stft(signal, n_fft=n_fft, hop_length=hop_length)  # (n_frames, n_freqs)
    mag = np.abs(S)                                        # 幅度谱
    flux = np.maximum(0.0, np.diff(mag, axis=0))          # 时间轴差分 + 半波整流
    return flux.sum(axis=1)                                # 按频率求和 → (n_frames-1,)
```

## 参考实现 2

`my_beat_track` — 用 onset 包络的自相关（autocorrelation）估计 BPM 和节拍时间。
`env`、`fps`、`min_lag`、`max_lag`、`lags` 已在 TODO 上方给出；此处补齐四步：
自相关向量 → 取峰值 lag → 换算 BPM → 以 `best_lag` 为步长回填节拍时间。

```python
def my_beat_track(signal, sample_rate, hop_length=HOP):
    """从自相关估计 BPM 和节拍时间。"""
    env = my_onset_envelope(signal, sample_rate, hop_length=hop_length)
    fps = sample_rate / hop_length

    # BPM 范围 40-240 对应的 lag 范围（单位：帧）
    min_lag = max(1, int(fps * 60 / 240))
    max_lag = min(len(env) - 1, int(fps * 60 / 40))
    lags = np.arange(min_lag, max_lag + 1)

    # 1. 自相关：env 与移位 env 的点积
    ac = np.array([np.dot(env[:len(env) - lag], env[lag:]) for lag in lags])
    # 2. 最优 lag（自相关最大处）
    best_lag = lags[np.argmax(ac)]
    # 3. 换算 BPM：BPM = 60 × fps / lag
    bpm = fps * 60.0 / best_lag
    # 4. 节拍时间（秒）：先找首拍相位，再以 best_lag 步进
    pos = np.argmax(env[:best_lag])              # 首拍帧索引
    beat_frames = np.arange(pos, len(env), best_lag)
    beats = beat_frames / fps                    # 转换为秒
    return bpm, beats
```
