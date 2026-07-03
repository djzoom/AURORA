---
tags: [aurora, concept, llm, interview]
aliases: [RAG, 检索增强生成, Retrieval-Augmented Generation, 检索增强]
domain: llm
whiteboard: ★★★★★
first_seen: L88
mastered: L89
---

# RAG · 检索增强生成（Retrieval-Augmented Generation）

[[_lifecycle|← 生命周期总表]] · [[../domains/llm|← LLM 领域]] · [[../INDEX|← Master Index]]

> **⚡ 一句话（Layer 8）**：让大模型回答前先去外部知识库检索相关片段、塞进提示词，用真实资料兜底——补上模型不知道的事，压住"一本正经胡编"。

---

## 📖 定义
RAG 是"检索 + 生成"的流水线：① **切片（Chunking）** 把文档切成小段；② **检索** 用 [[TF-IDF]] 或向量嵌入找出与问题最相关的 top-k 段；③ **提示词拼装** 把检索到的上下文按模板塞进 prompt；④ **生成** 让 [[Transformer|LLM]] 基于这些资料作答。核心思想：把"记忆"外包给可更新、可溯源的知识库，模型只负责"读材料 + 组织语言"。

## 🤔 为什么工程师要发明它（Layer 9）
- **不用它会怎样？** LLM 的知识冻结在训练时刻，遇到新事实、私有文档、专业细节就会**幻觉**——自信地编造。
- **它解决了什么真实问题？** 让模型回答前先查资料，答案有出处、可更新、可引用——这正是"ChatGPT 怎么知道它本不知道的事情"的答案。
- **为什么 TF-IDF 就够用？** 关键词检索不需要嵌入模型、可解释、易调试，很多场景效果不输向量检索，是 RAG 最轻量的检索器。

## ⏳ 生命周期（Layer 2 / 10）——今天难，是因为以后还会出现很多次
```
前置铺垫     L88  TF-IDF 检索器（大海捞针）
正式动机     L89  LLM 会幻觉、知识冻结 → 先检索再生成
拆解原理     L89  切片 → 检索 → 拼提示词 → 生成
真正掌握     L89  ★ 手写 chunk_text + format_rag_prompt，闭卷画数据流
再次使用     L90  agent 把 RAG 当一个可调用工具
最终应用     L92  Aurora 音频问答完整流水线 / L94 demo
```
👉 见自动生成的完整时间线：[[_lifecycle]]

## 🔗 依赖关系（Layer 3）——学 RAG 之前你得先会
```
RAG
 ├─ 需要 → [[TF-IDF|检索器]]               (L88)
 ├─ 需要 → [[Embedding|向量嵌入]]（可选检索） (L79)
 ├─ 需要 → [[Transformer|LLM 生成]]         (L83)
 └─ 需要 → 提示词工程（模板拼装）
被谁依赖 → agent · 企业知识问答 · 音频/文档问答系统
```

## ⚠️ 容易混淆（Layer 4）
| 别搞混 | 它是什么 | 一句话区分 |
|---|---|---|
| **RAG vs 微调(LoRA)** | 外挂知识库 vs 改模型权重 | RAG 换知识不用重训，微调改的是"能力/风格" |
| **RAG vs 长上下文** | 检索相关片段 vs 全塞进窗口 | RAG 先筛后喂，省 token 且能覆盖超大知识库 |
| **RAG vs agent** | 单次检索-生成 vs 多步规划调用 | agent 可以把 RAG 当其中一个工具反复调用 |

## 🧑‍🏫 白板要求（Layer 6）
**★★★★★（最高）** — 面试高频，必须做到：
- ✅ 闭卷画出 RAG 数据流：切片 → 检索 → 拼提示词 → 生成
- ✅ 解释为什么 TF-IDF 检索不需要 embedding 模型
- ✅ 说清 RAG 何时优于微调、失败点在哪（检索召回、切片粒度）

## 💼 面试标签（Layer 7）
`#interview` `#OpenAI` `#Anthropic` `#Google` `#Perplexity` `#企业知识库` `#LLM` `#NLP`
> LLM 应用岗几乎必问，"如何让模型不幻觉"的标准答案。

## 🌍 现实系统里它在哪发挥作用
Perplexity · ChatGPT 联网/文件问答 · Claude Projects · 企业知识库助手 · 客服/法律/医疗检索问答

## 📚 出现于（反查）
[[../lessons/L88]] · **[[../lessons/L89]]** · [[../lessons/L90]] · [[../lessons/L92]] · [[../lessons/L94]]
