# 参考实现 — L71_whisper_decoding

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def greedy_decode(prompt: list, max_steps: int = MAX_STEPS, eot: int = EOT) -> list:
    """贪婪解码：每步选概率最大的 token。

    从头实现，无任何黑盒解码库。返回含 prompt 与生成 token 的完整序列。
    """
    tokens = list(prompt)                     # 1. 拷贝 prompt，不修改输入
    for _ in range(max_steps):                # 2. 最多 max_steps 步
        logits = fake_lm(tokens)              #    a. 自回归前向：以当前序列为上文
        probs = softmax(logits)               #    b. 归一化为概率分布
        next_token = int(np.argmax(probs))    #    c. 取概率最大的 token（局部最优）
        tokens.append(next_token)             #    d. 追加到序列
        if next_token == eot:                 #    e. 命中 EOT 即停
            break
    return tokens                             # 3. 到达 max_steps 未命中 EOT 也返回
```

## 参考实现 2

```python
def beam_search(
    prompt: list, width: int = 2, max_steps: int = MAX_STEPS, eot: int = EOT
) -> list:
    """简单 beam search（从头实现，无黑盒）。返回累计对数概率最高的完整序列。

    分数 = 该路径上所有 log P(token_i | 前缀) 之和（越大越好）。
    用对数相加代替概率相乘，避免长序列下溢。
    命中 EOT 的 beam 移入 completed，不再扩展（允许各 beam 在不同步终止）。
    """
    beams = [(0.0, list(prompt))]             # (累计 log-prob, token 序列)
    completed = []                            # 已终止（末尾为 EOT）的候选
    for _ in range(max_steps):
        candidates = []
        for score, tokens in beams:
            logits = fake_lm(tokens)          # 自回归前向
            probs = softmax(logits)
            for token_id in range(VOCAB_SIZE):
                new_score = score + float(np.log(probs[token_id] + 1e-12))
                candidates.append((new_score, tokens + [token_id]))
        # 全部候选按累计对数概率降序，取 top-width（剪枝）
        candidates.sort(key=lambda x: x[0], reverse=True)
        candidates = candidates[:width]
        beams = []
        for score, tokens in candidates:
            if tokens[-1] == eot:             # 命中 EOT → 收入 completed
                completed.append((score, tokens))
            else:
                beams.append((score, tokens))
        if not beams:                         # 所有存活 beam 均已终止
            break
    # 从 completed + 未终止 beams 中取分数最高者
    finalists = completed + beams
    finalists.sort(key=lambda x: x[0], reverse=True)
    return finalists[0][1]
```
