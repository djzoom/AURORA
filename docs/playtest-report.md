# 10岁儿童视角通关测试报告（数学能力尚可版）

测试对象：`/Users/z/AURORA/notebooks/` 下全部 33 个 notebook。

测试方式：我故意扮演一个注意力稀缺、数学理解能力尚可、但编程经验和调试经验有限的 10 岁学习者。他能理解基本数量关系和简单公式，但不一定知道怎样把数学关系翻译成代码，也不一定知道 TODO、断言、报错、shape、notebook 运行顺序是什么意思。不提前填答案，不自动理解 TODO，不把技术报错翻译成人话。

## 总体结论

- 共测试 33 课；可一路运行到最后的有 8 课；会在中途失败的有 25 课。
- 27 课包含 TODO/练习占位；其中大量失败来自上一格函数仍返回 `None`，下一格直接进入检查。
- `NoneType` 类失败 19 个，`AssertionError` 类失败 5 个，维度/shape 类明显失败 1 个。
- 0 课仍存在较长讲解块，对 10 岁儿童或注意力稀缺学习者会偏重。
- 这份报告不再把主要困难归因为“数学不行”。更准确的判断是：数学直觉可能够用，但“从数学到代码”的桥还不够细，失败后的恢复路径也不够友好。
- 环境层面有一个重要发现：系统 `python3` 没有 `matplotlib/jupyterlab`，直接跑会全部失败；项目 `.venv` 环境可运行。儿童学习者需要一个非常醒目的“先用正确环境”的入口。

## 10岁儿童的第一反应

我喜欢有“剧情”“Boss 关卡”“只改一个旋钮”的部分，因为我知道自己现在在干什么。可是我还是经常在三个地方掉线：

1. 我不知道什么时候该停下来填 TODO。
2. 报错像大人之间说的话，比如 `NoneType`、`dimension`、`AssertionError`，我不知道它和我刚才学的内容有什么关系。
3. 有些词我未必完全怕，比如梯度、SVD、Nyquist、softmax、行列式、傅里叶；但我需要知道它们在代码里对应哪一步、哪个变量、哪一行输出。

## 最需要优先修的共性问题

### 1. TODO 后缺少“儿童安全护栏”

很多课的流程是：讲解 -> TODO 函数 -> 检查格。10 岁学习者如果没改 TODO，下一格就会爆 `NoneType`。这在成人眼里是正常测试失败，在孩子眼里像“电脑突然讨厌我”。

建议：每个检查格前加一个守门格，明确说：

```python
# 如果这里还是 None，说明上一格还没完成，不要继续跑检查格
probe = your_function(...)
print(probe)
```

### 2. 报错信息需要翻译成学习语言

现在的报错多是 Python 原生语言。课程需要把失败变成提示，例如：

- `NoneType` -> “上一格函数还没有真正返回答案，请回到 TODO。”
- `AssertionError` -> “结果不接近标准答案；先打印中间量 A/B/C。”
- `ValueError: dimensions` -> “两个数组形状拼不上；先看 `.shape`。”

### 3. 每课还需要更小的“半步练习”

Boss 关卡很好，但有些课从“看演示”到“自己写完整函数”跨度仍然大。建议每个 TODO 前补 2 个半步：

- 半步 1：只写中间变量，不 return。
- 半步 2：给出一行缺口填空。
- 最终步：完整实现函数。

### 4. 术语要绑定到代码动作

对这个孩子来说，问题不是完全听不懂 “Nyquist / SVD / 交叉熵”，而是听懂一点概念之后，不知道下一步该写哪行代码。术语最好绑定到代码动作：Nyquist 对应“比较 `freq` 和 `sample_rate/2`”，SVD 对应“看 `U, S, Vt` 的 shape”，交叉熵对应“取正确类别概率再 `-log`”。

## Audio Core Week 01

| 课程 | 通关结果 | 10岁儿童反应 | 主要困难 | 建议 |
|---|---|---|---|---|
| `week01/day1_numpy.ipynb`<br>Day 1 — numpy 流畅度：生成一条时间轴 | 通过 | 我能跑完，但 TODO 可能已经被写好了；如果让我自己解释，还是需要更慢的提示。 | TODO 后续检查缺少儿童友好提示；需要把声音感知和数组更紧密连接<br>关键术语：矩阵 | 保留当前可运行性；补一个“我看懂了吗”的口头解释题，防止只是一路运行。 |
| `week01/day2_sine.ipynb`<br>Day 2 — 自己实现正弦波，并和仓库对答案 | cell 16 `TypeError`: unsupported operand type(s) for -: 'NoneType' and 'float' | 我感觉自己刚刚还在跟着玩，下一格突然说 NoneType。我不知道这是因为我没填上一格，还是电脑坏了。 | TODO 后续检查缺少儿童友好提示；错误信息太技术化；需要把声音感知和数组更紧密连接<br>关键术语：相位, 弧度, 矩阵 | 在检查格前插入“如果上一格还是 return None，请先停下”的守门格，并给 2 个半成品提示。 |
| `week01/day3_aliasing.ipynb`<br>Day 3 — Nyquist 与混叠(aliasing) | cell 15 `TypeError`: '<=' not supported between instances of 'int' and 'NoneType' | 我感觉自己刚刚还在跟着玩，下一格突然说 NoneType。我不知道这是因为我没填上一格，还是电脑坏了。 | TODO 后续检查缺少儿童友好提示；错误信息太技术化；需要把声音感知和数组更紧密连接<br>关键术语：Nyquist, alias, 矩阵 | 在检查格前插入“如果上一格还是 return None，请先停下”的守门格，并给 2 个半成品提示。 |
| `week01/day4_euler.ipynb`<br>Day 4 — 复数与欧拉公式：FFT 的命根子 | cell 17 `TypeError`: unsupported operand type(s) for -: 'NoneType' and 'complex' | 我感觉自己刚刚还在跟着玩，下一格突然说 NoneType。我不知道这是因为我没填上一格，还是电脑坏了。 | TODO 后续检查缺少儿童友好提示；错误信息太技术化；需要把声音感知和数组更紧密连接<br>关键术语：FFT, Euler, 欧拉, 复数, 矩阵 | 在检查格前插入“如果上一格还是 return None，请先停下”的守门格，并给 2 个半成品提示。 |
| `week01/day5_windows.ipynb`<br>Day 5 — 读懂 io.py / windows.py，对比窗函数 | 通过 | 我能跑完，但 TODO 可能已经被写好了；如果让我自己解释，还是需要更慢的提示。 | TODO 后续检查缺少儿童友好提示；术语需要和代码动作绑定；需要把声音感知和数组更紧密连接<br>关键术语：复数, 矩阵, window, Hann, Hamming, Blackman | 保留当前可运行性；补一个“我看懂了吗”的口头解释题，防止只是一路运行。 |

## 复数与三角前导

