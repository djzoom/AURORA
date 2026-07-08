# 琳达 — L71 学习日志

## 我理解了什么（简要）

学到了自回归解码的两种选择：**贪婪解码**（每步选最可能的词，速度快但可能陷入"局部最优"）和**Beam Search**（同时跟踪多条候选路线，最后选分数最高的，质量更好但花计算）。通过玩具语言模型看到了代码框架：对每个生成步骤用神经网络的输出（logits）算概率，然后从里面选token。

## 遇到的困难和问题

### 【理解】Cell L71-0552：softmax里为什么要减 logits.max()?
```python
def softmax(logits):
    x = logits - logits.max()    # ← 为什么要这一步？
    e = np.exp(x)
    return e / e.sum()
```
这个减法没有讲清楚。我觉得softmax就是"概率 = e^logits / 和"，为什么要先减掉最大值？这样会改变结果吗？是不是为了某种"数值稳定"的高级技巧，我查不出来。希望课程能说一句：这是为了防止大数字的 exp 溢出。

### 【理解】Cell L71-0552：fake_lm 里 sum(context) % 137 是什么黑魔法？
```python
rng = np.random.RandomState(sum(context) % 137)
logits = rng.randn(VOCAB_SIZE)
```
为什么要把上文的所有token值加起来，然后模137？这样做是想让"相同的上文得到相同的logits"吗？137这个数字是哪来的？看起来像是"凑出来的素数"，但没人解释。希望课程说清这个"确定性伪随机种子"的原理和目的。

### 【理解】Cell L71-0556 & L71-0557：Beam Search的"宽度×宽度"候选到底是几个？
任务2说"width×width 候选"，但伪代码里写的是：
```python
for token_id in range(VOCAB_SIZE):  # ← 不是 range(width) 吗？
    new_score = score + np.log(probs[token_id] + 1e-12)
    candidates.append((new_score, tokens + [token_id]))
```
应该是**width×VOCAB_SIZE**（width条beam，每条扩展全部词表）才对吧？"width×width"这个说法让我困惑了，怕理解错了算法。希望澄清这个数字。

### 【理解】Cell L71-0557：为什么 log-prob 加 1e-12 防止 log(0)，没有更详细的解释？
```python
new_score = score + np.log(probs[token_id] + 1e-12)  # ← 1e-12 是什么？
```
白板挑战问4只给了"浮点下溢"的数值例子（0.1^100 ≈ 0），但没解释：
- 为什么softmax的输出可能包含0？（我算的softmax总和=1，不该有0啊）
- 1e-12 这个数字是怎么选的？太大或太小会怎样？
希望补充：什么情况下probs会有接近0的值，以及如何安全地处理log(接近0的数)。

### 【实践】Cell L71-0557：Beam Search 的最优性保证是啥？
验证代码说"beam search log-prob ≥ greedy log-prob（最优性保证）"。我想了想：beam一次性考虑W×V个候选，而贪婪只看argmax，所以beam的最高分肯定 ≥ 贪婪的分。但没想清这个"最优性"是不是全局最优（所有可能序列里）还是只是"比贪婪更优"。希望课程澄清。
