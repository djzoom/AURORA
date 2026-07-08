现在让我以"老陈"的身份读完这个notebook，逐个cell认真理解。

我边读边做了笔记。这个L64讲的是训练循环的实现——两个关键函数 `train_epoch` 和 `eval_accuracy`，以及怎样用混淆矩阵诊断模型。

让我梳理一遍我理解了什么，以及卡住的地方。

---

# 老陈 — L64 学习日志

## 我理解了什么

1. **训练的两个函数**：`train_epoch` 返回平均损失，`eval_accuracy` 返回准确率百分比。训练时 model.train()，评估时 model.eval()，这样能检查过拟合。

2. **混淆矩阵的含义**：一个表格，纵轴是真实类别，横轴是预测类别。对角线的数字越多说明预测对了，非对角线的数字说明哪两个类容易混淆。

3. **交叉熵损失的初始值**：10分类时随机猜测，loss ≈ 2.3，这是因为每个类的概率都是 1/10，-log(0.1) ≈ 2.3。

## 遇到的困难和问题

**【理解】Softmax 是什么？从 logit 到概率的转换**  
第5节说"logit 经过 softmax 转为概率"，代码里有 `softmax(logit)[y]`，但没有解释 softmax 的具体公式和为什么这样定义。PyTorch 的 CrossEntropyLoss 自动做 softmax，那么 softmax = exp(logit)/sum(exp(logit)) 吗？为什么要用 exp() 而不是直接归一化（比如 logit/sum(logit)）？这个 exp 有什么物理意义吗？

**【理解】Train 和 Eval 模式具体怎样影响 Dropout 和 BatchNorm**  
第4节表格只说"开启 dropout/BN 训练模式"，但我不知道 Dropout 和 BatchNorm 是什么。我猜 Dropout 可能是某种随机丢弃机制，Eval 时要关掉。但为什么 BatchNorm 的 mean/var 要在 train 和 eval 时用不同的值？是不是说 train 时计算当前 batch 的平均值，eval 时用之前保存的全局平均值？为了避免过拟合？

**【理解】为什么训练集和验证集必须分离**  
第18个 cell 有个关键注释："若 val_loader 和 train_loader 使用同一份数据，验证准确率等于训练准确率，模型永远无法展示泛化间隔，过拟合诊断也就无从谈起。" 我理解"同一份数据会导致准确率相同"，但没理解什么是"泛化间隔"和"过拟合诊断"具体怎样工作。是说：如果训练集上 loss 一直下降但验证集上准确率停止增长，那就是过拟合吗？这两条曲线之间的"间隔"就是过拟合的指标吗？

**【计算】argmax(dim=1) 中的 dim=1 是什么**  
eval_accuracy 里用 `model(x).argmax(dim=1)` 取预测类别。logit 的形状是 [B, C]，B 是 batch size，C 是类别数。argmax(dim=1) 是沿着第 1 维（列）取最大值吗？但为什么最大值索引就代表预测的类别？logit 最大的那一列对应某个类，那个类号就是预测结果？

**【推演】CrossEntropyLoss 的初始值推导细节**  
说"随机初始化时期望 loss ≈ log(num_classes)"，推导假设所有 logit 都相等。但实际上随机初始化（比如高斯分布 N(0, 0.01)）真的会让所有 logit 接近相等吗？还是说这个假设只是一个粗略的估计？如果初始值不是 2.3 而是 2.0 或 2.5，对观察 loss 下降有影响吗？

---