| 课程 | 通关结果 | 10岁儿童反应 | 主要困难 | 建议 |
|---|---|---|---|---|
| `prep_complex_trig/v1_visual_complex.ipynb`<br>图解·复数三角 — 把旋转和波画出来 | 通过 | 我能一路按下去，图很多，像看动画；但我不一定知道每张图为什么重要。 | 术语需要和代码动作绑定<br>关键术语：FFT, DFT, 欧拉, 复数, 相位, 矩阵 | 保留当前可运行性；补一个“我看懂了吗”的口头解释题，防止只是一路运行。 |
| `prep_complex_trig/x1_trig.ipynb`<br>前导·复数三角 1 — 正弦、余弦与三要素 | cell 15 `TypeError`: unsupported operand type(s) for -: 'NoneType' and 'float' | 我感觉自己刚刚还在跟着玩，下一格突然说 NoneType。我不知道这是因为我没填上一格，还是电脑坏了。 | TODO 后续检查缺少儿童友好提示；错误信息太技术化<br>关键术语：FFT, 复数, 相位, 矩阵 | 在检查格前插入“如果上一格还是 return None，请先停下”的守门格，并给 2 个半成品提示。 |
| `prep_complex_trig/x2_complex_numbers.ipynb`<br>前导·复数三角 2 — 复数：模与相位 | cell 14 `TypeError`: cannot unpack non-iterable NoneType object | 我感觉自己刚刚还在跟着玩，下一格突然说 NoneType。我不知道这是因为我没填上一格，还是电脑坏了。 | TODO 后续检查缺少儿童友好提示；错误信息太技术化<br>关键术语：FFT, 欧拉, 复数, 相位, 矩阵 | 在检查格前插入“如果上一格还是 return None，请先停下”的守门格，并给 2 个半成品提示。 |
| `prep_complex_trig/x3_euler.ipynb`<br>前导·复数三角 3 — 欧拉公式（FFT 的核心） | cell 14 `TypeError`: unsupported operand type(s) for -: 'NoneType' and 'int' | 我感觉自己刚刚还在跟着玩，下一格突然说 NoneType。我不知道这是因为我没填上一格，还是电脑坏了。 | TODO 后续检查缺少儿童友好提示；错误信息太技术化<br>关键术语：FFT, DFT, 欧拉, 复数, 矩阵 | 在检查格前插入“如果上一格还是 return None，请先停下”的守门格，并给 2 个半成品提示。 |
| `prep_complex_trig/x4_fourier_intuition.ipynb`<br>前导·复数三角 4 — 信号 = 正弦波之和（傅里叶直觉） | cell 14 `AssertionError`: 叠加足够多谐波后应接近方波 | 电脑说我不对，但没有告诉我应该回到哪一格改、改哪个变量。 | TODO 后续检查缺少儿童友好提示；断言失败缺少回退路线；概念不算不可理解，但需要更多从公式到代码的桥<br>关键术语：FFT, 复数, 矩阵 | 把 assert 的报错改成儿童语言：哪里错、回哪格、先打印哪个中间量。 |

## 线性代数前导

| 课程 | 通关结果 | 10岁儿童反应 | 主要困难 | 建议 |
|---|---|---|---|---|
| `prep_linear_algebra/p10_invertibility.ipynb`<br>线代 10 — 可逆性判据 | cell 14 `AssertionError`:  | 电脑说我不对，但没有告诉我应该回到哪一格改、改哪个变量。 | TODO 后续检查缺少儿童友好提示；断言失败缺少回退路线<br>关键术语：特征值, 行列式, 可逆, rank, 矩阵 | 把 assert 的报错改成儿童语言：哪里错、回哪格、先打印哪个中间量。 |
| `prep_linear_algebra/p1_vectors.ipynb`<br>前导·线代 1 — 向量(Vector) | cell 16 `TypeError`: unsupported operand type(s) for -: 'NoneType' and 'float' | 我感觉自己刚刚还在跟着玩，下一格突然说 NoneType。我不知道这是因为我没填上一格，还是电脑坏了。 | TODO 后续检查缺少儿童友好提示；错误信息太技术化<br>关键术语：矩阵 | 在检查格前插入“如果上一格还是 return None，请先停下”的守门格，并给 2 个半成品提示。 |
| `prep_linear_algebra/p2_dot_product.ipynb`<br>前导·线代 2 — 点积与相似度 | cell 15 `TypeError`: type NoneType doesn't define __round__ method | 我感觉自己刚刚还在跟着玩，下一格突然说 NoneType。我不知道这是因为我没填上一格，还是电脑坏了。 | TODO 后续检查缺少儿童友好提示；错误信息太技术化<br>关键术语：DFT, 矩阵 | 在检查格前插入“如果上一格还是 return None，请先停下”的守门格，并给 2 个半成品提示。 |
| `prep_linear_algebra/p3_norms.ipynb`<br>前导·线代 3 — 范数(长度)与归一化 | cell 16 `TypeError`: unsupported operand type(s) for *: 'NoneType' and 'NoneType' | 我感觉自己刚刚还在跟着玩，下一格突然说 NoneType。我不知道这是因为我没填上一格，还是电脑坏了。 | TODO 后续检查缺少儿童友好提示；错误信息太技术化<br>关键术语：矩阵, 范数 | 在检查格前插入“如果上一格还是 return None，请先停下”的守门格，并给 2 个半成品提示。 |
| `prep_linear_algebra/p4_matrices.ipynb`<br>前导·线代 4 — 矩阵 = 线性变换 | cell 16 `AssertionError`: 应与 A@x 一致 | 电脑说我不对，但没有告诉我应该回到哪一格改、改哪个变量。 | TODO 后续检查缺少儿童友好提示；断言失败缺少回退路线<br>关键术语：FFT, DFT, 复数, 矩阵 | 把 assert 的报错改成儿童语言：哪里错、回哪格、先打印哪个中间量。 |
| `prep_linear_algebra/p5_special_matrices.ipynb`<br>前导·线代 5 — 转置、逆、正交矩阵 | cell 16 `AssertionError`:  | 电脑说我不对，但没有告诉我应该回到哪一格改、改哪个变量。 | TODO 后续检查缺少儿童友好提示；断言失败缺少回退路线<br>关键术语：FFT, 矩阵, 正交 | 把 assert 的报错改成儿童语言：哪里错、回哪格、先打印哪个中间量。 |
| `prep_linear_algebra/p6_eigen_svd.ipynb`<br>前导·线代 6 — 特征值、PCA 与 SVD | cell 16 `TypeError`: unsupported operand type(s) for *: 'NoneType' and 'float' | 我感觉自己刚刚还在跟着玩，下一格突然说 NoneType。我不知道这是因为我没填上一格，还是电脑坏了。 | TODO 后续检查缺少儿童友好提示；错误信息太技术化；术语需要和代码动作绑定；概念不算不可理解，但需要更多从公式到代码的桥<br>关键术语：特征值, 特征向量, SVD, PCA, 低秩, rank, 矩阵 | 在检查格前插入“如果上一格还是 return None，请先停下”的守门格，并给 2 个半成品提示。 |
| `prep_linear_algebra/p7_linear_systems.ipynb`<br>线代 7 — 解线性方程组（高斯消元） | cell 12 `ValueError`: all the input array dimensions except for the concatenation axis must match exactly, but along dimension 0, the array at index 0 has size 2 and the array at index 1 has size 3 | 我看到一大串英文，像墙一样。我猜是数组形状错了，但不知道 shape 是什么。 | TODO 后续检查缺少儿童友好提示；维度/shape 需要前置小游戏<br>关键术语：rank, 矩阵 | 加入 shape 拼图小游戏：先预测 shape，再运行检查。 |
| `prep_linear_algebra/p8_determinant_inverse.ipynb`<br>线代 8 — 行列式、余子式与矩阵的逆 | cell 13 `TypeError`: unsupported operand type(s) for -: 'NoneType' and 'float' | 我感觉自己刚刚还在跟着玩，下一格突然说 NoneType。我不知道这是因为我没填上一格，还是电脑坏了。 | TODO 后续检查缺少儿童友好提示；错误信息太技术化<br>关键术语：行列式, 余子式, 可逆, 矩阵 | 在检查格前插入“如果上一格还是 return None，请先停下”的守门格，并给 2 个半成品提示。 |
| `prep_linear_algebra/p9_eigen_diagonalization.ipynb`<br>线代 9 — 特征值、特征向量与对角化 | cell 14 `TypeError`: type NoneType doesn't define __round__ method | 我感觉自己刚刚还在跟着玩，下一格突然说 NoneType。我不知道这是因为我没填上一格，还是电脑坏了。 | TODO 后续检查缺少儿童友好提示；错误信息太技术化；术语需要和代码动作绑定；概念不算不可理解，但需要更多从公式到代码的桥<br>关键术语：特征值, 特征向量, SVD, PCA, 矩阵, 正交 | 在检查格前插入“如果上一格还是 return None，请先停下”的守门格，并给 2 个半成品提示。 |
| `prep_linear_algebra/v1_visual_multiply.ipynb`<br>图解线代 1 — 把乘法画出来 | 通过 | 我能一路按下去，图很多，像看动画；但我不一定知道每张图为什么重要。 | 主要问题是解释和练习还可以更细<br>关键术语：FFT, DFT, SVD, 低秩, 矩阵 | 保留当前可运行性；补一个“我看懂了吗”的口头解释题，防止只是一路运行。 |
| `prep_linear_algebra/v2_visual_factorizations.ipynb`<br>图解线代 2 — 五大矩阵分解 | 通过 | 我能一路按下去，图很多，像看动画；但我不一定知道每张图为什么重要。 | 术语需要和代码动作绑定<br>关键术语：特征值, 特征向量, SVD, PCA, 矩阵, 正交 | 保留当前可运行性；补一个“我看懂了吗”的口头解释题，防止只是一路运行。 |
| `prep_linear_algebra/v3_aurora_as_matrices.ipynb`<br>图解线代 3 — Aurora 的音频运算其实都是矩阵 | 通过 | 我能一路按下去，图很多，像看动画；但我不一定知道每张图为什么重要。 | 主要问题是解释和练习还可以更细<br>关键术语：FFT, DFT, 复数, 矩阵 | 保留当前可运行性；补一个“我看懂了吗”的口头解释题，防止只是一路运行。 |

