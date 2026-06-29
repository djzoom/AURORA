---
tags: [aurora, glossary, probability, statistics]
modules: [4_probability]
created: 2026-06-27
---

# Domain: Probability & Statistics

[[../INDEX|← Index]] | [[calculus|Calculus]] | [[deep-learning|Deep Learning →]]

Terms drawn from module 4 (Probability, L27–L31).

---

## 概率基础

### 大数定律 (Law of Large Numbers)
- **英文全称**: Law of Large Numbers
- **缩写**: LLN
- **定义**: 重复实验次数趋向无穷时，样本频率依概率收敛到理论概率值的统计定理
- **出现课程**: L27, L29, L31
- **标注状态**: ❌ 缺失标注

### 条件概率 (Conditional Probability)
- **英文全称**: Conditional Probability
- **缩写**: 无
- **定义**: 在已知事件 B 发生的条件下事件 A 发生的概率，记为 P(A|B)
- **出现课程**: L27
- **标注状态**: ❌ 缺失标注

### 独立性 (Statistical Independence)
- **英文全称**: Statistical Independence
- **缩写**: 无
- **定义**: 两事件互不影响，即 P(A∩B) = P(A)·P(B) 的概率关系
- **出现课程**: L27
- **标注状态**: ❌ 缺失标注

### 频率 (Relative Frequency)
- **英文全称**: Relative Frequency
- **缩写**: 无
- **定义**: 随机实验中某事件发生次数与总实验次数之比，大样本下趋近理论概率
- **出现课程**: L27, L28, L31
- **标注状态**: ❌ 缺失标注

### 样本 (Sample)
- **英文全称**: Sample
- **缩写**: 无
- **定义**: 从总体中随机抽取的观测值集合
- **出现课程**: L27, L28, L29, L30, L31
- **标注状态**: ❌ 缺失标注

### 采样 (Sampling)
- **英文全称**: Sampling
- **缩写**: 无
- **定义**: 从概率分布中抽取随机观测值的操作，batch 采样和模型加噪均依赖此操作
- **出现课程**: L27, L29
- **标注状态**: ❌ 缺失标注

### 随机数发生器 (Random Number Generator)
- **英文全称**: Random Number Generator
- **缩写**: RNG
- **定义**: 产生伪随机数序列的算法对象，固定 seed 后输出可复现，numpy 实现为 default_rng
- **出现课程**: L27
- **标注状态**: ❌ 缺失标注

### 数据增强 (Data Augmentation)
- **英文全称**: Data Augmentation
- **缩写**: DA
- **定义**: 对训练数据进行随机变换以扩充样本多样性、减少过拟合的技术
- **出现课程**: L27
- **标注状态**: ❌ 缺失标注

### 掩码 (Mask)
- **英文全称**: Mask
- **缩写**: 无
- **定义**: 用于遮蔽或选择特定元素的二值张量，dropout 和注意力机制均使用此概念
- **出现课程**: L27
- **标注状态**: ❌ 缺失标注

---

## 描述统计

### 均值 (Mean)
- **英文全称**: Mean
- **缩写**: μ
- **定义**: 数据的算术平均值，衡量分布的中心位置
- **出现课程**: L27, L28, L29, L31
- **标注状态**: ❌ 缺失标注

### 方差 (Variance)
- **英文全称**: Variance
- **缩写**: σ²
- **定义**: 数据偏离均值的平方期望，衡量分布的离散程度
- **出现课程**: L28, L29, L31
- **标注状态**: ❌ 缺失标注

### 标准差 (Standard Deviation)
- **英文全称**: Standard Deviation
- **缩写**: SD / σ
- **定义**: 方差的平方根，与原数据量纲相同的离散度量，正态分布中控制曲线宽窄
- **出现课程**: L27, L28, L29, L31
- **标注状态**: ❌ 缺失标注

