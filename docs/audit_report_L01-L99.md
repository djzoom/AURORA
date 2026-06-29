# Aurora 课程全量审计报告（L01–L99）

> 生成日期：2026-06-29
> 审计范围：L01–L99，共 99 节课
> 审计模型：claude-sonnet-4-6

---

## 一、执行摘要

全课 99 节共发现 **411 个问题**（P0 崩溃级：76，P1 内容错误：156，P2 质量瑕疵：179），**无一节课达到"零问题"标准**（clean=0），其中 39 节评为"轻微"（minor），60 节评为"严重"（major）。最突出的系统性缺陷是 **验证单元格缺少 try/except 保护**：当学生尚未实现存根函数时，`None` 返回值会直接触发 `TypeError`，导致内核崩溃，此类 P0 问题几乎贯穿整个线性代数（L09–L21）与微积分（L22–L25）模块，是最集中的高风险区域。内容层面的 P1 问题中，**学习目标写成单句而非编号列表**是最高频的格式违规，超过 50 节课未遵循课程模板；此外大量课程存在 Markdown 描述与实际代码不一致、旧版路径/课程编号未更新等叙事错误。相对最整洁的模块是 **0_foundation（L01–L03）** 和 **10_integration 收尾段（L92–L99）**，以上各节均无 P0 崩溃，但仍存在格式与内容瑕疵，说明全课尚需系统性编辑打磨。

---

## 二、各课逐条报告（L01–L33）

> 本节覆盖本次审计批次的 33 节课（L01–L25 及 L92–L99），按课程编号升序排列。

---

### L01 · Aurora 是什么——从正弦波到 Whisper，6 个月的路线图

评级：⚠️ 轻微

- **[P1]** `course_purpose` 练习字典（cell c9）共 10 个键，覆盖 `'1_complex_trig'` 至 `'10_integration'`，静默遗漏了 `0_foundation` 模块——与第 4 节声称的"11 模块"以及 cell c7 的 `nb_root.iterdir()` 扫描结果（会显示全部 11 个目录）直接矛盾。
- **[P2]** `check_imports` 存根（cell c14）含有死代码 `result = {}`：该变量被初始化后因 `return None` 而被丢弃；学生最自然的编辑方式（仅修改 `return None` 这一行）会得到空字典 `{}`，而非注释所暗示的已填充字典。

---

### L02 · 声音的数字表示

评级：⚠️ 轻微

- **[P2]** 验证单元格 c20 中 `assert abs(s.get('max_abs', 0) - 1.0) < 0.02` 无法区分正确实现 `np.max(np.abs(x))` 与错误实现 `np.max(x)`——对对称单位振幅正弦波 `make_sine(1.0, 64, 3.0)` 而言，两者均约等于 1.0，均可静默通过。

---

### L03 · 谱图（spectrogram）直觉——在学 FFT 之前先看结果

评级：⚠️ 轻微

- **[P2]** cell c11 的练习提示指示学生"在下面 Markdown cell 里写预测"，但 c11 与 c12 之间不存在任何占位 Markdown 单元格，学生无处作答。
- **[P2]** cell c10 中 `vowel_approx(t, f0, f1, f2, sr=16000)` 声明了参数 `sr`，但函数体内从未引用——死参数/未使用参数。
- **[P2]** 验证单元格（cell-13）断言的是 `plt.specgram`（matplotlib 内置函数）的输出，而非任何学生存根；全课零学生实现，`assert abs(peak_freq - 440) < 20` 不能捕获任何学生错误，不具备教学门控意义。

---

### L04 · 正弦波（Sinusoid）

评级：❌ 严重

- **[P0]** 验证单元格 `bc6dba43` 无 try/except——`np.allclose(None, array)` 在存根返回 `None` 时抛出 `TypeError: unsupported operand type(s) for -: 'NoneType' and 'float'`（已确认），而非友好的"未实现"提示。
- **[P0]** 和弦演示单元格 `c_chord_demo` 三次调用 `sinusoid()` 后计算 `(c4 + e4 + g4) / 3.0`——存根返回 `None` 时，此处抛出 `TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'`（已确认），无任何错误处理。
- **[P2]** `bc6dba43` 中的唯一断言仅测试 `sinusoid(t, A=2, f=1, phi=0)`，学生若硬编码 `return 2*np.sin(2*np.pi*t)` 即可静默通过；未覆盖非零 `phi` 或 `A`/`f` 组合变化的测试用例。

---

### L05 · 复数几何本质

评级：❌ 严重

- **[P0]** 验证单元格 `242563b5` 对存根结果执行 `mag, ph = magnitude_phase(3 + 4j)` 解包，但存根返回 `None`；无 try/except 保护，直接抛出 `TypeError: cannot unpack non-iterable NoneType object`，内核崩溃，学生看不到任何友好反馈。
- **[P1]** `cell-5` 声称"角度每增加 π/4，坐标在单位圆上逆时针移一步"，但 `cell-6` 代码实际使用 `angles = np.array([0, np.pi/2, np.pi, 3*np.pi/2])`，步长为 π/2——叙述与代码矛盾。
- **[P1]** `cell-7` 描述"均匀取 8 个角度"，但 `cell-8` 循环 `for k in range(9)` 产生 9 个值（k = 0…8），描述差一。

---

### L06 · 欧拉公式

评级：❌ 严重

- **[P0]** 验证单元格 `25a0ea10` 无 try/except：存根返回 `None` 时，`abs(twiddle(0, 0, 8) - 1) < 1e-12` 立即抛出 `TypeError: unsupported operand type(s) for -: 'NoneType' and 'int'`，内核崩溃而非给出友好提示。
- **[P2]** `cell-8` 与 `cell-16` 均遍历一组角度并逐行验证 `np.exp(1j*theta) == cos(theta) + 1j*sin(theta)`——近似重复代码，第二个单元格不带来任何新的教学内容。
- **[P2]** `cell-17` 的 Markdown 说明"参数实验：观察相位均匀递减"，给出了围栏代码块示例，但没有对应的可运行代码单元格，学生只能手动复制粘贴才能执行。

---

### L07 · 万物皆正弦——用三角波叠加合成方波

评级：❌ 严重

- **[P0]** cell `35e71676` 中的存根返回 `np.zeros_like(t)`（全零），验证单元格 `d9ec446c` 无 try/except——运行时触发 `AssertionError: 方波峰值应接近 1（含 Gibbs 过冲），实际 0.000`，无任何友好引导。
- **[P1]** 学习目标（cell `f2126435`）写成单句："目标：很多正弦叠加能拼出复杂波形；反过来，任何波形都能拆成正弦成分。"——未提供含 3+ 条具体可操作项的编号列表。
- **[P1]** `cell-11` 承诺返回值域约为 `[-π/4, π/4]`（≈ ±0.785），但 n=50 的 Gibbs 超冲实际峰值约为 0.926；断言下界 0.85 与文档范围矛盾，错误信息"peak should be close to 1"也与所述公式输出冲突。
- **[P2]** 三个空 Markdown 单元格（`cell-2`、`cell-19`、`cell-20`）——占位残留。
- **[P2]** 最后一个 Markdown 单元格（`cell-20` 为空）缺少"下一课：**L08**"独立指针，课程跳转引用仅埋于 `cell-18` 的正文散文中。
- **[P2]** 断言 `0.85 < approx.max() < 1.15` 过弱：错误实现直接返回 `np.sin(2*np.pi*t)` 时 max≈1.0 同样通过，不能验证谐波是否实际被叠加。

---

### L08 · 复数平面可视化

评级：⚠️ 轻微

- **[P1]** 标题与学习目标均宣传"共轭（complex conjugate）"为教学主题（"用 matplotlib 把单位圆旋转、共轭（complex conjugate）和相位画出来"），但笔记本正文中无任何共轭相关章节、说明或可视化——五个章节分别覆盖欧拉公式、正弦波解剖、复数点图、单位根和傅里叶级数，与承诺不符。
- **[P1]** 学习目标（"目标"）写成单句，而非含 3+ 条具体项的编号列表，违反课程模板要求。
- **[P2]** `cell-7` 与 `cell-18` 近似重复：两者均循环 `for k in range(8|9)`，计算 `theta = 2*np.pi*k/8`，求 `z = np.exp(1j*theta)` 并打印坐标——`cell-18` 仅增加了 radius 打印且止步于 k=7，未引入任何新概念。

---

### L09 · 向量代数

评级：❌ 严重

- **[P0]** 验证单元格 `1129d458` 无 try/except：存根 `scale` 返回 `None`，`np.allclose(None, [0.3, -0.6, 0.9, -1.2])` 将抛出 TypeError 并崩溃内核，而非给出友好提示。
- **[P1]** Markdown `cell-8` 声称"非对角元素 `A[0][1]=1.0` 就是这个耦合的来源"，但 `cell-7` 定义的矩阵 `A` 是对角矩阵，`A[0][1]=0.0`；紧跟其后的 `cell-9` 讲的是基向量线性组合，从未引用 `A`——该注释既不描述前一个也不描述后一个代码单元格。
- **[P2]** 三个空 Markdown 单元格（`cell-2`、`cell-24`、`cell-25`）——占位残留。
- **[P2]** 结论单元格 `cell-23` 提及"下一节关于点积"，但未给出课程编号；`cell-24`/`cell-25` 为空，笔记本中不存在"下一课：**L10**"格式指针。

---

### L10 · 点积（dot product）

评级：❌ 严重

- **[P0]** 验证单元格 `9d64d7b5` 直接调用 `round(cosine_similarity(song1, song2), 3)` 且无 try/except；存根返回 `None`，该行立即崩溃并抛出 `TypeError: type NoneType doesn't define __round__ method`，断言未被执行。
- **[P1]** 开头单元格的学习目标是两句散文（"点积 = 逐元素相乘再求和；它能衡量两个向量……"和"为什么对 Aurora 重要"），而非含 3+ 条具体可操作项的编号列表。
- **[P2]** `cell-7` 包含矩阵-向量乘法样板代码（`A = np.array([[2.0, 0.0],[0.0, 0.5]]); A @ v`），与点积主题无关，疑似从线性变换课复制而来。
- **[P2]** `cell-18` 重复相同的矩阵变换模式（对四个探针向量执行 `A = np.array([[2.0, 1.0],[0.0, 1.0]]); A @ v`）——与点积/余弦相似度内容无关。
- **[P2]** 三个空 Markdown 单元格（`cell-2`、`cell-21`、`cell-22`）——占位残留。

---

### L11 · 向量范数

评级：❌ 严重

- **[P0]** 存根 `normalize`（cell `68130fba`）返回 `None`；验证单元格（`16166fa5`）无 try/except，`np.linalg.norm(u)` 立即抛出 `TypeError: unsupported operand type(s) for *: 'NoneType' and 'NoneType'`，内核崩溃，任何断言均未被执行。
- **[P1]** TODO 提示单元格（`c7bce6f0` 和 `cell-12`）仅描述 `v / np.linalg.norm(v)`，未提及 eps 保护，但验证单元格对零向量情形断言 `not any(x != x for x in z)`——按 TODO 实现的朴素版本会产生 NaN 并使断言失败。
- **[P1]** 标题单元格的学习目标（`**目标**`）写成单句复合句，而非含 3+ 条具体项的编号列表。
- **[P2]** 零向量断言 `assert not any(x != x for x in z)` 仅检查结果非 NaN；任何非 NaN 输出（包括 eps 除法得到的 `[0., 0.]`）均可静默通过，未验证实际期望值。

---

### L12 · 矩阵乘法

评级：⚠️ 轻微

- **[P1]** 标题单元格的学习目标写成单句复合句（"矩阵乘向量（vector）= 对向量做旋转/拉伸；矩阵乘矩阵 = 把多个变换串起来。"），而非含 3+ 条具体可测量项的编号列表。
- **[P2]** 结论单元格（`cell-22`）写"下一节看特殊矩阵"，但缺少标准格式的"下一课：**L13**"指针。

---

### L13 · 特殊矩阵——正交矩阵、对称矩阵、正定矩阵

评级：⚠️ 轻微

- **[P1]** 结论单元格（`cell-22`）写"L39 验证 `ifft(fft(x)) == x` 时直接依赖这条性质"，暗示 L39 才会验证这一点——但 `cell-21` 已经执行并打印了该验证，`cell-20` 的标题甚至写着"不用等 L39"。结论与笔记本正文自相矛盾。
- **[P2]** 最后一个 Markdown 单元格（`cell-22`）无"下一课：**L14**"指针，仅说"下一节进入特征值分解"，未给出课程编号。
- **[P2]** `cell-6` 与 `a770d882` 近似重复旋转矩阵演示：两者均构造 2×2 旋转矩阵、验证 `Q.T @ Q ≈ I`、用同一测试向量 `[3.0, 4.0]` 检查 `|v| = |Qv|`，唯一差异是 theta 值。

---

### L14 · 特征值（eigenvalue）与 SVD

评级：❌ 严重

- **[P0]** 验证单元格（`7640da6`）在断言前调用 `np.round(A1, 2)`，而 A1 为 `None`（存根返回值）；NumPy 抛出 `TypeError ('NoneType has no callable rint method')`，内核崩溃，学生看不到任何有意义的错误信息。
- **[P1]** 标题单元格（`5b890fd2`）的学习目标写成单句——"**目标**：建立特征向量……、PCA……、SVD……"——而非含 3+ 条具体可测量项的编号列表。
- **[P1]** `cell e1815b5a` 声明"前导线代课完成，下一块数学（微积分/概率）"，与 `cell-25` 正确指向的下一课 L15（线性方程组，仍属线性代数）相矛盾。
- **[P2]** 章节编号"3."被使用两次："## 3. SVD：任何矩阵都能拆成……"（cell `298f0cc3`）和"## 3. ✏️ 你的任务：低秩近似"（cell `25e6f24a`），破坏了笔记本大纲结构。

---

### L15 · 高斯消元——方程组 Ax=b 的消元过程、行阶梯形与解的存在性分类

评级：⚠️ 轻微

- **[P1]** 标题和章节标题均显著宣传"行阶梯形（row echelon form，REF）"为核心主题，但笔记本中无任何单元格完成或标注 REF——cell `0352c35f` 仅执行一步消元（`R2→2R2−3R1, R3→2R3−5R1`），"REF"一词此后再未出现。
- **[P2]** 最后一个 Markdown 单元格（`cell-25`）写"下一节介绍行列式与逆矩阵"，缺少标准格式"下一课：**L16**"指针（L16 已确认为 `L16_determinant_inverse.ipynb`）。

---

### L16 · 行列式（determinant）与逆矩阵（inverse matrix）

评级：❌ 严重

- **[P0]** `cell-11`（`det_2x2` 验证）：无 try/except；`print(f'det_2x2 = {got_det:.6f}')` 在存根返回 `None` 时抛出 `TypeError: unsupported format string passed to NoneType.__format__`，内核崩溃，断言从未被执行。
- **[P0]** `cell-12`（`inv_2x2` 验证）：无 try/except；`np.round(got_inv, 6)` 在存根返回 `None` 时抛出 `TypeError: unsupported operand type(s) for *: 'NoneType' and 'float'`，内核崩溃。
- **[P2]** 结论单元格 `cell-22` 说"下一节的特征分解"，未给出课程编号；缺少标准的"下一课：**L17**"指针（下一课已确认为 `L17_eigen_diagonalization.ipynb`）。
- **[P2]** Markdown `cell-21` 用散文描述了一个"随机矩阵 vs 奇异矩阵参数实验"，但无对应代码单元格——孤立的练习占位，无实现脚手架。

