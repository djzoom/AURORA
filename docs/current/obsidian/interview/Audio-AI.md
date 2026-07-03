---
tags: [aurora, interview, MOC]
---

# 🎧 Audio AI 面试冲刺图 (Interview Sprint Map)

[[../INDEX|← Master Index]]

> 按「白板要求」优先级排的面试冲刺清单（自动生成自 concept 页）。
> ★★★★★ = 面试必须闭卷推导 + 手写代码；先啃这些。

## ★★★★★ 必推导（最高优先，先啃）

| 概念 | 一句话 | 首次→掌握 | 相关公司 |
|---|---|---|---|
| [[../concepts/CTC\|CTC]] | 语音有 100 帧、答案只有 5 个字，没人标注哪个字对哪一帧——CTC 用"空白符 + 去重 + 对所有可能对齐求和"让模型自己学会对齐。 | [[L66]]→[[L69]] | #OpenAI #Google #Meta #NVIDIA #ElevenLabs |
| [[../concepts/Edit-Distance\|Edit-Distance]] | 把一个词改成另一个词，最少要几步"插入 / 删除 / 替换"——这个最少步数就是编辑距离，也是衡量"听错了多少"的尺子。 | [[L66]]→[[L67]] | #OpenAI #Google #Meta #ElevenLabs |
| [[../concepts/DCT\|DCT]] | 用一组固定的余弦波把一堆"你说了两遍"的相关数字重新洗牌，把有用信息挤到前几个、后面几乎归零——像不用训练的 PCA。 | [[L49]]→[[L49]] | #Google #Meta #Apple-Audio #NVIDIA |
| [[../concepts/DFT\|DFT]] | 一个频率一个频率地"审问"信号——问它"你里面有多少这个频率的成分"，把时间信号翻译成频率清单。 | [[L35]]→[[L37]] | #OpenAI #Google #Meta #Apple-Audio #NVIDIA #ElevenLabs |
| [[../concepts/FFT\|FFT]] | 把一个信号"拆成一堆正弦波"，本来要算 N² 次，FFT 用分治只要 N·log N 次——快到能实时处理声音。 | [[L35]]→[[L39]] | #OpenAI #Google #Meta #Apple-Audio #NVIDIA #ElevenLabs |
| [[../concepts/MFCC\|MFCC]] | 把一帧声音浓缩成十几个数字，既保留"这是什么音"的关键信息，又扔掉重复和噪声——经典语音特征。 | [[L50]]→[[L50]] | #OpenAI #Google #Meta #Apple-Audio #NVIDIA #ElevenLabs |
| [[../concepts/Mel\|Mel]] | 人耳听音高是按"翻倍"（对数）来的，不是按"加多少赫兹"，Mel 尺度就把这种听感拉直成一把等间距的尺子。 | [[L46]]→[[L47]] | #OpenAI #Google #Meta #Apple-Audio #NVIDIA #ElevenLabs |
| [[../concepts/STFT\|STFT]] | 把长声音切成一帧一帧的小片，每片单独做一次 [[FFT]]，就得到"什么频率、在第几秒出现"的时频图。 | [[L43]]→[[L44]] | #OpenAI #Google #Meta #Apple-Audio #NVIDIA #ElevenLabs |
| [[../concepts/Chain-Rule\|Chain-Rule]] | 函数套函数的求导规则——每穿过一层，就乘上那一层的斜率；一条乘法链，就是整个深度学习能训练的秘密。 | [[L24]]→[[L24]] | #OpenAI #Google #DeepMind #Meta #NVIDIA |
| [[../concepts/Autograd\|Autograd]] | 你只管写正向计算，系统在背后偷偷记下"每个数是怎么算出来的"，形成一张图；等你喊一声 `.backward()`，梯度就自动沿图回传。 | [[L54]]→[[L56]] | #OpenAI #Google #Meta #NVIDIA #Anthropic |
| [[../concepts/Backpropagation\|Backpropagation]] | 把梯度想成从输出口往回灌的水——每个节点收到上游水量，乘上自己这段管子的本地斜率，再往下游分；一趟走完，每个参数的梯度就都填好了。 | [[L54]]→[[L56]] | #OpenAI #Google #DeepMind #Meta #NVIDIA #Anthropic |
| [[../concepts/KV-Cache\|KV-Cache]] | 自回归生成时把每个已算过词的 K、V 存起来，生成下一个词就不用把整段历史重算一遍——总计算量从 O(seq²) 降到 O(seq)。 | [[L85]]→[[L85]] | #OpenAI #Meta #NVIDIA #Anthropic |
| [[../concepts/LoRA\|LoRA]] | 微调大模型时不去改那张巨大的原权重，只在旁边贴一对小小的低秩矩阵 `B·A` 来学新东西——可训练参数省掉 97~99%。 | [[L72]]→[[L84]] | #OpenAI #Meta #NVIDIA #Anthropic #ElevenLabs #HuggingFace |
| [[../concepts/RAG\|RAG]] | 让大模型回答前先去外部知识库检索相关片段、塞进提示词，用真实资料兜底——补上模型不知道的事，压住"一本正经胡编"。 | [[L88]]→[[L89]] | #OpenAI #Google #Anthropic |
| [[../concepts/Sampling\|Sampling]] | 生成下一个词时不总是挑概率最高的那个——用 temperature 调随机程度、用 top-k/top-p 圈定候选范围，让输出既通顺又不呆板重复。 | [[L71]]→[[L86]] | #OpenAI #Meta #NVIDIA #Anthropic #ElevenLabs |
| [[../concepts/Self-Attention\|Self-Attention]] | 让句子里每个词一步之内直接"看到"全句任意词，用相似度决定该关注谁——这就是大模型能读懂上下文的核心机制。 | [[L70]]→[[L83]] | #OpenAI #Meta #NVIDIA #Anthropic #ElevenLabs |
| [[../concepts/Transformer\|Transformer]] | 一种完全靠注意力、彻底扔掉 RNN 的网络架构——能并行读整句话，是今天所有大模型（GPT、Claude、Whisper）的共同骨架。 | [[L70]]→[[L83]] | #OpenAI #Meta #NVIDIA #Anthropic #ElevenLabs |

