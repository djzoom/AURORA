# 参考实现 — L90_agent

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def podcast_qa(question, rag_index, chunks, embed_fn, llm, history=None):
    if history is None:
        history = []

    # 步骤 1：裁剪历史
    history = truncate_history(history, max_turns=5)

    # 步骤 2：检索最相关片段
    context_chunks = retrieve(question, rag_index, chunks, embed_fn, top_k=3)

    # 步骤 3：组装 prompt
    prompt = build_prompt(context_chunks, history, question)

    # 步骤 4：调用 LLM
    answer = llm.generate(prompt)

    # 步骤 5：格式化来源并返回
    sources = format_sources(context_chunks)
    return answer, sources
```