---

### L17 · 特征值对角化

评级：❌ 严重

- **[P0]** 验证单元格 `bd87cdd6` 调用 `round(char_poly(A, lam), 6)` 且无 try/except，但存根（`8f1febad`）返回 `None`；`round(None, 6)` 立即抛出 TypeError，内核崩溃。
- **[P0]** 全局变量 `A` 在验证单元格 `bd87cdd6` 运行前已被 `cell-6` 和 `cell-8` 覆盖为 2×2 矩阵 `[[4.,1.],[2.,3.]]`，导致 `char_poly` 接收到错误矩阵；断言检查的是 3×3 矩阵的特征值 −3、−2、6，即便正确实现也必然失败。
- **[P1]** 单元格 `97e8c6b2` 的学习目标（`**目标**`）写成单句复合句（"掌握 Av=lambda\*v、特征方程 det(A−lambda\*I)=0；……"），而非含 3+ 条具体项的编号列表。
- **[P2]** 结论单元格 `cell-20` 写 `下一节（**L18**）`，而非标准格式 `下一课：**L18**`。

---

### L18 · 可逆性与秩

评级：❌ 严重

- **[P0]** 存根 `is_sdd`（cell `978af2b9`）返回 `None`；验证单元格 `9a32c935` 无 try/except，直接执行 `assert is_sdd(M1) and not is_sdd(M2) and not is_sdd(M3)`——等价于 `assert None`，内核以裸 AssertionError 崩溃，而非给出友好的"未实现"提示。
- **[P1]** 标题单元格的学习目标写成单句（"**目标**：判断一个方阵是否可逆的三条判据，以及「严格对角占优」这一快速充分条件。"），而非含 3+ 条具体可操作项的编号列表。

---

### L19 · 矩阵变换图解

评级：⚠️ 轻微

- **[P1]** 结论单元格（`cell-25`）写"下一节 `v2` 会用同一套图语把 SVD 和特征分解展开"——"`v2`"是已废弃的内部代号；实际下一课为 `L20_visual_factorizations.ipynb`，标准指针"下一课：**L20**"缺失。
- **[P2]** 最后 Markdown 单元格（`cell-25`）无"下一课：**LXX**"格式指针，仅包含旧版"v2"散文引用。
- **[P2]** `cell-17` 是孤立 Markdown，标题为"写代码前，先把变量表补完整"，指示学生实现 `mat_times_vec`，但对应存根不存在——`mat_times_vec` 已从 `aurora.laviz` 导入并直接调用。这是模板残留样板，会令学生困惑。

---

### L20 · 矩阵分解可视化（LU / QR / SVD）

评级：❌ 严重

- **[P1]** cell `78b37885` 引用旧课程名 `p7`，cell `f8e57a48` 代码注释重复（"与 p7 的行变换同源"）；该名称在当前 L01–L85 顺序方案中不存在。
- **[P1]** cell `7c5942eb` 引用旧课程名 `p9`（"对应你在 `p9` 学的对角化"），cell `31c61440` 代码注释也有"# p9 的同一个例子"；应指向当前 L 编号的特征分解课程。
- **[P1]** cell `e9bec99a` 引用旧课程名 `p6`（"`p6` 的 SVD，这里画出来"）；当前方案使用 L 前缀编号，该链接已失效。
- **[P1]** 结论单元格（`cell-21`）写"下一节 `v3` 将这套矩阵视角对准 Aurora 的音频核心"——"`v3`"为旧式过时引用；实际下一课为 `L21_aurora_matrices.ipynb`，标准"下一课：**L21**"指针缺失。

---

### L21 · 矩阵即滤波——DFT 矩阵 / Mel 矩阵

评级：❌ 严重

- **[P1]** 学习目标写成单句（"**目标**：把 DFT 和 mel 变换分别写成矩阵形式，验证 `W @ x` 与手写 DFT 的结果完全吻合。"），而非含 3+ 条具体项的编号列表。
- **[P1]** `cell-5` Markdown 承诺"A = diag(2, 0.5) 把 x 轴拉伸、y 轴压缩，向量长度 ||v|| 随之改变"，但紧随其后的代码单元格（`cell-6`）实现的是 DFT 矩阵 W——所承诺的对角矩阵实验从未被编写。
- **[P1]** `cell-7` Markdown 描述"A = [[2, 1], [0, 1]] 同时有拉伸和剪切——四个不同方向的探针向量"，但无对应代码单元格——这是从通用线性代数笔记本复制的孤立模板文本，从未被替换为课程相关内容。
- **[P2]** 结论单元格后有两个连续空 Markdown 单元格（`cell-21` 和 `cell-22`）——占位残留。
- **[P2]** `cell-23` 包含与 DFT 矩阵或 Mel 滤波器组无关的通用样板代码（`a = [1,2]`、`b = [3,4]`、`A = [[1,2],[0,1]]`、`a+b`、`A@a`、`a dot b`）——应删除或替换为课程相关内容。

---

### L22 · 导数

评级：❌ 严重

- **[P0]** 验证单元格 `c16216a4` 无 try/except：存根 `numeric_derivative` 返回 `None`，`abs(numeric_derivative(...) - 6.0)` 立即抛出 `TypeError: unsupported operand type(s) for -: 'NoneType' and 'float'`，内核崩溃。
- **[P1]** `fad8a754` 中的学习目标块（"目标"）写成单句（"导数就是「输入动一点，输出动多少」——曲线的斜率"），而非含 3+ 条具体可测量项的编号列表。
- **[P1]** 标题承诺"极限定义（limit definition）"，但笔记本中无任何单元格实现或陈述导数的 ε-δ/极限定义，仅覆盖中心差分数值方法。
- **[P1]** Markdown `cell-4` 说"下面的实验在 x=1.0 处计算 sin(x) 的数值导数"，但紧随其后的代码单元格（`24348482`）定义的是 `f = lambda x: x**2` 并在 x=3.0 处求值——函数和求值点均错误。
- **[P1]** Markdown `cell-6` 指示学生"确认误差与 cos(π/4)=0.7071 的差距在 1e-10 以内"，但代码单元格 `cell-7` 计算的是 `f(x)=x²` 在整数点 [-2,-1,0,1,2] 的斜率，完全不涉及 sin(x) 或 π/4。
- **[P1]** Markdown `cell-8` 说"在 [0, 2π] 上取 10 个点，逐点打印数值导数与 cos(x) 的差值"，但代码单元格 `cell-9` 使用 `f(x)=x²+2x`，在 [-3, 3] 上取 7 个点——函数、定义域、比较目标均错误。
- **[P2]** 三个热身代码单元格（`24348482`、`cell-7`、`cell-9`）均对多项式函数（x²、x²+2x）计算内联中心差分斜率——完全相同的样板模式重复三次。
- **[P2]** `c16216a4` 中的断言使用容差 `< 1e-3`，足够宽松以让前向差分等粗糙实现通过；正确的中心差分结果应以 1e-8 或更严格的容差测试。
- **[P2]** 三个空 Markdown 单元格（`cell-2`、`cell-19`、`cell-20`）——占位残留。

---

### L23 · 梯度（gradients）

评级：⚠️ 轻微

- **[P1]** 标题单元格的学习目标写成两句非正式段落（`cell ec08a282`：单行"目标：多变量函数对每个变量分别求导(偏导)，拼成一个向量=梯度。梯度指向函数上升最快的方向。"），而非含 3+ 条具体项的编号列表。
- **[P1]** Markdown `cell-16` 描述参数实验时使用"point = [1, 2] -> [2, 4]"，但实际前置代码单元格 `cell-15` 设置 `point = [3.0, 4.0]` 并断言梯度为 [6, 8]——描述与代码矛盾。
- **[P2]** `cell-7`（`f(x)=x^2` 中心差分热身）和 `cell-9`（`f(x)=x^2+2x` 斜率循环）是从 `L22_derivatives.ipynb` 逐字复制的样板代码，对梯度课程无新内容贡献。
- **[P2]** 三个空 Markdown 单元格：`cell-2`（紧随引言叙述之后）以及 `cell-19` 和 `cell-20`（结论单元格后的连续空单元格）。
- **[P2]** 主要学生验证单元格（`fd57152c`）使用 `atol=1e-2`——对于 h=1e-5 的中心差分（理论误差 O(h²)~1e-10）而言过于宽松；`cell-15` 中的次要检查正确使用了 `atol=1e-4`。
- **[P2]** Markdown `cell-16` 出现在它所描述的代码单元格 `cell-15` 之后——散文说明落后于它所介绍的实验，顺序颠倒。

---

### L24 · 链式法则（chain rule）

评级：❌ 严重

- **[P0]** 存根 `composite_derivative` 返回 `None`，验证单元格（`95883685`）执行 `assert abs(composite_derivative(x) - numeric) < 1e-3` 且无 try/except——直接崩溃，抛出 `TypeError: unsupported operand type(s) for -: 'NoneType' and 'float'`，而非友好的"未实现"提示。
- **[P1]** 学习目标（cell `298f3dd0`）写成单句（"目标：复合函数 f(g(x)) 的导数 = f'(g(x))·g'(x)——一层层连乘。"），而非含 3+ 条具体可操作项的编号列表。
- **[P1]** `cell-6` Markdown 说"观察 cos(x²)·2x 在 x 接近 0 时趋向何值"（描述的是 sin(x²) 的链式法则输出），但配对的代码 `cell-7` 计算的是普通 `f(x) = x²` 的斜率——无任何复合函数涉及；类似地，`cell-8` 说"确认链式法则在每个点都与数值差分吻合"，而 `cell-9` 测试的是 `f(x) = x² + 2x`，也是无链式法则的普通多项式。
- **[P2]** `cell-7` 和 `cell-9` 是模板样板（对 `x²` 和 `x²+2x` 的通用多项式斜率检查），与链式法则主题无关，重复了 L22/L23 中基础导数练习的风格。
- **[P2]** 三个空 Markdown 单元格（`cell-2`、`cell-19`、`cell-20`）——占位残留。

---

### L25 · 梯度下降（gradient descent）

评级：❌ 严重

- **[P0]** 验证单元格 `8a6ebfdb` 无 try/except：存根 `gd_step` 返回 `None`，第 2 次迭代时 `2*(x-3)` 变为 `2*(None-3)`，以隐晦的 `TypeError` 崩溃，而非给出友好的"未实现"提示。
- **[P1]** 标题单元格的"目标"块写成单句（"要让函数变小，就朝梯度的**反方向**走一小步，反复迭代。"），而非含 3+ 条具体学习目标的编号列表。
- **[P1]** cell `5487d725` 仍使用已退役的"Month N"命名方式："是 Month 2 线性回归（linear regression）的雏形"——应引用对应的 L 编号课程。
- **[P2]** `cell-2`、`cell-21`、`cell-22` 为完全空白的 Markdown 单元格（占位残留）。
- **[P2]** `cell-7` 和 `cell-9` 计算 `f(x)=x²` 和 `f(x)=x²+2x` 的数值斜率——与梯度下降主题无关的通用微积分样板，疑似从早期课程模板复制。
- **[P2]** `cell-17` 和 `cell-19` 近似重复梯度下降循环（对 `f(x)=(x-3)²` 从 `x=-2.0` 以 `lr=0.2` 运行 8 步相同算法；两者唯一差异是最终打印字符串）。
- **[P2]** 结论单元格 `cell-20` 的下一课指针嵌入散文（"下一节（L26）将通过……"），而非独立的"下一课：**L26**"标准行。

---

### L92 · 端到端流水线

评级：⚠️ 轻微

- **[P1]** cell-0 的学习目标写成单句（"目标：串联 Aurora 所有月份成果——实时录音 → Whisper 转写 → Podcast Agent 回答，建立对系统集成和延迟分布的直觉。"），而非含 3+ 条具体可测量项的编号列表。
- **[P1]** cell-0 标题列出"🔗 Aurora 连接：aurora.speech.whisper、aurora.rag.retriever、aurora.llm.agent"，暗示这些模块在笔记本中被使用，但 `whisper.py`、`retriever.py`、`agent.py` 均不存在于 src 目录，三者均未在任何位置被导入——所有 ASR、RAG 和 LLM 阶段均由 `time.sleep()` 模拟代替。
- **[P2]** cell-2 中 `from aurora.audio.io import read_wav` 为无条件导入（不在 try/except 内），且 `read_wav` 在笔记本中从未被调用；若 `aurora.audio.io` 未安装，该单元格会抛出裸 ImportError，尽管前面已有缺少模块的警告。
- **[P2]** 练习单元格 `0315ae52` 将所有 `stage_latency_ms` 硬编码为 `None` 并打印"请先填入实测数值（毫秒）"，无任何断言——是未经验证的占位。
- **[P2]** cell-12 有"n_trials = 3  # ✏️ TODO: 把 n_trials 改成 5"——TODO 注释在发布前未被解决。
- **[P2]** 第 4 节图示明确声明"parallel = 2500ms (−50ms)"，但 `run_pipeline_parallel` 新增了独立的 `rag_refine` await（`async_rag delay=0.03 s`），图中未体现，实际并行总时长约为 2530 ms，节省约 20 ms，而非 50 ms。

---

### L93 · MLOps 基础——W&B 实验追踪、模型版本管理、Docker 打包与部署脚本

评级：⚠️ 轻微

- **[P1]** cell 0 的学习目标写成单句（"**目标**：把 Aurora 服务打包成可复现的 Docker 容器，并用 Weights & Biases 追踪训练实验的全部超参（hyperparameter，HP）与指标。"），而非含 3+ 条具体可测量项的编号列表。
- **[P2]** 练习单元格（`48ecd68e`）无断言或最低阈值检查——打印"配置完整度：{filled}/{len(experiment_config)}"但从不断言 `filled >= N`，学生若不填写任何内容，得到 `1/12`（仅预填的 `"project"` 键）也不会收到任何失败信号。
- **[P2]** cell `99df8103` 导入 `import time, statistics`，但 `time` 在该单元格正文中从未被引用——仅 `statistics` 在 `monitor_inference_latency` 内部被使用。

---

### L94 · Aurora v1 全景 Demo——综合展示所有能力，面试材料与证据链

评级：❌ 严重

- **[P1]** cell-0 的学习目标写成单句（"打磨一个可展示的 Demo，整理 Aurora 的证据链，准备面试材料。"），而非含 3+ 条具体项的编号列表。
- **[P1]** cell-11 的 Demo 表格引用已废弃的重命名前路径（"week01/day4_euler.ipynb"、"month03/"、"month05/"），这些路径在 L01–L94 顺序重命名后已不存在；正确文件现为如 `L35_euler_fft.ipynb` 等形式。
- **[P1]** cell-6 的 WWHR 结果条目和 cell-8 的 M5 要点均写"WER（运行上方 cell 后查看实际 WER 值）"，但笔记本中不存在任何计算或显示 WER 值的单元格——占位符从未被填写。
- **[P2]** 最后 Markdown 单元格（cell-17，本课收束）无"下一课：**L95**"指针，尽管 `L95_research_papers.ipynb` 作为下一课已存在。
- **[P2]** cell `edbc1f74` 中 `readme_checklist` 字典所有值为 `None`，无条件打印"还有 6 项未填"；cell `7ca6cf26` 中 `first_blog` 同样所有值为 `None`——两者均为无自检逻辑的未填占位符。
- **[P2]** "`assert len(bullets) == 6`"（cell-8）和"`assert len(qa) == 10`"（cell-12）因为列表在其正上方被硬编码而必然为真——这些断言无法捕获任何真实错误。

---

