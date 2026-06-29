# 参考实现 — L60_pytorch_autograd

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def verify_gradients():
    a = torch.tensor(2.0, requires_grad=True)
    b = torch.tensor(3.0, requires_grad=True)
    L = a * b * b + a
    L.backward()
    da_torch = a.grad.item()
    db_torch = b.grad.item()
    da_ref = 3.0**2 + 1      # b^2 + 1 = 10.0（别忘了 +a 项的偏导为 1）
    db_ref = 2 * 2.0 * 3.0  # 2ab = 12.0
    print(f'torch  dL/da={da_torch:.4f}  dL/db={db_torch:.4f}')
    print(f'解析値 dL/da={da_ref:.4f}    dL/db={db_ref:.4f}')
    print(f'误差   dL/da={abs(da_torch-da_ref):.2e}  dL/db={abs(db_torch-db_ref):.2e}')
    return da_torch, db_torch
```

