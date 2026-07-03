---
tags: [aurora, concept, deep-learning, interview]
aliases: [CNN, 卷积神经网络, Convolutional Neural Network, ConvNet, Conv2d]
domain: deep-learning
whiteboard: ★★★
first_seen: L59
mastered: L63
---

# CNN · 卷积神经网络（Convolutional Neural Network）

[[_lifecycle|← 生命周期总表]] · [[../domains/deep-learning|← Deep Learning 领域]] · [[../INDEX|← Master Index]]

> **⚡ 一句话（Layer 8）**：用一个小窗口在图上滑动、到处套同一套权重，就能自动学出"边缘、纹理、图案"——处理频谱图和图像的利器。

---

## 📖 定义
卷积神经网络是**以卷积层为核心的神经网络**。卷积层用一组小尺寸的卷积核（kernel）在输入特征图上滑动，每个位置做局部加权求和，得到新的特征图。关键性质是**权重共享**（同一个核扫全图）和**局部连接**（只看邻域），大幅减少参数并带来平移不变性。配合池化下采样、堆叠多层后接 [[MLP]] 分类头。在 Aurora 里，输入是 mel 频谱图 `(B, 1, n_mels, T)`，输出关键词类别的 logit。

## 🤔 为什么工程师要发明它（Layer 9）
- **不用它会怎样？** 用全连接层处理一张 `40×32` 的频谱图，第一层就要几万个权重，参数爆炸还学不到局部结构。
- **它解决了什么真实问题？** 频谱图上"某个频段出现某种能量图案"是局部、可平移的特征——卷积核天然适配，参数少、泛化好。
- Aurora 里 L63 把 DSP 特征（mel）和深度模型第一次打通：CNN 直接"看图听懂"关键词。

## ⏳ 生命周期（Layer 2 / 10）——今天难，是因为以后还会出现很多次
```
第一次露面   L59  Tensor 学 unsqueeze，为 Conv2d 补 channel 维
正式动机     L62  KWS Dataset 把音频做成 (n_mels, T) 特征图
拆解原理     L63  定义 KeywordCNN：Conv2d → 池化 → MLP 头
真正掌握     L63  ★ 算清各层输出形状与参数量
再次使用     L64  训练评估、混淆矩阵、过拟合诊断
再次使用     L70  Whisper 编码器前端的 conv stem
最终应用     L79  音乐 embedding 的卷积特征提取
```
👉 见自动生成的完整时间线：[[_lifecycle]]

## 🔗 依赖关系（Layer 3）——学 CNN 之前你得先会
```
CNN
 ├─ 需要 → [[Convolution|卷积运算]]        (滑窗加权求和)
 ├─ 需要 → [[MLP]]                          (分类头 + 反向传播)
 ├─ 需要 → [[Mel]]（mel 频谱图）           (L46/L47, 输入特征)
 └─ 需要 → [[Tensor|张量]]                  (L59, B,C,H,W 布局)
被谁依赖 → [[Whisper]]（conv stem） · 音乐 embedding
```

## ⚠️ 容易混淆（Layer 4）
| 别搞混 | 它是什么 | 一句话区分 |
|---|---|---|
| **MLP** | 全连接 | CNN **共享卷积核 + 局部连接**，参数远少于 MLP |
| **卷积（DSP）** | 信号卷积 | 数学同源，但 CNN 的核是**学出来的**，不是固定滤波器 |
| **RNN/Transformer** | 建模序列依赖 | CNN 靠**局部感受野**堆叠扩大视野，不显式建长程依赖 |

## 🧑‍🏫 白板要求（Layer 6）
**★★★（理解 + 应用）** — 必须做到：
- ✅ 讲清权重共享 / 局部连接 / 平移不变性三大动机
- ✅ 算卷积输出尺寸 `out = (in - k + 2p)/s + 1`
- ✅ 说明为什么频谱图适合用 CNN（局部图案 + 可平移）

## 💼 面试标签（Layer 7）
`#interview` `#Google` `#Meta` `#NVIDIA` `#Apple-Audio` `#DeepLearning`
> 音频关键词检测（KWS）、声学事件分类的标准骨架。

## 🌍 现实系统里它在哪发挥作用
语音唤醒词检测（"Hey Siri"） · Whisper 编码器 conv 前端 · 声学事件/环境声分类 · 音乐流派识别

## 📚 出现于（反查）
[[../lessons/L59]] · [[../lessons/L62]] · **[[../lessons/L63]]** · [[../lessons/L64]] · [[../lessons/L70]] · [[../lessons/L79]]