### L95 · 研究论文入门——阅读、写作、投稿与学术合作

评级：⚠️ 轻微

- **[P1]** cell `b6ead143`："必读论文清单"表标注为"（按依赖顺序）"，将 Transformer（L83-L84）列于 Whisper（L70-L71）之前，但课程编号揭示 Whisper 实际在 L70 教授——早于 L83 的 Transformer——直接与所声称的依赖顺序及实际课程序列矛盾。
- **[P2]** cell `561b2e49`："与学术机构合作的实际路径"章节编号为"## 5."——重复了之前"## 5. 文献管理"章节的编号——导致笔记本标题序列中 6 和 7 两个编号完全缺失。

---

### L96 · 白板推导演练——FFT / CTC / 注意力机制

评级：⚠️ 轻微

- **[P1]** 结论反向引用"Attention → L83-L84"有误：L84 是 `lora.ipynb`（实现 `LoRALinear`，覆盖参数高效微调），不含任何注意力推导内容——注意力回顾引用应止于 L83。
- **[P2]** MFCC 流水线答案单元格（`a067e98e`）直接调用 `np.fft.rfft(frame0, n=n_fft)`，违反 CLAUDE.md 规定"NumPy 仅作数组容器，FFT 必须从头实现"的规则。
- **[P2]** 注意力答案单元格仅断言输出形状（`assert out.shape == (seq_q, d_v)`），无数值正确性检查——返回正确形状零矩阵的实现可静默通过。
- **[P2]** CTC 答案单元格将已完整实现的 `ctc_forward` 包裹于 `try/except NotImplementedError` 中并断言 `log_p is not None`，但由于参考实现在同一单元格内且从不抛出 `NotImplementedError`，两个守卫代码永久为死代码。

---

### L97 · 面试准备与技术沟通

评级：⚠️ 轻微

- **[P2]** 单元格 [10] 标题为"## 5. ✏️ 模拟面试练习"，重复了单元格 [6]（"## 5. 编程题准备：音频 AI 的高频手写题"）已使用的编号"## 5."；该单元格在笔记本顺序上位于第 7 和第 8 节之间，应重新编号（如 ## 8）以匹配其位置。
- **[P2]** 单元格 [7] 的 `frame_signal` 验证仅断言 `frames.shape == (4, 8)`——返回正确形状任意数组（如 `np.zeros((4,8))`）的错误实现可静默通过；检查还应验证 `frames[0]` 等于 `x[0:8]`，`frames[1]` 等于 `x[4:12]` 以捕获内容错误。

---

### L98 · 课程总结——做到了什么，还差什么

评级：⚠️ 轻微

- **[P1]** 全课章节编号已损坏：第 3 和第 5 节缺失，第 4 和第 6 节各出现两次——"## 4. 量化成果"之后紧接"## 4. 面试准备程度自评"，"## 6. 学习速度复盘"之后紧接"## 6. 公开证据清单"，最终序列为 1、2、4、4、6、6、7。
- **[P2]** 结论单元格（`ee6da094`）写"**最后一课 L99**：Aurora v2 与持续成长路线图"，而非全课统一使用的"下一课：**L99**"格式。

---

### L99 · Aurora v2 与持续成长——6 个月之后怎么走

评级：⚠️ 轻微

- **[P1]** 开篇单元格（`b4b574ee`）的学习目标写成单句复合句，而非含 3+ 条具体项的编号列表："目标：整理 Aurora v1 的能力边界，选定 Aurora v2 的延伸方向……并制定第 1 周的具体行动计划。"
- **[P2]** cell `671dd07e` 顶部运行 `import datetime`，但 `datetime` 在该单元格正文中从未被引用——未使用的导入。

---

*（第二部分 L26–L66 见下一节；第三部分 L67–L91 见续篇。）*
## 二、各课逐条报告（L34–L66）

### L34 · Nyquist 定理与混叠
评级：❌ 严重
- [P0] 验证单元 `6de0a05b` 无 try/except 保护：桩函数返回 `None`，`assert 0 <= alias <= sr/2` 立即抛出未处理的 `TypeError`，内核崩溃，无任何友好提示。
- [P1] 单元 `de71088c` 中的学习目标仅为两句平铺散文（"今日目标：理解为什么采样率……亲眼看到……"），缺少 3 条以上具体可衡量的编号列表。
- [P1] 结语单元 `cell-22` 写道"下一节（窗函数）"，但实际下一课是 `L35_euler_fft.ipynb`（欧拉公式/FFT）；窗函数为 L36，课程顺序描述有误。
- [P2] 三个空白 Markdown 单元（`cell-2`、`cell-23`、`cell-24`）遗留为模板占位残留。
- [P2] 最后一个单元无"下一课：**L35**"格式指针；结语仅以散文形式提及下一主题且引用了错误课号。
- [P2] 单元 `cell-25` 与 `cell-7` 几乎完全重复（相同的逐步正弦构建，仅频率从 2.0 改为 1.0），未添加任何与混叠主题相关的内容。

### L35 · 欧拉公式与 FFT 旋转因子
评级：❌ 严重
- [P0] 验证单元 `b835ad40` 无 try/except：两个桩函数均返回 `None`，`z = euler(theta)` 得 `None` 后，首个断言 `np.max(np.abs(z - np.exp(1j*theta)))` 立即抛出 `TypeError`，内核崩溃，学生未见任何友好提示。
- [P1] 标题单元学习目标为单句内联文字（"今日目标：用 cos θ + i·sin θ 手动拼出 euler(θ)，再导出 twiddle(k, n, N)……"），缺少 3 条以上具体可测试的编号列表。
- [P2] 三个空白 Markdown 单元（`cell-2`、`cell-28`、`cell-29`）为模板占位残留。
- [P2] 最后一个 Markdown 单元（`cell-29`）为空，缺少"下一课：**L36**"指针；结语散文（`cell-27`）虽提及 L36，但标准终止指针缺失。
- [P2] `twiddle` 断言 `assert abs(twiddle(0, 0, 8) - 1) < 1e-12` 仅测试 k·n=0（指数恒为 0，结果恒为 1），符号反向的错误实现或返回常数 1 的桩均可通过；文档字符串给出的示例 `twiddle(1, 2, 8) ≈ 0-1j` 从未被断言。
- [P2] 末尾 `cell-30` 是孤立的正弦波样板代码（sample_rate/duration/freq 设置与 np.sin），与 euler 或 twiddle 毫无关联，疑为复制粘贴模板残留。

### L36 · 窗函数（Window Function）原理
评级：⚠️ 轻微
- [P1] 桩函数（单元 `3e86ddcb`）的 TODO 注释写"打印 name、长度 len(w)、首尾值、峰值与峰值下标"（仅打印），但验证单元解包四元组 `first, last, peak, peak_idx = result`；学生只按 TODO 操作将永远不知道需要返回任何内容。
- [P1] 标题单元（`57c17e9e`）学习目标为两段短散文，而非 3 条以上具体可衡量的编号列表。
- [P2] 三个空白 Markdown 单元（`cell-2`、`cell-29`、`cell-30`）为模板占位残留。
- [P2] 结语单元（`cell-28`）仅以"下一节进入 FFT 实现"提及下一课，无"下一课：**L37**"标准格式指针；后续两个单元为空，笔记本以一个游离代码单元结尾。
- [P2] 最后一个代码单元（`cell-31`，"小检查：从短序列开始"）重复了 `cell-7` 已有的逐步正弦生成逻辑，与窗函数主题无关——模板样板未清理。

### L37 · DFT O(N²) 朴素实现
评级：⚠️ 轻微
- [P1] 单元 0 学习目标为单句（"**目标**：实现 O(N²) 朴素 DFT，理解每个频点 = 信号与旋转因子序列的点积"），缺少 3 条以上具体编号条目。
- [P2] 计时单元（`cell-15`）在桩函数未实现状态下无保护地调用 `naive_dft`——全零桩静默运行，打印出的 N² 计时比率为无意义噪声。
- [P2] 结语单元（`cell-17`）将下一课引用嵌入散文内联（"下一课（L38）"），而非独立格式指针"下一课：**L38**"。

### L38 · FFT 蝶形分治
评级：⚠️ 轻微
- [P1] `cell-0` 的"目标"块为单个复合句，而非 3 条以上具体学习目标的编号列表，违反课程规范。
- [P1] 中间链接单元（`fcdf275c`）引导学生打开"L42 · FFT 图形化"，但结语 `cell-17` 正确注明"下一课（L39）"——两处指针相互矛盾，L39 才是顺序上的下一课。
- [P2] `cell-16` 的实验函数 `fft_count` 调用自包含参考实现 `butterfly_counted`，而非学生的 `butterfly` 桩，因此无论学生进度如何，四行"FFT正确=True"始终打印，给学生以虚假信心。
- [P2] `cell-17` 结语末尾有孤立词"更新。"——已发布课文中遗留的草稿编辑痕迹。

### L39 · 从零手写 FFT — Cooley-Tukey 递归实现
评级：⚠️ 轻微
- [P1] `cell-0` 的"**目标**"为单句（"手写 Cooley-Tukey 递归 FFT，让 tests/audio/test_transforms.py 全绿。"），缺少 3 条以上具体学习目标的编号列表。
- [P2] `cell-2` 导入 `aurora_fft`（`from aurora.audio.transforms import fft as aurora_fft`），但该名称在笔记本中从未使用——无效导入，会令学生困惑。
- [P2] `cell-15`（速度基准测试）无桩保护地无条件调用 `my_fft(x_bench)`；桩返回 Ellipsis 时，`t_my` 接近零，打印出的 `t_naive/t_my` 比率毫无意义，而非提示"尚未实现"。
- [P2] `cell-17`（最后一个 Markdown）将"下一课 L40"嵌入散文句内，而非独立格式指针"下一课：**L40**"。

### L40 · 频谱分析实战
评级：❌ 严重
- [P0] `cell-13`（双峰定位实验单元）调用 `freqs = frequency_bins(N, sr)` 后立即执行 `freqs[top2_idx].astype(int)`，无 try/except 保护；`cell-10` 的桩返回 `...`（Ellipsis），导致该行崩溃抛出 `TypeError: 'ellipsis' object is not subscriptable`——`cell-11` 正确处理了 Ellipsis，但 `cell-13` 未作保护。
- [P1] 笔记本标题承诺涵盖"相位谱（phase spectrum）"主题，但笔记本中无任何单元计算或讨论相位谱；实际仅涉及幅度谱、功率谱和 dB 谱。
- [P1] `cell-0` 的学习目标为单句（"用实现好的 FFT 分析真实信号，计算频率轴、理解 bin 间距与实信号对称性。"），而非 3 条以上具体可衡量的编号列表。

### L41 · 加窗 FFT 完整流程
评级：⚠️ 轻微
- [P1] `cell-0` 学习目标为单句（"理解信号截断导致的频谱泄漏，掌握 Hann 窗的压制原理，完成 windowed_fft 并用它观察真实旁瓣差异。"），缺少 3 条以上具体编号条目。
- [P2] `cell-13`（参数实验）调用 `windowed_fft` 无 Ellipsis 保护——`windowed_fft(x, window_type="rectangular")[:N//2]` 在桩未实现时抛出 `TypeError: 'ellipsis' object is not subscriptable`。
- [P2] 结语 `cell-14` 仅以散文提及下一课（"下一课（L42 / FFT 图形化）"），缺少所需独立格式粗体指针"下一课：**L42**"。

### L42 · FFT 图形化
评级：❌ 严重
- [P1] 标题声称涵盖"纯音 / 和弦 / 噪声的频谱形态对比"，但笔记本中根本没有噪声频谱章节；实际仅展示纯音（440 Hz）与双音和弦（440+880 Hz）。
- [P1] `cell-9`（参数实验 Markdown）写明"duration=0.05（50 ms，N=400）"及对应 bin 估算，但实际代码（`cell-10`）使用 duration=0.032（N=256）；N=400 不是 2 的幂次，会导致 aurora 的 FFT 失败，且两套参数下的 bin 估算均在数值上有误。
- [P1] `cell-0` 学习目标为单句（"用图直觉建立 DFT 矩阵、蝶形网络、频谱对称性的视觉记忆……"），缺少 3 条以上具体可衡量的编号列表。
- [P2] `cell-6` 定义了 `y_pos` 和 `current_y` 变量，但在该单元中从未被读取，留下无效代码，令读者困惑。
- [P2] 结语单元（`cell-11`）将下一课内联提及为"下节 `L43_stft.ipynb`"，未使用课程模板要求的"下一课：**L43**"标准格式。

### L43 · STFT 原理 — frame_signal
评级：⚠️ 轻微
- [P1] `cell-0` 学习目标为单个长句（"理解……掌握……动手实现……"），而非 3 条以上独立陈述的具体编号条目。
- [P2] 结语单元（`cell-14`）以散文提及下一课（"下一课（L44）将实现……"），缺少标准独立格式粗体指针"下一课：**L44**"。

### L44 · 亲手写 STFT
评级：⚠️ 轻微
- [P1] 标题单元（`cell-0`）的"**目标**"为单句（"从零实现完整的 STFT，使输出与 `aurora.audio.stft.stft()` 在数值上严格一致（`atol=1e-9`）。"），缺少 3 条以上具体技能的编号列表。
- [P2] 结语单元（`cell-14`）的下一课指针嵌入段落内——"下一课（L45）将在 STFT 复数矩阵上生成声谱图……"——而非符合课程模板标准的独立格式行"下一课：**L45**"。

### L45 · 声谱图（Spectrogram）生成
评级：❌ 严重
- [P0] `cell-10` 桩使用 `S = ...`、`A = ...`、`dB = ...`（Ellipsis）而非抛出 `NotImplementedError`；学生运行未实现代码时，`np.abs(Ellipsis)` 立即抛出 `TypeError`，而非友好的"未实现"提示。
- [P0] `cell-11` 验证的 try/except 仅捕获 `NotImplementedError`，Ellipsis 桩产生的 `TypeError` 未被捕获，传播至内核并导致崩溃，任何诊断信息均未打印。
- [P0] `cell-11` 断言（`assert dB_ref.max() > -20` 与 `assert dB_ref.shape[0] == 513`）完全作用于来自参考实现 `_stft` 的 `dB_ref`，而非学生的 `plot_spectrogram`；即使学生函数错误或未实现，断言始终通过。
- [P1] 标题承诺"pcolormesh 热力图"，但笔记本中从未调用 `pcolormesh`；所有图均用 `plt.imshow` 绘制，标题描述了未出现在课程中的功能。
- [P1] `cell-0` 学习目标为单个长句（"把 STFT 复数矩阵转成幅度谱……"），而非 3 条以上具体可衡量的编号列表。
- [P2] `cell-14`（最后一个 Markdown 单元）仅以散文提及"下节课"，缺少必要的独立"下一课：**L46**"指针行。

### L46 · Mel 频率尺度
评级：❌ 严重
- [P0] `cell-10` 桩使用 `pass`（返回 `None`）；`cell-11` 首个断言 `abs(hz_to_mel(700) - 781.2) < 0.5` 立即抛出 `TypeError`（`NoneType` 与 `float` 不可相减），内核崩溃，无友好错误提示。
- [P1] `cell-0` 学习目标为单句（"实现 Hz↔Mel 转换和三角滤波器组……理解为什么 Mel 特征比线性频谱更适合 ASR"），缺少 3 条以上具体编号条目。
- [P1] 结语 `cell-17` 称"下一课（L47）将从零亲手实现 mel_filterbank"，但 mel_filterbank 已是本课的主要编程练习（`cell-13`），L47 实际实现的是 `log_mel_spectrogram`——下一课描述自相矛盾。
- [P2] `cell-13` 的 mel_filterbank 桩返回 `np.zeros((n_mels, n_bins))`；`cell-14` 中的形状断言和非负断言对零桩均静默通过——只有 `max(axis=1)==1.0` 检查能捕获未实现的函数。

