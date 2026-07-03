# 参考实现 — L87_local_inference

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def batch_quantize_error(W: np.ndarray, bits_list: list) -> dict:
    """对比不同位宽的仿射量化误差。

    Args:
        W: float32 权重矩阵
        bits_list: 位宽列表，如 [8, 6, 4, 3, 2]

    Returns:
        {bits: {"scale": float, "mean_err": float, "max_err": float}}
    """
    x_min, x_max = W.min(), W.max()
    result = {}
    for bits in bits_list:
        levels = 2 ** bits - 1                                  # 该位宽的量化格数
        scale = (x_max - x_min) / levels                       # 每格代表的 float 步长
        W_q = np.clip(np.round((W - x_min) / scale), 0, levels)  # 量化到 [0, levels]
        W_r = W_q * scale + x_min                              # 反量化回 float32
        abs_err = np.abs(W - W_r)
        result[bits] = {
            "scale": float(scale),
            "mean_err": float(abs_err.mean()),
            "max_err": float(abs_err.max()),
        }
    return result
```

