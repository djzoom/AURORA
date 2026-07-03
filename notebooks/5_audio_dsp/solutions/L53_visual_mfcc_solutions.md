# 参考实现 — L53_visual_mfcc

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1（DCT 重构误差）

```python
# 1. 截断系数（notebook 已给出）
dct_truncated = dct_todo.copy()
dct_truncated[:, N_KEEP:] = 0.0

# 2. 构建 DCT-II 正交基矩阵 B 并做逆变换
#    B[k, n] = scale[k] * cos(pi/N * (n+0.5) * k)，与 aurora dct_ii 的基一致；
#    ortho 缩放后 B @ B.T = I，因此逆变换就是右乘 B（行正交 → B 的行即逆基）。
N = N_MELS
k_arr = np.arange(N)
n_arr = np.arange(N)
B = np.cos(np.pi / N * np.outer(k_arr, n_arr + 0.5))      # (N, N)
scale = np.full(N, np.sqrt(2.0 / N))
scale[0] = np.sqrt(1.0 / N)
B = scale[:, None] * B

log_mel_recon = dct_truncated @ B                          # (n_frames, N_MELS)

# 3. RMS 误差
rms_error = np.sqrt(np.mean((log_mel_recon - log_mel_todo) ** 2))
print(f'重构 RMS 误差：{rms_error:.2f} dB')
assert rms_error < 8.0, f'误差 {rms_error:.2f} dB 超出预期（应 < 8 dB）'
print('✅ 截取 13 维重构误差在可接受范围内')
```

原理：`dct_ii` 计算 `Y = X @ B.T`（`B` 为 ortho 归一化 DCT 矩阵，`B @ B.T = I`），
所以 `X = Y @ B`。截断高阶系数后再右乘 `B`，得到的就是"只用前 13 维信息"的近似
log-Mel；chirp 信号频谱较丰富，参考实现的 RMS 误差约 6.1 dB（< 8 dB 阈值）。