## 微积分前导

| 课程 | 通关结果 | 10岁儿童反应 | 主要困难 | 建议 |
|---|---|---|---|---|
| `prep_calculus/c1_derivatives.ipynb`<br>前导·微积分 1 — 导数 = 变化率 | cell 14 `TypeError`: unsupported operand type(s) for -: 'NoneType' and 'float' | 我感觉自己刚刚还在跟着玩，下一格突然说 NoneType。我不知道这是因为我没填上一格，还是电脑坏了。 | TODO 后续检查缺少儿童友好提示；错误信息太技术化<br>关键术语：梯度, 矩阵 | 在检查格前插入“如果上一格还是 return None，请先停下”的守门格，并给 2 个半成品提示。 |
| `prep_calculus/c2_gradients.ipynb`<br>前导·微积分 2 — 偏导与梯度 | cell 14 `AssertionError`:  | 电脑说我不对，但没有告诉我应该回到哪一格改、改哪个变量。 | TODO 后续检查缺少儿童友好提示；断言失败缺少回退路线<br>关键术语：梯度, 偏导, 链式法则, 反向传播, 矩阵 | 把 assert 的报错改成儿童语言：哪里错、回哪格、先打印哪个中间量。 |
| `prep_calculus/c3_chain_rule.ipynb`<br>前导·微积分 3 — 链式法则（反向传播的心脏） | cell 14 `TypeError`: unsupported operand type(s) for -: 'NoneType' and 'float' | 我感觉自己刚刚还在跟着玩，下一格突然说 NoneType。我不知道这是因为我没填上一格，还是电脑坏了。 | TODO 后续检查缺少儿童友好提示；错误信息太技术化<br>关键术语：梯度, 链式法则, 反向传播, 矩阵 | 在检查格前插入“如果上一格还是 return None，请先停下”的守门格，并给 2 个半成品提示。 |
| `prep_calculus/c4_gradient_descent.ipynb`<br>前导·微积分 4 — 梯度下降（所有模型的训练内核） | cell 14 `TypeError`: unsupported operand type(s) for -: 'NoneType' and 'int' | 我感觉自己刚刚还在跟着玩，下一格突然说 NoneType。我不知道这是因为我没填上一格，还是电脑坏了。 | TODO 后续检查缺少儿童友好提示；错误信息太技术化<br>关键术语：梯度, learning_rate, 矩阵 | 在检查格前插入“如果上一格还是 return None，请先停下”的守门格，并给 2 个半成品提示。 |
| `prep_calculus/v1_visual_calculus.ipynb`<br>图解·微积分 — 把斜率和下山画出来 | 通过 | 我能一路按下去，图很多，像看动画；但我不一定知道每张图为什么重要。 | 主要问题是解释和练习还可以更细<br>关键术语：梯度, 矩阵 | 保留当前可运行性；补一个“我看懂了吗”的口头解释题，防止只是一路运行。 |

## 概率统计前导