### L47 · 亲手写 Mel 滤波器
评级：⚠️ 轻微
- [P1] 标题副标题承诺"mel_filterbank 从公式到 NumPy"，但学生练习（`cell-10` TODO）是实现 `log_mel_spectrogram`，后者只是调用现有的 `aurora.audio.mel.mel_filterbank`——filterbank 本身从未在本笔记本中从头实现。
- [P1] `cell-0` 学习目标为单句（"从零搭建 log-mel 流水线：STFT → 功率谱 → Mel 滤波 → log 压缩，得到 `(n_frames, n_mels)` 矩阵"），而非 3 条以上基于技能的具体编号条目。
- [P2] `cell-13`（n_mels 参数实验）调用 `log_mel_spectrogram` 后立即访问 `feat.T`，无 `None` 保护——若学生在实现桩之前运行此单元，会抛出 `AttributeError` 而非有意义的提示信息。

### L48 · 时频图解 — 线性谱 / Mel 谱 / 对数 Mel 谱三者视觉对比
评级：⚠️ 轻微
- [P1] `cell-0` 的"目标"为单句（"用图建立时频分析的完整视觉记忆——分帧、STFT热力图、Mel滤波器组、log-mel。"），而非 3 条以上具体学习目标的编号列表。
- [P1] `cell-8` 中 `M_db` 的注释有误：`M_db = (10 * np.log10(M + 1e-8)).T  # (n_frames, n_mels) → (n_frames, n_mels)`——经 `.T` 转置后形状实际为 `(n_mels, n_frames)`，注释声称的目标形状有误。
- [P2] 最后一个 Markdown 单元（`cell-9`）将下一课指针嵌入散文（"下节（**L49**）将在……"），而非独立"下一课：**L49**"行。

### L49 · DCT-II 实现
评级：❌ 严重
- [P0] `cell-13`（实验单元）调用 `X_dct = dct_ii(x_mel)` 后立即传递给 `_idct_ii_ref(X_dct)`，无 `None` 保护；桩返回 `None`，`len(None)` 抛出 `TypeError`，无友好的"未实现"提示。
- [P1] `cell-5` 声称"`M @ M.T / N` 应等于 2 倍单位阵（除第 0 行/列外）"——实际对角元素（k>0）为 N/2，即 `M @ M.T / N = 0.5 × I`，而非 `2 × I`；`cell-6` 展示了正确值（N/2=4，N=8），与该散文声明直接矛盾。
- [P1] `cell-0` 学习目标为单句（"从零实现 DCT-II，理解它如何把相关的 Mel 特征向量压缩成近似独立的倒谱系数"），而非 3 条以上具体可衡量的编号列表。
- [P2] `cell-14`（最后一个 Markdown）将下一课指针嵌入散文（"下一课（L50）"），而非标准"下一课：**L50**"粗体格式。

### L50 · MFCC 完整流水线
评级：❌ 严重
- [P0] `cell-11`（验证单元）无 try/except，立即在 `out.shape` 处崩溃，抛出 `AttributeError: 'NoneType' object has no attribute 'shape'`——`cell-10` 的未实现桩返回 `None`；学生在填写任何 TODO 前运行检查，只会看到神秘的回溯信息，而非友好的"未实现"提示。
- [P1] `cell-0` 学习目标为单句（"**目标**：串联所有 DSP 步骤，手工实现完整 MFCC 提取，结果与 `aurora.audio.mfcc.mfcc()` 数值对齐。"），而非 3 条以上具体可衡量的编号列表。
- [P2] `cell-14`（最后一个 Markdown）将下一课指针写为散文"下一课（L51）将……"，而非标准"下一课：**L51**"粗体链接格式。

### L51 · MFCC 工程实战
评级：⚠️ 轻微
- [P1] `cell-0` 学习目标为单句（"目标：用 aurora.audio 完整流水线处理真实（或仿真）语音，画出四层表示，目视验证元音谐波与辅音瞬态"），而非 3 条以上具体可衡量的编号列表。
- [P2] `cell-2` 从 `aurora.audio.io` 导入 `sine`（`from aurora.audio.io import read_wav, sine, write_wav`），但 `sine` 在笔记本中从未调用——无效导入，易令读者困惑。
- [P2] 结语单元（`cell-11`）将下一课指针嵌入散文（"下一课（L52）是 Audio Core 完结……"），而非独立规范的"下一课：**L52**"行。

### L52 · Audio Core 完结
评级：⚠️ 轻微
- [P1] `cell-0` 的"**目标**"为单句（"跑通 tests/audio/ 全部测试，分析性能，完成 Month 1 通关标志。"），而非 3 条以上具体学习目标的编号列表。
- [P2] `cell-11`（最后一个 Markdown）将下一课指针以散文嵌入（"下一课（L53）将用图形化方式展示……"），而非标准独立格式"下一课：**L53**"。

### L53 · MFCC 图形化
评级：❌ 严重
- [P1] 学习目标（`cell-0`）为单句（"**目标**：用图展示 DCT 如何压缩 Mel 频谱，直观理解 MFCC 前几个系数的含义。"），而非 3 条以上具体编号条目。
- [P1] 标题承诺四步可视化流水线"波形 → 声谱图（spectrogram） → Mel 谱 → 倒谱系数，逐层图示"，但笔记本无波形图、无 STFT/声谱图；内容直接从 log-mel 阶段开始，标题描述与实际内容不符。
- [P1] 结语单元（`cell-9`）描述流水线为"mel_spectrogram → power_to_db → dct_ii → 截取前 n_mfcc 列"，但笔记本代码始终使用手工计算 `10 * np.log10(mel_s + 1e-10)`，从未调用 `power_to_db`——结语描述与笔记本实际演示不一致。
- [P2] `cell-2` 从 `aurora.audio.io` 导入 `sine`、从 `aurora.audio.mfcc` 导入 `mfcc`，但两者在笔记本中均未使用——`cell-6` 和 `cell-8` 直接调用 `np.sin(...)` 和 `chirp()`。

### L54 · Value 计算图 — Autograd
评级：❌ 严重
- [P0] `cell-10` 中所有桩方法均使用裸 `pass`（返回 `None`），`cell-11` 首个断言 `c = a + b; assert c.data == 5.0` 立即崩溃抛出 `AttributeError: 'NoneType' object has no attribute 'data'`——无 try/except 保护。
- [P1] `cell-0` 学习目标为单句（"实现计算图的最小单元 Value……打地基"），而非 3 条以上具体可衡量的编号列表。
- [P1] 结语 `cell-14` 将下一课引用为"下一节（M2-A2）"——旧命名惯例；实际下一课是 `L55_forward_pass.ipynb`。
- [P2] 最后一个 Markdown 单元（`cell-14`）缺少标准"下一课：**L55**"指针；M2-A2 引用不符合全课程通用的 L 编号格式。

### L55 · 前向传播
评级：❌ 严重
- [P0] `cell-10` 桩使用 `...`（Ellipsis）作为占位符——`out = Value(...)` 与 `t = ...`——而 `Value.__init__` 立即调用 `float(data)`，`float(Ellipsis)` 抛出 `TypeError: float() argument must be a string or a real number, not 'ellipsis'`，而非友好的"未实现"提示；`__pow__`、`relu`、`tanh`、`exp` 四个方法均受影响。
- [P0] 验证 `cell-11` 包含裸 `assert` 调用，无 try/except，Ellipsis 桩产生的 `TypeError`（或若 `cell-10` 未运行则为 `NotImplementedError`）直接崩溃内核，而非打印诊断信息后继续。
- [P1] `cell-0` 学习目标为单段散文（"**目标**：为 `Value` 类补全……"），而非 3 条以上具体可衡量的编号列表。
- [P1] `cell-10` 中 `__pow__` 脚手架展示 `out = Value(...)` 仅传一个参数，`cell-9` 的提示同样省略了 children（`out = Value(self.data**n)`）；学生按此操作会生成 `_prev = set()` 的节点，静默断开 `self` 与计算图的连接，导致任何含 `**` 的链式反传均被破坏——但 `cell-11` 的孤立单节点测试仍通过，隐藏了这一 bug。
- [P2] 最后一个 Markdown 单元（`cell-14`）仅以散文嵌入下一课指针（"下一节（**L56**）……"），而非独立"下一课：**L56**"行。

### L56 · 反向传播（Backpropagation）手推
评级：⚠️ 轻微
- [P1] `cell-0` 学习目标为单句（"目标：实现 Value.backward()，从输出节点出发……"），而非 3 条以上具体编号条目。
- [P1] 结语单元（`cell-14`）使用旧命名"下一节（M2-A4）将在此基础上组装 MLP"——下一课实际为 `L57_mlp.ipynb`，M2-A4 命名已废弃。

### L57 · MLP 从零搭建
评级：❌ 严重
- [P0] `cell-12` 验证无 try/except：未实现的桩 `MLP.parameters()` 通过 `pass` 返回 `None`，`len(params)` 抛出 `TypeError: object of type 'NoneType' has no len()`，内核崩溃，无友好错误信息。
- [P0] `cell-14` 参数实验单元无 try/except：`MLP.__init__` 使用 `pass`，`self.layers` 从未被设置；`for i, layer in enumerate(m3.layers)` 立即抛出 `AttributeError: 'MLP' object has no attribute 'layers'`，内核崩溃。
- [P1] `cell-0` 的"**目标**"为单句（"实现 `Neuron → Layer → MLP`，每层支持前向传播（forward pass）和反向传播（`backward()`）。"），而非 3 条以上具体学习目标的编号列表。
- [P1] `cell-0` 将 PyTorch 后续课交叉引用为 `p3_nn.ipynb`——旧命名惯例；当前顺序名称为 `L61_pytorch_nn.ipynb`。
- [P2] `cell-15`（结语）将 L58 引用嵌入散文（"下一节 `L58_training_loop.ipynb` 将用……"），无专属"下一课：**L58**"标准格式指针行。

### L58 · 训练循环（Training Loop）
评级：❌ 严重
- [P0] 桩在 `cell-10` 中设置 `loss = None`，随后无条件调用 `loss.data`（`loss_history.append(loss.data)`），第 1 轮 epoch 即崩溃抛出 `AttributeError: 'NoneType' object has no attribute 'data'`；`cell-11` 对 `train()` 调用无 try/except 保护，内核硬崩溃，学生未见任何友好错误信息。
- [P1] 笔记本中无任何编号学习目标列表——`cell-0` 仅有单句"**目标**：用自制 autograd 训练一个 MLP，拟合二维月牙形分类问题，画出损失曲线，彻底理解训练循环的每一步"，而非所需的 3 条以上具体编号条目。
- [P2] 结语 `cell-14` 末尾含乱码残留片段"……为后续 nn.Module 构建做好基础。ch）随机梯度下降。"——"ch）随机梯度下降。"是真正结尾句后遗留的编辑垃圾。

---
*L59–L66 的审计数据不在本批次提供范围内，将在后续报告中补充。*
# Aurora 课程审计报告 · 第三部分

统计（全课程）：P0=76，P1=156，P2=179 | 良好=0，轻微=39，严重=60

---

## 二、各课逐条报告（L67–L99）

### L67 · 编辑距离（Edit Distance）
评级：⚠️ 轻微
- [P2] Cell-2 导入 `numpy as np`，但全文无任何 `np.` 用法——未使用的导入。
- [P2] `edit_distance`、`wer`、`alignment` 三个函数逐字复制了完整的 DP 算法，`wer` 和 `alignment` 应委托给 `edit_distance`，而非各自重写一遍。
- [P2] 末尾 Markdown 单元格（cell-11）以段落内嵌方式引用下一课："下一课（L68）"，不符合标准独立指针格式"下一课：**L68**"。

---

### L68 · CTC 对齐原理 — blank 符号、单调路径与标签折叠
评级：❌ 严重
- [P0] 验证单元格（cell 11）存在无条件 `print('✅ ctc_greedy_decode([a ∅ ∅ b b ∅ c]) =', result, '= [a, b, c]')`，位于 if/else None 判断之外——当 stub 返回 None 时，先打印 ⬜ 警告，紧接着无断言地打印假阳性 ✅。
- [P0] 同一验证单元格接着执行 `assert ctc_greedy_decode(logits_blank) == []`，无 None 守卫——stub 返回 None，`None == []` 为 False，引发 AssertionError，崩溃内核。
- [P0] 实验单元格（cell 13）无条件调用 `len(ctc_greedy_decode(logits_exp, blank=0))`——stub 返回 None，`len(None)` 引发 TypeError，崩溃内核。
- [P1] cell 0 学习目标是单句话（"理解 CTC 的核心思想——blank 符号＋去重规则＋路径求和……"），而非 3 条以上的编号列表。
- [P2] cell 2 中 `import torch` 无 try/except ImportError 保护，torch 是重型可选依赖。
- [P2] 结束单元格（cell 14）将下一课引用嵌入段落（"下一节（L69）"），且附加了不相关的 Whisper 交叉熵说明，未标注该内容是否出现在 L69 中。

---

### L69 · CTC 前向算法
评级：❌ 严重
- [P0] cell 6（验证）直接调用 `ctc_forward`，无 try/except；stub 以 `raise NotImplementedError('TODO')` 结尾，崩溃内核，无任何断言执行。
- [P0] cell 8（复杂度展示）在裸循环中调用 `ctc_forward`，无 try/except，同样崩溃内核。
- [P2] 断言 `assert np.isfinite(lp)` 和 `assert lp < 0` 过弱：返回预初始化哨兵值 `NEG_INF = -1e30` 的 stub 可静默通过，因为 -1e30 既有限又为负。

---

### L70 · Whisper 架构解析 — Log-Mel 输入、Transformer Encoder-Decoder、多任务头
评级：❌ 严重
- [P0] cell 11 验证无 try/except：stub `whisper_preprocess` 以 `pass` 结尾（返回 None），`feat.shape` 立即引发 `AttributeError: 'NoneType' object has no attribute 'shape'`，崩溃内核。
- [P1] cell 5 Markdown 存在自相矛盾的错误数学声明——"原论文实际用的 stride=2×2，总降采样 4 倍"断言降采样到 750 步，但同一单元格随即纠正"Whisper 官方代码的输出是 1500 步"；实际 Whisper Conv1d 使用 stride=1 再 stride=2，共 2 倍降采样。
- [P1] cell 6 打印语句错误：`tuple(torch.zeros(1,80,3000).shape)` 等于原始输入形状 `(1, 80, 3000)`，被标注为"Conv1 输出"，隐藏了实际 conv1 输出形状 `(1, 512, 3000)`，使打印的形状链条完全误导。
- [P1] cell 0 学习目标是单句话（"读懂 Whisper 论文的架构……"），而非 3 条以上的编号列表。
- [P2] cell 2 顶层导入 `torch` 无 try/except ImportError 保护。
- [P2] 结束单元格（cell 14）以一个残缺悬挂句收尾，开头带有孤立反引号："\` 加载的编码器，观察 cross-attention 权重……"——明显是早期草稿的遗留片段。

---

