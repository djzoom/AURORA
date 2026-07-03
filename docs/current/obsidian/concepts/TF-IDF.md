---
tags: [aurora, concept, llm, interview]
aliases: [TF-IDF, 词频逆文档频率, 词频-逆文档频率, Term Frequency-Inverse Document Frequency]
domain: llm
whiteboard: ★★★★
first_seen: L79
mastered: L88
---

# TF-IDF · 词频逆文档频率（Term Frequency–Inverse Document Frequency）

[[_lifecycle|← 生命周期总表]] · [[../domains/llm|← LLM 领域]] · [[../INDEX|← Master Index]]

> **⚡ 一句话（Layer 8）**：给每个词打分 = 它在这篇文章里出现得多（TF）× 在别的文章里出现得少（IDF），分高的词最能代表这篇文档。

---

## 📖 定义
TF-IDF 把文档变成一个词权重向量。**词频** `TF` = 词在本文出现次数；**逆文档频率** `IDF = log((N+1)/(df+1)) + 1`（N=文档总数，df=含该词的文档数）。两者相乘 `tfidf = TF × IDF`。检索时把查询也做成 TF-IDF 向量，用**余弦相似度**排序找最相关文档。`log` 让稀有度的价值边际递减，`+1` 平滑避免 IDF=0 或除零。

## 🤔 为什么工程师要发明它（Layer 9）
- **不用它会怎样？** 只数词频，"的、是、a、the"这类到处都有的词分数最高，完全淹没了真正有区分度的关键词。
- **它解决了什么真实问题？** IDF 惩罚"烂大街"的词、奖励稀有词，让机器像谷歌一样判断"你在找傅里叶变换而不是巴黎铁塔"——纯公式、零训练权重、结果可解释。
- **为什么不直接用向量嵌入？** TF-IDF 不需要任何预训练模型，关键词匹配够用，在 RAG 里往往比向量检索更好解释、更好调。

## ⏳ 生命周期（Layer 2 / 10）——今天难，是因为以后还会出现很多次
```
第一次露面   L79  音乐嵌入里对比 TF-IDF 式加权
正式动机     L88  只数词频会被停用词淹没
拆解原理     L88  TF × IDF，log 压扁稀有度，余弦排序
真正掌握     L88  ★ 纯 NumPy 手写 tokenize/build_tfidf/retrieve
再次使用     L89  RAG 流水线用它做检索器
再次使用     L90  agent 用它查工具/知识
最终应用     L92  完整音频问答检索层
```
👉 见自动生成的完整时间线：[[_lifecycle]]

## 🔗 依赖关系（Layer 3）——学 TF-IDF 之前你得先会
```
TF-IDF
 ├─ 需要 → [[Cosine-Similarity|余弦相似度]] / [[Dot-Product|点积]] (L10/L11)
 ├─ 需要 → [[Vector|向量表示]]              (L09)
 └─ 需要 → log 与概率直觉                   (L27)
被谁依赖 → [[RAG|检索增强生成]] · 关键词检索 · agent 工具选择
```

## ⚠️ 容易混淆（Layer 4）
| 别搞混 | 它是什么 | 一句话区分 |
|---|---|---|
| **TF-IDF vs 向量嵌入** | 稀疏关键词权重 vs 稠密语义向量 | TF-IDF 零训练、可解释；嵌入懂近义但要模型 |
| **TF vs IDF** | 本文出现多 vs 别处出现少 | TF 抬高本文热词，IDF 压低全局烂大街词 |
| **TF-IDF vs BM25** | 线性 TF vs 饱和 TF | BM25 给 TF 加饱和与长度归一，是 TF-IDF 的升级 |

## 🧑‍🏫 白板要求（Layer 6）
**★★★★（高）** — 必须做到：
- ✅ 闭卷手算一个小语料的 TF、IDF、TF-IDF 与余弦排序
- ✅ 讲清 IDF 里 `log` 和 `+1` 各自为什么存在
- ✅ 说清何时用 TF-IDF、何时该换向量检索

## 💼 面试标签（Layer 7）
`#interview` `#Google` `#OpenAI` `#Anthropic` `#Elastic` `#搜索推荐` `#NLP` `#RAG`
> 检索/搜索岗基础必问，也是 RAG 面试的第一环。

## 🌍 现实系统里它在哪发挥作用
Elasticsearch / Lucene · scikit-learn TfidfVectorizer · RAG 检索器 · 垃圾邮件过滤 · 关键词高亮

## 📚 出现于（反查）
[[../lessons/L79]] · **[[../lessons/L88]]** · [[../lessons/L89]] · [[../lessons/L90]] · [[../lessons/L92]]