| 课程 | 通关结果 | 10岁儿童反应 | 主要困难 | 建议 |
|---|---|---|---|---|
| `prep_probability/s1_basics.ipynb`<br>前导·概率 1 — 随机与大数定律 | cell 14 `TypeError`: type NoneType doesn't define __round__ method | 我感觉自己刚刚还在跟着玩，下一格突然说 NoneType。我不知道这是因为我没填上一格，还是电脑坏了。 | TODO 后续检查缺少儿童友好提示；错误信息太技术化<br>关键术语：矩阵 | 在检查格前插入“如果上一格还是 return None，请先停下”的守门格，并给 2 个半成品提示。 |
| `prep_probability/s2_descriptive.ipynb`<br>前导·概率 2 — 均值、方差与标准化 | cell 14 `AttributeError`: 'NoneType' object has no attribute 'mean' | 我感觉自己刚刚还在跟着玩，下一格突然说 NoneType。我不知道这是因为我没填上一格，还是电脑坏了。 | TODO 后续检查缺少儿童友好提示；错误信息太技术化<br>关键术语：标准化, z-score, 矩阵 | 在检查格前插入“如果上一格还是 return None，请先停下”的守门格，并给 2 个半成品提示。 |
| `prep_probability/s3_distributions.ipynb`<br>前导·概率 3 — 均匀分布与正态分布 | cell 14 `TypeError`: unsupported operand type(s) for -: 'NoneType' and 'float' | 我感觉自己刚刚还在跟着玩，下一格突然说 NoneType。我不知道这是因为我没填上一格，还是电脑坏了。 | TODO 后续检查缺少儿童友好提示；错误信息太技术化<br>关键术语：pdf, 正态分布, 矩阵 | 在检查格前插入“如果上一格还是 return None，请先停下”的守门格，并给 2 个半成品提示。 |
| `prep_probability/s4_softmax_crossentropy.ipynb`<br>前导·概率 4 — Softmax 与交叉熵 | cell 12 `TypeError`: unsupported operand type(s) for *: 'NoneType' and 'float' | 我感觉自己刚刚还在跟着玩，下一格突然说 NoneType。我不知道这是因为我没填上一格，还是电脑坏了。 | TODO 后续检查缺少儿童友好提示；错误信息太技术化；概念不算不可理解，但需要更多从公式到代码的桥<br>关键术语：softmax, cross_entropy, logits, 矩阵 | 在检查格前插入“如果上一格还是 return None，请先停下”的守门格，并给 2 个半成品提示。 |
| `prep_probability/v1_visual_probability.ipynb`<br>图解·概率统计 — 把分布和损失画出来 | 通过 | 我能一路按下去，图很多，像看动画；但我不一定知道每张图为什么重要。 | 主要问题是解释和练习还可以更细<br>关键术语：softmax, 正态分布, 标准化, z-score, 矩阵 | 保留当前可运行性；补一个“我看懂了吗”的口头解释题，防止只是一路运行。 |

## 逐课细节备忘

### `prep_calculus/c1_derivatives.ipynb` — 前导·微积分 1 — 导数 = 变化率

- 代码格运行：4/8；练习函数：f, f, numeric_derivative, f；TODO 数：1。
- 第一个失败：cell 14 `TypeError`: unsupported operand type(s) for -: 'NoneType' and 'float'。
- 小朋友视角：我感觉自己刚刚还在跟着玩，下一格突然说 NoneType。我不知道这是因为我没填上一格，还是电脑坏了。
- 困难标签：TODO 后续检查缺少儿童友好提示；错误信息太技术化。
- 已能看到的正反馈输出：cell 6: f(x)=x^2 在 x=3 的斜率 ≈ 6.000000000039306  (真值 2x=6)；cell 8: x = [-2. -1.  0.  1.  2.] / f(x) = [4. 1. 0. 1. 4.] / 近似斜率 = [-4. -2.  0.  2.  4.] / 理论斜率 2x = [-4. -2.  0.  2.  4.]。
- 下一步改进：在检查格前插入“如果上一格还是 return None，请先停下”的守门格，并给 2 个半成品提示。

### `prep_calculus/c2_gradients.ipynb` — 前导·微积分 2 — 偏导与梯度

- 代码格运行：4/8；练习函数：f, f, gradient, f；TODO 数：1。
- 第一个失败：cell 14 `AssertionError`: 。
- 小朋友视角：电脑说我不对，但没有告诉我应该回到哪一格改、改哪个变量。
- 困难标签：TODO 后续检查缺少儿童友好提示；断言失败缺少回退路线。
- 已能看到的正反馈输出：cell 6: ∂f/∂x ≈ 6.0 (真值2x=6)  ∂f/∂y ≈ 8.0 (真值2y=8)；cell 8: x = [-2. -1.  0.  1.  2.] / f(x) = [4. 1. 0. 1. 4.] / 近似斜率 = [-4. -2.  0.  2.  4.] / 理论斜率 2x = [-4. -2.  0.  2.  4.]。
- 下一步改进：把 assert 的报错改成儿童语言：哪里错、回哪格、先打印哪个中间量。

### `prep_calculus/c3_chain_rule.ipynb` — 前导·微积分 3 — 链式法则（反向传播的心脏）

- 代码格运行：4/8；练习函数：f, f, composite_derivative, f；TODO 数：1。
- 第一个失败：cell 14 `TypeError`: unsupported operand type(s) for -: 'NoneType' and 'float'。
- 小朋友视角：我感觉自己刚刚还在跟着玩，下一格突然说 NoneType。我不知道这是因为我没填上一格，还是电脑坏了。
- 困难标签：TODO 后续检查缺少儿童友好提示；错误信息太技术化。
- 已能看到的正反馈输出：cell 6: 链式法则: -0.3092  数值验证: -0.3092；cell 8: x = [-2. -1.  0.  1.  2.] / f(x) = [4. 1. 0. 1. 4.] / 近似斜率 = [-4. -2.  0.  2.  4.] / 理论斜率 2x = [-4. -2.  0.  2.  4.]。
- 下一步改进：在检查格前插入“如果上一格还是 return None，请先停下”的守门格，并给 2 个半成品提示。

### `prep_calculus/c4_gradient_descent.ipynb` — 前导·微积分 4 — 梯度下降（所有模型的训练内核）

- 代码格运行：4/9；练习函数：f, f, gd_step, f；TODO 数：1。
- 第一个失败：cell 14 `TypeError`: unsupported operand type(s) for -: 'NoneType' and 'int'。
- 小朋友视角：我感觉自己刚刚还在跟着玩，下一格突然说 NoneType。我不知道这是因为我没填上一格，还是电脑坏了。
- 困难标签：TODO 后续检查缺少儿童友好提示；错误信息太技术化。
- 已能看到的正反馈输出：cell 6: 收敛到 x = 2.9963  (最小值在 x=3)；cell 8: x = [-2. -1.  0.  1.  2.] / f(x) = [4. 1. 0. 1. 4.] / 近似斜率 = [-4. -2.  0.  2.  4.] / 理论斜率 2x = [-4. -2.  0.  2.  4.]。
- 下一步改进：在检查格前插入“如果上一格还是 return None，请先停下”的守门格，并给 2 个半成品提示。

### `prep_calculus/v1_visual_calculus.ipynb` — 图解·微积分 — 把斜率和下山画出来

- 代码格运行：10/10；练习函数：f, f, f, f；TODO 数：0。
- 第一个失败：通过。
- 小朋友视角：我能一路按下去，图很多，像看动画；但我不一定知道每张图为什么重要。
- 困难标签：主要问题是解释和练习还可以更细。
- 已能看到的正反馈输出：cell 4: Matplotlib is building the font cache; this may take a moment. / cviz 就绪；cell 7: x = [-2. -1.  0.  1.  2.] / f(x) = [4. 1. 0. 1. 4.] / 近似斜率 = [-4. -2.  0.  2.  4.] / 理论斜率 2x = [-4. -2.  0.  2.  4.]。
- 下一步改进：保留当前可运行性；补一个“我看懂了吗”的口头解释题，防止只是一路运行。

### `prep_complex_trig/v1_visual_complex.ipynb` — 图解·复数三角 — 把旋转和波画出来

