---
tags: [aurora, concept, linear-algebra, interview]
aliases: [Cosine Similarity, 余弦相似度, 余弦, cosine, cos(a,b)]
domain: linear-algebra
whiteboard: ★★★★
first_seen: L10
mastered: L10
---

# Cosine-Similarity · 余弦相似度（Cosine Similarity）

[[_lifecycle|← 生命周期总表]] · [[../domains/linear-algebra|← Linear Algebra 领域]] · [[../INDEX|← Master Index]]

> **⚡ 一句话（Layer 8）**：只看两个向量"方向像不像"，不管它们多长——把[[Dot-Product|点积]]除以两个[[Norm|范数]]，得到 −1~1 之间的一个数，越接近 1 越像。

---

## 📖 定义
`cos(a,b) = (a·b) / (‖a‖·‖b‖) = cosθ`，θ 是两向量夹角。取值 [−1, 1]：1 = 完全同向，0 = 正交（无关），−1 = 完全反向。等价于"先把两个向量各自 L2 归一化，再做点积"。关键结论：**向量做过 L2 归一化后，点积就等于余弦相似度**。

## 🤔 为什么工程师要发明它（Layer 9）
- **不用它会怎样？** 直接用点积测相似度，一首 10 分钟的长歌能量数值天然更大——即使风格不同，点积也可能很高，判断被"长度"污染。
- **它解决了什么真实问题？** Spotify 的"你可能也喜欢"：把每首歌变成向量，只比**方向**（风格），除以范数把长度影响消掉，于是长短不同的歌也能公平比较。
- **它是检索/推荐/RAG 的默认度量。** 训练好的 embedding 通常已 L2 归一化，所以点积检索 = 余弦检索，还能用矩阵乘法批量算。

## ⏳ 生命周期（Layer 2 / 10）——今天难，是因为以后还会出现很多次
```
第一次露面   L10  随点积一起登场
正式动机     L10  长歌能量大 → 点积失真 → 要归一化
拆解原理     L10  cos=a·b/(‖a‖‖b‖) 的几何含义
真正掌握     L10  ★ 手写 cosine_similarity，白板挑战（8 分钟）
再次使用     L79  音乐 embedding 相似度
再次使用     L80  纯 NumPy k-NN 检索（大应用）
再次使用     L83  Self-Attention 打分（缩放点积）
最终应用     L89  RAG：查询与文档块的相似度检索
```
👉 见自动生成的完整时间线：[[_lifecycle]]

## 🔗 依赖关系（Layer 3）——学余弦相似度之前你得先会
```
Cosine-Similarity
 ├─ 需要 → [[Dot-Product|点积]]   (L10)
 ├─ 需要 → [[Norm|范数]]（L2）     (L11)
 └─ 需要 → cosθ 的几何直觉         (L04)
被谁依赖 → k-NN 检索 · 推荐系统 · RAG · Self-Attention
```

## ⚠️ 容易混淆（Layer 4）
| 别搞混 | 它是什么 | 一句话区分 |
|---|---|---|
| **点积** | 方向 + 长度 | 余弦**去掉长度**；L2 归一化后二者相等 |
| **L2 距离** | 空间距离 `‖a−b‖` | 余弦看**角度**，L2 看**位置**；归一化后二者单调对应 |
| **皮尔逊相关** | 去均值后的余弦 | 相关系数 = **中心化向量**的余弦相似度 |

## 🧑‍🏫 白板要求（Layer 6）
**★★★★** — L10/L80 均有白板挑战，必须做到：
- ✅ 手写 `dot(a,b)/(norm(a)*norm(b))`，讲清 [−1,1] 与三种角度
- ✅ 证明 L2 归一化后点积 = 余弦，解释检索为何用矩阵乘批量算
- ✅ 说清与 L2 距离、点积的取舍场景

## 💼 面试标签（Layer 7）
`#interview` `#Google` `#OpenAI` `#Spotify` `#Meta` `#Retrieval`
> RAG / 推荐 / 向量数据库面试的核心度量，常问"为何用余弦而非点积/L2"。

## 🌍 现实系统里它在哪发挥作用
向量数据库（FAISS/Pinecone）· RAG 检索 · 推荐系统 · 说话人/人脸验证 · 语义搜索

## 📚 出现于（反查）
**[[../lessons/L10]]** · [[../lessons/L11]] · [[../lessons/L79]] · [[../lessons/L80]] · [[../lessons/L81]] · [[../lessons/L83]] · [[../lessons/L88]] · [[../lessons/L89]]
