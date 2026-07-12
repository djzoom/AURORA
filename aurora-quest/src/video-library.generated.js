// 自动生成：node scripts/generate_video_library_data.mjs（勿手改，改 VIDEO_LIBRARY.md）
export const videoLibrary = {
  "source": "docs/current/course/VIDEO_LIBRARY.md",
  "count": 92,
  "phases": [
    "Phase 0–1 · 数学与信号直觉基础（L01–L08）",
    "Phase 2 · 线性代数（L09–L21）",
    "Phase 3 · 微积分（L22–L26）",
    "Phase 4 · 概率统计（L27–L31）",
    "Phase 5 · Audio DSP 音频信号处理（L32–L53）",
    "Phase 6 · 机器学习 / 深度学习基础（L54–L65）",
    "Phase 7 · 语音识别 ASR / STT（L66–L75）",
    "Phase 8 · 音乐智能 / MIR（L76–L82）",
    "Phase 9 · LLM / RAG / Agent（L83–L91）",
    "Phase 10 · 系统集成 / MLOps / 面试（L92–L99）",
    "aurora.tts · 语音合成 TTS（延期模块，专项补充）"
  ],
  "items": [
    {
      "title": "线性代数的本质 Essence of Linear Algebra",
      "topPick": false,
      "phase": "Phase 0–1 · 数学与信号直觉基础（L01–L08）",
      "instructor": "Grant Sanderson (3Blue1Brown)",
      "links": "https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab",
      "type": "播放列表（16 集）",
      "difficulty": "入门",
      "language": "英文（社区中文字幕可选；B 站有官方双语搬运）",
      "duration": "约 3 小时",
      "covers": "向量/线性组合/张成空间、矩阵=线性变换、矩阵乘法=变换复合、行列式、逆矩阵/列空间/零空间、点积与叉积、特征值与特征向量、基变换、抽象向量空间",
      "align": "L05–L21（复数几何延伸到线代）",
      "why": "核心命题「矩阵就是线性变换」正是 AURORA「矩阵即滤波（DFT/Mel 矩阵）」思想源头；纯几何推导、零黑箱。Phase 1–2 的直觉总纲。",
      "urls": [
        {
          "url": "https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab",
          "label": "播放列表"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "入门"
      ],
      "langTags": [
        "中文",
        "英文"
      ],
      "searchable": "线性代数的本质 essence of linear algebra grant sanderson (3blue1brown) 向量/线性组合/张成空间、矩阵=线性变换、矩阵乘法=变换复合、行列式、逆矩阵/列空间/零空间、点积与叉积、特征值与特征向量、基变换、抽象向量空间 l05–l21（复数几何延伸到线代） 核心命题「矩阵就是线性变换」正是 aurora「矩阵即滤波（dft/mel 矩阵）」思想源头；纯几何推导、零黑箱。phase 1–2 的直觉总纲。 播放列表（16 集）"
    },
    {
      "title": "微积分的本质 Essence of Calculus",
      "topPick": false,
      "phase": "Phase 0–1 · 数学与信号直觉基础（L01–L08）",
      "instructor": "Grant Sanderson (3Blue1Brown)",
      "links": "https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr",
      "type": "播放列表（12 集）",
      "difficulty": "入门",
      "language": "英文（社区中文字幕可选）",
      "duration": "约 3 小时",
      "covers": "导数的几何本质、切线、幂/指数/三角函数求导、链式法则与乘积法则（可视化）、隐函数求导、极限、积分与微积分基本定理、泰勒级数",
      "align": "L22–L26（微积分）",
      "why": "第 4 集「可视化链式法则」是 AURORA 反向传播（L24–L25）的直觉基石；强调「让你觉得自己本可以发明微积分」，与第一性原理精神一致。",
      "urls": [
        {
          "url": "https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr",
          "label": "播放列表"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "入门"
      ],
      "langTags": [
        "中文",
        "英文"
      ],
      "searchable": "微积分的本质 essence of calculus grant sanderson (3blue1brown) 导数的几何本质、切线、幂/指数/三角函数求导、链式法则与乘积法则（可视化）、隐函数求导、极限、积分与微积分基本定理、泰勒级数 l22–l26（微积分） 第 4 集「可视化链式法则」是 aurora 反向传播（l24–l25）的直觉基石；强调「让你觉得自己本可以发明微积分」，与第一性原理精神一致。 播放列表（12 集）"
    },
    {
      "title": "傅里叶变换 & 傅里叶级数（两集可视化直觉）",
      "topPick": false,
      "phase": "Phase 0–1 · 数学与信号直觉基础（L01–L08）",
      "instructor": "Grant Sanderson (3Blue1Brown)",
      "links": "傅里叶变换 https://www.youtube.com/watch?v=spUNpyF58BY ｜ 傅里叶级数 https://www.youtube.com/watch?v=r6sGWTCMz2k",
      "type": "单视频 ×2",
      "difficulty": "入门 → 进阶",
      "language": "英文（社区中文字幕可选）",
      "duration": "约 21 分 + 25 分",
      "covers": "把信号「绕在圆上」求质心 → 频域分解的几何本质；旋转向量（复指数）叠加逼近任意波形/方波，即「方波 = 正弦叠加」",
      "align": "L07–L08（傅里叶直觉），并在 L35–L42 手写 DFT/FFT 时复看",
      "why": "用旋转向量把「复指数 e^{iθ} + 叠加 = 频谱」讲透，直接对应 AURORA 手写 DFT 前必须建立的直觉；比任何公式推导都更「可复现」。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=spUNpyF58BY",
          "label": "视频"
        },
        {
          "url": "https://www.youtube.com/watch?v=r6sGWTCMz2k",
          "label": "视频"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "入门",
        "进阶"
      ],
      "langTags": [
        "中文",
        "英文"
      ],
      "searchable": "傅里叶变换 & 傅里叶级数（两集可视化直觉） grant sanderson (3blue1brown) 把信号「绕在圆上」求质心 → 频域分解的几何本质；旋转向量（复指数）叠加逼近任意波形/方波，即「方波 = 正弦叠加」 l07–l08（傅里叶直觉），并在 l35–l42 手写 dft/fft 时复看 用旋转向量把「复指数 e^{iθ} + 叠加 = 频谱」讲透，直接对应 aurora 手写 dft 前必须建立的直觉；比任何公式推导都更「可复现」。 单视频 ×2"
    },
    {
      "title": "欧拉公式（群论视角）Euler's Formula via Group Theory",
      "topPick": false,
      "phase": "Phase 0–1 · 数学与信号直觉基础（L01–L08）",
      "instructor": "Grant Sanderson (3Blue1Brown)",
      "links": "https://www.youtube.com/watch?v=mvmuCPvRoWQ",
      "type": "单视频",
      "difficulty": "进阶",
      "language": "英文（社区中文字幕可选）",
      "duration": "约 24 分钟",
      "covers": "把「数」看作「作用（旋转/缩放）」，理解 e^{iθ} 为何是绕单位圆旋转、e^{iπ}=−1 的几何含义",
      "align": "L05–L06（复数几何=旋转+缩放、欧拉公式）",
      "why": "直击 AURORA 复数模块核心命题「复数乘法 = 旋转 + 缩放」；用「作用」而非死记公式来理解欧拉公式，第一性原理典范。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=mvmuCPvRoWQ",
          "label": "视频"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "进阶"
      ],
      "langTags": [
        "中文",
        "英文"
      ],
      "searchable": "欧拉公式（群论视角）euler's formula via group theory grant sanderson (3blue1brown) 把「数」看作「作用（旋转/缩放）」，理解 e^{iθ} 为何是绕单位圆旋转、e^{iπ}=−1 的几何含义 l05–l06（复数几何=旋转+缩放、欧拉公式） 直击 aurora 复数模块核心命题「复数乘法 = 旋转 + 缩放」；用「作用」而非死记公式来理解欧拉公式，第一性原理典范。 单视频"
    },
    {
      "title": "可汗学院（简体中文）Khan Academy Mandarin",
      "topPick": false,
      "phase": "Phase 0–1 · 数学与信号直觉基础（L01–L08）",
      "instructor": "Khan Academy 简体中文组",
      "links": "https://www.youtube.com/user/KhanAcademyMandarin （配套习题站 https://zh.khanacademy.org/math/linear-algebra ）",
      "type": "频道 / 完整课程",
      "difficulty": "入门",
      "language": "中文（简体配音/字幕）",
      "duration": "单集 5–15 分钟，成体系",
      "covers": "向量与线性组合、矩阵与线性方程、点积与投影、零空间/列空间、秩、特征值特征向量、正交化；另有微积分/概率分册",
      "align": "L09–L21（线代）、部分 L22–L31",
      "why": "满足「中文入门梯度」需求；小步骤讲解 + 习题，适合先用母语打通概念再回 3B1B/MIT 深化。",
      "urls": [
        {
          "url": "https://www.youtube.com/user/KhanAcademyMandarin",
          "label": "频道"
        },
        {
          "url": "https://zh.khanacademy.org/math/linear-algebra",
          "label": "zh.khanacademy.org"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "入门"
      ],
      "langTags": [
        "中文"
      ],
      "searchable": "可汗学院（简体中文）khan academy mandarin khan academy 简体中文组 向量与线性组合、矩阵与线性方程、点积与投影、零空间/列空间、秩、特征值特征向量、正交化；另有微积分/概率分册 l09–l21（线代）、部分 l22–l31 满足「中文入门梯度」需求；小步骤讲解 + 习题，适合先用母语打通概念再回 3b1b/mit 深化。 频道 / 完整课程"
    },
    {
      "title": "MIT 18.06 线性代数（Gilbert Strang 完整课程）",
      "topPick": false,
      "phase": "Phase 2 · 线性代数（L09–L21）",
      "instructor": "Prof. Gilbert Strang, MIT OpenCourseWare",
      "links": "https://www.youtube.com/playlist?list=PL221E2BBF13BECF6C （18.06SC, Fall 2011）",
      "type": "完整课程（约 35+ 讲，含习题精讲）",
      "difficulty": "进阶",
      "language": "英文（YouTube 字幕）",
      "duration": "约 35–40 小时",
      "covers": "高斯消元、A=LU、列空间/零空间/秩、正交性与投影、Gram-Schmidt/QR、行列式、特征值与对角化 A=PDP⁻¹、对称/正定矩阵、SVD、线性变换",
      "align": "L09–L21（线性代数）",
      "why": "AURORA 手写高斯消元、LU/QR/SVD、特征分解的权威严谨对照；Strang 边推导边讲「为什么」，是把 3B1B 直觉落到可手写实现的桥梁。",
      "urls": [
        {
          "url": "https://www.youtube.com/playlist?list=PL221E2BBF13BECF6C",
          "label": "播放列表"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "进阶"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "mit 18.06 线性代数（gilbert strang 完整课程） prof. gilbert strang, mit opencourseware 高斯消元、a=lu、列空间/零空间/秩、正交性与投影、gram-schmidt/qr、行列式、特征值与对角化 a=pdp⁻¹、对称/正定矩阵、svd、线性变换 l09–l21（线性代数） aurora 手写高斯消元、lu/qr/svd、特征分解的权威严谨对照；strang 边推导边讲「为什么」，是把 3b1b 直觉落到可手写实现的桥梁。 完整课程（约 35+ 讲，含习题精讲）"
    },
    {
      "title": "奇异值分解 SVD（Data-Driven Science & Engineering）",
      "topPick": false,
      "phase": "Phase 2 · 线性代数（L09–L21）",
      "instructor": "Prof. Steve Brunton, University of Washington",
      "links": "https://www.youtube.com/playlist?list=PLMrJAkhIeNNSVjnsviglFoY2nXildDCcv",
      "type": "播放列表（约 7 小时）",
      "difficulty": "进阶 → 高级",
      "language": "英文",
      "duration": "约 7 小时",
      "covers": "SVD 数学概览、矩阵低秩逼近、主导相关性、图像压缩（手写代码）、矩阵补全、PCA 与 SVD 关系、随机化 SVD",
      "align": "L18–L21（特征值/SVD、矩阵分解）",
      "why": "每个概念都配 Python/MATLAB 手撕代码，与 AURORA「NumPy 手写并对齐参考实现」的工作流几乎一模一样。",
      "urls": [
        {
          "url": "https://www.youtube.com/playlist?list=PLMrJAkhIeNNSVjnsviglFoY2nXildDCcv",
          "label": "播放列表"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "进阶",
        "高级"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "奇异值分解 svd（data-driven science & engineering） prof. steve brunton, university of washington svd 数学概览、矩阵低秩逼近、主导相关性、图像压缩（手写代码）、矩阵补全、pca 与 svd 关系、随机化 svd l18–l21（特征值/svd、矩阵分解） 每个概念都配 python/matlab 手撕代码，与 aurora「numpy 手写并对齐参考实现」的工作流几乎一模一样。 播放列表（约 7 小时）"
    },
    {
      "title": "Serrano.Academy（机器学习数学直觉）",
      "topPick": false,
      "phase": "Phase 2 · 线性代数（L09–L21）",
      "instructor": "Dr. Luis Serrano（前 Google/Apple/Udacity/Cohere，数学博士）",
      "links": "https://www.youtube.com/channel/UCgBncpylJ1kiVaPyP-PZauQ",
      "type": "频道（含 SVD/PCA、概率、softmax、Bayes 等播放列表）",
      "difficulty": "入门 → 进阶",
      "language": "英文（另有西语频道）",
      "duration": "单集 10–30 分钟",
      "covers": "奇异值分解与图像压缩、主成分分析、点积与投影、概率与贝叶斯、softmax/交叉熵、余弦相似度",
      "align": "L11–L21（线代）、L27–L31（概率统计）",
      "why": "擅长用类比/图示把 SVD、softmax 讲到「能自己重写一遍」，是 3B1B 与名校课之间的难度衔接层。",
      "urls": [
        {
          "url": "https://www.youtube.com/channel/UCgBncpylJ1kiVaPyP-PZauQ",
          "label": "频道"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "入门",
        "进阶"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "serrano.academy（机器学习数学直觉） dr. luis serrano（前 google/apple/udacity/cohere，数学博士） 奇异值分解与图像压缩、主成分分析、点积与投影、概率与贝叶斯、softmax/交叉熵、余弦相似度 l11–l21（线代）、l27–l31（概率统计） 擅长用类比/图示把 svd、softmax 讲到「能自己重写一遍」，是 3b1b 与名校课之间的难度衔接层。 频道（含 svd/pca、概率、softmax、bayes 等播放列表）"
    },
    {
      "title": "神经网络如何学习：梯度下降 + 反向传播直觉",
      "topPick": false,
      "phase": "Phase 3 · 微积分（L22–L26）",
      "instructor": "Grant Sanderson (3Blue1Brown)",
      "links": "梯度下降 https://www.youtube.com/watch?v=IHZwWFHWa-w ｜ 反向传播微积分 https://www.youtube.com/watch?v=tIeHLnjs5U8",
      "type": "单视频 ×2（隶属 Neural Networks 系列）",
      "difficulty": "进阶",
      "language": "英文（官方多语字幕，含简体中文）",
      "duration": "约 21 分 + 14 分",
      "covers": "代价函数曲面、梯度=最速下降方向、梯度下降迭代；反向传播如何按链式法则高效计算梯度",
      "align": "L24–L25（链式法则 / 梯度下降），延伸 L54–L57",
      "why": "把「链式法则 → 反向传播」的可视化讲到极致，是 AURORA 手写训练循环前的必看直觉课。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=IHZwWFHWa-w",
          "label": "视频"
        },
        {
          "url": "https://www.youtube.com/watch?v=tIeHLnjs5U8",
          "label": "视频"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "进阶"
      ],
      "langTags": [
        "中文",
        "英文"
      ],
      "searchable": "神经网络如何学习：梯度下降 + 反向传播直觉 grant sanderson (3blue1brown) 代价函数曲面、梯度=最速下降方向、梯度下降迭代；反向传播如何按链式法则高效计算梯度 l24–l25（链式法则 / 梯度下降），延伸 l54–l57 把「链式法则 → 反向传播」的可视化讲到极致，是 aurora 手写训练循环前的必看直觉课。 单视频 ×2（隶属 neural networks 系列）"
    },
    {
      "title": "MIT 18.02 多元微积分（梯度与偏导）",
      "topPick": false,
      "phase": "Phase 3 · 微积分（L22–L26）",
      "instructor": "Prof. Denis Auroux, MIT OpenCourseWare (Fall 2007)",
      "links": "https://www.youtube.com/playlist?list=PLEAYkSg4uSQ2dvsWLz9X6ANX_U-cwtOaX",
      "type": "完整课程（35 讲）",
      "difficulty": "进阶",
      "language": "英文",
      "duration": "约 30 小时",
      "covers": "偏导数、梯度与方向导数、多元链式法则、拉格朗日乘子、二重/三重积分、向量微积分",
      "align": "L23（梯度/偏导），支撑 L24–L25",
      "why": "为 AURORA 梯度下降与反向传播提供多元微积分的严谨底座；Auroux 的偏导/梯度两讲是把 3B1B 直觉补成可推导实现的关键。",
      "urls": [
        {
          "url": "https://www.youtube.com/playlist?list=PLEAYkSg4uSQ2dvsWLz9X6ANX_U-cwtOaX",
          "label": "播放列表"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "进阶"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "mit 18.02 多元微积分（梯度与偏导） prof. denis auroux, mit opencourseware (fall 2007) 偏导数、梯度与方向导数、多元链式法则、拉格朗日乘子、二重/三重积分、向量微积分 l23（梯度/偏导），支撑 l24–l25 为 aurora 梯度下降与反向传播提供多元微积分的严谨底座；auroux 的偏导/梯度两讲是把 3b1b 直觉补成可推导实现的关键。 完整课程（35 讲）"
    },
    {
      "title": "StatQuest 统计基础 Statistics Fundamentals",
      "topPick": false,
      "phase": "Phase 4 · 概率统计（L27–L31）",
      "instructor": "Josh Starmer (StatQuest)",
      "links": "https://www.youtube.com/playlist?list=PLblh5JKOoLUK0FLuzwntyYI10UQFUhsY9",
      "type": "播放列表（约 60 集）",
      "difficulty": "入门",
      "language": "英文（清晰口语 + 字幕）",
      "duration": "约 10–15 小时",
      "covers": "直方图/分布、均值/方差/标准差、正态分布、采样与总体参数、协方差与相关、中心极限定理、标准误、概率 vs 似然、最大似然估计、期望值、z-score",
      "align": "L27–L31（概率统计）",
      "why": "「把每个方法拆成最小步骤」的教学法与 AURORA 手写实现同频；均值/方差/z-score/分布采样（L28–L30）用它打底最省力。",
      "urls": [
        {
          "url": "https://www.youtube.com/playlist?list=PLblh5JKOoLUK0FLuzwntyYI10UQFUhsY9",
          "label": "播放列表"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "入门"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "statquest 统计基础 statistics fundamentals josh starmer (statquest) 直方图/分布、均值/方差/标准差、正态分布、采样与总体参数、协方差与相关、中心极限定理、标准误、概率 vs 似然、最大似然估计、期望值、z-score l27–l31（概率统计） 「把每个方法拆成最小步骤」的教学法与 aurora 手写实现同频；均值/方差/z-score/分布采样（l28–l30）用它打底最省力。 播放列表（约 60 集）"
    },
    {
      "title": "Harvard Stat 110: Probability（Joe Blitzstein 完整课程）",
      "topPick": false,
      "phase": "Phase 4 · 概率统计（L27–L31）",
      "instructor": "Prof. Joe Blitzstein, Harvard University",
      "links": "https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo",
      "type": "完整课程（34 讲）",
      "difficulty": "进阶 → 高级",
      "language": "英文",
      "duration": "约 28 小时",
      "covers": "概率与计数、条件概率/独立性、随机变量与分布（伯努利/二项/几何/泊松/均匀/正态/指数）、期望与线性性、方差/协方差、条件期望、不等式、大数定律与中心极限定理",
      "align": "L27–L31（概率统计）",
      "why": "条件概率/独立性/大数定律（L27）的黄金标准课；Blitzstein 坚持「从定义一步步推、拒绝套公式」。",
      "urls": [
        {
          "url": "https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo",
          "label": "播放列表"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "进阶",
        "高级"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "harvard stat 110: probability（joe blitzstein 完整课程） prof. joe blitzstein, harvard university 概率与计数、条件概率/独立性、随机变量与分布（伯努利/二项/几何/泊松/均匀/正态/指数）、期望与线性性、方差/协方差、条件期望、不等式、大数定律与中心极限定理 l27–l31（概率统计） 条件概率/独立性/大数定律（l27）的黄金标准课；blitzstein 坚持「从定义一步步推、拒绝套公式」。 完整课程（34 讲）"
    },
    {
      "title": "StatQuest 神经网络 / 深度学习（含 Softmax 与交叉熵导数）",
      "topPick": false,
      "phase": "Phase 4 · 概率统计（L27–L31）",
      "instructor": "Josh Starmer (StatQuest)",
      "links": "https://www.youtube.com/playlist?list=PLblh5JKOoLUIxGDQs4LFFD--41Vzf-ME1",
      "type": "播放列表",
      "difficulty": "进阶",
      "language": "英文",
      "duration": "约 6–8 小时",
      "covers": "ArgMax/SoftMax、SoftMax 导数逐步推导、交叉熵、交叉熵导数与反向传播、神经网络基础到 Transformer",
      "align": "L30–L31（softmax 与交叉熵），延伸 L55–L58",
      "why": "把 softmax 与交叉熵的导数一步步手推，正好对齐 AURORA 手写并验证梯度的要求。",
      "urls": [
        {
          "url": "https://www.youtube.com/playlist?list=PLblh5JKOoLUIxGDQs4LFFD--41Vzf-ME1",
          "label": "播放列表"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "进阶"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "statquest 神经网络 / 深度学习（含 softmax 与交叉熵导数） josh starmer (statquest) argmax/softmax、softmax 导数逐步推导、交叉熵、交叉熵导数与反向传播、神经网络基础到 transformer l30–l31（softmax 与交叉熵），延伸 l55–l58 把 softmax 与交叉熵的导数一步步手推，正好对齐 aurora 手写并验证梯度的要求。 播放列表"
    },
    {
      "title": "Audio Signal Processing for Machine Learning（必看 · 置顶）",
      "topPick": true,
      "phase": "Phase 5 · Audio DSP 音频信号处理（L32–L53）",
      "instructor": "Valerio Velardo — The Sound of AI",
      "links": "https://www.youtube.com/playlist?list=PL-wATfeyAMNqIee7cH3q1bh4QJFAaeNv0",
      "type": "播放列表（约 24 讲）",
      "difficulty": "入门 → 进阶",
      "language": "英文（自带英文字幕）",
      "duration": "累计约 12 小时",
      "covers": "声波与波形、时域/频域特征（RMS、过零率、频谱质心）、傅里叶变换与 STFT、频谱图、Mel 频率尺度与三角滤波器组、Mel 频谱、MFCC 完整流水线；每讲「直觉 + 数学 + Python 实现」三段式，配 GitHub 代码",
      "align": "L32–L53（Audio DSP 全阶段）",
      "why": "与本阶段几乎逐课对应，全网最贴合 AURORA 音频核心的系列；FFT/STFT/Mel/MFCC 全部亲手实现、不套黑箱，是「第一性原理手写」的范本。",
      "urls": [
        {
          "url": "https://www.youtube.com/playlist?list=PL-wATfeyAMNqIee7cH3q1bh4QJFAaeNv0",
          "label": "播放列表"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "入门",
        "进阶"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "audio signal processing for machine learning（必看 · 置顶） valerio velardo — the sound of ai 声波与波形、时域/频域特征（rms、过零率、频谱质心）、傅里叶变换与 stft、频谱图、mel 频率尺度与三角滤波器组、mel 频谱、mfcc 完整流水线；每讲「直觉 + 数学 + python 实现」三段式，配 github 代码 l32–l53（audio dsp 全阶段） 与本阶段几乎逐课对应，全网最贴合 aurora 音频核心的系列；fft/stft/mel/mfcc 全部亲手实现、不套黑箱，是「第一性原理手写」的范本。 播放列表（约 24 讲）"
    },
    {
      "title": "The Sound of AI 频道（Mel 谱 / MFCC 单课深挖）",
      "topPick": false,
      "phase": "Phase 5 · Audio DSP 音频信号处理（L32–L53）",
      "instructor": "Valerio Velardo — The Sound of AI",
      "links": "https://www.youtube.com/channel/UCZPFjMe1uRSirmSpznqvJfQ",
      "type": "频道（含多支独立长视频）",
      "difficulty": "进阶",
      "language": "英文",
      "duration": "单课 40–60 分钟",
      "covers": "单独成篇的 Mel 频谱、Cepstrum 倒谱、MFCC 逐步推导与可视化，及声道/语音生成物理解释",
      "align": "L46–L53（Mel / MFCC）",
      "why": "讲 MFCC 时把「信号→STFT→Mel→log→DCT」每一环拆开手算，直接支撑 L49–L53。⚠️ 单课直链未逐一核实，在该频道搜 \"Mel-Frequency Cepstral Coefficients Explained Easily\"。",
      "urls": [
        {
          "url": "https://www.youtube.com/channel/UCZPFjMe1uRSirmSpznqvJfQ",
          "label": "频道"
        }
      ],
      "unverified": true,
      "diffLevels": [
        "进阶"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "the sound of ai 频道（mel 谱 / mfcc 单课深挖） valerio velardo — the sound of ai 单独成篇的 mel 频谱、cepstrum 倒谱、mfcc 逐步推导与可视化，及声道/语音生成物理解释 l46–l53（mel / mfcc） 讲 mfcc 时把「信号→stft→mel→log→dct」每一环拆开手算，直接支撑 l49–l53。⚠️ 单课直链未逐一核实，在该频道搜 \"mel-frequency cepstral coefficients explained easily\"。 频道（含多支独立长视频）"
    },
    {
      "title": "But what is the Fourier Transform? / Fourier series（可视化直觉）",
      "topPick": false,
      "phase": "Phase 5 · Audio DSP 音频信号处理（L32–L53）",
      "instructor": "3Blue1Brown (Grant Sanderson)",
      "links": "变换 https://www.youtube.com/watch?v=spUNpyF58BY ｜ 级数 https://www.youtube.com/watch?v=r6sGWTCMz2k （另见 [Phase 0–1](#phase-01--数学与信号直觉基础l01l08)）",
      "type": "单视频 ×2",
      "difficulty": "入门",
      "language": "英文（含社区中文字幕）",
      "duration": "约 20 分 + 25 分",
      "covers": "旋转因子 e^{-2πift} 的几何意义、复指数求和逼近周期函数",
      "align": "L35, L37–L42",
      "why": "动手写 DFT 前建立「旋转因子/复指数」几何直觉，让 L35 欧拉公式与 L37 暴力 DFT 的求和不再是死公式。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=spUNpyF58BY",
          "label": "视频"
        },
        {
          "url": "https://www.youtube.com/watch?v=r6sGWTCMz2k",
          "label": "视频"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "入门"
      ],
      "langTags": [
        "中文",
        "英文"
      ],
      "searchable": "but what is the fourier transform? / fourier series（可视化直觉） 3blue1brown (grant sanderson) 旋转因子 e^{-2πift} 的几何意义、复指数求和逼近周期函数 l35, l37–l42 动手写 dft 前建立「旋转因子/复指数」几何直觉，让 l35 欧拉公式与 l37 暴力 dft 的求和不再是死公式。 单视频 ×2"
    },
    {
      "title": "Fourier Analysis [Data-Driven Science and Engineering]",
      "topPick": false,
      "phase": "Phase 5 · Audio DSP 音频信号处理（L32–L53）",
      "instructor": "Steve Brunton — University of Washington",
      "links": "https://www.youtube.com/playlist?list=PLMrJAkhIeNNT_Xh3Oy0Y4LTj0Oxo8GqsC",
      "type": "播放列表（完整课程）",
      "difficulty": "进阶",
      "language": "英文",
      "duration": "约 8 小时 / 40+ 讲",
      "covers": "傅里叶级数、复数傅里叶级数、傅里叶变换、DFT、FFT 算法、Gabor 变换/声谱图、小波；含 MATLAB + Python 实操（去噪、求导、解 PDE）",
      "align": "L35–L48",
      "why": "名校教授系统串讲 DFT→FFT 的数学与代码，DFT 矩阵分解视角直接指导 L37 O(N²) 暴力法与 L38–L42 蝶形分治的手写实现。",
      "urls": [
        {
          "url": "https://www.youtube.com/playlist?list=PLMrJAkhIeNNT_Xh3Oy0Y4LTj0Oxo8GqsC",
          "label": "播放列表"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "进阶"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "fourier analysis [data-driven science and engineering] steve brunton — university of washington 傅里叶级数、复数傅里叶级数、傅里叶变换、dft、fft 算法、gabor 变换/声谱图、小波；含 matlab + python 实操（去噪、求导、解 pde） l35–l48 名校教授系统串讲 dft→fft 的数学与代码，dft 矩阵分解视角直接指导 l37 o(n²) 暴力法与 l38–l42 蝶形分治的手写实现。 播放列表（完整课程）"
    },
    {
      "title": "The Fast Fourier Transform: Most Ingenious Algorithm Ever?",
      "topPick": false,
      "phase": "Phase 5 · Audio DSP 音频信号处理（L32–L53）",
      "instructor": "Reducible",
      "links": "https://www.youtube.com/watch?v=h7apO7q16V0",
      "type": "单视频",
      "difficulty": "进阶",
      "language": "英文",
      "duration": "约 28 分钟",
      "covers": "从多项式乘法引入，讲 N 次单位根、分治递归、Cooley-Tukey 蝶形结构与 IFFT，动画拆解 O(N log N)",
      "align": "L38–L42",
      "why": "全网讲「为什么 FFT 能分治」最清晰的动画，直接对标 L39–L40「从零手写 FFT」，递归结构可照着改写成 NumPy。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=h7apO7q16V0",
          "label": "视频"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "进阶"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "the fast fourier transform: most ingenious algorithm ever? reducible 从多项式乘法引入，讲 n 次单位根、分治递归、cooley-tukey 蝶形结构与 ifft，动画拆解 o(n log n) l38–l42 全网讲「为什么 fft 能分治」最清晰的动画，直接对标 l39–l40「从零手写 fft」，递归结构可照着改写成 numpy。 单视频"
    },
    {
      "title": "Denoising Data with FFT [Python]",
      "topPick": false,
      "phase": "Phase 5 · Audio DSP 音频信号处理（L32–L53）",
      "instructor": "Steve Brunton — University of Washington",
      "links": "https://www.youtube.com/watch?v=s2K1JfNR7Sc",
      "type": "单视频",
      "difficulty": "进阶",
      "language": "英文",
      "duration": "约 11 分钟",
      "covers": "用 Python/NumPy 对含噪信号做 FFT、看幅度谱、按功率阈值滤波再逆变换的完整代码演示",
      "align": "L40–L42（频谱分析实战）",
      "why": "一支端到端的「手写 FFT 频谱分析 + 幅度谱/功率谱」实操，可作为 AURORA 手写 FFT 后的验证案例。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=s2K1JfNR7Sc",
          "label": "视频"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "进阶"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "denoising data with fft [python] steve brunton — university of washington 用 python/numpy 对含噪信号做 fft、看幅度谱、按功率阈值滤波再逆变换的完整代码演示 l40–l42（频谱分析实战） 一支端到端的「手写 fft 频谱分析 + 幅度谱/功率谱」实操，可作为 aurora 手写 fft 后的验证案例。 单视频"
    },
    {
      "title": "How the Cooley-Tukey FFT Algorithm Works（逐步手推 FFT）",
      "topPick": false,
      "phase": "Phase 5 · Audio DSP 音频信号处理（L32–L53）",
      "instructor": "Mark Newman — Mark Newman Education",
      "links": "https://www.youtube.com/c/MarkNewmanEducation ⚠️（系列单视频直链未核实；频道已核实，配套图文见 dsprelated.com 同名 Part 1–4）",
      "type": "频道 / 多集系列",
      "difficulty": "进阶 → 高级",
      "language": "英文",
      "duration": "分 4 部分",
      "covers": "用归并排序类比讲奇偶分解，2 点 DFT 化为加减、bit-reversal 重排、twiddle factor 推导，直至可手写实现的蝶形图",
      "align": "L38–L42",
      "why": "把 FFT 拆到「能照着敲代码」的颗粒度，最契合从零实现 FFT（搜 \"Mark Newman Cooley-Tukey FFT\"）。",
      "urls": [
        {
          "url": "https://www.youtube.com/c/MarkNewmanEducation",
          "label": "频道"
        }
      ],
      "unverified": true,
      "diffLevels": [
        "进阶",
        "高级"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "how the cooley-tukey fft algorithm works（逐步手推 fft） mark newman — mark newman education 用归并排序类比讲奇偶分解，2 点 dft 化为加减、bit-reversal 重排、twiddle factor 推导，直至可手写实现的蝶形图 l38–l42 把 fft 拆到「能照着敲代码」的颗粒度，最契合从零实现 fft（搜 \"mark newman cooley-tukey fft\"）。 频道 / 多集系列"
    },
    {
      "title": "MIT RES.6.007 Signals and Systems（信号与系统全课）",
      "topPick": false,
      "phase": "Phase 5 · Audio DSP 音频信号处理（L32–L53）",
      "instructor": "Alan V. Oppenheim — MIT OpenCourseWare",
      "links": "https://www.youtube.com/playlist?list=PL41692B571DD0AF9B",
      "type": "完整课程（约 30 讲）",
      "difficulty": "高级",
      "language": "英文",
      "duration": "每讲约 50 分钟",
      "covers": "连续/离散时间信号与系统、傅里叶级数/变换、采样与重建、Laplace/Z 变换",
      "align": "L32–L48",
      "why": "DSP 泰斗、经典教材作者亲授，为 AURORA 的傅里叶与采样章节提供最权威的理论地基与符号规范。",
      "urls": [
        {
          "url": "https://www.youtube.com/playlist?list=PL41692B571DD0AF9B",
          "label": "播放列表"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "高级"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "mit res.6.007 signals and systems（信号与系统全课） alan v. oppenheim — mit opencourseware 连续/离散时间信号与系统、傅里叶级数/变换、采样与重建、laplace/z 变换 l32–l48 dsp 泰斗、经典教材作者亲授，为 aurora 的傅里叶与采样章节提供最权威的理论地基与符号规范。 完整课程（约 30 讲）"
    },
    {
      "title": "MIT RES.6.007 — Lecture 16: Sampling（采样 / Nyquist / 混叠）",
      "topPick": false,
      "phase": "Phase 5 · Audio DSP 音频信号处理（L32–L53）",
      "instructor": "Alan V. Oppenheim — MIT OpenCourseWare",
      "links": "https://www.youtube.com/watch?v=P3eLer1edx8",
      "type": "单视频（课程第 16 讲）",
      "difficulty": "高级",
      "language": "英文",
      "duration": "约 50 分钟",
      "covers": "冲激采样、频谱周期化、Nyquist 采样定理证明、混叠成因与频域图解、重建条件",
      "align": "L33–L34（Nyquist 与混叠）",
      "why": "权威推导 Nyquist 定理与混叠，正是 L34 aliasing 一课的理论出处。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=P3eLer1edx8",
          "label": "视频"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "高级"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "mit res.6.007 — lecture 16: sampling（采样 / nyquist / 混叠） alan v. oppenheim — mit opencourseware 冲激采样、频谱周期化、nyquist 采样定理证明、混叠成因与频域图解、重建条件 l33–l34（nyquist 与混叠） 权威推导 nyquist 定理与混叠，正是 l34 aliasing 一课的理论出处。 单视频（课程第 16 讲）"
    },
    {
      "title": "深度学习与人类语言处理 DLHLP（2020，含语音特征）",
      "topPick": false,
      "phase": "Phase 5 · Audio DSP 音频信号处理（L32–L53）",
      "instructor": "李宏毅 Hung-yi Lee — 台湾大学 NTU",
      "links": "https://www.youtube.com/playlist?list=PLJV_el3uVTsO07RpBYFsXg-bN5Lu0nhdG",
      "type": "完整课程",
      "difficulty": "进阶",
      "language": "中文（国语讲授，含中文字幕）",
      "duration": "每讲约 1 小时",
      "covers": "语音识别总览中的声学特征（MFCC/滤波器组）、frame 切分与特征提取，及后续 LAS/CTC/RNN-T 语音模型",
      "align": "L49–L53（特征工程的中文对应）",
      "why": "顶尖华语名师，用中文把「波形→帧→MFCC/filter bank 特征」讲清，补齐双语课程的中文侧。",
      "urls": [
        {
          "url": "https://www.youtube.com/playlist?list=PLJV_el3uVTsO07RpBYFsXg-bN5Lu0nhdG",
          "label": "播放列表"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "进阶"
      ],
      "langTags": [
        "中文"
      ],
      "searchable": "深度学习与人类语言处理 dlhlp（2020，含语音特征） 李宏毅 hung-yi lee — 台湾大学 ntu 语音识别总览中的声学特征（mfcc/滤波器组）、frame 切分与特征提取，及后续 las/ctc/rnn-t 语音模型 l49–l53（特征工程的中文对应） 顶尖华语名师，用中文把「波形→帧→mfcc/filter bank 特征」讲清，补齐双语课程的中文侧。 完整课程"
    },
    {
      "title": "Neural Networks: Zero to Hero（完整课程）",
      "topPick": true,
      "phase": "Phase 6 · 机器学习 / 深度学习基础（L54–L65）",
      "instructor": "Andrej Karpathy（前 OpenAI / 前 Tesla AI 总监）",
      "links": "https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ",
      "type": "播放列表（8 讲）",
      "difficulty": "入门 → 高级",
      "language": "英文（自动中英字幕）",
      "duration": "约 15+ 小时",
      "covers": "micrograd 标量自动微分引擎、反向传播、makemore（bigram→MLP→BatchNorm→手推反向 \"Backprop Ninja\"→WaveNet）、Let's build GPT",
      "align": "L54–L58（深度学习），并延伸 L83（LLM）",
      "why": "AURORA「第一性原理/手写实现」的黄金对标——全程从零手写节点、前向反向、训练循环，不用任何 wrapper。本主题必收核心。",
      "urls": [
        {
          "url": "https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ",
          "label": "播放列表"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "入门",
        "高级"
      ],
      "langTags": [
        "中文",
        "英文"
      ],
      "searchable": "neural networks: zero to hero（完整课程） andrej karpathy（前 openai / 前 tesla ai 总监） micrograd 标量自动微分引擎、反向传播、makemore（bigram→mlp→batchnorm→手推反向 \"backprop ninja\"→wavenet）、let's build gpt l54–l58（深度学习），并延伸 l83（llm） aurora「第一性原理/手写实现」的黄金对标——全程从零手写节点、前向反向、训练循环，不用任何 wrapper。本主题必收核心。 播放列表（8 讲）"
    },
    {
      "title": "The spelled-out intro to neural networks and backpropagation: building micrograd",
      "topPick": false,
      "phase": "Phase 6 · 机器学习 / 深度学习基础（L54–L65）",
      "instructor": "Andrej Karpathy",
      "links": "https://youtu.be/VMj-3S1tku0 （配套：makemore Part 2 (MLP) https://youtu.be/TCH_1BHY58I ｜\"Backprop Ninja\" https://youtu.be/q8SA3rM6ckI ）",
      "type": "单视频",
      "difficulty": "入门",
      "language": "英文（中英字幕）",
      "duration": "2 小时 25 分",
      "covers": "手写 Value 节点（add/mul/pow/tanh/exp）、构建动态计算图 DAG、链式法则逐层反向、手推梯度、在 micrograd 上搭 MLP 并训练",
      "align": "L54–L56（Value 计算图、算子补全、反向传播手推）",
      "why": "与 L54–L56 几乎逐点对应，最详尽的 \"spelled-out\" 反向传播讲解；配套 makemore Part 2 对齐 L57（MLP），\"Backprop Ninja\" 对齐 L55（手推反向）。",
      "urls": [
        {
          "url": "https://youtu.be/VMj-3S1tku0",
          "label": "视频"
        },
        {
          "url": "https://youtu.be/TCH_1BHY58I",
          "label": "视频"
        },
        {
          "url": "https://youtu.be/q8SA3rM6ckI",
          "label": "视频"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "入门"
      ],
      "langTags": [
        "中文",
        "英文"
      ],
      "searchable": "the spelled-out intro to neural networks and backpropagation: building micrograd andrej karpathy 手写 value 节点（add/mul/pow/tanh/exp）、构建动态计算图 dag、链式法则逐层反向、手推梯度、在 micrograd 上搭 mlp 并训练 l54–l56（value 计算图、算子补全、反向传播手推） 与 l54–l56 几乎逐点对应，最详尽的 \"spelled-out\" 反向传播讲解；配套 makemore part 2 对齐 l57（mlp），\"backprop ninja\" 对齐 l55（手推反向）。 单视频"
    },
    {
      "title": "Neural Networks（可视化系列）",
      "topPick": false,
      "phase": "Phase 6 · 机器学习 / 深度学习基础（L54–L65）",
      "instructor": "Grant Sanderson (3Blue1Brown)",
      "links": "https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi",
      "type": "播放列表（核心 4 集）",
      "difficulty": "入门",
      "language": "英文（官方多语字幕，含简体中文）",
      "duration": "约 1.5 小时",
      "covers": "什么是神经网络、梯度下降如何学习、反向传播直觉、反向传播微积分（链式法则）",
      "align": "L55–L57",
      "why": "用顶级动画把链式法则/反向传播的几何直觉讲透，是 L55 手推反向前的最佳直觉铺垫，与 Karpathy 的代码实现互补。",
      "urls": [
        {
          "url": "https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi",
          "label": "播放列表"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "入门"
      ],
      "langTags": [
        "中文",
        "英文"
      ],
      "searchable": "neural networks（可视化系列） grant sanderson (3blue1brown) 什么是神经网络、梯度下降如何学习、反向传播直觉、反向传播微积分（链式法则） l55–l57 用顶级动画把链式法则/反向传播的几何直觉讲透，是 l55 手推反向前的最佳直觉铺垫，与 karpathy 的代码实现互补。 播放列表（核心 4 集）"
    },
    {
      "title": "Neural Networks / Deep Learning",
      "topPick": false,
      "phase": "Phase 6 · 机器学习 / 深度学习基础（L54–L65）",
      "instructor": "StatQuest with Josh Starmer",
      "links": "https://www.youtube.com/playlist?list=PLblh5JKOoLUIxGDQs4LFFD--41Vzf-ME1",
      "type": "播放列表",
      "difficulty": "入门",
      "language": "英文（中英字幕）",
      "duration": "约 5–6 小时（多为 10–20 分钟短集）",
      "covers": "神经网络基础、反向传播主线思想、逐参数优化的链式法则、ReLU、CNN 图像分类",
      "align": "L55–L58、L64",
      "why": "\"Backpropagation Details Pt.1/Pt.2\" 把 L55 手推反向拆成最小步骤；CNN 集对齐 L64 音频分类的卷积直觉。",
      "urls": [
        {
          "url": "https://www.youtube.com/playlist?list=PLblh5JKOoLUIxGDQs4LFFD--41Vzf-ME1",
          "label": "播放列表"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "入门"
      ],
      "langTags": [
        "中文",
        "英文"
      ],
      "searchable": "neural networks / deep learning statquest with josh starmer 神经网络基础、反向传播主线思想、逐参数优化的链式法则、relu、cnn 图像分类 l55–l58、l64 \"backpropagation details pt.1/pt.2\" 把 l55 手推反向拆成最小步骤；cnn 集对齐 l64 音频分类的卷积直觉。 播放列表"
    },
    {
      "title": "MIT 6.S191: Introduction to Deep Learning",
      "topPick": false,
      "phase": "Phase 6 · 机器学习 / 深度学习基础（L54–L65）",
      "instructor": "MIT（Alexander Amini / Ava Soleimany）",
      "links": "https://www.youtube.com/playlist?list=PLtBw6njQRU-rwp5__7C0oIVt26ZgjG9NI （课程主页 https://introtodeeplearning.com/ ）",
      "type": "完整课程（每年更新）",
      "difficulty": "入门 → 进阶",
      "language": "英文（中英字幕）",
      "duration": "约 10 讲，每讲 45–60 分钟",
      "covers": "感知机与 MLP、反向传播、训练技巧（正则化/过拟合诊断）、CNN、RNN/Transformer，含 TensorFlow/PyTorch 实验",
      "align": "L54–L65（整体概览）",
      "why": "名校顶配、每年刷新的系统课，给 L54–L65 提供从 MLP 到 CNN、过拟合诊断的权威主线框架。",
      "urls": [
        {
          "url": "https://www.youtube.com/playlist?list=PLtBw6njQRU-rwp5__7C0oIVt26ZgjG9NI",
          "label": "播放列表"
        },
        {
          "url": "https://introtodeeplearning.com/",
          "label": "introtodeeplearning.com"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "入门",
        "进阶"
      ],
      "langTags": [
        "中文",
        "英文"
      ],
      "searchable": "mit 6.s191: introduction to deep learning mit（alexander amini / ava soleimany） 感知机与 mlp、反向传播、训练技巧（正则化/过拟合诊断）、cnn、rnn/transformer，含 tensorflow/pytorch 实验 l54–l65（整体概览） 名校顶配、每年刷新的系统课，给 l54–l65 提供从 mlp 到 cnn、过拟合诊断的权威主线框架。 完整课程（每年更新）"
    },
    {
      "title": "PyTorch for Audio + Music Processing",
      "topPick": true,
      "phase": "Phase 6 · 机器学习 / 深度学习基础（L54–L65）",
      "instructor": "Valerio Velardo — The Sound of AI",
      "links": "https://www.youtube.com/playlist?list=PL-wATfeyAMNoirN4idjev6aRu8ISZYVWm （代码 https://github.com/musikalkemist/pytorchforaudio ；示例 \"Training a Sound Classifier with PyTorch\" https://www.youtube.com/watch?v=MMkeLjcBTcI ）",
      "type": "播放列表",
      "difficulty": "进阶",
      "language": "英文（中英字幕）",
      "duration": "约 3–4 小时",
      "covers": "用 torchaudio 自定义音频 Dataset（__getitem__）、DataLoader 批量加载、提取 Mel 频谱、重采样/mixdown、搭 CNN 在 UrbanSound8K 上训练声音分类器、train loop",
      "align": "L62–L65",
      "why": "与 L62–L65 高度重合——自定义 Dataset/DataLoader + Mel 特征 + CNN 音频分类 + 训练闭环，几乎就是 AURORA 关键词识别任务的 PyTorch 蓝本。",
      "urls": [
        {
          "url": "https://www.youtube.com/playlist?list=PL-wATfeyAMNoirN4idjev6aRu8ISZYVWm",
          "label": "播放列表"
        },
        {
          "url": "https://github.com/musikalkemist/pytorchforaudio",
          "label": "代码"
        },
        {
          "url": "https://www.youtube.com/watch?v=MMkeLjcBTcI",
          "label": "视频"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "进阶"
      ],
      "langTags": [
        "中文",
        "英文"
      ],
      "searchable": "pytorch for audio + music processing valerio velardo — the sound of ai 用 torchaudio 自定义音频 dataset（__getitem__）、dataloader 批量加载、提取 mel 频谱、重采样/mixdown、搭 cnn 在 urbansound8k 上训练声音分类器、train loop l62–l65 与 l62–l65 高度重合——自定义 dataset/dataloader + mel 特征 + cnn 音频分类 + 训练闭环，几乎就是 aurora 关键词识别任务的 pytorch 蓝本。 播放列表"
    },
    {
      "title": "Learn PyTorch for Deep Learning – Full Course",
      "topPick": false,
      "phase": "Phase 6 · 机器学习 / 深度学习基础（L54–L65）",
      "instructor": "Daniel Bourke（freeCodeCamp.org 出品）",
      "links": "https://www.youtube.com/watch?v=V_xro1bcAuA （配套 https://www.learnpytorch.io/ ｜代码 https://github.com/mrdbourke/pytorch-deep-learning ）",
      "type": "单视频（约 25 小时）/ 完整课程",
      "difficulty": "入门 → 进阶",
      "language": "英文（中英字幕）",
      "duration": "约 25 小时",
      "covers": "PyTorch Tensor、autograd 与 requires_grad、nn.Module/Linear/Sequential、训练循环、自定义 Dataset、CNN、模型保存/加载",
      "align": "L59–L65",
      "why": "覆盖 L59–L65 全部 PyTorch 主题，可作为 PyTorch 段的系统主教程。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=V_xro1bcAuA",
          "label": "视频"
        },
        {
          "url": "https://www.learnpytorch.io/",
          "label": "learnpytorch.io"
        },
        {
          "url": "https://github.com/mrdbourke/pytorch-deep-learning",
          "label": "代码"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "入门",
        "进阶"
      ],
      "langTags": [
        "中文",
        "英文"
      ],
      "searchable": "learn pytorch for deep learning – full course daniel bourke（freecodecamp.org 出品） pytorch tensor、autograd 与 requires_grad、nn.module/linear/sequential、训练循环、自定义 dataset、cnn、模型保存/加载 l59–l65 覆盖 l59–l65 全部 pytorch 主题，可作为 pytorch 段的系统主教程。 单视频（约 25 小时）/ 完整课程"
    },
    {
      "title": "PyTorch Tutorials — Complete Beginner Course",
      "topPick": false,
      "phase": "Phase 6 · 机器学习 / 深度学习基础（L54–L65）",
      "instructor": "Patrick Loeber（现 Google DeepMind DevRel）",
      "links": "https://www.youtube.com/playlist?list=PLqnslRFeH2UrcDBWF5mfPGpqQDSta6VK4 （代码 https://github.com/patrickloeber/pytorchTutorial ）",
      "type": "播放列表",
      "difficulty": "入门",
      "language": "英文（中英字幕）",
      "duration": "约 4–5 小时",
      "covers": "Tensor 基础与 NumPy 互转、autograd 机制、backward 与梯度、手写线性/逻辑回归训练、nn.Module、Dataset & DataLoader、激活函数",
      "align": "L59–L62",
      "why": "短小精悍、逐个概念拆解，先手写训练循环再用 nn 封装，契合「先第一性原理后封装」的节奏。",
      "urls": [
        {
          "url": "https://www.youtube.com/playlist?list=PLqnslRFeH2UrcDBWF5mfPGpqQDSta6VK4",
          "label": "播放列表"
        },
        {
          "url": "https://github.com/patrickloeber/pytorchTutorial",
          "label": "代码"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "入门"
      ],
      "langTags": [
        "中文",
        "英文"
      ],
      "searchable": "pytorch tutorials — complete beginner course patrick loeber（现 google deepmind devrel） tensor 基础与 numpy 互转、autograd 机制、backward 与梯度、手写线性/逻辑回归训练、nn.module、dataset & dataloader、激活函数 l59–l62 短小精悍、逐个概念拆解，先手写训练循环再用 nn 封装，契合「先第一性原理后封装」的节奏。 播放列表"
    },
    {
      "title": "Deep Learning (For Audio) With Python",
      "topPick": false,
      "phase": "Phase 6 · 机器学习 / 深度学习基础（L54–L65）",
      "instructor": "Valerio Velardo — The Sound of AI",
      "links": "频道 https://www.youtube.com/@ValerioVelardoTheSoundofAI （代码 https://github.com/musikalkemist/DeepLearningForAudioWithPython ）⚠️ 播放列表直链未逐一核实，从频道 \"Playlists\" 进入 \"Deep Learning (For Audio) With Python\"",
      "type": "播放列表",
      "difficulty": "入门 → 进阶",
      "language": "英文（中英字幕）",
      "duration": "约 5–6 小时",
      "covers": "从零手写神经元与反向传播 → 声音/波形/傅里叶/STFT/Mel 谱/MFCC → MLP/CNN/RNN-LSTM 音乐流派分类",
      "align": "L54–L55、L63–L64",
      "why": "前几集从零手写神经元+反向传播（呼应 L54–L55），后半系统讲 Mel/MFCC 与 CNN 分类（呼应 L63–L64），把手写 ML 与音频 AI 打通。",
      "urls": [
        {
          "url": "https://www.youtube.com/@ValerioVelardoTheSoundofAI",
          "label": "频道"
        },
        {
          "url": "https://github.com/musikalkemist/DeepLearningForAudioWithPython",
          "label": "代码"
        }
      ],
      "unverified": true,
      "diffLevels": [
        "入门",
        "进阶"
      ],
      "langTags": [
        "中文",
        "英文"
      ],
      "searchable": "deep learning (for audio) with python valerio velardo — the sound of ai 从零手写神经元与反向传播 → 声音/波形/傅里叶/stft/mel 谱/mfcc → mlp/cnn/rnn-lstm 音乐流派分类 l54–l55、l63–l64 前几集从零手写神经元+反向传播（呼应 l54–l55），后半系统讲 mel/mfcc 与 cnn 分类（呼应 l63–l64），把手写 ml 与音频 ai 打通。 播放列表"
    },
    {
      "title": "Practical Deep Learning for Coders 2022",
      "topPick": false,
      "phase": "Phase 6 · 机器学习 / 深度学习基础（L54–L65）",
      "instructor": "Jeremy Howard（fast.ai）",
      "links": "https://www.youtube.com/playlist?list=PLfYUBJiXbdtSvpQjSnJJ_PmDQB_VyT5iU （课程主页 https://course.fast.ai/ ）",
      "type": "完整课程（9 讲）",
      "difficulty": "入门 → 进阶",
      "language": "英文（中英字幕）",
      "duration": "每讲约 90 分钟",
      "covers": "训练与部署模型、从零实现 MLP 与反向传播（\"从矩阵乘法搭起\"）、SGD 训练循环、CNN、过拟合诊断",
      "align": "L57–L65",
      "why": "以「先能跑通再拆内部」的工程视角补充 Karpathy；从零实现神经网络与训练循环，对齐 L57–L58 并延伸完整训练评估闭环。",
      "urls": [
        {
          "url": "https://www.youtube.com/playlist?list=PLfYUBJiXbdtSvpQjSnJJ_PmDQB_VyT5iU",
          "label": "播放列表"
        },
        {
          "url": "https://course.fast.ai/",
          "label": "course.fast.ai"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "入门",
        "进阶"
      ],
      "langTags": [
        "中文",
        "英文"
      ],
      "searchable": "practical deep learning for coders 2022 jeremy howard（fast.ai） 训练与部署模型、从零实现 mlp 与反向传播（\"从矩阵乘法搭起\"）、sgd 训练循环、cnn、过拟合诊断 l57–l65 以「先能跑通再拆内部」的工程视角补充 karpathy；从零实现神经网络与训练循环，对齐 l57–l58 并延伸完整训练评估闭环。 完整课程（9 讲）"
    },
    {
      "title": "機器學習 / 深度學習（Machine Learning, NTU 2021）",
      "topPick": false,
      "phase": "Phase 6 · 机器学习 / 深度学习基础（L54–L65）",
      "instructor": "李宏毅 Hung-yi Lee（台湾大学）",
      "links": "https://www.youtube.com/playlist?list=PLJV_el3uVTsPy9oCRY30oBPNLCo89yu49 （课程主页 https://speech.ee.ntu.edu.tw/~hylee/ml/2021-spring.html ）",
      "type": "完整课程",
      "difficulty": "入门 → 高级",
      "language": "中文（国语讲授，中文投影片）",
      "duration": "数十小时",
      "covers": "反向传播、梯度下降与优化、MLP/CNN、训练技巧（过拟合/正则化/批归一化）、深度学习理论",
      "align": "L54–L65",
      "why": "华语圈公认最佳中文深度学习课，反向传播与优化章节直接支撑 L55–L58，可作中文学习者主线。",
      "urls": [
        {
          "url": "https://www.youtube.com/playlist?list=PLJV_el3uVTsPy9oCRY30oBPNLCo89yu49",
          "label": "播放列表"
        },
        {
          "url": "https://speech.ee.ntu.edu.tw/~hylee/ml/2021-spring.html",
          "label": "speech.ee.ntu.edu.tw"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "入门",
        "高级"
      ],
      "langTags": [
        "中文"
      ],
      "searchable": "機器學習 / 深度學習（machine learning, ntu 2021） 李宏毅 hung-yi lee（台湾大学） 反向传播、梯度下降与优化、mlp/cnn、训练技巧（过拟合/正则化/批归一化）、深度学习理论 l54–l65 华语圈公认最佳中文深度学习课，反向传播与优化章节直接支撑 l55–l58，可作中文学习者主线。 完整课程"
    },
    {
      "title": "Machine Learning Specialization / DeepLearning.AI",
      "topPick": false,
      "phase": "Phase 6 · 机器学习 / 深度学习基础（L54–L65）",
      "instructor": "Andrew Ng（斯坦福 / DeepLearning.AI）",
      "links": "https://www.youtube.com/playlist?list=PLkDaE6sCZn6FNC6YRfRQc_FbeQrF8BwGI （频道 https://www.youtube.com/c/deeplearningai ）",
      "type": "播放列表 / 完整课程",
      "difficulty": "入门",
      "language": "英文（中英字幕）",
      "duration": "数十小时",
      "covers": "神经网络与深度学习基础、前向/反向传播、逻辑回归到深层网络、梯度下降、超参数与正则化",
      "align": "L54–L58",
      "why": "最经典的入门权威，把 MLP、前向反向、训练收敛讲得极稳，适合作为 Karpathy 手写实现的理论对照。",
      "urls": [
        {
          "url": "https://www.youtube.com/playlist?list=PLkDaE6sCZn6FNC6YRfRQc_FbeQrF8BwGI",
          "label": "播放列表"
        },
        {
          "url": "https://www.youtube.com/c/deeplearningai",
          "label": "频道"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "入门"
      ],
      "langTags": [
        "中文",
        "英文"
      ],
      "searchable": "machine learning specialization / deeplearning.ai andrew ng（斯坦福 / deeplearning.ai） 神经网络与深度学习基础、前向/反向传播、逻辑回归到深层网络、梯度下降、超参数与正则化 l54–l58 最经典的入门权威，把 mlp、前向反向、训练收敛讲得极稳，适合作为 karpathy 手写实现的理论对照。 播放列表 / 完整课程"
    },
    {
      "title": "李宏毅 DLHLP 2020 — Speech Recognition 系列（LAS / CTC / RNN-T / HMM）",
      "topPick": true,
      "phase": "Phase 7 · 语音识别 ASR / STT（L66–L75）",
      "instructor": "李宏毅 Hung-yi Lee（台大 NTU）",
      "links": "课程页 https://speech.ee.ntu.edu.tw/~hylee/dlhlp/2020-spring.php ｜频道 https://www.youtube.com/@HungyiLeeNTU",
      "type": "完整课程（内含 \"Speech Recognition\" 7 讲子系列）",
      "difficulty": "入门 → 进阶",
      "language": "中文（国语讲授）",
      "duration": "语音识别部分约 3–4 小时",
      "covers": "端到端 ASR 全景；Listen-Attend-Spell、CTC、RNN-T、HMM 对齐、beam search 解码直觉",
      "align": "L66–L75",
      "why": "全网最好的中文语音识别原理课，把 CTC / seq2seq / HMM→E2E 讲成直觉故事，和 AURORA「第一性原理」完全同频。中文置顶首选。",
      "urls": [
        {
          "url": "https://speech.ee.ntu.edu.tw/~hylee/dlhlp/2020-spring.php",
          "label": "speech.ee.ntu.edu.tw"
        },
        {
          "url": "https://www.youtube.com/@HungyiLeeNTU",
          "label": "频道"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "入门",
        "进阶"
      ],
      "langTags": [
        "中文"
      ],
      "searchable": "李宏毅 dlhlp 2020 — speech recognition 系列（las / ctc / rnn-t / hmm） 李宏毅 hung-yi lee（台大 ntu） 端到端 asr 全景；listen-attend-spell、ctc、rnn-t、hmm 对齐、beam search 解码直觉 l66–l75 全网最好的中文语音识别原理课，把 ctc / seq2seq / hmm→e2e 讲成直觉故事，和 aurora「第一性原理」完全同频。中文置顶首选。 完整课程（内含 \"speech recognition\" 7 讲子系列）"
    },
    {
      "title": "CMU 11-785 Introduction to Deep Learning — CTC / Seq2Seq",
      "topPick": false,
      "phase": "Phase 7 · 语音识别 ASR / STT（L66–L75）",
      "instructor": "Bhiksha Raj、Rita Singh（卡内基梅隆 CMU）",
      "links": "频道 https://www.youtube.com/channel/UC8hYZGEkI2dDO8scT8C5UQA ｜课程页 https://www.cs.cmu.edu/~bhiksha/courses/deeplearning/ ｜CTC 讲座 https://www.youtube.com/watch?v=5Rj0J9AuGw0",
      "type": "完整课程中的专题讲座",
      "difficulty": "进阶 → 高级",
      "language": "英文",
      "duration": "单讲约 80 分钟",
      "covers": "CTC 前向-后向算法逐步推导、blank 符号、路径求和、CTC beam search；seq2seq/attention 对齐",
      "align": "L67–L69（CTC 对齐 + 前向算法）",
      "why": "名校课程里对 CTC 前向算法数学推导最扎实的一档，正对 AURORA「纯 NumPy 手写 CTC 前向」的目标，可直接照着实现。",
      "urls": [
        {
          "url": "https://www.youtube.com/channel/UC8hYZGEkI2dDO8scT8C5UQA",
          "label": "频道"
        },
        {
          "url": "https://www.cs.cmu.edu/~bhiksha/courses/deeplearning/",
          "label": "cs.cmu.edu"
        },
        {
          "url": "https://www.youtube.com/watch?v=5Rj0J9AuGw0",
          "label": "视频"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "进阶",
        "高级"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "cmu 11-785 introduction to deep learning — ctc / seq2seq bhiksha raj、rita singh（卡内基梅隆 cmu） ctc 前向-后向算法逐步推导、blank 符号、路径求和、ctc beam search；seq2seq/attention 对齐 l67–l69（ctc 对齐 + 前向算法） 名校课程里对 ctc 前向算法数学推导最扎实的一档，正对 aurora「纯 numpy 手写 ctc 前向」的目标，可直接照着实现。 完整课程中的专题讲座"
    },
    {
      "title": "Whisper Paper Explained — Robust Speech Recognition via Large-Scale Weak Supervision",
      "topPick": false,
      "phase": "Phase 7 · 语音识别 ASR / STT（L66–L75）",
      "instructor": "Aladdin Persson（以「从零实现」著称）",
      "links": "频道 https://www.youtube.com/@AladdinPersson ｜搜索：\"Aladdin Persson Whisper Paper Explained\" ⚠️ 单视频精确 URL 未核实（约 33 分钟）",
      "type": "单视频（论文精读）",
      "difficulty": "进阶",
      "language": "英文",
      "duration": "约 33 分钟",
      "covers": "Whisper 架构（log-Mel + conv + encoder-decoder）、68 万小时弱监督数据、zero-shot 评测、长音频转写",
      "align": "L70–L71（Whisper 架构 + 解码）",
      "why": "「from scratch」教育风格作者，讲论文紧扣工程实现取舍，是理解 Whisper 设计动机的高性价比入口。",
      "urls": [
        {
          "url": "https://www.youtube.com/@AladdinPersson",
          "label": "频道"
        }
      ],
      "unverified": true,
      "diffLevels": [
        "进阶"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "whisper paper explained — robust speech recognition via large-scale weak supervision aladdin persson（以「从零实现」著称） whisper 架构（log-mel + conv + encoder-decoder）、68 万小时弱监督数据、zero-shot 评测、长音频转写 l70–l71（whisper 架构 + 解码） 「from scratch」教育风格作者，讲论文紧扣工程实现取舍，是理解 whisper 设计动机的高性价比入口。 单视频（论文精读）"
    },
    {
      "title": "Whisper 解码器复用：Let's build GPT（Karpathy）",
      "topPick": false,
      "phase": "Phase 7 · 语音识别 ASR / STT（L66–L75）",
      "instructor": "Andrej Karpathy",
      "links": "https://www.youtube.com/watch?v=kCc8FmEb1nY （配套代码 https://github.com/karpathy/build-nanogpt ；完整介绍见 [Phase 9](#phase-9--llm--rag--agent-l83l91)）",
      "type": "单视频",
      "difficulty": "进阶",
      "language": "英文",
      "duration": "约 1 小时 56 分",
      "covers": "从零手写 Transformer 解码器（self-attention、causal mask、自回归生成）",
      "align": "L70（Whisper 解码器部分）",
      "why": "Whisper 是 encoder-decoder Transformer，其 GPT 式解码器可直接复用本课手写实现，再叠加音频 encoder 与 cross-attention。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=kCc8FmEb1nY",
          "label": "视频"
        },
        {
          "url": "https://github.com/karpathy/build-nanogpt",
          "label": "代码"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "进阶"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "whisper 解码器复用：let's build gpt（karpathy） andrej karpathy 从零手写 transformer 解码器（self-attention、causal mask、自回归生成） l70（whisper 解码器部分） whisper 是 encoder-decoder transformer，其 gpt 式解码器可直接复用本课手写实现，再叠加音频 encoder 与 cross-attention。 单视频"
    },
    {
      "title": "wav2vec 2.0 论文精读",
      "topPick": false,
      "phase": "Phase 7 · 语音识别 ASR / STT（L66–L75）",
      "instructor": "Yannic Kilcher",
      "links": "https://www.youtube.com/watch?v=aUSXvoWfy3w （标题已核实 \"wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations\"；频道 https://www.youtube.com/c/YannicKilcher ）",
      "type": "单视频（论文逐段精读）",
      "difficulty": "高级",
      "language": "英文",
      "duration": "约 50 分钟",
      "covers": "自监督语音表征、latent masking、contrastive loss、product quantization、微调后超越半监督",
      "align": "L72（进阶：wav2vec 2.0）",
      "why": "Yannic 的招牌逐段读论文，把自监督预训练直觉讲透，是进阶章节 wav2vec 2.0 的权威精读。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=aUSXvoWfy3w",
          "label": "视频"
        },
        {
          "url": "https://www.youtube.com/c/YannicKilcher",
          "label": "频道"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "高级"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "wav2vec 2.0 论文精读 yannic kilcher 自监督语音表征、latent masking、contrastive loss、product quantization、微调后超越半监督 l72（进阶：wav2vec 2.0） yannic 的招牌逐段读论文，把自监督预训练直觉讲透，是进阶章节 wav2vec 2.0 的权威精读。 单视频（论文逐段精读）"
    },
    {
      "title": "Hugging Face Audio Course + Fine-Tune Whisper 实战",
      "topPick": false,
      "phase": "Phase 7 · 语音识别 ASR / STT（L66–L75）",
      "instructor": "Hugging Face（Sanchit Gandhi 等）",
      "links": "课程 https://huggingface.co/learn/audio-course ｜CTC 章节 https://huggingface.co/learn/audio-course/chapter3/ctc ｜Whisper 微调 https://huggingface.co/blog/fine-tune-whisper",
      "type": "完整课程 + 动手 Notebook（官方免费课程，非 YouTube）",
      "difficulty": "入门 → 进阶",
      "language": "英文（社区多语翻译）",
      "duration": "自定进度",
      "covers": "CTC 架构（Wav2Vec2/HuBERT）、Whisper encoder-decoder、在 Common Voice/LibriSpeech 上微调 whisper-small、WER 评测",
      "align": "L69、L72（Whisper-small 微调）",
      "why": "直接对齐 L72「Whisper-small 微调」；CTC 章节讲清 encoder-only+CTC 与 Whisper 端到端两条路线的差异，最贴近实操。",
      "urls": [
        {
          "url": "https://huggingface.co/learn/audio-course",
          "label": "huggingface.co"
        },
        {
          "url": "https://huggingface.co/learn/audio-course/chapter3/ctc",
          "label": "huggingface.co"
        },
        {
          "url": "https://huggingface.co/blog/fine-tune-whisper",
          "label": "huggingface.co"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "入门",
        "进阶"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "hugging face audio course + fine-tune whisper 实战 hugging face（sanchit gandhi 等） ctc 架构（wav2vec2/hubert）、whisper encoder-decoder、在 common voice/librispeech 上微调 whisper-small、wer 评测 l69、l72（whisper-small 微调） 直接对齐 l72「whisper-small 微调」；ctc 章节讲清 encoder-only+ctc 与 whisper 端到端两条路线的差异，最贴近实操。 完整课程 + 动手 notebook（官方免费课程，非 youtube）"
    },
    {
      "title": "Stanford CS224S — Spoken Language Processing",
      "topPick": false,
      "phase": "Phase 7 · 语音识别 ASR / STT（L66–L75）",
      "instructor": "Stanford（Dan Jurafsky 传统 + 近年 LLM-speech 客座）",
      "links": "课程页 https://web.stanford.edu/class/cs224s/ ｜Stanford Online https://online.stanford.edu/courses/cs224s-spoken-language-processing ｜端到端语音讲座（含 CTC）https://www.youtube.com/watch?v=3MjIkWxXigM",
      "type": "完整课程（部分公开讲座 + 讲义）",
      "difficulty": "进阶 → 高级",
      "language": "英文",
      "duration": "一学期",
      "covers": "WER 评估、HMM-GMM、CTC/attention 端到端、解码策略、口语处理全景",
      "align": "L66–L75",
      "why": "名校完整口语处理课，系统覆盖 WER→CTC→端到端，讲义可作全章脚手架（注：完整视频多在注册学生 Canvas 内，YouTube 仅部分公开讲座）。",
      "urls": [
        {
          "url": "https://web.stanford.edu/class/cs224s/",
          "label": "web.stanford.edu"
        },
        {
          "url": "https://online.stanford.edu/courses/cs224s-spoken-language-processing",
          "label": "online.stanford.edu"
        },
        {
          "url": "https://www.youtube.com/watch?v=3MjIkWxXigM",
          "label": "视频"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "进阶",
        "高级"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "stanford cs224s — spoken language processing stanford（dan jurafsky 传统 + 近年 llm-speech 客座） wer 评估、hmm-gmm、ctc/attention 端到端、解码策略、口语处理全景 l66–l75 名校完整口语处理课，系统覆盖 wer→ctc→端到端，讲义可作全章脚手架（注：完整视频多在注册学生 canvas 内，youtube 仅部分公开讲座）。 完整课程（部分公开讲座 + 讲义）"
    },
    {
      "title": "Valerio Velardo — Deep Learning for Audio / 构建 ASR 系统",
      "topPick": false,
      "phase": "Phase 7 · 语音识别 ASR / STT（L66–L75）",
      "instructor": "Valerio Velardo（The Sound of AI）",
      "links": "频道 https://www.youtube.com/channel/UCZPFjMe1uRSirmSpznqvJfQ ｜Deep Learning (For Audio) with Python 播放列表 https://www.youtube.com/playlist?list=PL-wATfeyAMNrtbkCNsLcpoAyBBRJZVlnf",
      "type": "播放列表",
      "difficulty": "入门 → 进阶",
      "language": "英文",
      "duration": "约 15–18 段",
      "covers": "音频特征（mel spectrogram/MFCC）、CNN/RNN 声学建模、从设计到部署搭建语音识别 app",
      "align": "L66、L73（音频前端 + 声学建模）",
      "why": "「直觉+数学+代码」三段式，补齐 AURORA ASR 章节所需的音频前端第一性原理。",
      "urls": [
        {
          "url": "https://www.youtube.com/channel/UCZPFjMe1uRSirmSpznqvJfQ",
          "label": "频道"
        },
        {
          "url": "https://www.youtube.com/playlist?list=PL-wATfeyAMNrtbkCNsLcpoAyBBRJZVlnf",
          "label": "播放列表"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "入门",
        "进阶"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "valerio velardo — deep learning for audio / 构建 asr 系统 valerio velardo（the sound of ai） 音频特征（mel spectrogram/mfcc）、cnn/rnn 声学建模、从设计到部署搭建语音识别 app l66、l73（音频前端 + 声学建模） 「直觉+数学+代码」三段式，补齐 aurora asr 章节所需的音频前端第一性原理。 播放列表"
    },
    {
      "title": "University of Edinburgh — Automatic Speech Recognition (ASR)",
      "topPick": false,
      "phase": "Phase 7 · 语音识别 ASR / STT（L66–L75）",
      "instructor": "Steve Renals、Hiroshi Shimodaira（爱丁堡大学 CSTR）",
      "links": "课程页 https://www.inf.ed.ac.uk/teaching/courses/asr/ ｜HMM-GMM 讲义 https://www.inf.ed.ac.uk/teaching/courses/asr/2018-19/asr03-hmmgmm-handout.pdf",
      "type": "完整课程（公开讲义/PDF；视频对注册学生开放）",
      "difficulty": "高级",
      "language": "英文",
      "duration": "18 讲",
      "covers": "HMM-GMM 声学模型、维特比解码、WFST、DNN-HMM 混合、直至端到端（CTC/attention）的演变",
      "align": "L75（进阶：传统声学模型→端到端）",
      "why": "讲传统 HMM-GMM→DNN-HMM→端到端演进最权威的公开材料，正对 AURORA「从 HMM-GMM 到端到端」进阶主题。",
      "urls": [
        {
          "url": "https://www.inf.ed.ac.uk/teaching/courses/asr/",
          "label": "inf.ed.ac.uk"
        },
        {
          "url": "https://www.inf.ed.ac.uk/teaching/courses/asr/2018-19/asr03-hmmgmm-handout.pdf",
          "label": "inf.ed.ac.uk"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "高级"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "university of edinburgh — automatic speech recognition (asr) steve renals、hiroshi shimodaira（爱丁堡大学 cstr） hmm-gmm 声学模型、维特比解码、wfst、dnn-hmm 混合、直至端到端（ctc/attention）的演变 l75（进阶：传统声学模型→端到端） 讲传统 hmm-gmm→dnn-hmm→端到端演进最权威的公开材料，正对 aurora「从 hmm-gmm 到端到端」进阶主题。 完整课程（公开讲义/pdf；视频对注册学生开放）"
    },
    {
      "title": "AssemblyAI — 语音识别 / Whisper 直觉讲解",
      "topPick": false,
      "phase": "Phase 7 · 语音识别 ASR / STT（L66–L75）",
      "instructor": "AssemblyAI（工业界语音 API 团队，教育向内容）",
      "links": "频道 https://www.youtube.com/@assemblyai ｜搜索：\"AssemblyAI Whisper how it works\"",
      "type": "频道 / 系列短视频",
      "difficulty": "入门",
      "language": "英文",
      "duration": "单集约 10–20 分钟",
      "covers": "ASR 流程直觉、Whisper 工作原理、CTC vs seq2seq、实时/流式转写概念",
      "align": "L70、L74（入门 + 流式概念）",
      "why": "轻量入门与全局直觉，适合作 L70 Whisper、L74 流式 ASR 的「预热」层，再进 CMU/李宏毅深水区。",
      "urls": [
        {
          "url": "https://www.youtube.com/@assemblyai",
          "label": "频道"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "入门"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "assemblyai — 语音识别 / whisper 直觉讲解 assemblyai（工业界语音 api 团队，教育向内容） asr 流程直觉、whisper 工作原理、ctc vs seq2seq、实时/流式转写概念 l70、l74（入门 + 流式概念） 轻量入门与全局直觉，适合作 l70 whisper、l74 流式 asr 的「预热」层，再进 cmu/李宏毅深水区。 频道 / 系列短视频"
    },
    {
      "title": "Audio Signal Processing for Machine Learning（特征地基）",
      "topPick": false,
      "phase": "Phase 8 · 音乐智能 / MIR（L76–L82）",
      "instructor": "Valerio Velardo — The Sound of AI",
      "links": "https://www.youtube.com/playlist?list=PL-wATfeyAMNqIee7cH3q1bh4QJFAaeNv0 （完整介绍见 [Phase 5](#phase-5--audio-dsp-音频信号处理l32l53)）",
      "type": "播放列表",
      "difficulty": "入门 → 进阶",
      "language": "英文",
      "duration": "约 8–10 小时",
      "align": "L76–L78（特征地基）",
      "why": "chromagram/onset 之前必备的特征提取地基；与 AURORA「NumPy 手写音频特征」理念高度一致。",
      "urls": [
        {
          "url": "https://www.youtube.com/playlist?list=PL-wATfeyAMNqIee7cH3q1bh4QJFAaeNv0",
          "label": "播放列表"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "入门",
        "进阶"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "audio signal processing for machine learning（特征地基） valerio velardo — the sound of ai l76–l78（特征地基） chromagram/onset 之前必备的特征提取地基；与 aurora「numpy 手写音频特征」理念高度一致。 播放列表"
    },
    {
      "title": "Music Processing using Chroma Features",
      "topPick": true,
      "phase": "Phase 8 · 音乐智能 / MIR（L76–L82）",
      "instructor": "Meinard Müller — AudioLabs Erlangen（FMP《Fundamentals of Music Processing》作者）",
      "links": "https://www.youtube.com/watch?v=PF05xP1NqUM （开源 FMP Notebooks https://www.audiolabs-erlangen.de/FMP ）",
      "type": "单视频（FMP 配套导览）",
      "difficulty": "入门 → 进阶",
      "language": "英文",
      "duration": "短片",
      "covers": "pitch class / 色度概念、从频谱到 chromagram 的映射、色度在和弦识别与音乐同步/对齐中的作用",
      "align": "L76–L77（chroma）",
      "why": "MIR 领域权威、FMP 教科书作者；强烈建议搭配其开源 FMP Notebooks（纯 Python/Jupyter 参考实现），正是 AURORA「第一性原理手写」的黄金对照。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=PF05xP1NqUM",
          "label": "视频"
        },
        {
          "url": "https://www.audiolabs-erlangen.de/FMP",
          "label": "audiolabs-erlangen.de"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "入门",
        "进阶"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "music processing using chroma features meinard müller — audiolabs erlangen（fmp《fundamentals of music processing》作者） pitch class / 色度概念、从频谱到 chromagram 的映射、色度在和弦识别与音乐同步/对齐中的作用 l76–l77（chroma） mir 领域权威、fmp 教科书作者；强烈建议搭配其开源 fmp notebooks（纯 python/jupyter 参考实现），正是 aurora「第一性原理手写」的黄金对照。 单视频（fmp 配套导览）"
    },
    {
      "title": "Tempo and Beat Tracking",
      "topPick": true,
      "phase": "Phase 8 · 音乐智能 / MIR（L76–L82）",
      "instructor": "Meinard Müller — AudioLabs Erlangen",
      "links": "https://www.youtube.com/watch?v=FmwpkdcAXl0 （FMP C6 章节 Notebook）",
      "type": "单视频（FMP 配套导览）",
      "difficulty": "进阶",
      "language": "英文",
      "duration": "短片",
      "covers": "onset 检测与 spectral novelty（起音包络）、脉冲/周期性分析、tempo 估计与 beat tracking 的核心思路",
      "align": "L78（onset envelope + beat tracking）",
      "why": "直接对应 L78，把「起音包络→自相关/新颖度→节拍」链路讲清，配 FMP C6 Notebook 可逐步手写复现。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=FmwpkdcAXl0",
          "label": "视频"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "进阶"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "tempo and beat tracking meinard müller — audiolabs erlangen onset 检测与 spectral novelty（起音包络）、脉冲/周期性分析、tempo 估计与 beat tracking 的核心思路 l78（onset envelope + beat tracking） 直接对应 l78，把「起音包络→自相关/新颖度→节拍」链路讲清，配 fmp c6 notebook 可逐步手写复现。 单视频（fmp 配套导览）"
    },
    {
      "title": "Learn Music Theory in Half an Hour（乐理速成）",
      "topPick": false,
      "phase": "Phase 8 · 音乐智能 / MIR（L76–L82）",
      "instructor": "Andrew Huang",
      "links": "https://www.youtube.com/watch?v=rgaTLrZGlk0",
      "type": "单视频",
      "difficulty": "入门",
      "language": "英文",
      "duration": "约 30 分钟",
      "covers": "音、八度、半音/全音、音阶与音程、和弦构成——十二平均律下的音高组织直觉",
      "align": "L76（pitch class / chroma wheel / MIDI↔Hz）",
      "why": "为 L76 补齐乐理直觉，帮助纯工程背景者理解为何 chroma 要按 12 个 pitch class 折叠。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=rgaTLrZGlk0",
          "label": "视频"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "入门"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "learn music theory in half an hour（乐理速成） andrew huang 音、八度、半音/全音、音阶与音程、和弦构成——十二平均律下的音高组织直觉 l76（pitch class / chroma wheel / midi↔hz） 为 l76 补齐乐理直觉，帮助纯工程背景者理解为何 chroma 要按 12 个 pitch class 折叠。 单视频"
    },
    {
      "title": "Generating Sound with Neural Networks（VAE 生成声音）",
      "topPick": false,
      "phase": "Phase 8 · 音乐智能 / MIR（L76–L82）",
      "instructor": "Valerio Velardo — The Sound of AI",
      "links": "https://www.youtube.com/playlist?list=PL-wATfeyAMNpEyENTc-tVH5tfLGKtSWPp",
      "type": "播放列表",
      "difficulty": "进阶",
      "language": "英文",
      "duration": "约 5–6 小时",
      "covers": "自编码器→变分自编码器（VAE）原理与手写实现，在梅尔频谱域学习潜在表示（latent embedding）并重建/生成音频",
      "align": "L79（音乐嵌入模型）",
      "why": "MusicEncoder 的本质就是把音频压进 embedding 空间；本系列逐行实现 VAE 编码器/解码器与潜空间，是理解「音乐嵌入」最贴近手写的桥梁。",
      "urls": [
        {
          "url": "https://www.youtube.com/playlist?list=PL-wATfeyAMNpEyENTc-tVH5tfLGKtSWPp",
          "label": "播放列表"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "进阶"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "generating sound with neural networks（vae 生成声音） valerio velardo — the sound of ai 自编码器→变分自编码器（vae）原理与手写实现，在梅尔频谱域学习潜在表示（latent embedding）并重建/生成音频 l79（音乐嵌入模型） musicencoder 的本质就是把音频压进 embedding 空间；本系列逐行实现 vae 编码器/解码器与潜空间，是理解「音乐嵌入」最贴近手写的桥梁。 播放列表"
    },
    {
      "title": "C4W4L04 Triplet Loss",
      "topPick": false,
      "phase": "Phase 8 · 音乐智能 / MIR（L76–L82）",
      "instructor": "Andrew Ng — DeepLearning.AI",
      "links": "https://www.youtube.com/watch?v=d2XB5-tuCWU",
      "type": "单视频",
      "difficulty": "进阶",
      "language": "英文",
      "duration": "约 15 分钟",
      "covers": "anchor/positive/negative 三元组、margin、把同类拉近异类推远的 embedding 学习目标（FaceNet 思路）",
      "align": "L79（triplet loss）",
      "why": "权威名师对 triplet loss 的经典讲解；损失函数与 AURORA MusicEncoder 的 triplet 训练完全通用，公式可直接迁移到 NumPy 手写。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=d2XB5-tuCWU",
          "label": "视频"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "进阶"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "c4w4l04 triplet loss andrew ng — deeplearning.ai anchor/positive/negative 三元组、margin、把同类拉近异类推远的 embedding 学习目标（facenet 思路） l79（triplet loss） 权威名师对 triplet loss 的经典讲解；损失函数与 aurora musicencoder 的 triplet 训练完全通用，公式可直接迁移到 numpy 手写。 单视频"
    },
    {
      "title": "SimCLR Explained（NT-Xent 对比学习）",
      "topPick": false,
      "phase": "Phase 8 · 音乐智能 / MIR（L76–L82）",
      "instructor": "Yannic Kilcher",
      "links": "https://www.youtube.com/watch?v=7Id8SPH31UE",
      "type": "单视频",
      "difficulty": "进阶",
      "language": "英文",
      "duration": "约 14–16 分钟",
      "covers": "正/负样本对、数据增强、NT-Xent（温度缩放的归一化交叉熵）损失、batch 内负样本机制",
      "align": "L79（NT-Xent 对比学习）",
      "why": "直接对应 L79 的 NT-Xent，把 SimCLR 对比目标拆到公式级，帮助理解音乐嵌入的对比学习分支如何手写。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=7Id8SPH31UE",
          "label": "视频"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "进阶"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "simclr explained（nt-xent 对比学习） yannic kilcher 正/负样本对、数据增强、nt-xent（温度缩放的归一化交叉熵）损失、batch 内负样本机制 l79（nt-xent 对比学习） 直接对应 l79 的 nt-xent，把 simclr 对比目标拆到公式级，帮助理解音乐嵌入的对比学习分支如何手写。 单视频"
    },
    {
      "title": "【機器學習 2022】語音與影像上的自督導式學習",
      "topPick": false,
      "phase": "Phase 8 · 音乐智能 / MIR（L76–L82）",
      "instructor": "李宏毅 Hung-yi Lee — 台湾大学（NTU）",
      "links": "https://www.youtube.com/watch?v=lMIN1iKYNmA",
      "type": "单视频",
      "difficulty": "进阶",
      "language": "中文（国语讲授，繁体字幕）",
      "duration": "约 35 分钟",
      "covers": "语音/音频上的自监督与对比式表示学习（CPC、wav2vec 类思路）、正负样本与预测式目标",
      "align": "L79（对比学习音频嵌入）",
      "why": "少有的高质量中文资源，把「音频如何在无标签下学表示」讲得系统清晰，为 L79 提供中文视角理论补充。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=lMIN1iKYNmA",
          "label": "视频"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "进阶"
      ],
      "langTags": [
        "中文"
      ],
      "searchable": "【機器學習 2022】語音與影像上的自督導式學習 李宏毅 hung-yi lee — 台湾大学（ntu） 语音/音频上的自监督与对比式表示学习（cpc、wav2vec 类思路）、正负样本与预测式目标 l79（对比学习音频嵌入） 少有的高质量中文资源，把「音频如何在无标签下学表示」讲得系统清晰，为 l79 提供中文视角理论补充。 单视频"
    },
    {
      "title": "Recommendation Systems using Nearest Neighbors（kNN 推荐）",
      "topPick": false,
      "phase": "Phase 8 · 音乐智能 / MIR（L76–L82）",
      "instructor": "Krish Naik",
      "links": "https://www.youtube.com/watch?v=kccT0FVK6OY",
      "type": "单视频（教程）",
      "difficulty": "入门 → 进阶",
      "language": "英文",
      "duration": "约 20 分钟",
      "covers": "基于最近邻的相似度检索、用户/物品相似度、用 kNN 做 top-k 推荐的实现流程",
      "align": "L80–L81（相似度检索 + 推荐）",
      "why": "直接对应 L80–L81「纯 kNN 相似度检索 + 推荐」，可对照 AURORA 用 NumPy 手写余弦相似度 + top-k（注：社区教程，作实操参考）。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=kccT0FVK6OY",
          "label": "视频"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "入门",
        "进阶"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "recommendation systems using nearest neighbors（knn 推荐） krish naik 基于最近邻的相似度检索、用户/物品相似度、用 knn 做 top-k 推荐的实现流程 l80–l81（相似度检索 + 推荐） 直接对应 l80–l81「纯 knn 相似度检索 + 推荐」，可对照 aurora 用 numpy 手写余弦相似度 + top-k（注：社区教程，作实操参考）。 单视频（教程）"
    },
    {
      "title": "MusicGen Paper Explained（Meta 音乐生成）",
      "topPick": false,
      "phase": "Phase 8 · 音乐智能 / MIR（L76–L82）",
      "instructor": "AI Bites",
      "links": "https://www.youtube.com/watch?v=cbAa7kart-4",
      "type": "单视频（论文精讲）",
      "difficulty": "高级",
      "language": "英文",
      "duration": "约 13 分钟",
      "covers": "EnCodec 编解码、残差向量量化（RVQ）、codebook 交织模式、文本/旋律条件生成、单一语言模型架构",
      "align": "进阶（MusicGen 音乐生成）",
      "why": "把「音频→离散 token→语言模型生成」核心机制讲清，是理解现代音乐生成范式的高性价比入口。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=cbAa7kart-4",
          "label": "视频"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "高级"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "musicgen paper explained（meta 音乐生成） ai bites encodec 编解码、残差向量量化（rvq）、codebook 交织模式、文本/旋律条件生成、单一语言模型架构 进阶（musicgen 音乐生成） 把「音频→离散 token→语言模型生成」核心机制讲清，是理解现代音乐生成范式的高性价比入口。 单视频（论文精讲）"
    },
    {
      "title": "How Shazam Works (Probably!)（音频指纹）",
      "topPick": false,
      "phase": "Phase 8 · 音乐智能 / MIR（L76–L82）",
      "instructor": "David Domminney Fowler — Computerphile",
      "links": "https://www.youtube.com/watch?v=RRsq9apr5QY",
      "type": "单视频",
      "difficulty": "进阶",
      "language": "英文",
      "duration": "约 14 分钟",
      "covers": "FFT/频谱图峰值提取、星座图（constellation map）、峰值配对哈希生成指纹、数据库匹配检索",
      "align": "进阶（音频指纹 / 精确检索）",
      "why": "把 Shazam 指纹算法讲到可复现的程度，是相似度检索之外的另一条「精确检索」思路。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=RRsq9apr5QY",
          "label": "视频"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "进阶"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "how shazam works (probably!)（音频指纹） david domminney fowler — computerphile fft/频谱图峰值提取、星座图（constellation map）、峰值配对哈希生成指纹、数据库匹配检索 进阶（音频指纹 / 精确检索） 把 shazam 指纹算法讲到可复现的程度，是相似度检索之外的另一条「精确检索」思路。 单视频"
    },
    {
      "title": "Let's build GPT: from scratch, in code, spelled out",
      "topPick": true,
      "phase": "Phase 9 · LLM / RAG / Agent（L83–L91）",
      "instructor": "Andrej Karpathy",
      "links": "单视频 https://www.youtube.com/watch?v=kCc8FmEb1nY ｜全课播放列表 https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ",
      "type": "单视频（含所属完整课程）",
      "difficulty": "进阶",
      "language": "英文",
      "duration": "约 1h56m",
      "covers": "从零逐行手写并训练一个 Transformer（bigram baseline → 自注意力 → 多头 → 位置编码 → 残差/LayerNorm/FFN），最终得到 nanoGPT 核心",
      "align": "L83–L84",
      "why": "全网最经典的「从空文件手写 GPT」，每一步矩阵运算讲透，与 AURORA「不用 wrapper、手写注意力」完全一致。必收第一顺位。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=kCc8FmEb1nY",
          "label": "视频"
        },
        {
          "url": "https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ",
          "label": "播放列表"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "进阶"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "let's build gpt: from scratch, in code, spelled out andrej karpathy 从零逐行手写并训练一个 transformer（bigram baseline → 自注意力 → 多头 → 位置编码 → 残差/layernorm/ffn），最终得到 nanogpt 核心 l83–l84 全网最经典的「从空文件手写 gpt」，每一步矩阵运算讲透，与 aurora「不用 wrapper、手写注意力」完全一致。必收第一顺位。 单视频（含所属完整课程）"
    },
    {
      "title": "Let's reproduce GPT-2 (124M)",
      "topPick": false,
      "phase": "Phase 9 · LLM / RAG / Agent（L83–L91）",
      "instructor": "Andrej Karpathy",
      "links": "https://www.youtube.com/watch?v=l8pRSuU81PU",
      "type": "单视频",
      "difficulty": "高级",
      "language": "英文",
      "duration": "约 4 小时",
      "covers": "从空文件复现 GPT-2：搭网络 → 权重加载 → 训练优化（混合精度、梯度累积、学习率调度）→ 采样/评测",
      "align": "L83–L87",
      "why": "把 L83 手写 Transformer 拉通到真实预训练与推理采样，是 L85–L86 KV/采样与 L87 推理的工业级参照。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=l8pRSuU81PU",
          "label": "视频"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "高级"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "let's reproduce gpt-2 (124m) andrej karpathy 从空文件复现 gpt-2：搭网络 → 权重加载 → 训练优化（混合精度、梯度累积、学习率调度）→ 采样/评测 l83–l87 把 l83 手写 transformer 拉通到真实预训练与推理采样，是 l85–l86 kv/采样与 l87 推理的工业级参照。 单视频"
    },
    {
      "title": "Let's build the GPT Tokenizer",
      "topPick": false,
      "phase": "Phase 9 · LLM / RAG / Agent（L83–L91）",
      "instructor": "Andrej Karpathy",
      "links": "https://www.youtube.com/watch?v=zduSFxRajkE",
      "type": "单视频",
      "difficulty": "进阶",
      "language": "英文",
      "duration": "约 2h13m",
      "covers": "从零实现 BPE（Byte Pair Encoding）分词器：Unicode/字节编码、训练、encode/decode、正则切分",
      "align": "L87（本地推理前的输入处理）",
      "why": "分词是 LLM 独立且易被忽视的一环，纯手写 BPE 完全契合「第一性原理」。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=zduSFxRajkE",
          "label": "视频"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "进阶"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "let's build the gpt tokenizer andrej karpathy 从零实现 bpe（byte pair encoding）分词器：unicode/字节编码、训练、encode/decode、正则切分 l87（本地推理前的输入处理） 分词是 llm 独立且易被忽视的一环，纯手写 bpe 完全契合「第一性原理」。 单视频"
    },
    {
      "title": "Deep Dive into LLMs like ChatGPT",
      "topPick": false,
      "phase": "Phase 9 · LLM / RAG / Agent（L83–L91）",
      "instructor": "Andrej Karpathy",
      "links": "https://www.youtube.com/watch?v=7xTGNNLPyMI",
      "type": "单视频",
      "difficulty": "入门 → 进阶",
      "language": "英文",
      "duration": "约 3h31m",
      "covers": "LLM 完整训练栈心智模型：预训练/分词/架构 → SFT → RLHF，含幻觉、工具调用、知识表示",
      "align": "L83–L91（全链路）",
      "why": "少公式、重全局，帮学员在动手手写各模块前后建立端到端认知，串起 L83–L91（含 RAG/Agent 动机）。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=7xTGNNLPyMI",
          "label": "视频"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "入门",
        "进阶"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "deep dive into llms like chatgpt andrej karpathy llm 完整训练栈心智模型：预训练/分词/架构 → sft → rlhf，含幻觉、工具调用、知识表示 l83–l91（全链路） 少公式、重全局，帮学员在动手手写各模块前后建立端到端认知，串起 l83–l91（含 rag/agent 动机）。 单视频"
    },
    {
      "title": "Neural Networks · Chapter 5–7（Transformers / Attention 可视化）",
      "topPick": false,
      "phase": "Phase 9 · LLM / RAG / Agent（L83–L91）",
      "instructor": "3Blue1Brown（Grant Sanderson）",
      "links": "播放列表 https://www.youtube.com/playlist?list=PLZZWrBYkx7Otcjr3eCLZDCgfpqnxMY29s ｜Ch5 Transformers https://www.youtube.com/watch?v=wjZofJX0v4M ｜Ch6 Attention https://www.youtube.com/watch?v=eMlx5fFNoYc",
      "type": "播放列表（单集可独立看）",
      "difficulty": "入门 → 进阶",
      "language": "英文（官方多语字幕，含中文）",
      "duration": "每集约 26–27 分钟",
      "covers": "词嵌入与 Transformer 数据流（Ch5）、注意力/QKV 逐步可视化（Ch6）、MLP/事实存储章节",
      "align": "L83",
      "why": "全网最清晰的注意力几何直觉可视化，先建直觉再手写 NumPy，L83 自注意力/多头的「看得见」版。",
      "urls": [
        {
          "url": "https://www.youtube.com/playlist?list=PLZZWrBYkx7Otcjr3eCLZDCgfpqnxMY29s",
          "label": "播放列表"
        },
        {
          "url": "https://www.youtube.com/watch?v=wjZofJX0v4M",
          "label": "视频"
        },
        {
          "url": "https://www.youtube.com/watch?v=eMlx5fFNoYc",
          "label": "视频"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "入门",
        "进阶"
      ],
      "langTags": [
        "中文",
        "英文"
      ],
      "searchable": "neural networks · chapter 5–7（transformers / attention 可视化） 3blue1brown（grant sanderson） 词嵌入与 transformer 数据流（ch5）、注意力/qkv 逐步可视化（ch6）、mlp/事实存储章节 l83 全网最清晰的注意力几何直觉可视化，先建直觉再手写 numpy，l83 自注意力/多头的「看得见」版。 播放列表（单集可独立看）"
    },
    {
      "title": "Coding a Transformer from scratch on PyTorch",
      "topPick": true,
      "phase": "Phase 9 · LLM / RAG / Agent（L83–L91）",
      "instructor": "Umar Jamil",
      "links": "https://www.youtube.com/watch?v=ISNdQcPhsts ｜频道 https://www.youtube.com/@umarjamilai",
      "type": "单视频",
      "difficulty": "进阶",
      "language": "英文",
      "duration": "约 3 小时",
      "covers": "逐层手写完整 encoder-decoder Transformer（输入嵌入、位置编码、多头自注意力、投影层）+ 翻译任务训练 + 注意力可视化",
      "align": "L83–L84",
      "why": "「从零编码」路线标杆，逐行 PyTorch 对照论文，与 AURORA 手写哲学高度契合（其整条 from-scratch 系列见频道）。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=ISNdQcPhsts",
          "label": "视频"
        },
        {
          "url": "https://www.youtube.com/@umarjamilai",
          "label": "频道"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "进阶"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "coding a transformer from scratch on pytorch umar jamil 逐层手写完整 encoder-decoder transformer（输入嵌入、位置编码、多头自注意力、投影层）+ 翻译任务训练 + 注意力可视化 l83–l84 「从零编码」路线标杆，逐行 pytorch 对照论文，与 aurora 手写哲学高度契合（其整条 from-scratch 系列见频道）。 单视频"
    },
    {
      "title": "LoRA: Low-Rank Adaptation — 讲解 + PyTorch 从零实现",
      "topPick": false,
      "phase": "Phase 9 · LLM / RAG / Agent（L83–L91）",
      "instructor": "Umar Jamil",
      "links": "https://www.youtube.com/watch?v=PXWYUTMt-AU",
      "type": "单视频",
      "difficulty": "进阶",
      "language": "英文",
      "duration": "约 26 分钟",
      "covers": "LoRA 数学原理（冻结原权重 + 低秩 B·A 增量）+ MNIST 上从零 PyTorch 实现",
      "align": "L84（LoRA 低秩适配）",
      "why": "直接命中 L84，先讲低秩分解直觉再手写，便于用 NumPy 复刻。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=PXWYUTMt-AU",
          "label": "视频"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "进阶"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "lora: low-rank adaptation — 讲解 + pytorch 从零实现 umar jamil lora 数学原理（冻结原权重 + 低秩 b·a 增量）+ mnist 上从零 pytorch 实现 l84（lora 低秩适配） 直接命中 l84，先讲低秩分解直觉再手写，便于用 numpy 复刻。 单视频"
    },
    {
      "title": "Coding LLaMA 2 from scratch（KV-Cache / RoPE / GQA / RMSNorm）",
      "topPick": false,
      "phase": "Phase 9 · LLM / RAG / Agent（L83–L91）",
      "instructor": "Umar Jamil",
      "links": "https://www.youtube.com/watch?v=oM4VmoabDAI",
      "type": "单视频",
      "difficulty": "高级",
      "language": "英文",
      "duration": "约 3 小时",
      "covers": "从零手写 LLaMA 2：KV-Cache、旋转位置编码、Grouped-Query Attention、RMSNorm、SwiGLU，并覆盖采样策略（greedy/beam/temperature/top-k/top-p）",
      "align": "L85–L86（KV-Cache + 采样策略）",
      "why": "L85 KV-Cache + L86 采样策略的最佳单一来源，逐行实现让 NumPy 版 KV-Cache 有清晰蓝本。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=oM4VmoabDAI",
          "label": "视频"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "高级"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "coding llama 2 from scratch（kv-cache / rope / gqa / rmsnorm） umar jamil 从零手写 llama 2：kv-cache、旋转位置编码、grouped-query attention、rmsnorm、swiglu，并覆盖采样策略（greedy/beam/temperature/top-k/top-p） l85–l86（kv-cache + 采样策略） l85 kv-cache + l86 采样策略的最佳单一来源，逐行实现让 numpy 版 kv-cache 有清晰蓝本。 单视频"
    },
    {
      "title": "Quantization explained with PyTorch（PTQ / QAT）",
      "topPick": false,
      "phase": "Phase 9 · LLM / RAG / Agent（L83–L91）",
      "instructor": "Umar Jamil",
      "links": "https://www.youtube.com/watch?v=0VdNflU08yA",
      "type": "单视频",
      "difficulty": "进阶 → 高级",
      "language": "英文",
      "duration": "约 1h39m",
      "covers": "整数/浮点数值表示、对称/非对称量化、量化范围与粒度、动态/静态量化、PTQ 与 QAT、GPU MAC 硬件加速",
      "align": "L87（INT8 量化从零）",
      "why": "L87 的理论+实现底座，把「缩放/零点/取整」讲到硬件层，支撑手写量化内核。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=0VdNflU08yA",
          "label": "视频"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "进阶",
        "高级"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "quantization explained with pytorch（ptq / qat） umar jamil 整数/浮点数值表示、对称/非对称量化、量化范围与粒度、动态/静态量化、ptq 与 qat、gpu mac 硬件加速 l87（int8 量化从零） l87 的理论+实现底座，把「缩放/零点/取整」讲到硬件层，支撑手写量化内核。 单视频"
    },
    {
      "title": "Retrieval Augmented Generation (RAG) Explained",
      "topPick": false,
      "phase": "Phase 9 · LLM / RAG / Agent（L83–L91）",
      "instructor": "Umar Jamil",
      "links": "https://www.youtube.com/watch?v=rhZgXNdhWDY",
      "type": "单视频",
      "difficulty": "进阶",
      "language": "英文",
      "duration": "约 35 分钟",
      "covers": "RAG 全管线：嵌入、Sentence-BERT、向量数据库与 HNSW 近邻检索、检索拼 prompt 生成",
      "align": "L88–L90",
      "why": "系统讲透 RAG 每一环（chunk→索引→检索→拼 prompt→生成）；学员可将其向量检索替换为 AURORA 的手写 TF-IDF/余弦，理解原理映射。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=rhZgXNdhWDY",
          "label": "视频"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "进阶"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "retrieval augmented generation (rag) explained umar jamil rag 全管线：嵌入、sentence-bert、向量数据库与 hnsw 近邻检索、检索拼 prompt 生成 l88–l90 系统讲透 rag 每一环（chunk→索引→检索→拼 prompt→生成）；学员可将其向量检索替换为 aurora 的手写 tf-idf/余弦，理解原理映射。 单视频"
    },
    {
      "title": "Transformers & Attention, Clearly Explained",
      "topPick": false,
      "phase": "Phase 9 · LLM / RAG / Agent（L83–L91）",
      "instructor": "StatQuest with Josh Starmer",
      "links": "Transformer https://www.youtube.com/watch?v=zxQyTK8quyY ｜Attention https://www.youtube.com/watch?v=PSs6nxngL6k",
      "type": "单视频（同频道成系列）",
      "difficulty": "入门",
      "language": "英文",
      "duration": "约 36 分 / 16 分",
      "covers": "词嵌入、位置编码、自注意力、encoder-decoder 与并行计算，及注意力机制单独精讲",
      "align": "L83",
      "why": "极慢极清晰的入门首选，为 L83 手写前打好零基础直觉，配合 Karpathy 形成「直觉→实现」梯度。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=zxQyTK8quyY",
          "label": "视频"
        },
        {
          "url": "https://www.youtube.com/watch?v=PSs6nxngL6k",
          "label": "视频"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "入门"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "transformers & attention, clearly explained statquest with josh starmer 词嵌入、位置编码、自注意力、encoder-decoder 与并行计算，及注意力机制单独精讲 l83 极慢极清晰的入门首选，为 l83 手写前打好零基础直觉，配合 karpathy 形成「直觉→实现」梯度。 单视频（同频道成系列）"
    },
    {
      "title": "注意力机制数学原理（Serrano.Academy）",
      "topPick": false,
      "phase": "Phase 9 · LLM / RAG / Agent（L83–L91）",
      "instructor": "Luis Serrano（前 Google/Apple、Udacity ML 负责人）",
      "links": "播放列表 https://www.youtube.com/@SerranoAcademy/playlists ｜数学精讲 https://www.youtube.com/watch?v=g2BRIuln4uc",
      "type": "播放列表（三部曲）",
      "difficulty": "入门 → 进阶",
      "language": "英文",
      "duration": "单集约 20–38 分钟",
      "covers": "嵌入、相似度、Keys/Queries/Values 矩阵与注意力的数学推导，三部曲递进到 Transformer",
      "align": "L83",
      "why": "用类比+图解把 QKV 的线性代数讲透，衔接 3B1B 直觉与手写实现之间的数学台阶。",
      "urls": [
        {
          "url": "https://www.youtube.com/@SerranoAcademy/playlists",
          "label": "频道"
        },
        {
          "url": "https://www.youtube.com/watch?v=g2BRIuln4uc",
          "label": "视频"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "入门",
        "进阶"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "注意力机制数学原理（serrano.academy） luis serrano（前 google/apple、udacity ml 负责人） 嵌入、相似度、keys/queries/values 矩阵与注意力的数学推导，三部曲递进到 transformer l83 用类比+图解把 qkv 的线性代数讲透，衔接 3b1b 直觉与手写实现之间的数学台阶。 播放列表（三部曲）"
    },
    {
      "title": "The Narrated Transformer Language Model",
      "topPick": false,
      "phase": "Phase 9 · LLM / RAG / Agent（L83–L91）",
      "instructor": "Jay Alammar（\"The Illustrated Transformer\" 作者，Cohere）",
      "links": "https://www.youtube.com/watch?v=sMPq4cVS4kg",
      "type": "单视频",
      "difficulty": "入门 → 进阶",
      "language": "英文",
      "duration": "约 30 分钟",
      "covers": "Transformer 语言模型组件的可视化叙述：分词、嵌入、自注意力、前馈网络、输出投影",
      "align": "L83",
      "why": "Illustrated Transformer 的视频版讲演，图解直观，是 L83 架构总览的经典补充。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=sMPq4cVS4kg",
          "label": "视频"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "入门",
        "进阶"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "the narrated transformer language model jay alammar（\"the illustrated transformer\" 作者，cohere） transformer 语言模型组件的可视化叙述：分词、嵌入、自注意力、前馈网络、输出投影 l83 illustrated transformer 的视频版讲演，图解直观，是 l83 架构总览的经典补充。 单视频"
    },
    {
      "title": "Attention Is All You Need（论文精读）",
      "topPick": false,
      "phase": "Phase 9 · LLM / RAG / Agent（L83–L91）",
      "instructor": "Yannic Kilcher",
      "links": "https://www.youtube.com/watch?v=iDulhoQ2pro",
      "type": "单视频",
      "difficulty": "高级",
      "language": "英文",
      "duration": "约 27 分钟",
      "covers": "逐节精读 Vaswani et al. 2017 原论文：纯注意力架构、位置编码、多头注意力、去 RNN/CNN 的动机与实验",
      "align": "L83",
      "why": "回到第一性来源——原始论文，帮学员用原文校准手写实现的每个设计决策。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=iDulhoQ2pro",
          "label": "视频"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "高级"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "attention is all you need（论文精读） yannic kilcher 逐节精读 vaswani et al. 2017 原论文：纯注意力架构、位置编码、多头注意力、去 rnn/cnn 的动机与实验 l83 回到第一性来源——原始论文，帮学员用原文校准手写实现的每个设计决策。 单视频"
    },
    {
      "title": "【機器學習2021】自注意力機制 Self-attention & Transformer（中文）",
      "topPick": false,
      "phase": "Phase 9 · LLM / RAG / Agent（L83–L91）",
      "instructor": "李宏毅 Hung-yi Lee（台大 NTU）",
      "links": "Self-attention(上) https://www.youtube.com/watch?v=hYdO9CscNes ｜(下) https://www.youtube.com/watch?v=gmsMY5kc-zw ｜Transformer(上) https://www.youtube.com/watch?v=n9TlOhRjYoc",
      "type": "单视频（属 ML2021 完整课程）",
      "difficulty": "入门 → 进阶",
      "language": "中文（国语讲解，含中文字幕）",
      "duration": "每集约 28–60 分钟",
      "covers": "自注意力动机与 QKV 计算、多头、位置编码，Transformer 的 seq2seq/encoder-decoder 与训练",
      "align": "L83–L84",
      "why": "华语区公认最佳中文 Transformer 讲解，为中文学员提供母语原理入口。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=hYdO9CscNes",
          "label": "视频"
        },
        {
          "url": "https://www.youtube.com/watch?v=gmsMY5kc-zw",
          "label": "视频"
        },
        {
          "url": "https://www.youtube.com/watch?v=n9TlOhRjYoc",
          "label": "视频"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "入门",
        "进阶"
      ],
      "langTags": [
        "中文"
      ],
      "searchable": "【機器學習2021】自注意力機制 self-attention & transformer（中文） 李宏毅 hung-yi lee（台大 ntu） 自注意力动机与 qkv 计算、多头、位置编码，transformer 的 seq2seq/encoder-decoder 与训练 l83–l84 华语区公认最佳中文 transformer 讲解，为中文学员提供母语原理入口。 单视频（属 ml2021 完整课程）"
    },
    {
      "title": "Full Stack Deep Learning — 2022 完整课程",
      "topPick": true,
      "phase": "Phase 10 · 系统集成 / MLOps / 面试（L92–L99）",
      "instructor": "Josh Tobin、Sergey Karayev、Charles Frye（UC Berkeley 背景，FSDL）",
      "links": "https://www.youtube.com/playlist?list=PL1T8fO7ArWleMMI8KPJ_5D5XSlovTW_Ur （主页 https://fullstackdeeplearning.com/course/2022/ ）",
      "type": "完整课程（12 讲 + Labs）",
      "difficulty": "进阶",
      "language": "英文",
      "duration": "15–20 小时",
      "covers": "DL 产品全栈——训练基础设施与工具、数据管理/版本化、模型部署为 Web 服务、监控、ML 团队与项目管理、「从 demo 到产品」",
      "align": "L92–L94（整门课即 Aurora v1 capstone 方法论蓝本）",
      "why": "全网公认「从模型到产品」的权威课程，直接对应 L94「Aurora v1 demo + 证据链」与云部署 live demo。必收第一条。",
      "urls": [
        {
          "url": "https://www.youtube.com/playlist?list=PL1T8fO7ArWleMMI8KPJ_5D5XSlovTW_Ur",
          "label": "播放列表"
        },
        {
          "url": "https://fullstackdeeplearning.com/course/2022/",
          "label": "fullstackdeeplearning.com"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "进阶"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "full stack deep learning — 2022 完整课程 josh tobin、sergey karayev、charles frye（uc berkeley 背景，fsdl） dl 产品全栈——训练基础设施与工具、数据管理/版本化、模型部署为 web 服务、监控、ml 团队与项目管理、「从 demo 到产品」 l92–l94（整门课即 aurora v1 capstone 方法论蓝本） 全网公认「从模型到产品」的权威课程，直接对应 l94「aurora v1 demo + 证据链」与云部署 live demo。必收第一条。 完整课程（12 讲 + labs）"
    },
    {
      "title": "Made With ML — MLOps Course",
      "topPick": false,
      "phase": "Phase 10 · 系统集成 / MLOps / 面试（L92–L99）",
      "instructor": "Goku Mohandas（Made With ML / Anyscale）",
      "links": "https://madewithml.com/courses/mlops/ （代码 https://github.com/GokuMohandas/mlops-course ｜视频 https://www.youtube.com/playlist?list=PLqy_sIcckLC2jrxQhyqWDhL_9Uwxz8UFq ）",
      "type": "完整课程（网站 + GitHub + YouTube）",
      "difficulty": "进阶",
      "language": "英文",
      "duration": "自定进度",
      "covers": "生产级 ML 设计→数据→模型（训练/追踪/调优/评估/serving）→测试（代码/数据/模型）→复现与版本化→CI/CD→监控",
      "align": "L93–L94",
      "why": "GitHub 顶流 MLOps 开源课，把「第一性原理手写系统」落到工程规范（测试、CI/CD、监控），补足 FSDL 之外的可复制代码骨架。",
      "urls": [
        {
          "url": "https://madewithml.com/courses/mlops/",
          "label": "madewithml.com"
        },
        {
          "url": "https://github.com/GokuMohandas/mlops-course",
          "label": "代码"
        },
        {
          "url": "https://www.youtube.com/playlist?list=PLqy_sIcckLC2jrxQhyqWDhL_9Uwxz8UFq",
          "label": "播放列表"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "进阶"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "made with ml — mlops course goku mohandas（made with ml / anyscale） 生产级 ml 设计→数据→模型（训练/追踪/调优/评估/serving）→测试（代码/数据/模型）→复现与版本化→ci/cd→监控 l93–l94 github 顶流 mlops 开源课，把「第一性原理手写系统」落到工程规范（测试、ci/cd、监控），补足 fsdl 之外的可复制代码骨架。 完整课程（网站 + github + youtube）"
    },
    {
      "title": "Weights & Biases — 官方频道与课程",
      "topPick": false,
      "phase": "Phase 10 · 系统集成 / MLOps / 面试（L92–L99）",
      "instructor": "Weights & Biases 官方",
      "links": "频道 https://www.youtube.com/channel/UCBp3w4DCEC64FZr4k9ROxig ｜官方课程 https://wandb.ai/site/courses/",
      "type": "频道 + 完整课程",
      "difficulty": "入门 → 进阶",
      "language": "英文",
      "duration": "单集 5–30 分钟",
      "covers": "实验跟踪、指标/模型日志、数据集版本化、超参 sweeps、模型评估与协作复现",
      "align": "L93（MLOps 实验跟踪）",
      "why": "L93 明确点名 W&B；官方一手教程，把 Aurora 训练实验的可追溯/可复现做扎实，直接支撑 L94 证据链。",
      "urls": [
        {
          "url": "https://www.youtube.com/channel/UCBp3w4DCEC64FZr4k9ROxig",
          "label": "频道"
        },
        {
          "url": "https://wandb.ai/site/courses/",
          "label": "wandb.ai"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "入门",
        "进阶"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "weights & biases — 官方频道与课程 weights & biases 官方 实验跟踪、指标/模型日志、数据集版本化、超参 sweeps、模型评估与协作复现 l93（mlops 实验跟踪） l93 明确点名 w&b；官方一手教程，把 aurora 训练实验的可追溯/可复现做扎实，直接支撑 l94 证据链。 频道 + 完整课程"
    },
    {
      "title": "Build a Fully Local AI Voice Assistant (STT + LLM + TTS)",
      "topPick": false,
      "phase": "Phase 10 · 系统集成 / MLOps / 面试（L92–L99）",
      "instructor": "独立教程（⚠️ 频道名未核实，标题与内容已核实）",
      "links": "https://www.youtube.com/watch?v=2IffgzB8USw （备用检索：\"fully local AI voice assistant Whisper TTS\"）",
      "type": "单视频",
      "difficulty": "入门 → 进阶",
      "language": "英文",
      "duration": "约 30–60 分钟",
      "covers": "纯本地、无云 API 的语音助手——Whisper STT + 本地 LLM + TTS，Python orchestrator 串起 mic→ASR→LLM→TTS 循环，含延迟讨论",
      "align": "aurora.realtime（mic→ASR→LLM→TTS 实时管线）、L92",
      "why": "与 L92/aurora.realtime 目标同构的最小可跑实现，天然「不用 wrapper」路线；可作为 <500ms 目标的起点基线去逐层砍延迟。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=2IffgzB8USw",
          "label": "视频"
        }
      ],
      "unverified": true,
      "diffLevels": [
        "入门",
        "进阶"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "build a fully local ai voice assistant (stt + llm + tts) 独立教程（⚠️ 频道名未核实，标题与内容已核实） 纯本地、无云 api 的语音助手——whisper stt + 本地 llm + tts，python orchestrator 串起 mic→asr→llm→tts 循环，含延迟讨论 aurora.realtime（mic→asr→llm→tts 实时管线）、l92 与 l92/aurora.realtime 目标同构的最小可跑实现，天然「不用 wrapper」路线；可作为 <500ms 目标的起点基线去逐层砍延迟。 单视频"
    },
    {
      "title": "freeCodeCamp — Docker Tutorial for Beginners",
      "topPick": false,
      "phase": "Phase 10 · 系统集成 / MLOps / 面试（L92–L99）",
      "instructor": "freeCodeCamp.org",
      "links": "https://www.youtube.com/watch?v=fqMOX6JJhGo",
      "type": "单视频（完整课程）",
      "difficulty": "入门",
      "language": "英文",
      "duration": "约 2 小时",
      "covers": "容器 vs 虚机、Dockerfile 与镜像构建、Docker Hub、网络与存储卷、Docker Compose 多容器编排",
      "align": "L93（Docker 容器化）",
      "why": "为 Aurora 把 realtime/serving 组件打包成可复现镜像、进而上云 GPU 铺路。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=fqMOX6JJhGo",
          "label": "视频"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "入门"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "freecodecamp — docker tutorial for beginners freecodecamp.org 容器 vs 虚机、dockerfile 与镜像构建、docker hub、网络与存储卷、docker compose 多容器编排 l93（docker 容器化） 为 aurora 把 realtime/serving 组件打包成可复现镜像、进而上云 gpu 铺路。 单视频（完整课程）"
    },
    {
      "title": "MLOps Tutorial #1 — CI/CD for ML Pipelines with GitHub Actions",
      "topPick": false,
      "phase": "Phase 10 · 系统集成 / MLOps / 面试（L92–L99）",
      "instructor": "DVCorg / Iterative（DVC 团队）",
      "links": "https://www.youtube.com/watch?v=9I8X-3HIErc",
      "type": "单视频（系列第一集）",
      "difficulty": "进阶",
      "language": "英文",
      "duration": "约 20–40 分钟",
      "covers": "用 GitHub Actions 为 ML 管线做持续集成——PR 触发测试、自动跑训练/评估、把 metrics 回贴 PR，合并后触发部署",
      "align": "L93（CI/CD）",
      "why": "聚焦 ML 的 CI/CD 实战（非泛 DevOps），把 Made With ML 的概念落到 GitHub Actions 具体 workflow。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=9I8X-3HIErc",
          "label": "视频"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "进阶"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "mlops tutorial #1 — ci/cd for ml pipelines with github actions dvcorg / iterative（dvc 团队） 用 github actions 为 ml 管线做持续集成——pr 触发测试、自动跑训练/评估、把 metrics 回贴 pr，合并后触发部署 l93（ci/cd） 聚焦 ml 的 ci/cd 实战（非泛 devops），把 made with ml 的概念落到 github actions 具体 workflow。 单视频（系列第一集）"
    },
    {
      "title": "A Practical Tutorial on Building ML Demos with Gradio",
      "topPick": false,
      "phase": "Phase 10 · 系统集成 / MLOps / 面试（L92–L99）",
      "instructor": "Abubakar Abid（Gradio 创始人 / Hugging Face）",
      "links": "https://www.youtube.com/watch?v=97KxA1r184o",
      "type": "单视频",
      "difficulty": "入门",
      "language": "英文",
      "duration": "约 1 小时",
      "covers": "用纯 Python 快速搭交互式 demo 与 Web 界面，音频/文本输入组件、分享链接、托管到 Spaces",
      "align": "L94（live demo）",
      "why": "一手创始人讲解，是 L94「Aurora v1 live demo URL」最省力路径；原生支持麦克风/音频，可直接包住 aurora.realtime 管线。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=97KxA1r184o",
          "label": "视频"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "入门"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "a practical tutorial on building ml demos with gradio abubakar abid（gradio 创始人 / hugging face） 用纯 python 快速搭交互式 demo 与 web 界面，音频/文本输入组件、分享链接、托管到 spaces l94（live demo） 一手创始人讲解，是 l94「aurora v1 live demo url」最省力路径；原生支持麦克风/音频，可直接包住 aurora.realtime 管线。 单视频"
    },
    {
      "title": "How to Deploy ML Models with FastAPI, Docker & Fly.io",
      "topPick": false,
      "phase": "Phase 10 · 系统集成 / MLOps / 面试（L92–L99）",
      "instructor": "独立教程",
      "links": "https://www.youtube.com/watch?v=jzGzw98Eikk",
      "type": "单视频（端到端）",
      "difficulty": "进阶",
      "language": "英文",
      "duration": "约 30–50 分钟",
      "covers": "把模型封装为 FastAPI 推理服务、容器化、部署到 Fly.io 拿到公网 URL 的完整链路",
      "align": "L93–L94、aurora.realtime 服务化",
      "why": "直接产出 L94 需要的「云上 live demo URL」；FastAPI + Docker 是 realtime 后端 serving 的主流栈。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=jzGzw98Eikk",
          "label": "视频"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "进阶"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "how to deploy ml models with fastapi, docker & fly.io 独立教程 把模型封装为 fastapi 推理服务、容器化、部署到 fly.io 拿到公网 url 的完整链路 l93–l94、aurora.realtime 服务化 直接产出 l94 需要的「云上 live demo url」；fastapi + docker 是 realtime 后端 serving 的主流栈。 单视频（端到端）"
    },
    {
      "title": "Enable Model Quantization for ONNX and TensorRT",
      "topPick": false,
      "phase": "Phase 10 · 系统集成 / MLOps / 面试（L92–L99）",
      "instructor": "Nicolai Nielsen",
      "links": "https://www.youtube.com/watch?v=phmFvMOHt4I ⚠️（标题经搜索核实，未逐帧核对）",
      "type": "单视频",
      "difficulty": "高级",
      "language": "英文",
      "duration": "约 15–30 分钟",
      "covers": "训练模型→导出 ONNX→TensorRT 引擎构建与 INT8/FP8 量化标定，GPU 低延迟高吞吐推理",
      "align": "L94（部署优化）、aurora.realtime（<500ms 延迟预算）",
      "why": "aurora.realtime 要压到 <500ms，量化 + ONNX/TensorRT 是把 ASR/TTS 模型提速的关键工程手段。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=phmFvMOHt4I",
          "label": "视频"
        }
      ],
      "unverified": true,
      "diffLevels": [
        "高级"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "enable model quantization for onnx and tensorrt nicolai nielsen 训练模型→导出 onnx→tensorrt 引擎构建与 int8/fp8 量化标定，gpu 低延迟高吞吐推理 l94（部署优化）、aurora.realtime（<500ms 延迟预算） aurora.realtime 要压到 <500ms，量化 + onnx/tensorrt 是把 asr/tts 模型提速的关键工程手段。 单视频"
    },
    {
      "title": "Machine Learning System Design Interview — Hello Interview",
      "topPick": false,
      "phase": "Phase 10 · 系统集成 / MLOps / 面试（L92–L99）",
      "instructor": "Hello Interview（FAANG 资深工程师/招聘经理）",
      "links": "频道 https://www.youtube.com/@hello_interview ｜指南 https://www.hellointerview.com/learn/ml-system-design",
      "type": "频道 + 配套课程",
      "difficulty": "进阶 → 高级",
      "language": "英文",
      "duration": "单集 20–60 分钟",
      "covers": "ML 系统设计框架、推荐/检索/排序经典题、真人 mock 与反馈、把业务问题翻译成 ML 方案",
      "align": "L95–L99（ML/系统设计面试）",
      "why": "L96–L98 面试准备核心；「框架化 + mock + 反馈」正对研究工程师岗的 ML System Design 环节，可拿 Aurora 项目做 design 素材。",
      "urls": [
        {
          "url": "https://www.youtube.com/@hello_interview",
          "label": "频道"
        },
        {
          "url": "https://www.hellointerview.com/learn/ml-system-design",
          "label": "hellointerview.com"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "进阶",
        "高级"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "machine learning system design interview — hello interview hello interview（faang 资深工程师/招聘经理） ml 系统设计框架、推荐/检索/排序经典题、真人 mock 与反馈、把业务问题翻译成 ml 方案 l95–l99（ml/系统设计面试） l96–l98 面试准备核心；「框架化 + mock + 反馈」正对研究工程师岗的 ml system design 环节，可拿 aurora 项目做 design 素材。 频道 + 配套课程"
    },
    {
      "title": "NeetCode — 编程/白板面试频道 + Roadmap",
      "topPick": false,
      "phase": "Phase 10 · 系统集成 / MLOps / 面试（L92–L99）",
      "instructor": "Navdeep Singh（前 Google/Amazon 工程师）",
      "links": "频道 https://www.youtube.com/c/neetcode ｜路线图 https://neetcode.io/roadmap",
      "type": "频道 + 结构化 roadmap",
      "difficulty": "入门 → 高级",
      "language": "英文",
      "duration": "410+ 视频",
      "covers": "NeetCode 150 / Blind 75 按模式（双指针、滑窗、树、图、DP…）递进，每题干净的思路 + 编码讲解",
      "align": "L95–L99（白板/coding 面试）",
      "why": "算法/白板面试事实标准，直接支撑 L96–L98 的 coding 环节与刷题复盘。",
      "urls": [
        {
          "url": "https://www.youtube.com/c/neetcode",
          "label": "频道"
        },
        {
          "url": "https://neetcode.io/roadmap",
          "label": "neetcode.io"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "入门",
        "高级"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "neetcode — 编程/白板面试频道 + roadmap navdeep singh（前 google/amazon 工程师） neetcode 150 / blind 75 按模式（双指针、滑窗、树、图、dp…）递进，每题干净的思路 + 编码讲解 l95–l99（白板/coding 面试） 算法/白板面试事实标准，直接支撑 l96–l98 的 coding 环节与刷题复盘。 频道 + 结构化 roadmap"
    },
    {
      "title": "跟李沐学AI — 论文精读系列（研究技能）",
      "topPick": false,
      "phase": "Phase 10 · 系统集成 / MLOps / 面试（L92–L99）",
      "instructor": "李沐（Amazon 资深首席科学家，d2l 作者）",
      "links": "汇总仓库 https://github.com/mli/paper-reading ｜\"如何读论文\" https://www.bilibili.com/video/BV1H44y1t75x/ （B 站主页「跟李沐学AI」，YouTube 有同名镜像）",
      "type": "播放列表/系列",
      "difficulty": "进阶 → 高级",
      "language": "中文",
      "duration": "数十集",
      "covers": "逐段精读 Transformer/BERT/ViT/ResNet/GAN/InstructGPT 等，并示范「如何读论文」方法论",
      "align": "L95–L99（研究技能、复盘）",
      "why": "L95「研究技能」中文首选；示范研究工程师如何拆解论文、提炼贡献与证据链，与 AURORA「第一性原理复现」气质一致。",
      "urls": [
        {
          "url": "https://github.com/mli/paper-reading",
          "label": "代码"
        },
        {
          "url": "https://www.bilibili.com/video/BV1H44y1t75x/",
          "label": "B站"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "进阶",
        "高级"
      ],
      "langTags": [
        "中文"
      ],
      "searchable": "跟李沐学ai — 论文精读系列（研究技能） 李沐（amazon 资深首席科学家，d2l 作者） 逐段精读 transformer/bert/vit/resnet/gan/instructgpt 等，并示范「如何读论文」方法论 l95–l99（研究技能、复盘） l95「研究技能」中文首选；示范研究工程师如何拆解论文、提炼贡献与证据链，与 aurora「第一性原理复现」气质一致。 播放列表/系列"
    },
    {
      "title": "李宏毅 DLHLP 2020 — 語音合成 (1/2)：Tacotron",
      "topPick": true,
      "phase": "aurora.tts · 语音合成 TTS（延期模块，专项补充）",
      "instructor": "李宏毅 Hung-yi Lee / 台大 (NTU)",
      "links": "https://www.youtube.com/watch?v=DMxKeHW8KdM",
      "type": "单视频（属 DLHLP 2020）",
      "difficulty": "入门 → 进阶",
      "language": "中文（繁体投影片，中英术语）",
      "duration": "约 50 分钟",
      "covers": "TTS 总体流水线、深度学习前的做法、端到端思路，Tacotron 的 seq2seq + attention 架构、CBHG、吐出 mel/线性谱、Griffin-Lim",
      "align": "aurora.tts（声学模型）",
      "why": "华语圈最权威的语音深度学习课，从第一性原理讲清「文本→谱」为什么这么设计，是理解声学模型的最佳起点。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=DMxKeHW8KdM",
          "label": "视频"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "入门",
        "进阶"
      ],
      "langTags": [
        "中文",
        "英文"
      ],
      "searchable": "李宏毅 dlhlp 2020 — 語音合成 (1/2)：tacotron 李宏毅 hung-yi lee / 台大 (ntu) tts 总体流水线、深度学习前的做法、端到端思路，tacotron 的 seq2seq + attention 架构、cbhg、吐出 mel/线性谱、griffin-lim aurora.tts（声学模型） 华语圈最权威的语音深度学习课，从第一性原理讲清「文本→谱」为什么这么设计，是理解声学模型的最佳起点。 单视频（属 dlhlp 2020）"
    },
    {
      "title": "李宏毅 DLHLP 2020 — 語音合成 (2/2)：More than Tacotron",
      "topPick": false,
      "phase": "aurora.tts · 语音合成 TTS（延期模块，专项补充）",
      "instructor": "李宏毅 Hung-yi Lee / 台大 (NTU)",
      "links": "https://www.youtube.com/watch?v=Eau1Fr2x86Y",
      "type": "单视频（续集）",
      "difficulty": "进阶",
      "language": "中文",
      "duration": "约 50 分钟",
      "covers": "Tacotron 痛点与改良、Tacotron2 + WaveNet 声码器、非自回归 FastSpeech、可控合成（speaker/prosody）、对齐与 attention 失败模式",
      "align": "aurora.tts（声学模型 + 声码器衔接）",
      "why": "承接上集，把「为什么要非自回归、为什么要独立声码器」讲透，对应路线图里 FastSpeech/HiFi-GAN 方向的动机。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=Eau1Fr2x86Y",
          "label": "视频"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "进阶"
      ],
      "langTags": [
        "中文"
      ],
      "searchable": "李宏毅 dlhlp 2020 — 語音合成 (2/2)：more than tacotron 李宏毅 hung-yi lee / 台大 (ntu) tacotron 痛点与改良、tacotron2 + wavenet 声码器、非自回归 fastspeech、可控合成（speaker/prosody）、对齐与 attention 失败模式 aurora.tts（声学模型 + 声码器衔接） 承接上集，把「为什么要非自回归、为什么要独立声码器」讲透，对应路线图里 fastspeech/hifi-gan 方向的动机。 单视频（续集）"
    },
    {
      "title": "Text-to-Speech & Voice Cloning Course（完整课程）",
      "topPick": true,
      "phase": "aurora.tts · 语音合成 TTS（延期模块，专项补充）",
      "instructor": "Valerio Velardo — The Sound of AI",
      "links": "课程首集 https://www.youtube.com/watch?v=_MFrEYPdEn8 ｜频道全部视频 https://www.youtube.com/c/ValerioVelardoTheSoundofAI/videos",
      "type": "完整课程（分集连载，持续更新）",
      "difficulty": "入门 → 进阶",
      "language": "英文",
      "duration": "单集约 30–45 分钟",
      "covers": "concatenative→neural 演进、双阶段流水线（声学模型 + 声码器）、mel 谱作桥梁、WaveNet/WaveGlow/HiFi-GAN 声码器、FastSpeech/Glow-TTS 并行架构、VALL-E/AudioLM/SPEAR-TTS 等 codec 生成、声音克隆",
      "align": "aurora.tts（全流水线）",
      "why": "目前 YouTube 上体系最完整的英文 TTS 课，讲解偏「理解内部机制」而非调 API，可作 aurora.tts 主线英文教材。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=_MFrEYPdEn8",
          "label": "视频"
        },
        {
          "url": "https://www.youtube.com/c/ValerioVelardoTheSoundofAI/videos",
          "label": "频道"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "入门",
        "进阶"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "text-to-speech & voice cloning course（完整课程） valerio velardo — the sound of ai concatenative→neural 演进、双阶段流水线（声学模型 + 声码器）、mel 谱作桥梁、wavenet/waveglow/hifi-gan 声码器、fastspeech/glow-tts 并行架构、vall-e/audiolm/spear-tts 等 codec 生成、声音克隆 aurora.tts（全流水线） 目前 youtube 上体系最完整的英文 tts 课，讲解偏「理解内部机制」而非调 api，可作 aurora.tts 主线英文教材。 完整课程（分集连载，持续更新）"
    },
    {
      "title": "The Neural TTS Revolution（单集精华总览）",
      "topPick": false,
      "phase": "aurora.tts · 语音合成 TTS（延期模块，专项补充）",
      "instructor": "Valerio Velardo — The Sound of AI",
      "links": "https://www.youtube.com/watch?v=4Lbox-d0UcE",
      "type": "单视频",
      "difficulty": "入门 → 进阶",
      "language": "英文",
      "duration": "约 41 分钟",
      "covers": "2016 WaveNet/Tacotron 起点、双阶段流水线、mel 谱桥梁、各类声码器、并行架构、codec 生成",
      "align": "aurora.tts（概念地图）",
      "why": "一集把整个神经 TTS 版图串成时间线，适合作 aurora.tts 的「导航图」，看完再深入各论文不会迷路。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=4Lbox-d0UcE",
          "label": "视频"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "入门",
        "进阶"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "the neural tts revolution（单集精华总览） valerio velardo — the sound of ai 2016 wavenet/tacotron 起点、双阶段流水线、mel 谱桥梁、各类声码器、并行架构、codec 生成 aurora.tts（概念地图） 一集把整个神经 tts 版图串成时间线，适合作 aurora.tts 的「导航图」，看完再深入各论文不会迷路。 单视频"
    },
    {
      "title": "End-to-End Adversarial Text-to-Speech (EATS) — Paper Explained",
      "topPick": false,
      "phase": "aurora.tts · 语音合成 TTS（延期模块，专项补充）",
      "instructor": "Yannic Kilcher",
      "links": "https://www.youtube.com/watch?v=WTB2p4bqtXU",
      "type": "单视频（论文精读）",
      "difficulty": "高级",
      "language": "英文",
      "duration": "约 41 分钟",
      "covers": "多阶段 TTS 流水线的问题、对抗训练、端到端训练、判别器/生成器结构、对齐问题与 aligner、谱预测损失、DTW",
      "align": "aurora.tts（端到端/对抗）",
      "why": "把「对齐为何是 TTS 核心难点」讲到公式层面，是理解 VITS 等端到端对抗模型的前置精读。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=WTB2p4bqtXU",
          "label": "视频"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "高级"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "end-to-end adversarial text-to-speech (eats) — paper explained yannic kilcher 多阶段 tts 流水线的问题、对抗训练、端到端训练、判别器/生成器结构、对齐问题与 aligner、谱预测损失、dtw aurora.tts（端到端/对抗） 把「对齐为何是 tts 核心难点」讲到公式层面，是理解 vits 等端到端对抗模型的前置精读。 单视频（论文精读）"
    },
    {
      "title": "In-depth Review of VALL-E — Zero-Shot TTS",
      "topPick": false,
      "phase": "aurora.tts · 语音合成 TTS（延期模块，专项补充）",
      "instructor": "⚠️ 出品频道未核实（视频标题与内容已核实指向 VALL-E 论文精读）",
      "links": "https://www.youtube.com/watch?v=fCtbnhR83UI ｜若失效搜：\"VALL-E paper explained neural codec language model zero-shot TTS\"",
      "type": "单视频（论文精读）",
      "difficulty": "高级",
      "language": "英文",
      "duration": "约 20–40 分钟",
      "covers": "把 TTS 当条件语言建模、EnCodec 离散音频码替代 mel 谱、自回归 + 非自回归两级解码、3 秒提示做 zero-shot 声音克隆",
      "align": "aurora.tts（zero-shot 声音克隆）",
      "why": "对齐「VALL-E 思路 / zero-shot voice cloning」，讲清 codec-LM 范式与传统 mel 谱路线的分野；建议与论文 arXiv 2301.02111 对照。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=fCtbnhR83UI",
          "label": "视频"
        }
      ],
      "unverified": true,
      "diffLevels": [
        "高级"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "in-depth review of vall-e — zero-shot tts ⚠️ 出品频道未核实（视频标题与内容已核实指向 vall-e 论文精读） 把 tts 当条件语言建模、encodec 离散音频码替代 mel 谱、自回归 + 非自回归两级解码、3 秒提示做 zero-shot 声音克隆 aurora.tts（zero-shot 声音克隆） 对齐「vall-e 思路 / zero-shot voice cloning」，讲清 codec-lm 范式与传统 mel 谱路线的分野；建议与论文 arxiv 2301.02111 对照。 单视频（论文精读）"
    },
    {
      "title": "Text Processing for Speech Synthesis（TTS 前端 · G2P/正规化）",
      "topPick": false,
      "phase": "aurora.tts · 语音合成 TTS（延期模块，专项补充）",
      "instructor": "Prof. Simon King / University of Edinburgh (CSTR)，SPCC 2016",
      "links": "https://www.youtube.com/watch?v=6lMs1VcUrYc ｜同系列 HMM 合成 https://www.youtube.com/watch?v=3Ffd75PVjjc",
      "type": "单视频（讲座系列）",
      "difficulty": "进阶",
      "language": "英文",
      "duration": "约 1 小时",
      "covers": "文本正规化、字素→音素 (G2P)、词典与发音、韵律/停顿标注，TTS 前端如何把文本变成模型输入",
      "align": "aurora.tts（前端 text→phoneme/G2P）",
      "why": "神经 TTS 视频普遍跳过前端，而 aurora.tts 流水线第一环正是「文本→音素/G2P」；Edinburgh 语音合成组是该领域最权威学派。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=6lMs1VcUrYc",
          "label": "视频"
        },
        {
          "url": "https://www.youtube.com/watch?v=3Ffd75PVjjc",
          "label": "视频"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "进阶"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "text processing for speech synthesis（tts 前端 · g2p/正规化） prof. simon king / university of edinburgh (cstr)，spcc 2016 文本正规化、字素→音素 (g2p)、词典与发音、韵律/停顿标注，tts 前端如何把文本变成模型输入 aurora.tts（前端 text→phoneme/g2p） 神经 tts 视频普遍跳过前端，而 aurora.tts 流水线第一环正是「文本→音素/g2p」；edinburgh 语音合成组是该领域最权威学派。 单视频（讲座系列）"
    },
    {
      "title": "Audio Signal Processing for ML（DSP 衔接）",
      "topPick": false,
      "phase": "aurora.tts · 语音合成 TTS（延期模块，专项补充）",
      "instructor": "Valerio Velardo — The Sound of AI",
      "links": "https://www.youtube.com/playlist?list=PL-wATfeyAMNqIee7cH3q1bh4QJFAaeNv0 （完整介绍见 [Phase 5](#phase-5--audio-dsp-音频信号处理l32l53)）",
      "type": "播放列表",
      "difficulty": "入门 → 进阶",
      "language": "英文",
      "covers": "从零推导 STFT→mel 谱，正是声学模型输出与声码器输入的公共表示",
      "align": "aurora.tts ↔ aurora.audio 衔接",
      "why": "直接对接「TTS 与 AURORA 已实现的 DSP（Mel 谱/STFT）如何衔接」，是连接两模块的桥梁课。",
      "urls": [
        {
          "url": "https://www.youtube.com/playlist?list=PL-wATfeyAMNqIee7cH3q1bh4QJFAaeNv0",
          "label": "播放列表"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "入门",
        "进阶"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "audio signal processing for ml（dsp 衔接） valerio velardo — the sound of ai 从零推导 stft→mel 谱，正是声学模型输出与声码器输入的公共表示 aurora.tts ↔ aurora.audio 衔接 直接对接「tts 与 aurora 已实现的 dsp（mel 谱/stft）如何衔接」，是连接两模块的桥梁课。 播放列表"
    },
    {
      "title": "WaveNet by Google DeepMind | Two Minute Papers #93",
      "topPick": false,
      "phase": "aurora.tts · 语音合成 TTS（延期模块，专项补充）",
      "instructor": "Károly Zsolnai-Fehér — Two Minute Papers",
      "links": "https://www.youtube.com/watch?v=CqFIVCD1WWo",
      "type": "单视频（概览）",
      "difficulty": "入门",
      "language": "英文",
      "duration": "约 4 分钟",
      "covers": "WaveNet 直接建模原始波形、自回归生成、听感飞跃（概念层）",
      "align": "aurora.tts（声码器概览）",
      "why": "神经声码器起点 WaveNet 的「为什么重要」引子，开课前快速建直觉；深入机制回到李宏毅第 2 集与 Valerio 课程。",
      "urls": [
        {
          "url": "https://www.youtube.com/watch?v=CqFIVCD1WWo",
          "label": "视频"
        }
      ],
      "unverified": false,
      "diffLevels": [
        "入门"
      ],
      "langTags": [
        "英文"
      ],
      "searchable": "wavenet by google deepmind | two minute papers #93 károly zsolnai-fehér — two minute papers wavenet 直接建模原始波形、自回归生成、听感飞跃（概念层） aurora.tts（声码器概览） 神经声码器起点 wavenet 的「为什么重要」引子，开课前快速建直觉；深入机制回到李宏毅第 2 集与 valerio 课程。 单视频（概览）"
    }
  ]
};
