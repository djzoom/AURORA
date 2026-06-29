# 参考实现 — L68_ctc_alignment

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def ctc_greedy_decode(logits: np.ndarray, blank: int = 0) -> list:
    """CTC 贪婪解码：argmax 每帧，去相邻重复，去 blank。
    
    Args:
        logits: shape (T, vocab_size)，未经 softmax 的原始分数
        blank:  blank 符号的 token id，默认 0
    Returns:
        解码后的 token id 列表
    """
    preds = np.argmax(logits, axis=1)          # (T,)
    deduped = [int(p) for i, p in enumerate(preds)
               if i == 0 or p != preds[i - 1]] # 去相邻重复
    return [p for p in deduped if p != blank]  # 去 blank
```