### L71 · Whisper 解码策略 — 贪婪解码与 beam search 从原理到实现
评级：❌ 严重
- [P0] cell-5 在定义 stub（`raise NotImplementedError("TODO")`）后立即调用 `greedy_decode(prompt)`，无 try/except——运行该单元格崩溃内核。
- [P0] cell-7 同样直接调用 `beam_search(prompt, width=2)`，stub 同样 raise NotImplementedError——内核崩溃。
- [P1] cell-7 的 beam search 验证部分零断言；即使 NotImplementedError 被修复，任何不崩溃的错误实现都会静默"通过"，因为输出仅为无条件打印语句，无任何正确性检查。
- [P2] cell-8 结束单元格使用非正式表述"下一步 L72"，而非标准加粗指针"下一课：**L72**"。

---

### L72 · Whisper 微调 — LoRA 低秩注入 vs 全参数，中文/方言数据适配实战
评级：❌ 严重
- [P0] cell 6 调用 `load_dataset('librispeech_asr', 'clean', split={..., 'test': 'test'})`，但 'clean' 配置中该 split 名称应为 'test.clean'，运行时以 SplitNotFoundError 崩溃。
- [P1] cell 0 学习目标（'目标'）是单句话（"用 HuggingFace Trainer + LoRA … WER 压到 5% 以下"），而非 3 条以上编号列表。
- [P1] cell 0 标题承诺"中文/方言数据适配实战"，但正文全程使用英文 LibriSpeech 数据，无任何中文或方言内容。
- [P2] cell 2、6、8 顶层导入 `transformers`、`peft`、`datasets`、`torch`、`jiwer` 等重型可选库，均无 try/except ImportError 保护。
- [P2] cell 6 使用 `Seq2SeqTrainingArguments(evaluation_strategy='steps', ...)`，该参数在 transformers ≥ 4.46 中已重命名为 `eval_strategy`，当前版本会引发 TypeError。

---

### L73 · WER 评估
评级：⚠️ 轻微
- [P1] 标题承诺"jiwer 对比逐句分析"，但 jiwer 从未被导入或使用，也不存在任何对比章节。
- [P1] 学习目标（cell 0）是单句行内句（"**目标**：系统评估……定位薄弱点。"），而非 3 条以上编号列表。
- [P2] 验证断言 `assert 0.0 <= result["wer"] <= 2.0` 过弱——注释中明确期望值为 0.40，但从未实际断言。
- [P2] 验证断言 `assert len(result["worst_examples"]) <= 5` 允许空列表通过，掩盖了跳过填充 worst_examples 的 stub。
- [P2] 末尾 Markdown 单元格（cell 14）仅以行内形式提及 L74（"下一节（L74）……"），无独立"下一课：**L74**"指针行。

---

### L74 · ASR 错误分析 — 替换/删除/插入模式，从 WER 到可改进方向
评级：❌ 严重
- [P0] cell-2 中 `wer()` 函数是完整的参考实现（无 raise NotImplementedError），但验证单元格（id=5b9819a7）将其包裹在 `try/except NotImplementedError` 中——守卫永远不会触发，每个断言总是通过，学生拿到假绿灯却无任何代码需要填写。
- [P1] 学习目标第 2 条承诺"统计最高频的错误模式混淆矩阵（confusion matrix）"，但全文从未构建或展示混淆矩阵，仅有 Counter.most_common() 的文本打印。
- [P1] cell-8 将 L75 描述为"把这些分析做成可视化仪表板"，但 L75（L75_visual_asr.ipynb）实际内容是 CTC 对齐路径与 Whisper cross-attention 热力图——下一课预告不准确。
- [P2] 末尾 Markdown 单元格（cell-10）以行内形式引用 L75（"下一课（L75）将……"），而非标准加粗指针"下一课：**L75**"。

---

### L75 · 训练可视化（Visual ASR）
评级：❌ 严重
- [P1] 学习目标（cell 0）是单句话——"目标：用图直观理解 CTC 多路径对齐、Whisper 解码器的 cross-attention 热力图、以及 WER 误差的结构"——而非 3 条以上编号列表。
- [P1] cell 0 目标和标题均承诺"WER 误差的结构"可视化，但正文中无任何 WER 相关内容（指标定义、误差分解或图表）。
- [P1] 标题承诺"波形→声谱图→token→文字路径可视化"，但没有任何波形或声谱图；正文仅包含合成 CTC lattice 和合成 cross-attention 热力图。
- [P1] 结束单元格（cell 9）描述"下一课：L76 音乐理论基础——从音阶、和弦到调性"，但 L76 的实际标题是"音乐理论速成 — 音高、音程、色度轮与十二平均律"，涵盖音高/音程/色度，并非和弦或调性。

---

### L76 · 音乐理论速成 — 音高、音程、色度轮与十二平均律
评级：❌ 严重
- [P0] cell 4 验证块调用 `midi_to_freq(midi)` 和 `freq_to_midi(440.0)`，无 try/except；两个 stub 均 raise `NotImplementedError('TODO')`，运行该单元格立即崩溃内核。
- [P0] cell 6 验证循环调用 `chroma_from_freq(freq)`，无 try/except；stub raise `NotImplementedError('TODO')`，第一次迭代即崩溃内核。
- [P1] 标题承诺"音程"（intervals）为主题，但正文中无任何音程章节——该概念仅作为半音比率隐含在汇总表中。
- [P2] cell 6 验证在 f-string 内打印 `'✅' if pc==expected_pc else '❌'`，但无任何 `assert`——错误的 `chroma_from_freq` 实现打印 ❌ 后执行仍正常继续，无报错。

---

### L77 · 音乐特征工程 — chroma、RMS 能量、ZCR
评级：❌ 严重
- [P0] cell-13 中 `rms_envelope` stub 硬编码 `n_frames = 0` 并返回 `np.zeros(0)`；cell-14 对空数组调用 `rms_sil.max()`，引发 `ValueError: zero-size array to reduction operation maximum which has no identity`，崩溃内核，无 try/except。
- [P0] 同一 `np.zeros(0)` 返回值导致 `assert np.allclose(rms_const, 0.5, atol=1e-6)` 静默通过：`np.allclose(np.zeros(0), 0.5)` 由于空数组的空真（vacuous truth）返回 True，正确性检查从未真正测试任何实现。
- [P1] 标题（cell-0）承诺"chroma、RMS 能量、ZCR"，但零交叉率（ZCR）在正文中从未被提及、定义或实现——第三个命名特征完全缺失。
- [P1] cell-0 学习目标是单句话（"实现三个音乐特有特征——chroma 向量调性、RMS 能量包络、节拍检测"），而非 3 条以上独立编号项。
- [P2] 末尾 Markdown 单元格（cell-17）仅以行内形式提及 L78（"下一节（**L78**）将从零实现……"），缺少独立"下一课：**L78**"指针行。

---

### L78 · 节拍追踪从零实现
评级：❌ 严重
- [P0] cell 5 在 stub（raise `NotImplementedError("TODO")`）之后立即调用 `env = my_onset_envelope(signal, SR)`，无 try/except——在学生实现函数之前运行该单元格，异常未被捕获，内核崩溃。
- [P0] cell 7 调用 `bpm, beats = my_beat_track(signal, SR)` 后立即执行 `assert abs(bpm - 120) < 15`，无 try/except——`my_beat_track` 内部调用未实现的 `my_onset_envelope`，NotImplementedError 向上传播，崩溃内核。
- [P1] cell 9 汇总表将 L79 描述为"有了 chroma + RMS + BPM 特征，就可以构建音乐嵌入向量"，但 L79 实际实现的是用三元组损失训练的 CNN MusicEncoder——描述不准确且与其下方段落矛盾。
- [P2] cell 7 的 `assert abs(bpm - 120) < 15` 对设计为恰好 120 BPM 的合成信号容忍 ±15 BPM 误差，过弱——返回 107 或 134 BPM 的实现会静默通过。
- [P2] 结束单元格使用"下一课（L79）将用对比学习……"，而非标准"下一课：**L79**"格式。

---

### L79 · 音乐嵌入向量 — 对比学习
评级：⚠️ 轻微
- [P1] cell-0 学习目标是单句话（"训练一个对比学习音乐编码器……"），而非 3 条以上编号列表。
- [P1] 结束单元格 cell-14（"本课收束"）将下一课引用为"下一节 **M4-MU3**"——旧命名体系——而非序列号 L80。
- [P2] cell-2 顶层无条件导入 torch 和 torch.nn，无 try/except ImportError 保护。
- [P2] 末尾 Markdown 单元格（eadb2c04）使用非正式表述"打开 L80"，而非标准"下一课：**L80**"格式。

---

### L80 · 向量相似度检索
评级：⚠️ 轻微
- [P1] cell-0 学习目标是单句话（"目标：用 L2 归一化 embedding 做余弦相似度搜索，找最相似的 k 首歌。"），而非 3 条以上编号列表。
- [P1] 结束单元格（cell-14）将下一课引用为"MU4"（旧命名体系）而非当前序列号"L81"："下一节 MU4 将在此基础上构建完整的播放列表推荐流水线。"
- [P2] 末尾 Markdown 单元格（cell-14）无标准"下一课：**L81**"格式指针；引用埋于段落且名称错误。

---

### L81 · 音乐推荐系统 — 用户喜好→embedding→k-NN→推荐列表
评级：⚠️ 轻微
- [P1] cell 0 学习目标是单句话（"目标：实现完整推荐流程……"），而非 3 条以上编号列表。
- [P2] cell 2 包含使用陈旧 'month04' 路径约定的注释导入：`# from month04.mu3_sim import find_similar`——应引用 `aurora.music.sim` 或直接删除。
- [P2] cell 13 将实验图表保存为 `mu4_precision_experiment.png`，使用与当前 L81 序列命名不一致的旧 'mu4' 前缀。
- [P2] 末尾 Markdown 单元格（2a5fd2cc）无"下一课：**L82**"指针；L82 引用嵌入在正文中早先的结束单元格（cell-14），而非最终 Markdown 单元格。

---

### L82 · 音乐可视化（visual_music）
评级：⚠️ 轻微
- [P1] cell-3 中色度音高公式错误：`p = round(12 * log2(f / 440)) mod 12` 以 A4=440 Hz 为原点（A→0），但 y 轴标签使用 C=0 约定。正确公式应为 `round(12 * log2(f / 440) + 9) mod 12`（或以 C4≈261.63 Hz 为参考）。
- [P1] cell-0 学习目标（"**目标**：可视化音乐特征空间——chroma 热力图……"）是单句话，而非 3 条以上编号列表。
- [P2] 章节编号重复：t-SNE 参数实验（cell-7）和节拍网格可视化（cell-9）均标题为 `## 3.`；节拍章节应为 §4，相似度热力图应为 §5。
- [P2] cell 4、10、12 无条件打印 `✅ …`，无任何断言——chroma、节拍、相似度热力图步骤无论输出值如何均报告成功。

---

### L83 · Transformer 从零复现 — Multi-Head Attention + PE + FFN
评级：❌ 严重
- [P0] cell-11 softmax 行和断言从 Q 和 K 直接内联重算 `w`（未调用 `scaled_dot_product_attention`），因此 `assert np.allclose(w.sum(axis=-1), 1.0)` 恒为真——返回 `np.zeros((2,4,16))` 的学生可通过所有三个 ✅ 检查。
- [P0] cell-19 Transformer Block 集成演示使用局部参考函数 `sdpa` 而非学生的 `scaled_dot_product_attention`，因此打印"✅ Attention + PE + FFN 完整前向传播通过"的最终演示从未实际调用 stub。
- [P1] 两个章节共用编号"## 6."——cell-14 是"## 6. 位置编码"，cell-16 是"## 6. 前馈网络"；FFN 应为第 7 节，后续集成章节应为第 8 节。
- [P1] cell-7 包含失效前向引用："multi-head 的投影矩阵 Wq/Wk/Wv/Wo 将在 **L2** 中封装进 MultiHeadAttention 类"——"L2"是占位符，不是本课程 L83–L94 序列中的真实课号。
- [P1] cell-0 学习目标是单句话（"**目标**：从头实现 scaled_dot_product_attention，理解 Q/K/V 的几何含义……"），而非 3 条以上独立编号项。
- [P2] cell-13 调用 `scaled_dot_product_attention(Q_parallel, K_exp, V_exp)` 并将结果存为 `out1`，但随后从头重算权重且从未使用 `out1`——当 stub 返回 None 时无任何反馈打印。
- [P2] cell-6 定义的 `softmax` 与 cell-19 定义的 `softmax_2d` 功能完全相同（相同的数值稳定 softmax 公式）——重复工具函数，无任何区分。
- [P2] 末尾 Markdown 单元格（cell-20）仅以行内形式提及 L84（"下节（**L84**）将在……"），无独立"下一课：**L84**"导航行。

---

### L84 · LoRA 低秩适配
评级：❌ 严重
- [P0] cell-13（秩对比实验）无条件调用 `LoRALinear(d, d, rank=4, alpha=4.0)` 和 `LoRALinear(d, d, rank=16, alpha=16.0)`，无 try/except；stub 在 `__init__` 中 raise NotImplementedError，运行该单元格前崩溃内核。
- [P1] cell-0 学习目标是单句复合句（"实现 LoRALinear 层，理解为什么……"），而非 3 条以上编号列表。
- [P2] cell-2 中 `import torch` 和 `import torch.nn as nn` 无 try/except ImportError 保护，torch 是重型可选依赖。
- [P2] 结束单元格 cell-14 行内引用下一课（"下一节（L85）"），缺少标准独立指针"下一课：**L85**"。

---

### L85 · KV-Cache 从零实现
评级：❌ 严重
- [P0] cell 3：stub `scaled_dot_product_attention` raise `NotImplementedError('TODO')`，验证块（`out = scaled_dot_product_attention(Q, K, V)` + assert + print）在同一单元格内立即运行，无 try/except——首次运行即崩溃内核。
- [P0] cell 6：KVCache 验证循环调用 `cache.update(0, new_k, new_v)`（raise NotImplementedError）和 `scaled_dot_product_attention(...)`（同），单元格内无任何 try/except——内核崩溃。
- [P0] cell 6：`print('✅ KV-Cache 实现验证通过')` 是无条件语句——整个单元格无任何 `assert`，单元格注释甚至承认"数值可能不同"，结果无论正确性如何总打印成功。
- [P1] cell 6：`cache = KVCache(n_heads=4, head_dim=64)` 构造参数与测试数据（`n_heads, total_seq, d = 2, 6, 8`）矛盾，cache 对象的存储元数据与其接收的每个数组均不匹配。
- [P1] cell 0：学习目标以无序列表（`-`）书写，违反要求 3 条以上编号具体项的格式规范。
- [P2] cell 6：测试将非因果全注意力输出（`out_no_cache`）与因果逐步缓存输出（`out_with_cache`）进行比较——即使函数实现正确，这两个量数学上不相等，"比较"作为正确性检查毫无意义。

---

### L86 · 采样策略从零实现 — temperature / top-k / top-p，纯 NumPy
评级：❌ 严重
- [P0] cell 8（可视化）在裸列表推导中调用两个 stub——`[top_k_sample(logits, k=VOCAB, temperature=0.5) for _ in range(500)]` 和 `[top_p_sample(logits, p=0.9) for _ in range(500)]`——无 try/except；两个 stub 均 raise NotImplementedError，从头到尾顺序运行即崩溃内核。
- [P2] cell 9 top-p 断言过弱：`assert 0 <= result_topp < len(test_logits)` 仅验证索引在范围内；无条件返回 `np.argmax(probs)` 的学生（忽略累积截止）可静默通过。
- [P2] 结束单元格（cell 10）写"下一步 L87：INT8 量化原理……"，而非标准"下一课：**L87**"加粗指针。

