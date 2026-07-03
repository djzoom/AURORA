# 参考实现 — L56_backward_pass

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def backward(self):
    topo = []
    visited = set()
    def build(v):
        if v not in visited:
            visited.add(v)
            for child in v._prev:
                build(child)
            topo.append(v)
    build(self)
    self.grad = 1.0
    for node in reversed(topo):
        node._backward()
```


## 参考实现 2 · 闭卷推导格：2 层 MLP 反向传播矩阵公式（三个 TODO 行）

```python
dL_dW2 = dL_dyhat @ a1.T                    # ∂L/∂W² = (ŷ-y) · a¹ᵀ（外积）
delta1 = (W2.T @ dL_dyhat) * dsigmoid(z1)   # δ¹ = W²ᵀ(ŷ-y) ⊙ σ'(z¹)（Hadamard 积）
dL_dW1 = delta1 @ x.T                       # ∂L/∂W¹ = δ¹ · xᵀ（外积）
```

## 参考实现 3 · 推导练习：两层 relu 网络的手推梯度

```python
# loss = ((W2 @ relu(W1 @ x)) - y)²，令 h = relu(W1 @ x)
dL_dW2 = np.outer(2*(yhat - y), h)          # ∂loss/∂W2 = 2(ŷ-y) · hᵀ
dL_dh  = W2.T @ (2*(yhat - y))              # 回传到 h
dL_dW1 = np.outer(dL_dh * (W1 @ x > 0), x)  # 过 relu 掩码后与 x 外积
```