- 代码格运行：11/11；练习函数：无练习函数；TODO 数：0。
- 第一个失败：通过。
- 小朋友视角：我能一路按下去，图很多，像看动画；但我不一定知道每张图为什么重要。
- 困难标签：术语需要和代码动作绑定。
- 已能看到的正反馈输出：cell 4: xviz 就绪；cell 7: 角度 = [0.    1.571 3.142 4.712] / 实部 cos = [ 1.  0. -1. -0.] / 虚部 sin = [ 0.  1.  0. -1.] / 复数 z = [ 1.+0.j  0.+1.j -1.+0.j -0.-1.j]。
- 下一步改进：保留当前可运行性；补一个“我看懂了吗”的口头解释题，防止只是一路运行。

### `prep_complex_trig/x1_trig.ipynb` — 前导·复数三角 1 — 正弦、余弦与三要素

- 代码格运行：4/8；练习函数：sinusoid；TODO 数：1。
- 第一个失败：cell 15 `TypeError`: unsupported operand type(s) for -: 'NoneType' and 'float'。
- 小朋友视角：我感觉自己刚刚还在跟着玩，下一格突然说 NoneType。我不知道这是因为我没填上一格，还是电脑坏了。
- 困难标签：TODO 后续检查缺少儿童友好提示；错误信息太技术化。
- 已能看到的正反馈输出：cell 6: <string>:5: UserWarning: FigureCanvasAgg is non-interactive, and thus cannot be ；cell 8: 角度 = [0.    1.571 3.142 4.712] / 实部 cos = [ 1.  0. -1. -0.] / 虚部 sin = [ 0.  1.  0. -1.] / 复数 z = [ 1.+0.j  0.+1.j -1.+0.j -0.-1.j]。
- 下一步改进：在检查格前插入“如果上一格还是 return None，请先停下”的守门格，并给 2 个半成品提示。

### `prep_complex_trig/x2_complex_numbers.ipynb` — 前导·复数三角 2 — 复数：模与相位

- 代码格运行：4/8；练习函数：magnitude_phase；TODO 数：1。
- 第一个失败：cell 14 `TypeError`: cannot unpack non-iterable NoneType object。
- 小朋友视角：我感觉自己刚刚还在跟着玩，下一格突然说 NoneType。我不知道这是因为我没填上一格，还是电脑坏了。
- 困难标签：TODO 后续检查缺少儿童友好提示；错误信息太技术化。
- 已能看到的正反馈输出：cell 6: 实部: 3.0  虚部: 4.0 / 模 /z/ = 5.0  (=√(3²+4²)=5) / 相位(弧度) = 0.9272952180016122；cell 8: 角度 = [0.    1.571 3.142 4.712] / 实部 cos = [ 1.  0. -1. -0.] / 虚部 sin = [ 0.  1.  0. -1.] / 复数 z = [ 1.+0.j  0.+1.j -1.+0.j -0.-1.j]。
- 下一步改进：在检查格前插入“如果上一格还是 return None，请先停下”的守门格，并给 2 个半成品提示。

### `prep_complex_trig/x3_euler.ipynb` — 前导·复数三角 3 — 欧拉公式（FFT 的核心）

- 代码格运行：4/9；练习函数：twiddle；TODO 数：1。
- 第一个失败：cell 14 `TypeError`: unsupported operand type(s) for -: 'NoneType' and 'int'。
- 小朋友视角：我感觉自己刚刚还在跟着玩，下一格突然说 NoneType。我不知道这是因为我没填上一格，还是电脑坏了。
- 困难标签：TODO 后续检查缺少儿童友好提示；错误信息太技术化。
- 已能看到的正反馈输出：cell 6: 与 np.exp(iθ) 一致: True / 每个点模长都是1: True；cell 8: 角度 = [0.    1.571 3.142 4.712] / 实部 cos = [ 1.  0. -1. -0.] / 虚部 sin = [ 0.  1.  0. -1.] / 复数 z = [ 1.+0.j  0.+1.j -1.+0.j -0.-1.j]。
- 下一步改进：在检查格前插入“如果上一格还是 return None，请先停下”的守门格，并给 2 个半成品提示。

### `prep_complex_trig/x4_fourier_intuition.ipynb` — 前导·复数三角 4 — 信号 = 正弦波之和（傅里叶直觉）

- 代码格运行：4/8；练习函数：square_approx；TODO 数：1。
- 第一个失败：cell 14 `AssertionError`: 叠加足够多谐波后应接近方波。
- 小朋友视角：电脑说我不对，但没有告诉我应该回到哪一格改、改哪个变量。
- 困难标签：TODO 后续检查缺少儿童友好提示；断言失败缺少回退路线；概念不算不可理解，但需要更多从公式到代码的桥。
- 已能看到的正反馈输出：cell 6: <string>:4: UserWarning: FigureCanvasAgg is non-interactive, and thus cannot be ；cell 8: 角度 = [0.    1.571 3.142 4.712] / 实部 cos = [ 1.  0. -1. -0.] / 虚部 sin = [ 0.  1.  0. -1.] / 复数 z = [ 1.+0.j  0.+1.j -1.+0.j -0.-1.j]。
- 下一步改进：把 assert 的报错改成儿童语言：哪里错、回哪格、先打印哪个中间量。

### `prep_linear_algebra/p10_invertibility.ipynb` — 线代 10 — 可逆性判据

- 代码格运行：4/9；练习函数：is_sdd；TODO 数：1。
- 第一个失败：cell 14 `AssertionError`: 。
- 小朋友视角：电脑说我不对，但没有告诉我应该回到哪一格改、改哪个变量。
- 困难标签：TODO 后续检查缺少儿童友好提示；断言失败缺少回退路线。
- 已能看到的正反馈输出：cell 6: det = 2 / 特征值: [0.268 2.    3.732] / 两条充要判据都说：可逆 = True；cell 8: v = [3. 4.] shape = (2,) / A = / [[2.  0. ] /  [0.  0.5]] / A shape = (2, 2)。
- 下一步改进：把 assert 的报错改成儿童语言：哪里错、回哪格、先打印哪个中间量。

### `prep_linear_algebra/p1_vectors.ipynb` — 前导·线代 1 — 向量(Vector)

- 代码格运行：5/11；练习函数：scale；TODO 数：1。
- 第一个失败：cell 16 `TypeError`: unsupported operand type(s) for -: 'NoneType' and 'float'。
- 小朋友视角：我感觉自己刚刚还在跟着玩，下一格突然说 NoneType。我不知道这是因为我没填上一格，还是电脑坏了。
- 困难标签：TODO 后续检查缺少儿童友好提示；错误信息太技术化。
- 已能看到的正反馈输出：cell 6: v = [3. 4.] / 维度: (2,) / audio 是一个 5 维向量；cell 8: v = [3. 4.] shape = (2,) / A = / [[2.  0. ] /  [0.  0.5]] / A shape = (2, 2)。
- 下一步改进：在检查格前插入“如果上一格还是 return None，请先停下”的守门格，并给 2 个半成品提示。

### `prep_linear_algebra/p2_dot_product.ipynb` — 前导·线代 2 — 点积与相似度

