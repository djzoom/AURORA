# 参考实现 — L57_mlp

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1 · Neuron

```python
class Neuron:
    def __init__(self, nin, nonlin=True):
        self.w = [Value(random.uniform(-1, 1)) for _ in range(nin)]
        self.b = Value(0.0)
        self.nonlin = nonlin

    def __call__(self, x):
        act = sum((wi * xi for wi, xi in zip(self.w, x)), Value(0.0)) + self.b
        return act.tanh() if self.nonlin else act

    def parameters(self):
        return self.w + [self.b]

    def __repr__(self):
        kind = "Tanh" if self.nonlin else "Linear"
        return f"{kind}Neuron({len(self.w)})"
```

## 参考实现 2 · Layer

```python
class Layer:
    def __init__(self, nin, nout, **kwargs):
        self.neurons = [Neuron(nin, **kwargs) for _ in range(nout)]

    def __call__(self, x):
        outs = [n(x) for n in self.neurons]
        return outs[0] if len(outs) == 1 else outs

    def parameters(self):
        return [p for n in self.neurons for p in n.parameters()]

    def __repr__(self):
        return f"Layer([{', '.join(str(n) for n in self.neurons)}])"
```

## 参考实现 3 · MLP

```python
class MLP:
    def __init__(self, nin, nouts):
        sz = [nin] + nouts
        self.layers = [Layer(sz[i], sz[i+1], nonlin=(i != len(nouts)-1))
                       for i in range(len(nouts))]

    def __call__(self, x):
        for layer in self.layers:
            x = layer(x)
        return x if isinstance(x, list) else [x]

    def parameters(self):
        return [p for layer in self.layers for p in layer.parameters()]

    def __repr__(self):
        return f"MLP([{', '.join(str(l) for l in self.layers)}])"
```

要点：

- `MLP.__init__` 中只有最后一层 `nonlin=False`（线性输出，不截断回归值 / logit）。
- `MLP(3, [4, 4, 1])` 参数总数 = 4×(3+1) + 4×(4+1) + 1×(4+1) = 16 + 20 + 5 = **41**。
- `parameters()` 逐层拍平，训练时对每个 `Value` 执行 `p.data -= lr * p.grad`，再 `p.grad = 0.0` 清零。
