# 参考实现 — L89_rag_pipeline

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1 — `chunk_text` 滑动窗口切片

```python
def chunk_text(text: str, max_words: int = 80, overlap: int = 10) -> list:
    """将长文本切成有重叠的词块。"""
    words = text.split()
    if len(words) <= max_words:
        return [text]
    step = max_words - overlap          # 每次前进 step 个词，保留 overlap 个重叠
    chunks = []
    for i in range(0, len(words), step):
        chunks.append(" ".join(words[i:i + max_words]))
        if i + max_words >= len(words):  # 已覆盖到结尾，停止
            break
    return chunks
```

**要点**
- `step = max_words - overlap`：相邻块共享 `overlap` 个词，防止关键信息被切断在边界。
- 200 词、`max_words=80`、`overlap=10` → `step=70` → 窗口起点 0/70/140 → 3 个块，最后一块 60 词，每块 ≤ 80。
- 短文本（≤ `max_words`）在函数开头直接返回 `[text]`，单块。

## 参考实现 2 — `format_rag_prompt` 提示词模板

```python
def format_rag_prompt(query: str, retrieved_docs: list) -> str:
    """将检索到的段落填入提示词模板。

    Expected output format:
    Context:
    [1] <first retrieved passage>
    [2] <second retrieved passage>

    Question: <query>

    Answer:
    """
    context = "\n".join(
        f"[{i + 1}] {doc}" for i, (doc, score) in enumerate(retrieved_docs)
    )
    return f"Context:\n{context}\n\nQuestion: {query}\n\nAnswer:"
```

**要点**
- `retrieved_docs` 是 `[(doc_str, score), ...]`，解包时忽略 `score`，只取文档正文。
- `[{i+1}]` 编号让 LLM 能够引用来源；固定的 `Answer:` 结尾提示 LLM 从哪里开始生成。
- 输出以 `Context:` 起、`Answer:` 收，结构稳定，便于下游解析与来源归因。

## 闭卷推导参考 — RAG 数据流图

| 步骤 | 操作 | 输入 | 输出 |
|------|------|------|------|
| 1 | Chunking | 原始文档 (str) | `List[str]`（块列表） |
| 2 | TF-IDF 索引构建 | `List[str]` | TF-IDF 矩阵 `(n_chunks, vocab)` + 词表 vocab |
| 3 | Query 向量化 | 用户问题 (str) | 稀疏 query 向量 `(vocab,)` |
| 4 | Cosine 检索 | query 向量 + TF-IDF 矩阵 | Top-k 文档块 `[(doc, score), ...]` |
| 5 | Prompt 构建 | 问题 + Top-k 块 | prompt (str) |
| 6 | LLM 生成 | prompt (str) | 回答 (str) |

**为什么 TF-IDF 检索不需要 embedding 模型？**
TF-IDF 把每篇文档表示成"词频 × 逆文档频率"的稀疏向量，向量的维度就是词表大小，值由**统计计数**直接算出——没有可训练参数，不需要 GPU、不需要预训练。检索时对 query 做同样的向量化，再用余弦相似度排序即可。对"FFT""Nyquist"这类术语精确匹配的技术文档，关键词命中已足够好，因此整个检索栈可以完全离线、纯 NumPy 运行。
