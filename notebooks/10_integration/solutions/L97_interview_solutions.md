# 参考实现 — L97_interview

> ⚠️ 请先独立完成练习，再查看参考实现。

本课第 5 节的动手练习是**限时手写题**：不看任何参考，5 分钟内写出 `hz_to_mel(f)`
和 `frame_signal(x, win_len, hop)`。这两道题模拟音频 AI 岗位面试里最常见的「当场写代码」
环节——考的不是记忆，而是能否把公式和数据流即刻翻译成正确的 NumPy 代码。

## 参考实现 — `hz_to_mel()`

```python
def hz_to_mel(f):
    """把线性频率 Hz 转换为 Mel 标度（HTK 公式）。"""
    return 2595 * np.log10(1 + f / 700)
```

## 参考实现 — `frame_signal()`

```python
def frame_signal(x, win_len, hop):
    """
    把 1D 信号 x 切成帧，返回 shape (n_frames, win_len) 的 2D 数组。
    """
    n_frames = 1 + (len(x) - win_len) // hop
    return np.stack([x[i * hop : i * hop + win_len] for i in range(n_frames)])
```

## 讲解

1. **`hz_to_mel` 就是 HTK 公式的直译**：`mel = 2595 · log₁₀(1 + f/700)`。因为传入的 `f`
   是 NumPy 数组，`np.log10` 会逐元素广播，一行就能同时处理 `[0, 1000, 4000]` 三个频点，
   无需显式循环。这正是 L46「Mel 频率尺度」里推导的对数感知曲线。

2. **`frame_signal` 的帧数公式**：从下标 0 开始，每隔 `hop` 取一个长度 `win_len` 的窗口，
   最后一个完整窗口的起点是 `(n_frames-1)·hop`，要满足 `(n_frames-1)·hop + win_len ≤ len(x)`，
   解得 `n_frames = 1 + (len(x) - win_len) // hop`。用整除 `//` 自动丢弃末尾凑不满一帧的样本。
   验证用例 `len=20, win_len=8, hop=4` → `1 + (20-8)//4 = 4`，形状 `(4, 8)`，与断言一致。

3. **为什么用 `np.stack` 而非预分配**：列表推导先生成 4 个 `(8,)` 视图切片，`np.stack`
   再沿新轴 0 堆成 `(4, 8)`。教学场景下这样最直观；追求零拷贝时可换成
   `np.lib.stride_tricks.sliding_window_view(x, win_len)[::hop]`，但要小心它返回的是共享内存
   的视图（面试时能主动点出这一 tradeoff 是加分项）。这与 L44「亲手写 STFT」里的分帧逻辑同源。

## 验证要点

第 5 节代码格自带断言：

```python
assert np.allclose(hz_to_mel(f_test), mel_ref, atol=0.1), "hz_to_mel 公式有误"
assert frames.shape == (4, 8), f"期望 (4,8)，得到 {frames.shape}"
```

两处断言通过后分别打印 `hz_to_mel ✅` 和 `frame_signal ✅`，整篇 notebook 即可跑到结尾。

## 延伸练习

- 补上配套的 `mel_to_hz(m)`（HTK 逆公式 `700 · (10^{m/2595} − 1)`），并验证
  `mel_to_hz(hz_to_mel(f)) ≈ f`——这是第 5 节表格里点名的另一半。
- 给 `frame_signal` 加一个 `center=True` 选项：先在两端各 pad `win_len//2`，
  让帧以样本为中心对齐，这正是 STFT 默认的 `center` 行为（见 L43/L44）。
