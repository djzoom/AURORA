# 参考实现 — L30_softmax_crossentropy

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
e = np.exp(z - np.max(z))
return e / e.sum()
```

## 参考实现 2

```python
return -np.log(probs[true_idx])
```