---

### L87 · 量化与本地推理
评级：⚠️ 轻微
- [P1] cell 1 公式写 `x_q = round(x / scale) + zero_point`（先取整再加 zero_point），但标准仿射量化公式为 `x_q = round(x/scale + zero_point)`；cell 3 实现采用非标准形式，指令和代码嵌入了相同的细微舍入误差。
- [P2] cell 3 中 `except NotImplementedError` 分支是死代码——`quantize_int8` 和 `dequantize_int8` 在同一单元格中完整实现，从不 raise NotImplementedError，使练习 stub 守卫成为永远不会触发的误导性样板代码。
- [P2] 末尾 Markdown 单元格（cell 7）以"下一课（L88）实现 TF-IDF 稀疏检索……"结尾，而非课程模板要求的标准"下一课：**L88**"加粗链接格式。

---

### L88 · TF-IDF 检索从零实现
评级：❌ 严重
- [P0] cell 5、7、9 均在验证代码中直接调用 stub，无 try/except——例如 `assert tokenize('Hello World!') == ['hello', 'world']` 和 `matrix, vocab = build_tfidf(DOCS)` 在学生未实现函数时以 NotImplementedError 崩溃内核。
- [P0] cell 10 仅运行参考实现（`ref_build`、`ref_retrieve`），然后无条件打印 `print('✅ TF-IDF 检索验证通过')`，无任何将学生 `matrix`/`cosine_retrieve` 输出与参考对比的断言——无论学生是否实现任何代码，✅ 均会触发。
- [P1] cell 7 的 TODO 注释写"计算 TF 矩阵 (n_docs, vocab_size)"，但 `build_tfidf` 必须计算 IDF 并返回 TF × IDF；遵循该提示的学生会返回原始 TF 矩阵，而非要求的 TF-IDF 矩阵。
- [P1] cell 9 的 TODO 注释写"构建查询向量"，但 `cosine_retrieve` 还需计算余弦相似度、对分数进行分区并返回排序后的 `(doc, score)` 对——提示仅覆盖所需实现的极小一部分。

---

### L89 · RAG 完整流水线
评级：❌ 严重
- [P0] cell-5 在 stub 定义后立即调用 `chunk_text(long_text, max_words=80)`（200 词文本），无 try/except；由于 200 > 80，stub 的提前返回守卫不触发，裸 `raise NotImplementedError("TODO")` 未被捕获，内核崩溃，`all_chunks` 从未被填充。
- [P0] cell-10（`format_rag_prompt` stub）语法损坏：在 `raise NotImplementedError("TODO")` 之后，残留模板文本（`Context:`、`{context}`、`Question: {query}`、`Answer:\"\"\".strip()`、`return prompt`）出现在模块级别；`Answer:\"\"\".strip()` 中未闭合的 `"""` 产生 SyntaxError，单元格完全无法执行。
- [P0] 端到端验证单元格（id `cbc38021`）使用 `matrix`、`vocab`、`all_chunks`，这些变量仅在后续 cell-11 中定义（`matrix, vocab = build_tfidf(all_chunks)`）；try/except 静默捕获由此产生的 NameError，即使完整实现后仍始终打印"⬜ 未实现"。
- [P1] `format_rag_prompt` 验证单元格（id `9f212137`）在 notebook 顺序中位于 stub 定义单元格（cell-10）之前，因此总是以 NameError 解析并打印"⬜ format_rag_prompt 未实现"，即使学生实现已存在。
- [P2] 结束单元格（cell-13）使用"下一步 L90"而非标准"下一课：**L90**"指针格式。
- [P2] 学习目标（cell-0）是无序项目符号列表，而非课程模板要求的 3 条以上编号具体可衡量项。

---

### L90 · 对话式 RAG — 会话记忆、来源归因与 Podcast Q&A 流水线
评级：⚠️ 轻微
- [P1] cell 0 学习目标是单句话（"**目标**：串联 RAG 检索 + 本地 LLM，构建能回答音频/播客内容问题的对话引擎"），而非 3 条以上编号列表。
- [P1] cell 2 `build_rag_index` docstring 说"返回 (embeddings_matrix, chunks) 作为索引"，但实现仅返回 `vecs`（嵌入矩阵本身）；docstring 与代码直接矛盾，会误导阅读 API 的读者。
- [P2] 验证单元格（cell 11）断言过弱：仅确认 `answer` 是非空字符串且每个来源以"📄"开头，因此返回硬编码字符串如 `return 'dummy answer', ['📄 fake']` 的学生无需调用 retrieve 或 build_prompt 即可通过所有三个断言。
- [P2] 实验单元格 13 使用 `_test_llm`，该函数对每个查询无条件返回"John played lead guitar in this episode."，导致 5 个 RAG 对比行中有 4 个显示"❌"——直接与声明的观察"有 RAG 时答案直接引用 chunk 文本"矛盾。

---

### L91 · 注意力图解 — 多头注意力权重热力图，LoRA 低秩结构可视化
评级：⚠️ 轻微
- [P1] 标题承诺"Multi-Head Attention (MHA)"，但正文仅实现单头缩放点积注意力——无任何头分割、并行多头计算或拼接（concat）操作。
- [P1] 学习目标（cell-0"**目标**"）是单句话，而非 3 条以上编号列表。
- [P2] cell-2 中 `import torch` 无 try/except ImportError 保护，且 torch 在正文任何代码单元格中从未实际使用。
- [P2] 末尾 Markdown 单元格（cell-9）无"下一课：**LXX**"指针——仅说"本模块 LLM 应用告一段落"，无任何前向链接。

---

### L92 · 端到端流水线
评级：⚠️ 轻微
- [P1] cell-0 学习目标是单句话（"目标：串联 Aurora 所有月份成果——实时录音 → Whisper 转写 → Podcast Agent 回答，建立对系统集成和延迟分布的直觉。"），而非 3 条以上编号技能列表。
- [P1] cell-0 头部列出"Aurora 连接：aurora.speech.whisper、aurora.rag.retriever、aurora.llm.agent"，但三者均不存在于 src 目录，也不在任何地方被导入——ASR、RAG、LLM 所有阶段均以 time.sleep() 模拟替代。
- [P2] cell-2 中 `from aurora.audio.io import read_wav` 是无条件导入（无 try/except），而 read_wav 在正文中从未调用；若 aurora.audio.io 未安装，尽管有前置警告，该单元格仍以裸 ImportError 崩溃。
- [P2] 练习单元格（0315ae52）将所有 stage_latency_ms 值硬编码为 None 并打印"请先填入实测数值（毫秒）"，无任何断言——是未经验证的占位符。
- [P2] cell-12 包含"n_trials = 3  # ✏️ TODO: 把 n_trials 改成 5"——该 TODO 注释在发布前从未被解决。
- [P2] 第 4 节图示明确声明"parallel = 2500ms (−50ms)"，但 run_pipeline_parallel 还添加了图示中未显示的独立 rag_refine await（async_rag delay=0.03 s），使实际并行总时间约为 2530 ms，节省约 20 ms 而非 50 ms。

---

### L93 · MLOps 基础 — W&B 实验追踪、模型版本管理、Docker 打包与部署脚本
评级：⚠️ 轻微
- [P1] cell 0 学习目标是单句话（"**目标**：把 Aurora 服务打包成可复现的 Docker 容器，并用 Weights & Biases 追踪训练实验的全部超参（hyperparameter，HP）与指标。"），而非 3 条以上编号列表。
- [P2] 练习单元格（48ecd68e）无任何断言或最低阈值检查——打印"配置完整度：{filled}/{len(experiment_config)}"但从不断言 `filled >= N`，填入任何内容的学生均得到 `1/12`（预填的 `"project"` 键），无任何失败信号。
- [P2] 单元格 99df8103 导入 `import time, statistics`，但 `time` 在单元格正文中从未被引用——仅 `statistics` 在 `monitor_inference_latency` 内部使用。

---

### L94 · Aurora v1 全景 Demo — 综合展示所有能力，面试材料与证据链
评级：❌ 严重
- [P1] cell-0 学习目标是单句话（"打磨一个可展示的 Demo，整理 Aurora 的证据链，准备面试材料。"），而非 3 条以上编号列表。
- [P1] cell-11 演示表引用陈旧的重命名前路径（'week01/day4_euler.ipynb'、'month03/'、'month05/'），重命名为 L01–L94 序列后这些路径已不存在；正确文件现在是 L35_euler_fft.ipynb 等。
- [P1] cell-6 的 WWHR Results 条目和 cell-8 的 M5 项目均写"WER（运行上方 cell 后查看实际 WER 值）"，但正文中无任何计算或显示 WER 值的单元格——占位符从未被填充。
- [P2] 末尾 Markdown 单元格（cell-17，本课收束）无"下一课：**L95**"指针，尽管 L95_research_papers.ipynb 作为下一课已存在。
- [P2] readme_checklist 字典（cell-edbc1f74）所有值均为 None，无条件打印"还有6项未填"；first_blog（cell-7ca6cf26）同样所有值为 None——两者均是未填充的占位符，无自检逻辑。
- [P2] `assert len(bullets) == 6`（cell-8）和 `assert len(qa) == 10`（cell-12）恒为真，因为列表在其正上方被硬编码——这些断言不检测任何真实错误。

---

### L95 · 研究论文入门——阅读、写作、投稿与学术合作
评级：⚠️ 轻微
- [P1] 单元格 b6ead143 中"必读论文清单"表格标注"（按依赖顺序）"，将 Transformer（L83-L84）列在 Whisper（L70-L71）之前，但课程号显示 Whisper 实际上在 L70——早于 L83 的 Transformer——直接与声明的依赖顺序和实际课程序列矛盾。
- [P2] 单元格 561b2e49："与学术机构合作的实际路径"章节编号为"## 5."——与早先的"## 5. 文献管理"重复——导致第 6 和第 7 节编号在正文标题序列中完全缺失。

---

### L96 · 白板推导演练——FFT / CTC / 注意力机制
评级：⚠️ 轻微
- [P1] 结束反向引用"Attention → L83-L84"错误：L84 是 lora.ipynb（实现 LoRALinear，涵盖参数高效微调），无任何注意力推导内容——注意力复习引用应止于 L83。
- [P2] MFCC 流水线答案单元格（a067e98e）直接调用 `np.fft.rfft(frame0, n=n_fft)`，违反 CLAUDE.md 规定"NumPy 仅作数组容器，FFT 必须从头实现"的规则。
- [P2] 注意力答案单元格仅断言输出形状（`assert out.shape == (seq_q, d_v)`），无数值正确性检查——返回正确形状零矩阵的实现可静默通过。
- [P2] CTC 答案单元格将完整实现的 `ctc_forward` 包裹在 `try/except NotImplementedError` 中，并断言 `assert log_p is not None`，但由于参考实现在同一单元格中且从不 raise NotImplementedError，两个守卫均为永久死代码。

---

### L97 · 面试准备与技术沟通
评级：⚠️ 轻微
- [P2] 单元格[10]标题为"## 5. ✏️ 模拟面试练习"，与单元格[6]的"## 5. 编程题准备：音频 AI 的高频手写题"重复使用编号"## 5."；该单元格在 notebook 顺序中位于第 7 和第 8 节之间，应重编号（例如 ## 8）。
- [P2] 单元格[7]中 frame_signal 验证仅断言 `frames.shape == (4, 8)`——返回任意正确形状数组（如 np.zeros((4,8))）的错误实现静默通过；检查还应验证 frames[0] 等于 x[0:8]，frames[1] 等于 x[4:12]，以捕获内容错误。

---

### L98 · 课程总结——做到了什么，还差什么
评级：⚠️ 轻微
- [P1] 章节编号全程混乱：第 3 和第 5 节缺失，第 4 和第 6 节各出现两次——"## 4. 量化成果"紧接"## 4. 面试准备程度自评"，"## 6. 学习速度复盘"紧接"## 6. 公开证据清单"，最终序列为 1、2、4、4、6、6、7。
- [P2] 结束单元格（ee6da094）写"**最后一课 L99**：Aurora v2 与持续成长路线图"，而非其他所有 notebook 使用的标准"下一课：**L99**"指针格式。

---

### L99 · Aurora v2 与持续成长——6 个月之后怎么走
评级：⚠️ 轻微
- [P1] 开场单元格（b4b574ee）学习目标是单句话，而非 3 条以上编号列表："目标：整理 Aurora v1 的能力边界，选定 Aurora v2 的延伸方向……并制定第 1 周的具体行动计划。"
- [P2] 单元格 671dd07e 顶部运行 `import datetime`，但 `datetime` 在单元格正文中从未被引用——未使用的导入。

---

## 三、按模块质量汇总

### 模块 0：基础入门（L01–L08）
| 指标 | 值 |
|------|---|
| 严重（❌） | 4（L04、L05、L06、L07） |
| 轻微（⚠️） | 4（L01、L02、L03、L08） |
| 良好（✅） | 0 |

**主要问题模式**：
- 正弦波/复数/傅里叶系列（L04–L07）集中了最早的 P0 崩溃——stub 返回 None 后，下游单元格以 TypeError 或 AssertionError 直接崩溃内核。
- L05 存在两处散文/代码不匹配（描述 8 点但代码用 9 点，描述 π/4 步长但代码用 π/2 步长）。
- 纯可视化课（L03、L08）无 stub 故无崩溃，但均缺少编号学习目标且承诺了内容而正文未兑现（L08 声称讲复共轭但从未出现）。

---

### 模块 2：线性代数（L09–L21）
| 指标 | 值 |
|------|---|
| 严重（❌） | 8（L09、L10、L11、L14、L16、L17、L18、L20、L21） |
| 轻微（⚠️） | 4（L12、L13、L15、L19） |
| 良好（✅） | 0 |

**主要问题模式**：
- P0 崩溃集中：stub 返回 None 后，`round()`、`np.round()`、`np.allclose()` 等函数在未保护的验证单元格中立即触发 TypeError。
- L17 存在额外的全局变量覆盖 bug：矩阵 `A` 在验证单元格前被演示单元格静默覆盖，导致即使正确实现也永远无法通过断言。
- L20、L21 存在大量陈旧引用（p6、p7、p9、v3 旧命名体系），从未更新为 L 序列号。
- 三个空占位 Markdown 单元格（cell-2、cell-21、cell-22）在多个笔记本中反复出现。

---

### 模块 3：微积分（L22–L26）
| 指标 | 值 |
|------|---|
| 严重（❌） | 3（L22、L24、L25） |
| 轻微（⚠️） | 2（L23、L26） |
| 良好（✅） | 0 |

**主要问题模式**：
- 各笔记本均存在与 L22 完全相同的样板代码（x²、x²+2x 中心差分斜率循环），与当课主题无关。
- L22 有 3 处散文/代码不匹配（均描述 sin(x) 实验，代码实际使用 x²）。
- 三个空 Markdown 单元格（cell-2、cell-21、cell-22）在每个微积分笔记本中均出现。
- P0 崩溃模式相同：stub 返回 None，`abs(None - numeric)` 触发 TypeError。

---

### 模块 4：概率（L27–L31）
| 指标 | 值 |
|------|---|
| 严重（❌） | 4（L27、L28、L29、L30） |
| 轻微（⚠️） | 1（L31） |
| 良好（✅） | 0 |

**主要问题模式**：
- L30 有三个 P0——最严重的是 softmax 在验证后被重定义为参考实现，使所有后续检查恒为真，即使 stub 完全未实现。
- L29 的 P0 属于"始终通过"类型：normal_cdf 内联重算公式而非调用学生 stub，68-95-99.7% 断言组永远通过。
- 三个空 Markdown 单元格同样在每个概率笔记本中出现。