- 代码格运行：4/9；练习函数：cosine_similarity；TODO 数：1。
- 第一个失败：cell 15 `TypeError`: type NoneType doesn't define __round__ method。
- 小朋友视角：我感觉自己刚刚还在跟着玩，下一格突然说 NoneType。我不知道这是因为我没填上一格，还是电脑坏了。
- 困难标签：TODO 后续检查缺少儿童友好提示；错误信息太技术化。
- 已能看到的正反馈输出：cell 6: 逐元素相乘: [ 4. 10. 18.] / 点积(求和): 32.0 / 也可写作 a @ b = 32.0；cell 8: v = [3. 4.] shape = (2,) / A = / [[2.  0. ] /  [0.  0.5]] / A shape = (2, 2)。
- 下一步改进：在检查格前插入“如果上一格还是 return None，请先停下”的守门格，并给 2 个半成品提示。

### `prep_linear_algebra/p3_norms.ipynb` — 前导·线代 3 — 范数(长度)与归一化

- 代码格运行：5/10；练习函数：normalize；TODO 数：1。
- 第一个失败：cell 16 `TypeError`: unsupported operand type(s) for *: 'NoneType' and 'NoneType'。
- 小朋友视角：我感觉自己刚刚还在跟着玩，下一格突然说 NoneType。我不知道这是因为我没填上一格，还是电脑坏了。
- 困难标签：TODO 后续检查缺少儿童友好提示；错误信息太技术化。
- 已能看到的正反馈输出：cell 6: 手算: 5.0 / numpy: 5.0 / L1 范数(绝对值之和): 7.0；cell 8: v = [3. 4.] shape = (2,) / A = / [[2.  0. ] /  [0.  0.5]] / A shape = (2, 2)。
- 下一步改进：在检查格前插入“如果上一格还是 return None，请先停下”的守门格，并给 2 个半成品提示。

### `prep_linear_algebra/p4_matrices.ipynb` — 前导·线代 4 — 矩阵 = 线性变换

- 代码格运行：5/10；练习函数：matvec；TODO 数：1。
- 第一个失败：cell 16 `AssertionError`: 应与 A@x 一致。
- 小朋友视角：电脑说我不对，但没有告诉我应该回到哪一格改、改哪个变量。
- 困难标签：TODO 后续检查缺少儿童友好提示；断言失败缺少回退路线。
- 已能看到的正反馈输出：cell 6: W @ x = [2. 3.]；cell 8: v = [3. 4.] shape = (2,) / A = / [[2.  0. ] /  [0.  0.5]] / A shape = (2, 2)。
- 下一步改进：把 assert 的报错改成儿童语言：哪里错、回哪格、先打印哪个中间量。

### `prep_linear_algebra/p5_special_matrices.ipynb` — 前导·线代 5 — 转置、逆、正交矩阵

- 代码格运行：5/10；练习函数：is_orthogonal；TODO 数：1。
- 第一个失败：cell 16 `AssertionError`: 。
- 小朋友视角：电脑说我不对，但没有告诉我应该回到哪一格改、改哪个变量。
- 困难标签：TODO 后续检查缺少儿童友好提示；断言失败缺少回退路线。
- 已能看到的正反馈输出：cell 6: 单位阵 I= /  [[1. 0. 0.] /  [0. 1. 0.] /  [0. 0. 1.]] / 转置 A.T=；cell 8: v = [3. 4.] shape = (2,) / A = / [[2.  0. ] /  [0.  0.5]] / A shape = (2, 2)。
- 下一步改进：把 assert 的报错改成儿童语言：哪里错、回哪格、先打印哪个中间量。

### `prep_linear_algebra/p6_eigen_svd.ipynb` — 前导·线代 6 — 特征值、PCA 与 SVD

- 代码格运行：5/10；练习函数：low_rank_approx；TODO 数：1。
- 第一个失败：cell 16 `TypeError`: unsupported operand type(s) for *: 'NoneType' and 'float'。
- 小朋友视角：我感觉自己刚刚还在跟着玩，下一格突然说 NoneType。我不知道这是因为我没填上一格，还是电脑坏了。
- 困难标签：TODO 后续检查缺少儿童友好提示；错误信息太技术化；术语需要和代码动作绑定；概念不算不可理解，但需要更多从公式到代码的桥。
- 已能看到的正反馈输出：cell 6: 特征值 λ: [2. 3.] / 特征向量(按列): /  [[1. 0.] /  [0. 1.]]；cell 8: v = [3. 4.] shape = (2,) / A = / [[2.  0. ] /  [0.  0.5]] / A shape = (2, 2)。
- 下一步改进：在检查格前插入“如果上一格还是 return None，请先停下”的守门格，并给 2 个半成品提示。

### `prep_linear_algebra/p7_linear_systems.ipynb` — 线代 7 — 解线性方程组（高斯消元）

- 代码格运行：3/10；练习函数：classify_system；TODO 数：1。
- 第一个失败：cell 12 `ValueError`: all the input array dimensions except for the concatenation axis must match exactly, but along dimension 0, the array at index 0 has size 2 and the array at index 1 has size 3。
- 小朋友视角：我看到一大串英文，像墙一样。我猜是数组形状错了，但不知道 shape 是什么。
- 困难标签：TODO 后续检查缺少儿童友好提示；维度/shape 需要前置小游戏。
- 已能看到的正反馈输出：cell 6: 解 = [ 1.  2. -3.]  (课件 [1, 2, -3])；cell 8: v = [3. 4.] shape = (2,) / A = / [[2.  0. ] /  [0.  0.5]] / A shape = (2, 2)。
- 下一步改进：加入 shape 拼图小游戏：先预测 shape，再运行检查。

### `prep_linear_algebra/p8_determinant_inverse.ipynb` — 线代 8 — 行列式、余子式与矩阵的逆

- 代码格运行：3/10；练习函数：det_2x2, inv_2x2；TODO 数：1。
- 第一个失败：cell 13 `TypeError`: unsupported operand type(s) for -: 'NoneType' and 'float'。
- 小朋友视角：我感觉自己刚刚还在跟着玩，下一格突然说 NoneType。我不知道这是因为我没填上一格，还是电脑坏了。
- 困难标签：TODO 后续检查缺少儿童友好提示；错误信息太技术化。
- 已能看到的正反馈输出：cell 10: v = [3. 4.] shape = (2,) / A = / [[2.  0. ] /  [0.  0.5]] / A shape = (2, 2)；cell 12: A = / [[2. 1.] /  [0. 1.]] / v=[1. 0.] -> A@v=[2. 0.] / v=[0. 1.] -> A@v=[1. 1.]。
- 下一步改进：在检查格前插入“如果上一格还是 return None，请先停下”的守门格，并给 2 个半成品提示。

### `prep_linear_algebra/p9_eigen_diagonalization.ipynb` — 线代 9 — 特征值、特征向量与对角化

