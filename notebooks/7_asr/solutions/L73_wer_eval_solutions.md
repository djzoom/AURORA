# 参考实现 — L73_wer_eval

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

`analyze_errors(hypotheses, references)` — 批量计算全局 WER 与 S/D/I 三分类比率。

沿用 L67《Edit Distance 从零实现》的记号：`WER = (S + D + I) / N`，其中
S=替换（Substitution）、D=删除（Deletion）、I=插入（Insertion）、N=参考词总数。
内层 `edit_counts` 就是词级 Levenshtein DP + 回溯：对角线走替换/匹配，
`i` 方向（hypothesis 多一词）计 I，`j` 方向（reference 多一词）计 D。

```python
def analyze_errors(hypotheses, references):
    # hypotheses: list[list[str]]  模型识别输出（词列表的列表）
    # references:  list[list[str]]  参考文本（词列表的列表）
    # 返回: dict，包含 wer / S_rate / D_rate / I_rate / worst_examples

    def edit_counts(hyp, ref):
        # 词级 Levenshtein DP：hyp 为行 i，ref 为列 j
        H, R = len(hyp), len(ref)
        dp = [[0] * (R + 1) for _ in range(H + 1)]
        for i in range(H + 1):
            dp[i][0] = i          # 删空 hyp = i 次删除
        for j in range(R + 1):
            dp[0][j] = j          # 补齐 ref = j 次插入
        for i in range(1, H + 1):
            for j in range(1, R + 1):
                if hyp[i - 1] == ref[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1],   # 替换 S
                                       dp[i - 1][j],        # 插入 I（hyp 多一词）
                                       dp[i][j - 1])        # 删除 D（ref 多一词）
        # 回溯累计 S/D/I（与本课 _edit_ops 的走向一致）
        S = D = I = 0
        i, j = H, R
        while i > 0 or j > 0:
            if i > 0 and j > 0 and hyp[i - 1] == ref[j - 1]:
                i -= 1; j -= 1                       # 匹配 C，不计错
            elif i > 0 and j > 0 and dp[i][j] == dp[i - 1][j - 1] + 1:
                S += 1; i -= 1; j -= 1               # 替换
            elif i > 0 and dp[i][j] == dp[i - 1][j] + 1:
                I += 1; i -= 1                       # hyp 多一词 → 插入
            else:
                D += 1; j -= 1                       # ref 多一词 → 删除
        return S, D, I

    total_S = total_D = total_I = total_N = 0
    per_wer = []
    for hyp, ref in zip(hypotheses, references):
        S, D, I = edit_counts(hyp, ref)
        total_S += S; total_D += D; total_I += I
        total_N += len(ref)
        per_wer.append((S + D + I) / max(len(ref), 1))   # 逐句 WER，N=0 兜底

    # WER 最高的 5 个样本（含原始索引），便于长尾定位
    order = sorted(range(len(per_wer)), key=lambda k: per_wer[k], reverse=True)
    worst = [(idx, per_wer[idx]) for idx in order[:5]]

    return {
        'wer': (total_S + total_D + total_I) / max(total_N, 1),
        'S_rate': total_S / max(total_N, 1),
        'D_rate': total_D / max(total_N, 1),
        'I_rate': total_I / max(total_N, 1),
        'worst_examples': worst,
    }
```