---

### 模块 5：音频 DSP（L32–L53）
| 指标 | 值 |
|------|---|
| 严重（❌） | 10（L32、L33、L34、L35、L40、L45、L46、L49、L50、L53） |
| 轻微（⚠️） | 12（L36、L37、L38、L39、L41、L42、L43、L44、L47、L48、L51、L52） |
| 良好（✅） | 0 |

**主要问题模式**：
- L32 有特殊的 P0：练习单元格包含完整参考答案，验证单元格恒通过。
- L45 有三个 P0：Ellipsis stub 触发 TypeError 而非 NotImplementedError，try/except 类型不匹配导致异常逃逸；验证断言对参考实现而非学生 stub 运行。
- 约从 L36 起，stub 处理逐步改善；但 Ellipsis 与 None 的 stub 约定不一致，要求 try/except 分别匹配不同异常类型。
- L40 的 P0 属于"下游单元格"类型：主验证单元格（cell 11）有保护，但实验单元格（cell 13）无保护，同样崩溃。

---

### 模块 6：深度学习（L54–L65）
| 指标 | 值 |
|------|---|
| 严重（❌） | 10（L54、L55、L57、L58、L59、L60、L61、L62、L63、L64） |
| 轻微（⚠️） | 2（L56、L65 降级后） |
| 良好（✅） | 0 |

**注**：L65 在提供的数据中评级为 major；以 major 计算则严重=11，轻微=1。

**主要问题模式**：
- 几乎全部为严重——这是整个课程中质量最差的模块。
- 陈旧命名引用集中：L60 的 `a3_backward.ipynb`，L61 的 `a4_mlp`，L63 的 `M2-K3`，L65 的 `month02/`，L57 的 `p3_nn.ipynb`。
- 缺少 torch/torch.nn ImportError 保护是系统性问题，几乎每一课都有。
- L55 展示了双重 P0：Ellipsis stub 触发 TypeError，且 `__pow__` scaffold 误导学生创建断开计算图但单节点测试仍通过的实现。

---

### 模块 7：ASR（L66–L75）
| 指标 | 值 |
|------|---|
| 严重（❌） | 7（L66、L68、L69、L70、L71、L72、L74、L75） |
| 轻微（⚠️） | 2（L67、L73） |
| 良好（✅） | 0 |

**注**：L75 在数据中评级为 major；严重=8，轻微=2。

**主要问题模式**：
- L74 的 P0 属于特殊"反向"类型：参考实现完全保留在 stub 位置，try/except 守卫永远不触发，学生无任何代码需要填写。
- L72 的 P0 是运行时数据问题（错误的 dataset split 名称），与其他 stub 相关崩溃不同。
- 内容不符（L73 承诺 jiwer 但未使用；L75 承诺 WER 可视化但缺席；L72 承诺中文数据但全是英文）是本模块特有的严重问题。
- 下一课预告错误频发：L74 对 L75 的描述与实际内容不符；L75 对 L76 的描述错误。

---

### 模块 8：音乐（L76–L82）
| 指标 | 值 |
|------|---|
| 严重（❌） | 3（L76、L77、L78） |
| 轻微（⚠️） | 4（L79、L80、L81、L82） |
| 良好（✅） | 0 |

**主要问题模式**：
- 崩溃集中在前三课（L76–L78），后四课（L79–L82）无内核崩溃。
- L77 的 P0 具有双重性质：stub 硬编码零大小数组，一个 P0 导致 ValueError 崩溃，另一个 P0 导致 np.allclose 的空真通过——同一 stub 同时触发两类相反的失败。
- L79–L81 存在陈旧命名引用（M4-MU3、MU4、month04 路径）。
- L82 的 P1 是数学错误而非结构错误（色度公式参考音高与 y 轴标签不一致）。

---

### 模块 9：LLM（L83–L91）
| 指标 | 值 |
|------|---|
| 严重（❌） | 6（L83、L84、L85、L86、L88、L89） |
| 轻微（⚠️） | 3（L87、L90、L91） |
| 良好（✅） | 0 |

**主要问题模式**：
- L83 和 L85 有"验证绕过 stub"类型的 P0：验证代码使用内联参考函数而非学生 stub，结果恒为真。
- L89 同时拥有三类 P0：崩溃型（chunk_text）、语法错误型（SyntaxError）、变量顺序型（NameError 因单元格乱序）。
- L88 的假阳性 ✅ 来自参考实现占据验证角色而非学生 stub。
- L91 承诺 MHA 但仅实现单头注意力，是模块内最严重的内容不符。

---

### 模块 10：集成收尾（L92–L99）
| 指标 | 值 |
|------|---|
| 严重（❌） | 1（L94） |
| 轻微（⚠️） | 7（L92、L93、L95、L96、L97、L98、L99） |
| 良好（✅） | 0 |

**主要问题模式**：
- 本模块是整个课程质量最高的模块，无内核崩溃风险（L94 的 P1 均为内容问题而非运行时崩溃）。
- 陈旧路径引用集中在 L94（week01/、month03/、month05/）。
- 单句学习目标和非标准下一课指针是本模块唯一系统性问题。
- L98 的章节编号紊乱（3 和 5 缺失，4 和 6 各重复一次）是本模块最显眼的结构缺陷。

---

## 四、P0 高优先级修复清单

以下按课号列出全部 76 个 P0 问题及精确修复建议。

### L04 · 正弦波生成（sinusoid）
1. **`bc6dba43` — TypeError：`np.allclose(None, array)` 崩溃**  
   修复：将 stub 改为 `raise NotImplementedError("TODO")`；验证单元格加 `try/except (NotImplementedError, TypeError)`。
2. **`c_chord_demo` — 和弦演示 `(None + None)` TypeError 崩溃**  
   修复：在和弦演示代码开头加 `if any(v is None for v in [c4, e4, g4]): print('⬜ 未实现'); raise SystemExit`。

### L05 · 复数几何本质
3. **`242563b5` — `mag, ph = magnitude_phase(3 + 4j)` 解包 None 崩溃**  
   修复：stub 改为 `raise NotImplementedError("TODO")`；验证单元格加 `try/except NotImplementedError`。

### L06 · 欧拉公式
4. **`25a0ea10` — `abs(twiddle(0, 0, 8) - 1) < 1e-12` 对 None 做减法崩溃**  
   修复：验证单元格包裹在 `try/except (NotImplementedError, TypeError)` 中。

### L07 · 万物皆正弦
5. **`35e71676`/`d9ec446c` — stub 返回 `np.zeros_like(t)`，验证无保护，AssertionError 崩溃**  
   修复：stub 改为 `raise NotImplementedError("TODO")`；验证单元格加 try/except。

### L09 · 向量代数
6. **`1129d458` — `np.allclose(None, [0.3, -0.6, 0.9, -1.2])` TypeError 崩溃**  
   修复：验证单元格加 `try/except (NotImplementedError, TypeError)`。

### L10 · 点积
7. **`9d64d7b5` — `round(cosine_similarity(...), 3)` 对 None 崩溃**  
   修复：验证单元格加 try/except；stub 改为 raise NotImplementedError。

### L11 · 向量范数
8. **`16166fa5` — `np.linalg.norm(None)` TypeError 崩溃**  
   修复：验证单元格加 try/except；stub 改为 raise NotImplementedError。

### L14 · 特征值与 SVD
9. **`7640da6` — `np.round(None, 2)` TypeError 崩溃**  
   修复：验证单元格加 try/except；stub 改为 raise NotImplementedError。

### L16 · 行列式与逆矩阵
10. **`cell-11` — `f'{got_det:.6f}'` 对 None 崩溃**  
    修复：验证单元格加 `try/except (NotImplementedError, TypeError)`；stub 改为 raise NotImplementedError。
11. **`cell-12` — `np.round(got_inv, 6)` 对 None 崩溃**  
    修复：同上。

### L17 · 特征对角化
12. **`bd87cdd6` — `round(char_poly(A, lam), 6)` 对 None 崩溃**  
    修复：验证单元格加 try/except。
13. **`bd87cdd6` — 全局 `A` 被覆盖为 2×2 矩阵，即使正确实现也无法通过 3×3 断言**  
    修复：在验证单元格顶部重新本地赋值正确的 3×3 矩阵 `A`，不依赖全局变量。

### L18 · 可逆性与秩
14. **`9a32c935` — `assert is_sdd(M1) and not is_sdd(M2)...` 对 None 裸断言崩溃**  
    修复：验证单元格加 try/except；stub 改为 raise NotImplementedError。

### L22 · 导数
15. **`c16216a4` — `abs(numeric_derivative(...) - 6.0)` 对 None 崩溃**  
    修复：验证单元格加 try/except；stub 改为 raise NotImplementedError。

### L24 · 链式法则
16. **`95883685` — `abs(composite_derivative(x) - numeric) < 1e-3` 对 None 崩溃**  
    修复：同 L22。

### L25 · 梯度下降
17. **`8a6ebfdb` — `2*(None-3)` TypeError（迭代第 2 次）崩溃**  
    修复：验证单元格加 try/except 包裹整个循环；stub 改为 raise NotImplementedError。

### L27 · 概率基础
18. **`41b0398e` — `round(None, 4)` TypeError 崩溃**  
    修复：验证单元格加 try/except；stub 改为 raise NotImplementedError。

### L28 · 描述性统计
19. **`54b51a46` — `z.mean()` 对 None 崩溃**  
    修复：验证单元格加 `try/except (NotImplementedError, AttributeError)`。

### L29 · 常见概率分布
20. **`cell-18` — `normal_cdf` 内联重算 PDF，68-95-99.7% 断言始终通过，stub 未被测试**  
    修复：将 `normal_cdf` 内部公式替换为 `gaussian_pdf` 调用；或将 68-95-99.7% 验证移到显式调用学生 `gaussian_pdf` 的独立单元格。

### L30 · Softmax 与交叉熵
21. **`e6fa73dd` — `np.round(None, 3)` 和 `None.sum()` AttributeError 崩溃**  
    修复：验证单元格加 try/except；stub 改为 raise NotImplementedError。
22. **`0d09cc9e` — `round(None, 3)` TypeError 崩溃**  
    修复：同上，针对 cross_entropy stub。
23. **`cell-25` — softmax 被重定义为参考实现，`cell-29` 的检查恒通过**  
    修复：将参考实现重命名为 `_ref_softmax`，最终检查单元格调用学生 `softmax`，并在 `if softmax is _ref_softmax` 时报错。

### L32 · NumPy 信号基础
24. **`f180f27f` — `from aurora.audio import sine` ModuleNotFoundError 崩溃**  
    修复：加 `try/except ImportError as e: print(f'⬜ aurora 未安装: {e}'); sine = None`。
25. **`1a118e69` — 练习单元格包含完整参考答案，验证恒通过**  
    修复：将参考答案替换为 `raise NotImplementedError("TODO")`，另建参考答案单独单元格。

### L33 · 正弦波生成
26. **`8617b5a4` — `np.abs(None - ref)` TypeError 崩溃**  
    修复：验证单元格加 try/except。

### L34 · Nyquist 定理与混叠
27. **`6de0a05b` — `assert 0 <= None <= sr/2` TypeError 崩溃**  
    修复：验证单元格加 try/except；stub 改为 raise NotImplementedError。

### L35 · Euler FFT
28. **`b835ad40` — `euler(theta)` 返回 None，`z - np.exp(1j*theta)` TypeError 崩溃**  
    修复：验证单元格加 try/except；stub 改为 raise NotImplementedError。

### L40 · 频谱分析实战
29. **cell 13（实验单元格）— `freqs[top2_idx]` 对 Ellipsis `TypeError: 'ellipsis' object is not subscriptable` 崩溃**  
    修复：cell 13 开头加 `if freqs is ...: print('⬜ 未实现'); raise SystemExit`。

### L45 · 声谱图生成
30. **cell 10 — Ellipsis stub，`np.abs(Ellipsis)` TypeError 崩溃（try/except 只捕获 NotImplementedError）**  
    修复：stub 改为 `raise NotImplementedError("TODO")`；验证单元格 try/except 改为捕获 `(NotImplementedError, TypeError)`。
31. **cell 11 — try/except 类型不匹配，TypeError 逃逸，内核崩溃**  
    修复：同上，统一异常类型。
32. **cell 11 — 断言对 `dB_ref`（参考实现）而非学生 stub 运行，恒通过**  
    修复：将断言改为对学生 `plot_spectrogram` 输出运行，使用 `dB_student` 而非 `dB_ref`。

### L46 · Mel 频率尺度
33. **cell 10 — `hz_to_mel` 以 `pass` 返回 None，`abs(None - 781.2)` TypeError 崩溃**  
    修复：验证单元格加 try/except；stub 改为 raise NotImplementedError。

### L49 · DCT-II
34. **cell-13 — `len(None)` TypeError 崩溃（stub 返回 None）**  
    修复：cell-13 开头加 `if X_dct is None: print('⬜ 未实现'); raise SystemExit`。

### L50 · MFCC 完整流水线
35. **cell 11 — `out.shape` AttributeError 崩溃（stub 返回 None）**  
    修复：验证单元格加 try/except；stub 改为 raise NotImplementedError。

### L54 · Value 计算图
36. **cell 11 — `c = a + b; c.data` AttributeError 崩溃（所有 stub 方法返回 None）**  
    修复：所有 stub 方法改为 raise NotImplementedError；验证单元格加 try/except。

### L55 · 前向传播
37. **cell-10 — Ellipsis stub 触发 `float(Ellipsis)` TypeError，而非 NotImplementedError**  
    修复：所有 stub 改为 `raise NotImplementedError("TODO")`；验证单元格 try/except 统一捕获。
38. **cell-11 — 裸 assert 无 try/except，异常逃逸崩溃内核**  
    修复：验证单元格加 try/except。

### L57 · MLP 从零搭建
39. **cell-12 — `len(None)` TypeError 崩溃（`MLP.parameters()` 返回 None）**  
    修复：验证单元格加 try/except；stub 改为 raise NotImplementedError。
40. **cell-14 — `for i, layer in enumerate(m3.layers)` AttributeError 崩溃（`MLP.__init__` 为 pass）**  
    修复：验证单元格加 try/except；`__init__` stub 改为 raise NotImplementedError。

### L58 · 训练循环
41. **cell-10/11 — `train()` 设 `loss = None` 后立即调用 `loss.data`，AttributeError 崩溃**  
    修复：stub `train()` 改为 raise NotImplementedError；验证单元格加 try/except。

### L59 · PyTorch Tensor 基础
42. **cell 11 — `batch.shape` 对 None AttributeError 崩溃**  
    修复：验证单元格加 try/except；stub 改为 raise NotImplementedError。

### L61 · nn.Module 实战
43. **cell-11 — `out.shape` 对 None AttributeError 崩溃（`forward()` 以 pass 结尾）**  
    修复：`forward()` stub 改为 raise NotImplementedError；验证单元格加 try/except。

### L62 · Dataset 与 DataLoader
44. **cell 11 — `extract_features()` raise NotImplementedError 未捕获，崩溃内核**  
    修复：验证单元格加 `try/except NotImplementedError`。

### L63 · KeywordCNN 模型
45. **cell-11 — `out.shape` 对 None AttributeError 崩溃（`forward` 以 pass 结尾）**  
    修复：`forward` stub 改为 raise NotImplementedError；验证单元格加 try/except。

### L64 · 训练评估闭环
46. **cell 11（train_epoch 验证）— NotImplementedError 未捕获崩溃**  
    修复：验证单元格加 `try/except NotImplementedError`。