- 代码格运行：4/10；练习函数：char_poly；TODO 数：1。
- 第一个失败：cell 14 `TypeError`: type NoneType doesn't define __round__ method。
- 小朋友视角：我感觉自己刚刚还在跟着玩，下一格突然说 NoneType。我不知道这是因为我没填上一格，还是电脑坏了。
- 困难标签：TODO 后续检查缺少儿童友好提示；错误信息太技术化；术语需要和代码动作绑定；概念不算不可理解，但需要更多从公式到代码的桥。
- 已能看到的正反馈输出：cell 6: 特征值: [np.int64(-3), np.int64(-2), np.int64(6)]  (课件 -3,-2,6)；cell 8: v = [3. 4.] shape = (2,) / A = / [[2.  0. ] /  [0.  0.5]] / A shape = (2, 2)。
- 下一步改进：在检查格前插入“如果上一格还是 return None，请先停下”的守门格，并给 2 个半成品提示。

### `prep_linear_algebra/v1_visual_multiply.ipynb` — 图解线代 1 — 把乘法画出来

- 代码格运行：10/10；练习函数：无练习函数；TODO 数：0。
- 第一个失败：通过。
- 小朋友视角：我能一路按下去，图很多，像看动画；但我不一定知道每张图为什么重要。
- 困难标签：主要问题是解释和练习还可以更细。
- 已能看到的正反馈输出：cell 6: laviz 就绪；cell 8: v = [3. 4.] shape = (2,) / A = / [[2.  0. ] /  [0.  0.5]] / A shape = (2, 2)。
- 下一步改进：保留当前可运行性；补一个“我看懂了吗”的口头解释题，防止只是一路运行。

### `prep_linear_algebra/v2_visual_factorizations.ipynb` — 图解线代 2 — 五大矩阵分解

- 代码格运行：10/10；练习函数：无练习函数；TODO 数：0。
- 第一个失败：通过。
- 小朋友视角：我能一路按下去，图很多，像看动画；但我不一定知道每张图为什么重要。
- 困难标签：术语需要和代码动作绑定。
- 已能看到的正反馈输出：cell 4: 就绪；cell 7: v = [3. 4.] shape = (2,) / A = / [[2.  0. ] /  [0.  0.5]] / A shape = (2, 2)。
- 下一步改进：保留当前可运行性；补一个“我看懂了吗”的口头解释题，防止只是一路运行。

### `prep_linear_algebra/v3_aurora_as_matrices.ipynb` — 图解线代 3 — Aurora 的音频运算其实都是矩阵

- 代码格运行：10/10；练习函数：无练习函数；TODO 数：0。
- 第一个失败：通过。
- 小朋友视角：我能一路按下去，图很多，像看动画；但我不一定知道每张图为什么重要。
- 困难标签：主要问题是解释和练习还可以更细。
- 已能看到的正反馈输出：cell 4: 就绪；cell 7: v = [3. 4.] shape = (2,) / A = / [[2.  0. ] /  [0.  0.5]] / A shape = (2, 2)。
- 下一步改进：保留当前可运行性；补一个“我看懂了吗”的口头解释题，防止只是一路运行。

### `prep_probability/s1_basics.ipynb` — 前导·概率 1 — 随机与大数定律

- 代码格运行：4/8；练习函数：estimate_prob_six；TODO 数：1。
- 第一个失败：cell 14 `TypeError`: type NoneType doesn't define __round__ method。
- 小朋友视角：我感觉自己刚刚还在跟着玩，下一格突然说 NoneType。我不知道这是因为我没填上一格，还是电脑坏了。
- 困难标签：TODO 后续检查缺少儿童友好提示；错误信息太技术化。
- 已能看到的正反馈输出：cell 6: 1000 次抛硬币，正面比例 ≈ 0.537  (应接近 0.5)；cell 8: n=   10  估计 P(掷到6) = 0.100 / n=  100  估计 P(掷到6) = 0.160 / n=10000  估计 P(掷到6) = 0.169。
- 下一步改进：在检查格前插入“如果上一格还是 return None，请先停下”的守门格，并给 2 个半成品提示。

### `prep_probability/s2_descriptive.ipynb` — 前导·概率 2 — 均值、方差与标准化

- 代码格运行：4/9；练习函数：zscore；TODO 数：1。
- 第一个失败：cell 14 `AttributeError`: 'NoneType' object has no attribute 'mean'。
- 小朋友视角：我感觉自己刚刚还在跟着玩，下一格突然说 NoneType。我不知道这是因为我没填上一格，还是电脑坏了。
- 困难标签：TODO 后续检查缺少儿童友好提示；错误信息太技术化。
- 已能看到的正反馈输出：cell 6: 均值 mean : 5.0 / 方差 var  : 4.0 / 标准差 std: 2.0；cell 8: n=   10  估计 P(掷到6) = 0.100 / n=  100  估计 P(掷到6) = 0.160 / n=10000  估计 P(掷到6) = 0.169。
- 下一步改进：在检查格前插入“如果上一格还是 return None，请先停下”的守门格，并给 2 个半成品提示。

### `prep_probability/s3_distributions.ipynb` — 前导·概率 3 — 均匀分布与正态分布

- 代码格运行：4/8；练习函数：gaussian_pdf；TODO 数：1。
- 第一个失败：cell 14 `TypeError`: unsupported operand type(s) for -: 'NoneType' and 'float'。
- 小朋友视角：我感觉自己刚刚还在跟着玩，下一格突然说 NoneType。我不知道这是因为我没填上一格，还是电脑坏了。
- 困难标签：TODO 后续检查缺少儿童友好提示；错误信息太技术化。
- 已能看到的正反馈输出：cell 6: <string>:7: UserWarning: FigureCanvasAgg is non-interactive, and thus cannot be ；cell 8: n=   10  估计 P(掷到6) = 0.100 / n=  100  估计 P(掷到6) = 0.160 / n=10000  估计 P(掷到6) = 0.169。
- 下一步改进：在检查格前插入“如果上一格还是 return None，请先停下”的守门格，并给 2 个半成品提示。

### `prep_probability/s4_softmax_crossentropy.ipynb` — 前导·概率 4 — Softmax 与交叉熵

- 代码格运行：3/9；练习函数：softmax, cross_entropy；TODO 数：2。
- 第一个失败：cell 12 `TypeError`: unsupported operand type(s) for *: 'NoneType' and 'float'。
- 小朋友视角：我感觉自己刚刚还在跟着玩，下一格突然说 NoneType。我不知道这是因为我没填上一格，还是电脑坏了。
- 困难标签：TODO 后续检查缺少儿童友好提示；错误信息太技术化；概念不算不可理解，但需要更多从公式到代码的桥。
- 已能看到的正反馈输出：cell 9: n=   10  估计 P(掷到6) = 0.100 / n=  100  估计 P(掷到6) = 0.160 / n=10000  估计 P(掷到6) = 0.169；cell 11: n=  20 -> [0.2  0.15 0.15 0.05 0.3 ] 平均= 0.17 / n= 200 -> [0.21  0.18  0.155 0.16  0.21 ] 平均= 0.183 / n=2000 -> [0.174 0.184 0.17  0.158 0.176] 平均= 0.172。
- 下一步改进：在检查格前插入“如果上一格还是 return None，请先停下”的守门格，并给 2 个半成品提示。

### `prep_probability/v1_visual_probability.ipynb` — 图解·概率统计 — 把分布和损失画出来

