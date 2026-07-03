# 参考实现 — L19_visual_multiply

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1 — classify_transform

```python
def classify_transform(A, tol=1e-9):
    """返回 'rotation' | 'reflection' | 'scaling' | 'shear'"""
    A = np.asarray(A, float)
    d = np.linalg.det(A)
    # 正交矩阵：AᵀA = I（保长度、保角度）→ 旋转或反射，由 det 符号区分
    if np.allclose(A.T @ A, np.eye(A.shape[0]), atol=tol):
        return 'rotation' if d > 0 else 'reflection'
    # 非正交：对角阵 = 各轴独立缩放；否则为剪切
    if np.allclose(A, np.diag(np.diag(A)), atol=tol):
        return 'scaling'
    return 'shear'
```
