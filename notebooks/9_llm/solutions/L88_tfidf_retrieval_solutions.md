# 参考实现 — L88_tfidf_retrieval

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1 — `tokenize`

```python
def tokenize(text: str) -> list:
    """简单 tokenizer：提取小写 ASCII 单词。"""
    return re.findall(r"[a-z]+", text.lower())
```

## 参考实现 2 — `build_tfidf`

```python
def build_tfidf(docs: list) -> tuple:
    """构建 TF-IDF 矩阵。返回 (matrix, vocab)。"""
    tokenized = [tokenize(d) for d in docs]
    all_terms = sorted({t for tokens in tokenized for t in tokens})
    word_idx = {w: i for i, w in enumerate(all_terms)}

    # (1) TF 矩阵：TF(t,d) = count(t,d) / |d|
    tf = np.zeros((len(docs), len(all_terms)), dtype=np.float32)
    for i, tokens in enumerate(tokenized):
        counts = Counter(tokens)
        total = max(len(tokens), 1)
        for word, count in counts.items():
            if word in word_idx:
                tf[i, word_idx[word]] = count / total

    # (2) IDF 向量：IDF(t) = log((N+1)/(df(t)+1)) + 1
    df = (tf > 0).sum(axis=0).astype(np.float32)   # df(t) = 含词 t 的文档数
    N = len(docs)
    idf = np.log((N + 1.0) / (df + 1.0)) + 1.0     # 平滑 IDF

    # (3) TF × IDF（广播 (n_docs, V) × (V,)）
    return (tf * idf), all_terms
```

## 参考实现 3 — `cosine_retrieve`

```python
def cosine_retrieve(query: str, tfidf_matrix, vocab: list, docs: list, top_k=3) -> list:
    """余弦相似度检索，返回 (doc, score) 列表。"""
    word_idx = {w: i for i, w in enumerate(vocab)}
    tokens = tokenize(query)
    counts = Counter(tokens)
    total = max(len(tokens), 1)

    # (1) 查询向量 q（TF，不乘 IDF）；词不在词表中直接忽略
    q_vec = np.zeros(len(vocab), dtype=np.float32)
    for word, count in counts.items():
        if word in word_idx:
            q_vec[word_idx[word]] = count / total

    # (2)+(3) 点积 + 余弦归一化（零向量得 0 分）
    q_norm = float(np.linalg.norm(q_vec))
    if q_norm < 1e-8:
        return [(docs[i], 0.0) for i in range(min(top_k, len(docs)))]
    d_norms = np.maximum(np.linalg.norm(tfidf_matrix, axis=1), 1e-8).astype(np.float32)
    scores = (tfidf_matrix @ q_vec) / (d_norms * q_norm)

    # (4) top_k：按得分降序返回 [(doc, score), ...]
    k = min(top_k, len(docs))
    idx = np.argsort(scores)[::-1][:k]
    return [(docs[i], float(scores[i])) for i in idx]
```

> 与 `aurora.llm.retrieve` 对齐：TF = 相对词频，IDF 用平滑公式 `log((N+1)/(df+1))+1`，
> 查询向量只用 TF（不乘 IDF），余弦分母为零时得分记 0。数值与生产实现 `atol=1e-5` 一致。

## 参考实现 4 — 闭卷推导（TF-IDF 手算）

文档：D0 `"the cat run"`，D1 `"the dog run run"`，D2 `"cat cat dog"`；词表 `{cat, dog, run, the}`。

1. **df（含该词的文档数）**
   - cat：D0、D2 → df=2
   - dog：D1、D2 → df=2
   - run：D0、D1 → df=2
   - the：D0、D1 → df=2

2. **IDF** = `log((3+1)/(2+1)) + 1` = `log(4/3) + 1` ≈ `0.2877 + 1` = **1.2877**（四个词相同，因 df 都是 2）

3. **D1 的 TF 向量**（D1 有 4 个词：the, dog, run, run）
   按 sorted 词表 `[cat, dog, run, the]`：
   `[0, 1/4, 2/4, 1/4]` = `[0, 0.25, 0.50, 0.25]`

4. **D1 的 TF-IDF 向量** = TF × 1.2877
   `[0, 0.3219, 0.6438, 0.3219]`

5. **查询 "cat run" 余弦相似度最高的文档？**
   查询 TF `q = [0.5, 0, 0.5, 0]`（IDF 全相等，不影响排序，可直接比 TF 方向）。
   - cos(q, D0) ≈ 0.816　（D0 同时含 cat 和 run）
   - cos(q, D2) ≈ 0.632
   - cos(q, D1) ≈ 0.577
   → **D0 最相似**，因为它同时命中查询里的两个词 cat 和 run。