- 代码格运行：12/12；练习函数：无练习函数；TODO 数：0。
- 第一个失败：通过。
- 小朋友视角：我能一路按下去，图很多，像看动画；但我不一定知道每张图为什么重要。
- 困难标签：主要问题是解释和练习还可以更细。
- 已能看到的正反馈输出：cell 4: sviz 就绪；cell 7: n=   10  估计 P(掷到6) = 0.100 / n=  100  估计 P(掷到6) = 0.160 / n=10000  估计 P(掷到6) = 0.169。
- 下一步改进：保留当前可运行性；补一个“我看懂了吗”的口头解释题，防止只是一路运行。

### `week01/day1_numpy.ipynb` — Day 1 — numpy 流畅度：生成一条时间轴

- 代码格运行：10/10；练习函数：time_axis；TODO 数：1。
- 第一个失败：通过。
- 小朋友视角：我能跑完，但 TODO 可能已经被写好了；如果让我自己解释，还是需要更慢的提示。
- 困难标签：TODO 后续检查缺少儿童友好提示；需要把声音感知和数组更紧密连接。
- 已能看到的正反馈输出：cell 7: numpy 已就绪: 2.4.6；cell 9: N = 8 / 采样点编号 n = [0 1 2 3 4 5 6 7] / 时间轴 t = [0.    0.125 0.25  0.375 0.5   0.625 0.75  0.875] / 角度 angle = [ 0.     1.571  3.142  4.712  6.283  7.854  9.425 10.996] / sin(angle) = [ 0.  1.  0. -1. -0.  1.  0. -1.]。
- 下一步改进：保留当前可运行性；补一个“我看懂了吗”的口头解释题，防止只是一路运行。

### `week01/day2_sine.ipynb` — Day 2 — 自己实现正弦波，并和仓库对答案

- 代码格运行：4/10；练习函数：my_sine；TODO 数：1。
- 第一个失败：cell 16 `TypeError`: unsupported operand type(s) for -: 'NoneType' and 'float'。
- 小朋友视角：我感觉自己刚刚还在跟着玩，下一格突然说 NoneType。我不知道这是因为我没填上一格，还是电脑坏了。
- 困难标签：TODO 后续检查缺少儿童友好提示；错误信息太技术化；需要把声音感知和数组更紧密连接。
- 已能看到的正反馈输出：cell 6: 就绪；cell 8: N = 8 / 采样点编号 n = [0 1 2 3 4 5 6 7] / 时间轴 t = [0.    0.125 0.25  0.375 0.5   0.625 0.75  0.875] / 角度 angle = [ 0.     1.571  3.142  4.712  6.283  7.854  9.425 10.996] / sin(angle) = [ 0.  1.  0. -1. -0.  1.  0. -1.]。
- 下一步改进：在检查格前插入“如果上一格还是 return None，请先停下”的守门格，并给 2 个半成品提示。

### `week01/day3_aliasing.ipynb` — Day 3 — Nyquist 与混叠(aliasing)

- 代码格运行：4/10；练习函数：predict_alias_freq；TODO 数：1。
- 第一个失败：cell 15 `TypeError`: '<=' not supported between instances of 'int' and 'NoneType'。
- 小朋友视角：我感觉自己刚刚还在跟着玩，下一格突然说 NoneType。我不知道这是因为我没填上一格，还是电脑坏了。
- 困难标签：TODO 后续检查缺少儿童友好提示；错误信息太技术化；需要把声音感知和数组更紧密连接。
- 已能看到的正反馈输出：cell 6: 就绪；cell 8: N = 8 / 采样点编号 n = [0 1 2 3 4 5 6 7] / 时间轴 t = [0.    0.125 0.25  0.375 0.5   0.625 0.75  0.875] / 角度 angle = [ 0.     1.571  3.142  4.712  6.283  7.854  9.425 10.996] / sin(angle) = [ 0.  1.  0. -1. -0.  1.  0. -1.]。
- 下一步改进：在检查格前插入“如果上一格还是 return None，请先停下”的守门格，并给 2 个半成品提示。

### `week01/day4_euler.ipynb` — Day 4 — 复数与欧拉公式：FFT 的命根子

- 代码格运行：5/11；练习函数：euler, twiddle；TODO 数：2。
- 第一个失败：cell 17 `TypeError`: unsupported operand type(s) for -: 'NoneType' and 'complex'。
- 小朋友视角：我感觉自己刚刚还在跟着玩，下一格突然说 NoneType。我不知道这是因为我没填上一格，还是电脑坏了。
- 困难标签：TODO 后续检查缺少儿童友好提示；错误信息太技术化；需要把声音感知和数组更紧密连接。
- 已能看到的正反馈输出：cell 6: 就绪；虚数单位示例: (-1+0j)；cell 8: N = 8 / 采样点编号 n = [0 1 2 3 4 5 6 7] / 时间轴 t = [0.    0.125 0.25  0.375 0.5   0.625 0.75  0.875] / 角度 angle = [ 0.     1.571  3.142  4.712  6.283  7.854  9.425 10.996] / sin(angle) = [ 0.  1.  0. -1. -0.  1.  0. -1.]。
- 下一步改进：在检查格前插入“如果上一格还是 return None，请先停下”的守门格，并给 2 个半成品提示。

### `week01/day5_windows.ipynb` — Day 5 — 读懂 io.py / windows.py，对比窗函数

- 代码格运行：14/14；练习函数：describe_window；TODO 数：1。
- 第一个失败：通过。
- 小朋友视角：我能跑完，但 TODO 可能已经被写好了；如果让我自己解释，还是需要更慢的提示。
- 困难标签：TODO 后续检查缺少儿童友好提示；术语需要和代码动作绑定；需要把声音感知和数组更紧密连接。
- 已能看到的正反馈输出：cell 6: 就绪；cell 8: N = 8 / 采样点编号 n = [0 1 2 3 4 5 6 7] / 时间轴 t = [0.    0.125 0.25  0.375 0.5   0.625 0.75  0.875] / 角度 angle = [ 0.     1.571  3.142  4.712  6.283  7.854  9.425 10.996] / sin(angle) = [ 0.  1.  0. -1. -0.  1.  0. -1.]。
- 下一步改进：保留当前可运行性；补一个“我看懂了吗”的口头解释题，防止只是一路运行。

## 下一轮课程改良建议

1. 给所有 TODO 后面加“不要继续跑，先检查上一格是否仍是 None”的守门格。
2. 把所有 `assert` 改成儿童友好检查函数，失败时输出“回哪一格、看哪个变量”。
3. 每课新增 2 个填空式半步练习，降低从演示到完整函数的跨度。
4. 给关键术语加“这个词对应哪一行代码”的迷你卡片。
5. 在 `notebooks/README.md` 顶部补一个“如果你看到 ModuleNotFoundError 怎么办”的环境急救区。

## 结论

这套课程已经比普通数理 notebook 更有故事感，也有不少可运行实验。但从 10 岁儿童视角看，真正的主要障碍不是“数学不行”，也不只是“讲得不够多”，而是“数学到代码的翻译过程不够可见，失败时不够温柔、不够可恢复”。下一轮最有价值的改法，是把错误、TODO、断言、shape 问题都变成教学环节，而不是让它们以 Python 原生报错的形式突然出现。
