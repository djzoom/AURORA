# 参考实现 — L82_visual_music

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def detect_minor_triad(chroma_frame: np.ndarray, threshold: float = 0.5) -> list[int]:
    """在一帧 chroma 向量中检测小三和弦根音。

    小三和弦相对根音 r 的音高类别为 (r, (r+3)%12, (r+7)%12)：
    根音、小三度（3 个半音）、纯五度（7 个半音）。
    某根音被判定「激活」当且仅当这三个音高的能量均超过 threshold。

    Args:
        chroma_frame: shape (12,)，各音高类别的归一化能量（0–1）。
        threshold: 能量阈值，超过该值视为「激活」。

    Returns:
        所有满足条件的根音列表（0–11），空列表表示无检测到小三和弦。
    """
    roots = []
    for r in range(12):
        third = (r + 3) % 12
        fifth = (r + 7) % 12
        if (
            chroma_frame[r] > threshold
            and chroma_frame[third] > threshold
            and chroma_frame[fifth] > threshold
        ):
            roots.append(r)
    return roots
```
