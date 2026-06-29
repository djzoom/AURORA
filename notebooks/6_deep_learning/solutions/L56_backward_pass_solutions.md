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