### 描述性统计 (Descriptive Statistics)
- **英文全称**: Descriptive Statistics
- **缩写**: 无
- **定义**: 用均值、方差、中位数等指标对数据集进行汇总描述的统计方法
- **出现课程**: L28
- **标注状态**: ❌ 缺失标注

### 标准化 (Standardization)
- **英文全称**: Standardization
- **缩写**: z-score
- **定义**: 对数据减均值除标准差，使结果均值为 0、标准差为 1 的变换，即 z-score 变换
- **出现课程**: L28, L30, L31
- **标注状态**: ✅ 已标注（首次标注于 L28）

### 归一化 (Normalization)
- **英文全称**: Normalization
- **缩写**: 无
- **定义**: 将数据缩放至固定范围或使之满足特定约束（如概率和为 1）的变换
- **出现课程**: L28, L29, L30
- **标注状态**: ❌ 缺失标注

### 梯度爆炸 (Gradient Explosion)
- **英文全称**: Gradient Explosion
- **缩写**: 无
- **定义**: 神经网络反向传播时梯度数值变得极大，导致权重更新失控的现象
- **出现课程**: L28
- **标注状态**: ❌ 缺失标注

### 梯度消失 (Vanishing Gradient)
- **英文全称**: Vanishing Gradient
- **缩写**: 无
- **定义**: 神经网络反向传播时梯度接近零，导致底层参数几乎无法更新的现象
- **出现课程**: L28
- **标注状态**: ❌ 缺失标注

### 梯度 (Gradient)
- **英文全称**: Gradient
- **缩写**: 无
- **定义**: 损失函数对模型参数的偏导数向量，指示参数更新的方向和大小
- **出现课程**: L28, L30, L31
- **标注状态**: ❌ 缺失标注

### 频段 (Frequency Band)
- **英文全称**: Frequency Band
- **缩写**: 无
- **定义**: 频谱中一定频率范围内的能量带，mel 滤波器组中每个滤波器对应一个频段
- **出现课程**: L28
- **标注状态**: ❌ 缺失标注

### 分类器 (Classifier)
- **英文全称**: Classifier
- **缩写**: 无
- **定义**: 将输入映射到离散类别标签的模型，最后一层通常接 softmax 输出概率
- **出现课程**: L28, L30
- **标注状态**: ❌ 缺失标注

---

## 概率分布

### 概率分布 (Probability Distribution)
- **英文全称**: Probability Distribution
- **缩写**: 无
- **定义**: 描述随机变量取各值的概率规律的数学函数
- **出现课程**: L01, L29, L30, L31
- **标注状态**: ❌ 缺失标注

### 均匀分布 (Uniform Distribution)
- **英文全称**: Uniform Distribution
- **缩写**: 无
- **定义**: 在给定区间内各点概率密度相等的连续概率分布
- **出现课程**: L29, L31
- **标注状态**: ❌ 缺失标注

### 正态分布 (Normal Distribution)
- **英文全称**: Normal Distribution / Gaussian Distribution
- **缩写**: 无
- **定义**: 由均值 μ 和标准差 σ 确定的钟形对称连续概率分布，亦称高斯分布
- **出现课程**: L29, L31
- **标注状态**: ❌ 缺失标注

### 伯努利分布 (Bernoulli Distribution)
- **英文全称**: Bernoulli Distribution
- **缩写**: 无
- **定义**: 描述单次二值（成功/失败）随机试验结果的离散概率分布
- **出现课程**: L29
- **标注状态**: ❌ 缺失标注

### 概率密度函数 (PDF)
- **英文全称**: Probability Density Function
- **缩写**: PDF
- **定义**: 连续随机变量在各点处的概率密度，积分等于 1 的非负函数
- **出现课程**: L29
- **标注状态**: ⚠️ 部分标注（L29 标题中以 PDF 缩写出现）

### 累积分布函数 (CDF)
- **英文全称**: Cumulative Distribution Function
- **缩写**: CDF
- **定义**: 随机变量取值不超过某点的概率，即 PDF 的积分
- **出现课程**: L29
- **标注状态**: ⚠️ 部分标注（L29 标题和代码均以 CDF 缩写出现）

