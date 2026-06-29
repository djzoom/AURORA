# 参考实现 — L64_kws_train_eval

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def train_epoch(model, loader, optimizer, criterion):
    model.train()
    total_loss = 0.0
    for x, y in loader:
        optimizer.zero_grad()
        out = model(x)
        loss = criterion(out, y)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    return total_loss / len(loader)
```

## 参考实现 2

```python
def eval_accuracy(model, loader):
    """在 loader 上评估分类准确率。"""
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for x, y in loader:
            out = model(x)
            preds = out.argmax(dim=1)
            correct += (preds == y).sum().item()
            total += y.size(0)
    return correct / total
```

