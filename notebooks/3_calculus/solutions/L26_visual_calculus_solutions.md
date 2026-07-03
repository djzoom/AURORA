# 参考实现 — L26_visual_calculus

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def central_diff(f, x, h=1e-5):
    """用中心差分近似 f 在 x 处的一阶导数。
    参数:
        f : 可调用，接受标量返回标量
        x : float，求导点
        h : float，步长（默认 1e-5）
    返回: float
    """
    return (f(x + h) - f(x - h)) / (2 * h)
```
