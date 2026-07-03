# 参考实现 — L76_music_theory

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def midi_to_freq(midi: float) -> float:
    """MIDI 编号 → 频率 Hz。A4=69=440Hz。"""
    # f(n) = 440 × 2^((n-69)/12)
    return FREQ_A4 * 2 ** ((midi - MIDI_A4) / 12)

def freq_to_midi(freq: float) -> float:
    """频率 Hz → 浮点 MIDI 编号。"""
    # 逆公式：n = 69 + 12 × log2(f / 440)
    return MIDI_A4 + 12 * np.log2(freq / FREQ_A4)
```

## 参考实现 2

```python
def chroma_from_freq(freq: float) -> int:
    """频率 Hz → 音高类别 0-11 (C=0, C#=1, ..., B=11)。"""
    # 用 freq_to_midi 换算后 round() 取整，再取 mod 12。
    # ⚠️ 必须用 round() 而非 int()：B4=493.88Hz → midi≈70.9999，
    #    int() 会截断成 70 (A#)，round() 得 71 (B) 才正确。
    n = round(freq_to_midi(freq))
    return n % 12
```
