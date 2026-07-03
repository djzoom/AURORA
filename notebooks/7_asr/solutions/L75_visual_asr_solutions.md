# 参考实现 — L75_visual_asr

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def my_ctc_decode(path):
    """CTC decode a path (list of str tokens) -> list of str.
    Step 1: collapse consecutive duplicates.
    Step 2: remove blanks ('-').
    """
    collapsed = [path[0]] + [path[i] for i in range(1, len(path)) if path[i] != path[i - 1]]
    return [c for c in collapsed if c != '-']
```

解释：
- **第 1 步 去连续重复**：只保留与前一个 token 不同的 token（首个 token 无条件保留）。这一步不区分是否为 blank，例如 `H H - I -` → `H - I -`。
- **第 2 步 去 blank**：过滤掉所有 `'-'`，得到最终字符序列。
- 顺序不能颠倒：先去 blank 再去重会把被 blank 隔开的重复字符（如 `I - I`）错误地合并成一个 `I`，从而丢失 `HII` 这类合法解码。