47. **cell 14（eval_accuracy 验证）— NotImplementedError 未捕获崩溃**  
    修复：同上。

### L66 · ASR 系统全览
48. **cell 11 — `abs(None - 0.0)` TypeError 崩溃（`compute_wer` 以 pass 返回 None）**  
    修复：验证单元格加 try/except；stub 改为 raise NotImplementedError。

### L68 · CTC 对齐原理
49. **cell 11 — 假阳性 ✅ 在 None 守卫之外无条件打印**  
    修复：将无条件 print 移入 if/else 块内，仅在结果正确时打印 ✅。
50. **cell 11 — `assert ctc_greedy_decode(logits_blank) == []` 无 None 守卫，AssertionError 崩溃**  
    修复：整个验证块包裹在 `try/except (NotImplementedError, AssertionError)` 中，且在调用前检查 `if result is None`。
51. **cell 13 — `len(ctc_greedy_decode(...))` 对 None TypeError 崩溃**  
    修复：实验单元格加 `try/except (NotImplementedError, TypeError)`。

### L69 · CTC 前向算法
52. **cell 6（验证）— `ctc_forward` raise NotImplementedError 未捕获崩溃**  
    修复：验证单元格加 `try/except NotImplementedError`。
53. **cell 8（实验）— 同上**  
    修复：同上。

### L70 · Whisper 架构解析
54. **cell 11 — `feat.shape` 对 None AttributeError 崩溃（stub 以 pass 返回 None）**  
    修复：验证单元格加 try/except；stub 改为 raise NotImplementedError。

### L71 · Whisper 解码策略
55. **cell-5 — `greedy_decode(prompt)` raise NotImplementedError 未捕获崩溃**  
    修复：验证单元格加 `try/except NotImplementedError`。
56. **cell-7 — `beam_search(prompt, width=2)` raise NotImplementedError 未捕获崩溃**  
    修复：同上。

### L72 · Whisper 微调
57. **cell 6 — `load_dataset(..., split={'test': 'test'})` SplitNotFoundError（正确名称为 'test.clean'）**  
    修复：将 `'test': 'test'` 改为 `'test': 'test.clean'`。

### L74 · ASR 错误分析
58. **cell-2 — `wer()` 是完整参考实现，try/except NotImplementedError 守卫永远不触发，验证恒通过**  
    修复：将 `wer()` 函数体替换为 `raise NotImplementedError("TODO")`，另建 `_ref_wer` 隐藏参考实现。

### L76 · 音乐理论速成
59. **cell 4 — `midi_to_freq`/`freq_to_midi` raise NotImplementedError 未捕获崩溃**  
    修复：验证单元格加 `try/except NotImplementedError`。
60. **cell 6 — `chroma_from_freq` raise NotImplementedError 在循环中未捕获崩溃**  
    修复：循环外加 try/except。

### L77 · 音乐特征工程
61. **cell-14 — `rms_sil.max()` 对空数组 `np.zeros(0)` ValueError 崩溃**  
    修复：stub 改为 `raise NotImplementedError("TODO")` 而非返回零大小数组；验证单元格加 try/except。
62. **cell-14 — `np.allclose(np.zeros(0), 0.5)` 空真返回 True，正确性检查永远通过**  
    修复：同上，stub 改为 raise NotImplementedError 后问题自动消失；或在断言前检查 `len(rms_const) > 0`。

### L78 · 节拍追踪
63. **cell 5 — `my_onset_envelope(signal, SR)` raise NotImplementedError 未捕获崩溃**  
    修复：验证单元格加 `try/except NotImplementedError`。
64. **cell 7 — `my_beat_track` 内部调用未实现 stub，NotImplementedError 传播崩溃内核**  
    修复：cell 7 的整个 assert 块加 `try/except NotImplementedError`。

### L83 · Transformer 从零复现
65. **cell-11 — softmax 行和断言从 Q/K 内联重算，未调用学生 stub，恒为真**  
    修复：删除内联重算；断言改为 `assert np.allclose(scaled_dot_product_attention(Q, K, V).sum(axis=-1), ...)` 直接调用学生函数（适当调整期望值）。
66. **cell-19 — 集成演示使用 `sdpa`（参考函数）而非学生 `scaled_dot_product_attention`，最终 ✅ 不测试 stub**  
    修复：将 `sdpa` 替换为 `scaled_dot_product_attention`；加 try/except 保护。

### L84 · LoRA 低秩适配
67. **cell-13 — `LoRALinear(...)` raise NotImplementedError 未捕获崩溃**  
    修复：cell-13 加 `try/except NotImplementedError`。

### L85 · KV-Cache 从零实现
68. **cell 3 — stub 与验证在同一单元格，raise NotImplementedError 未捕获崩溃**  
    修复：将 stub 定义和验证代码分入独立单元格；验证单元格加 try/except。
69. **cell 6 — `cache.update()` 和 `scaled_dot_product_attention()` raise NotImplementedError 未捕获崩溃**  
    修复：验证单元格加 `try/except NotImplementedError`。
70. **cell 6 — `print('✅ KV-Cache 实现验证通过')` 无条件，无任何 assert**  
    修复：添加真实断言（如 `assert out_with_cache.shape == expected_shape`）并使 ✅ 打印依赖断言通过。

### L86 · 采样策略
71. **cell 8 — 可视化列表推导调用两个 stub，raise NotImplementedError 未捕获崩溃**  
    修复：可视化单元格加 `try/except NotImplementedError`；或在可视化前检查函数是否已实现。

### L88 · TF-IDF 检索
72. **cell 5、7、9 — 验证代码直接调用 stub 无 try/except，NotImplementedError 崩溃内核**  
    修复：每个验证单元格加 `try/except NotImplementedError`。
73. **cell 10 — 仅运行参考实现，无条件打印 ✅，学生 stub 从未被验证**  
    修复：在 cell 10 末尾添加将学生 `matrix`/`cosine_retrieve` 输出与 `ref_build`/`ref_retrieve` 对比的断言。

### L89 · RAG 完整流水线
74. **cell-5 — `chunk_text(long_text, max_words=80)` raise NotImplementedError 未捕获崩溃**  
    修复：验证单元格加 `try/except NotImplementedError`。
75. **cell-10 — `format_rag_prompt` stub 存在 SyntaxError（未闭合 `"""` 字符串），单元格完全无法执行**  
    修复：删除 stub 中 `raise NotImplementedError("TODO")` 之后的所有残留模板文本；stub 只保留 `def format_rag_prompt(...): raise NotImplementedError("TODO")`。
76. **验证单元格（`cbc38021`）— 使用仅在后续 cell-11 定义的 `matrix`/`vocab`/`all_chunks`，NameError 被 try/except 静默捕获，永远打印"⬜ 未实现"**  
    修复：将端到端验证单元格移至 cell-11 之后；或在验证单元格顶部重新构建所需变量。

---

## 五、共性问题与改进建议

### 问题一：Stub 返回 None 与无保护验证单元格（影响约 40 课）

**现象**：最常见的 P0 模式。Stub 函数以 `pass` 结尾（Python 默认返回 None），验证单元格直接对返回值调用 `.shape`、`round()`、`len()`、`abs(x - numeric)` 等操作，导致 TypeError 或 AttributeError 崩溃内核，学生在看到任何有用信息前已面对一段意义不明的报错。

**根本原因**：Stub 约定不统一（部分用 `pass`，部分用 `...`，部分用 `raise NotImplementedError`），且验证单元格编写时假设函数已实现。

**修复建议**：
1. **统一 stub 约定**：所有待实现函数改为 `raise NotImplementedError("TODO：请在这里实现你的代码")`，彻底消除 None 返回值。
2. **验证单元格模板**：所有验证单元格采用统一模板：
   ```python
   try:
       result = student_function(...)
       assert result == expected, f"期望 {expected}，实际 {result}"
       print("✅ 通过")
   except NotImplementedError:
       print("⬜ 尚未实现")
   except AssertionError as e:
       print(f"❌ 失败：{e}")
   ```
3. **全局 grep 修复**：`grep -rn "^\s*pass$" notebooks/` 找出所有 stub，批量替换。

---

### 问题二：学习目标单句化（影响约 85 课，几乎全部）

**现象**：几乎所有 99 课的"目标"/"今日目标"块都是一句简短段落，而非模板要求的"3 条以上编号具体可衡量项"。这削弱了课程的可测量性，学生无法明确知道完成后应达到什么标准。

**根本原因**：笔记本模板的目标字段未强制要求格式；批量创建时可能复制了单句占位符。

**修复建议**：
1. 为每课目标块制定格式规范：每条目标使用"能够……（可验证行为）"句式，最少 3 条，编号列出。
2. 批量扫描并标记：`grep -L "^1\. " notebooks/**/*.ipynb` 找出所有缺少编号列表的笔记本，优先处理 P0/P1 课程。
3. 建立 CI 检查（例如 pre-commit hook 或 pytest-notebook）：解析第一个 Markdown 单元格，若无 `^[0-9]+\.` 列表则报告警告。

---

### 问题三：下一课指针格式不一致（影响约 70 课）

**现象**：课程结束处的下一课引用使用至少 8 种不同格式：
- "下一节（L68）"（括号格式）
- "下一步 L87"（"下一步"格式）
- "打开 L80"（动词格式）
- "下节 `L43_stft.ipynb`"（文件名格式）
- "下一节进入 FFT 实现"（无编号格式）
- "下一课：**L68**"（标准格式，仅少数课使用）

**根本原因**：无统一的课程模板结尾块；各课独立编写时自由发挥。

**修复建议**：
1. 规定结束 Markdown 单元格必须以独立行 `下一课：**LXX**` 结尾（其中 XX 为两位数字序号）。
2. 编写 Python 脚本批量扫描并修复：`grep -rn "下一" notebooks/**/*.ipynb | grep -v "下一课：\*\*L"` 找出所有不合规格式，自动生成修复 patch。

---

### 问题四：陈旧命名引用（影响约 25 课）

**现象**：大量笔记本引用已废弃的旧命名体系，包括：
- `month02/`、`month04/` 路径（L21、L25、L65、L81、L94）
- `M2-A3`、`M2-K3`、`M4-MU3`、`M2-P3` 等月份/模块编码（L54、L60、L63、L79、L80）
- `p3`、`p6`、`p7`、`p9`、`v2`、`v3` 等旧编码（L19、L20、L57）
- `week01/day4_euler.ipynb`、`month03/`、`month05/` 路径（L94）
- `a3_backward.ipynb`、`a4_mlp` 等旧文件名（L60、L61）

**根本原因**：L01–L99 重命名时只重命名了文件，未 grep 替换内部所有交叉引用。

**修复建议**：
1. 建立"重命名映射表"（旧名 → 新 L 编号），作为工具脚本运行一次性替换全库。
2. 未来重命名时在同一 commit 中运行 `grep -rn "旧名称" notebooks/` 并修复所有引用。
3. 当前可运行：`grep -rn "month0[1-5]\|M[0-9]-[A-Z][0-9]\|week0[0-9]" notebooks/ --include="*.ipynb"` 定位所有剩余引用。

---

### 问题五：标题/目标承诺与内容实际不符（影响约 20 课）

**现象**：标题或目标单元格列出的主题在正文中从未出现：
- L42：承诺噪声频谱，无噪声内容
- L53：标题写"波形→声谱图→Mel→MFCC"四步流水线，正文只有后两步
- L72：承诺中文/方言数据，全部使用英文 LibriSpeech
- L73：标题写"jiwer 对比"，从未导入 jiwer
- L75：承诺 WER 可视化，无任何 WER 内容；承诺波形/声谱图，无任何此类图
- L77：标题写 ZCR，正文完全没有 ZCR
- L91：标题写"多头注意力（MHA）"，只实现了单头注意力
- L92：头部列出三个 aurora 模块为"连接"，实际上均不存在

**根本原因**：笔记本标题和目标在实现前就已编写，实现时内容发生改变但标题未同步更新。

**修复建议**：
1. 将标题/目标审计作为课程发布 checklist 的强制项：发布前对照标题逐条核查正文是否包含对应内容。
2. 对内容缺失选择二选一：要么补充内容（推荐），要么修改标题去掉未实现的承诺。
3. 对"将在下一课实现"的承诺，明确在正文中注明"（本课不涉及，详见 LXX）"。

---

### 问题六：验证逻辑绕过学生 Stub（影响约 8 课）

**现象**：验证代码使用内联参考实现或内部局部函数，而非学生 stub，导致无论 stub 内容如何验证恒通过：
- L29：`normal_cdf` 内联重算 PDF，不调用 `gaussian_pdf` stub
- L30：`softmax` 在验证后被重定义为参考实现，后续检查始终测试参考版本
- L45：断言对 `dB_ref` 而非学生 `plot_spectrogram` 运行
- L74：`wer()` 是完整参考实现，try/except NotImplementedError 永远不触发
- L83：softmax 行和断言内联重算权重，integration demo 使用 `sdpa` 而非学生函数

**根本原因**：作者为保证演示正常运行而引入参考实现，但忘记将验证切换回学生函数。

**修复建议**：
1. 命名约定：参考实现统一用 `_ref_` 前缀（如 `_ref_softmax`），验证代码中禁止出现 `_ref_` 前缀函数。
2. 验证代码审查规则：每个 ✅ 打印语句之前必须有调用学生函数的代码行，且该行不得包含 `_ref_`。
3. 对现有问题逐一修复：找出所有"验证单元格中引用与 stub 同名但非 stub 本体的函数"的实例。

---

### 问题七：可选重型依赖缺乏 ImportError 保护（影响约 30 课）

**现象**：`torch`、`torch.nn`、`torchaudio`、`transformers`、`peft`、`sklearn`、`jiwer` 等库在深度学习（L59–L65）和 LLM（L83–L91）模块中被顶层裸导入，未安装时内核立即崩溃，无任何友好提示。

**修复建议**：
所有重型可选依赖使用以下模板：
```python
try:
    import torch
    import torch.nn as nn
except ImportError:
    print("⬜ torch 未安装。运行 `pip install torch` 后重试。")
    raise SystemExit
```
或者，在 `make install` 中将这些依赖纳入对应 extras（`[dl]`、`[asr]`、`[llm]`），并在每个模块的第一课中统一检查环境。

---

### 问题八：测试/断言强度不足（影响约 35 课）

**现象**：大量验证断言过弱，可被错误实现静默通过：
- 形状断言（`assert out.shape == (8, 10)`）——零张量即可通过
- 宽容区间（`assert abs(bpm - 120) < 15`，`assert 0.0 <= wer <= 2.0`）——几乎任何值均通过
- 空真断言（`np.allclose(np.zeros(0), scalar)`）——空数组恒返回 True
- 单参数测试——仅测试 A=2, f=1, phi=0，不测试 phi≠0 或其他参数组合
- 索引范围断言（`assert 0 <= result < vocab_size`）——不验证算法逻辑

**修复建议**：
1. **数值正确性**：对所有算法单元格，在形状断言之外增加 `np.allclose(result, reference, atol=1e-6)` 类的数值断言。
2. **参数覆盖**：至少覆盖 2–3 个独立参数组合，确保 phi≠0、A≠1、f≠1 等边界情况均被测试。
3. **非退化性检查**：对返回分布/概率的函数，增加 `assert result.max() > threshold`（而非仅检查形状或范围）以排除零/常数输出。
4. **参考对比**：优先使用 `np.allclose(student_result, ref_result)` 而非手动硬编码期望值，减少维护负担。
