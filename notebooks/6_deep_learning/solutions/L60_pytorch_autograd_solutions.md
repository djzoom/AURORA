# 参考实现 — L60_pytorch_autograd

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def verify_gradients():
    a = torch.tensor(2.0, requires_grad=True)
    b = torch.tensor(3.0, requires_grad=True)
    L = 2 * a * b + 3 * b
    L.backward()
    da, db = a.grad.item(), b.grad.item()
    da_ref = 2 * 3.0        # dL/da = 2b = 6.0
    db_ref = 2 * 2.0 + 3.0  # dL/db = 2a + 3 = 7.0
    assert abs(da - da_ref) < 1e-6, f'dL/da 应为 {da_ref}，实际 {da}'
    assert abs(db - db_ref) < 1e-6, f'dL/db 应为 {db_ref}，实际 {db}'
    print(f'a.grad={da}, b.grad={db}')
    return da, db
```