### 中心极限定理 (CLT)
- **英文全称**: Central Limit Theorem
- **缩写**: CLT
- **定义**: 大量独立同分布随机变量之和的分布趋向正态分布的统计定理
- **出现课程**: L29
- **标注状态**: ❌ 缺失标注

### 权重初始化 (Weight Initialization)
- **英文全称**: Weight Initialization
- **缩写**: 无
- **定义**: 神经网络训练前为各层参数设置初始值的方法，如 Xavier/He 初始化
- **出现课程**: L29
- **标注状态**: ⚠️ 部分标注（L29 以括号注明了 Xavier/He 具体方案但未给出英文术语本身）

### 隐变量 (Latent Variable)
- **英文全称**: Latent Variable
- **缩写**: 无
- **定义**: 生成模型中用于表示潜在结构的未观测随机变量，VAE 中隐变量先验为 N(0,1)
- **出现课程**: L29
- **标注状态**: ❌ 缺失标注

### 先验 (Prior)
- **英文全称**: Prior
- **缩写**: 无
- **定义**: 贝叶斯推断中在观测数据之前对参数分布的假设，VAE 中为标准正态 N(0,1)
- **出现课程**: L29
- **标注状态**: ❌ 缺失标注

### 扩散模型 (Diffusion Model)
- **英文全称**: Diffusion Model
- **缩写**: 无
- **定义**: 通过逐步叠加和去除高斯噪声来生成数据的生成模型
- **出现课程**: L29
- **标注状态**: ❌ 缺失标注

### KL散度 (KL Divergence)
- **英文全称**: KL Divergence / Kullback-Leibler divergence
- **缩写**: KL
- **定义**: 衡量两个概率分布差异的非对称度量；t-SNE 的优化目标，衡量高维邻域概率分布 P 与低维 Student-t 分布 Q 之间的差异
- **出现课程**: L29
- **标注状态**: ⚠️ 部分标注（KL 为缩写，散度 divergence 部分未注释英文）

---

## Softmax 与损失

### 交叉熵 (Cross Entropy)
- **英文全称**: Cross Entropy
- **缩写**: CE
- **定义**: 衡量预测概率分布与真实标签分布差异的损失函数，计算为负对数似然：-log(p_true)
- **出现课程**: L01, L30, L31
- **标注状态**: ❌ 缺失标注

### 损失函数 (Loss Function)
- **英文全称**: Loss Function
- **缩写**: 无
- **定义**: 衡量模型预测与真实值之间差距的标量函数，训练时通过梯度下降被最小化
- **出现课程**: L30
- **标注状态**: ❌ 缺失标注

### 分类头 (Classification Head)
- **英文全称**: Classification Head
- **缩写**: 无
- **定义**: 神经网络最后一层将特征向量映射为各类别分数的线性层，输出接 softmax
- **出现课程**: L31
- **标注状态**: ❌ 缺失标注

### 温度 (Temperature)
- **英文全称**: Temperature
- **缩写**: T
- **定义**: softmax 中控制概率分布集中程度的缩放参数，T 越小输出越集中，T 越大越均匀
- **出现课程**: L31
- **标注状态**: ⚠️ 部分标注（首次标注于 L31）

### 知识蒸馏 (Knowledge Distillation)
- **英文全称**: Knowledge Distillation
- **缩写**: KD
- **定义**: 用大模型（教师）的软标签指导小模型（学生）训练的迁移学习方法，常调节 temperature 参数
- **出现课程**: L31
- **标注状态**: ❌ 缺失标注

### 可视化 (Visualization)
- **英文全称**: Visualization
- **缩写**: 无
- **定义**: 将数学对象或数据分布用图形方式直观展示的技术手段
- **出现课程**: L31
- **标注状态**: ❌ 缺失标注