## ★★★★ 必掌握

| 概念 | 一句话 | 首次→掌握 | 相关公司 |
|---|---|---|---|
| [[../concepts/Beam-Search\|Beam-Search]] | 每步只留下最好的 K 条候选句子继续往下扩展——比"每步都选最高分"更聪明，又比"枚举所有可能"便宜得多。 | [[L66]]→[[L71]] | #OpenAI #Google #Meta #ElevenLabs |
| [[../concepts/Whisper\|Whisper]] | 把声音变成 log-Mel 频谱图，喂进一个 Transformer 编码器—解码器，用特殊 token 一次搞定"识别 / 翻译 / 语种检测"多种任务——这就是能听懂 99 种语言的 Whisper。 | [[L01]]→[[L70]] | #OpenAI #Google #Meta #Apple-Audio #ElevenLabs |
| [[../concepts/Aliasing\|Aliasing]] | 采样太稀疏时，高频会"伪装"成低频——6 kHz 的音被 8 kHz 采样后听起来像 2 kHz。 | [[L33]]→[[L34]] | #Google #Apple-Audio #NVIDIA #ElevenLabs |
| [[../concepts/Spectrogram\|Spectrogram]] | 给声音拍一张"X 光片"——横轴是时间、纵轴是频率、颜色越亮代表那一刻那个频率能量越强，一眼看出声音怎么随时间变化。 | [[L03]]→[[L45]] | #OpenAI #Google #Apple-Audio #NVIDIA #ElevenLabs |
| [[../concepts/Windowing\|Windowing]] | 给截取的一段信号做"淡入淡出"，让两端平滑归零，FFT 就不会把突兀的切口误当成高频噪声。 | [[L36]]→[[L36]] | #Google #Apple-Audio #NVIDIA #ElevenLabs |
| [[../concepts/twiddle factor\|twiddle factor]] | 单位圆上的一根"秒针"——每个 `e^{-2πikn/N}` 都是转到某个角度的复数，[[DFT]] 就是用它去"问"信号在这个频率上有多少成分。 | [[L35]]→[[L35]] | #Google #Meta #Apple-Audio #NVIDIA |
| [[../concepts/Gradient\|Gradient]] | 把函数在每个方向上的坡度打包成一个向量，它指向"上坡最陡"的方向——想让损失变小，就朝它的反方向走。 | [[L23]]→[[L23]] | #OpenAI #Google #Meta #NVIDIA |
| [[../concepts/Gradient-Descent\|Gradient-Descent]] | 蒙上眼睛下山——每一步都朝当前最陡的下坡方向（负梯度）挪一小步，反复几十次，就走到谷底（损失最小）。 | [[L25]]→[[L25]] | #OpenAI #Google #Meta #NVIDIA |
| [[../concepts/Activation-Function\|Activation-Function]] | 在每层线性变换后加一个"弯一下"的非线性函数——没有它，叠再多层也只等于一层直线，网络学不会复杂形状。 | [[L55]]→[[L55]] | #OpenAI #Google #Meta #NVIDIA #ElevenLabs |
| [[../concepts/MLP\|MLP]] | 把一堆"加权求和 + 非线性"的神经元一层层叠起来，就能拟合任意复杂的函数——这就是最基础的神经网络。 | [[L54]]→[[L57]] | #OpenAI #Google #Meta #NVIDIA |
| [[../concepts/Cosine-Similarity\|Cosine-Similarity]] | 只看两个向量"方向像不像"，不管它们多长——把[[Dot-Product/点积]]除以两个[[Norm/范数]]，得到 −1~1 之间的一个数，越接近 1 越像。 | [[L10]]→[[L10]] | #OpenAI #Google #Meta |
| [[../concepts/Dot-Product\|Dot-Product]] | 把两个向量对应位置相乘再全加起来，得到**一个数**——这个数告诉你它们"方向有多一致"，是整个深度学习里出现最频繁的运算。 | [[L09]]→[[L10]] | #OpenAI #Google #Meta |
| [[../concepts/Eigendecomposition\|Eigendecomposition]] | 给矩阵找到一组"天然坐标系"（特征向量），在这个坐标系里，复杂的矩阵乘法退化成"每个方向各自乘一个数"（特征值）。 | [[L14]]→[[L17]] | #Google #Meta #NVIDIA |
| [[../concepts/Matrix-Multiplication\|Matrix-Multiplication]] | 矩阵不是"数字表格"，是一台**坐标变换机器**；矩阵乘法就是把一次次变换串起来，而每个输出元素其实只是一次[[Dot-Product/点积]]。 | [[L12]]→[[L12]] | #OpenAI #Google #Meta #NVIDIA |
| [[../concepts/Norm\|Norm]] | 给向量量一个"长度"——但量法不止一种，直线距离是 L2、街区距离是 L1、最长的那一步是 L∞，选哪把尺子取决于任务。 | [[L11]]→[[L11]] | #OpenAI #Google #Meta |
| [[../concepts/SVD\|SVD]] | 把**任意**一个矩阵按"重要性"排好序拆成一叠方向，前几个方向往往就装下了绝大部分信息——SVD 不是为了"算"，是为了**扔掉不重要的方向**。 | [[L14]]→[[L14]] | #OpenAI #Google #Meta |
| [[../concepts/Quantization\|Quantization]] | 把模型权重从 32 位小数压成 8 位整数，体积和显存直接缩到 1/4，而精度几乎不掉——这就是 7B 大模型能塞进笔记本的原因。 | [[L87]]→[[L87]] | #OpenAI #Meta #Apple #NVIDIA |
| [[../concepts/TF-IDF\|TF-IDF]] | 给每个词打分 = 它在这篇文章里出现得多（TF）× 在别的文章里出现得少（IDF），分高的词最能代表这篇文档。 | [[L79]]→[[L88]] | #OpenAI #Google #Anthropic |
| [[../concepts/Beat-Tracking\|Beat-Tracking]] | 先找出音乐里"每个音符敲下去"的时刻（onset），再用自相关看这些敲击隔多久重复一次——就能估出节拍周期和 BPM，让 AI 跟着音乐点头。 | [[L77]]→[[L78]] |  |
| [[../concepts/Chroma\|Chroma]] | 钢琴有 88 个键，但只有 12 种音（C, C#, …, B）循环出现——把每个频率的能量按这 12 类加总，就得到一首歌的"调性指纹"，12 维的色度向量。 | [[L76]]→[[L77]] |  |
| [[../concepts/Cross-Entropy\|Cross-Entropy]] | 衡量"模型猜的概率分布"离"正确答案"有多远的一把尺子——猜得越自信越对，损失越小；错得越离谱，惩罚越狠。 | [[L27]]→[[L30]] | #OpenAI #Google #Meta #NVIDIA #ElevenLabs |
| [[../concepts/Softmax\|Softmax]] | 把模型吐出的一排任意分数（可以是负数、加起来不为 1）压成一个合法概率分布——每项都在 0~1 之间、加起来正好等于 1。 | [[L29]]→[[L30]] | #OpenAI #Google #Meta #NVIDIA #ElevenLabs |

## ★★★ 理解即可

| 概念 | 一句话 | 首次→掌握 | 相关公司 |
|---|---|---|---|
| [[../concepts/WER\|WER]] | 把语音识别结果和标准答案对齐，数出替换、删除、插入几个词，除以标准答案的词数——这就是衡量 ASR 好坏的头号指标。 | [[L66]]→[[L73]] | #OpenAI #Google #Meta #ElevenLabs |
| [[../concepts/CNN\|CNN]] | 用一个小窗口在图上滑动、到处套同一套权重，就能自动学出"边缘、纹理、图案"——处理频谱图和图像的利器。 | [[L59]]→[[L63]] | #Google #Meta #Apple-Audio #NVIDIA |

