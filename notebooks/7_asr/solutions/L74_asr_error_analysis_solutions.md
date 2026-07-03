# 参考实现 — L74_asr_error_analysis

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def wer(ref_str, hyp_str):
    """词错率 = (S+D+I) / |ref|，用 alignment() 统计各操作"""
    ops = alignment(ref_str, hyp_str)
    S = sum(1 for op, *_ in ops if op == 'S')  # 替换
    D = sum(1 for op, *_ in ops if op == 'D')  # 删除
    I = sum(1 for op, *_ in ops if op == 'I')  # 插入
    return (S + D + I) / len(ref_str.split())
```

