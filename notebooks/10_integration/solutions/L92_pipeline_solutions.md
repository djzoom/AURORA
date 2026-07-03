# 参考实现 — L92_pipeline

> ⚠️ 请先独立完成练习，再查看参考实现。

本课以 mock 函数演示 mic → ASR → RAG → LLM 的集成模式，无需 GPU 或外部模型即可跑通。练习点集中在两处：Section 5 的参数实验（`n_trials`）与 Section 6 的思考题。

## 参考实现 1 — Section 5 参数实验：`n_trials` 改为 5

```python
# ✏️ TODO 原为 n_trials = 3，改成 5 以观察各阶段耗时的波动
n_trials = 5
all_timings = []

print(f'运行 {n_trials} 次端到端流水线...')
for i in range(n_trials):
    timings, status = simulate_pipeline()
    total = sum(timings.values())
    all_timings.append(timings)
    print(f'  试验 {i+1}: asr={timings["asr"]*1000:.0f}ms  '
          f'rag={timings["rag"]*1000:.0f}ms  '
          f'llm={timings["llm"]*1000:.0f}ms  '
          f'total={total*1000:.0f}ms')

avg = {k: np.mean([t[k] for t in all_timings]) for k in all_timings[0]}
bottleneck = max(avg, key=avg.get)
assert bottleneck == 'llm', '预期 LLM 是主要瓶颈'
```

**观察**：`simulate_pipeline` 给每阶段加了 `random.uniform` 抖动，试验轮数越多，各阶段均值越稳定；无论如何，`llm`（≈2000ms）始终是瓶颈，占总延迟约 78%（`2000 / (0 + 500 + 50 + 2000) ≈ 78%`）。轮数越多，`assert bottleneck == 'llm'` 越不易被单次抖动翻转。

## 参考实现 2 — Section 6 思考题：把 `llm_delay` 从 2.0s 降到 0.5s，总延迟降幅是多少？

```python
# 各阶段基准耗时：audio_check≈0, asr=0.5s, rag=0.05s, llm=llm_delay
def total_latency(llm_delay):
    return 0.0 + 0.5 + 0.05 + llm_delay   # 秒

t_before = total_latency(2.0)   # ≈ 2.55 s
t_after  = total_latency(0.5)   # ≈ 1.05 s
drop_pct = (t_before - t_after) / t_before * 100
print(f'{t_before*1000:.0f}ms → {t_after*1000:.0f}ms，降幅 {drop_pct:.1f}%')
# 2550ms → 1050ms，降幅 ≈ 58.8%
```

**要点**：LLM 占大头（≈78%），把它砍到 0.5s 让总延迟从 2550ms 降到约 1050ms，**降幅约 59%**。这印证了「优化要打在瓶颈上」——同样是省 1.5s，砍 LLM 的收益远大于优化 ASR/RAG。实践中降低 LLM 延迟的手段包括：更小的模型、量化（见 [L87 量化与本地推理](../../9_llm/L87_local_inference.ipynb)）、KV-Cache（见 [L85 KV-Cache 从零实现](../../9_llm/L85_kv_cache.ipynb)）、以及流式输出降低**感知**延迟（本课 Section 3）。

## 参考实现 3 — Section 4 概念题：为什么 ASR 与 RAG 可以并行，RAG 精化却不能？

```
[ASR 500ms ─────────────]   ┐ 二者无数据依赖，asyncio.gather 并发
[RAG 预热 50ms]              ┘
                 [RAG 精化 30ms]   ← 依赖 ASR 转写文本，必须串行等 ASR
                          [LLM 2000ms]  ← 依赖精化后的 context
```

**判据**：能否并行取决于**数据依赖**。ASR（音频→文本）与 RAG 预热（加载/缓存索引）互不依赖，可并发；RAG 精化查询需要 ASR 的转写文本作为 query，属真依赖，必须等 ASR 完成。并行只省下 `min(ASR, RAG预热)` 那一段（此处 RAG 预热 50ms 被 ASR 500ms 覆盖，净省约 20ms）。若未来 RAG 预热涨到 200ms，并行收益才显著——这也是为什么当前 mock 下加速比接近 1.0。

## 说明

- 本课不引入任何真实 ASR/LLM 权重：`async_asr` / `async_llm` / `mock_llm_stream` 均为 `asyncio.sleep` 占位，`simulate_pipeline` 用 `time.sleep` 模拟耗时，故整本 notebook 在纯 CPU、无网络环境下可完整跑通。
- `aurora.speech`（ASR）与 `aurora.rag`（独立检索核）尚为占位模块，届时把对应 mock 函数替换为真实实现即可；Whisper 集成模板见 Section 4 的 `HF_WHISPER_TEMPLATE`。
