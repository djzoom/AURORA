export const courseSnapshot = {
  "title": "Aurora 学习计划（6 个月 · 全职 · 零基础起步）",
  "subtitle": "一条从开场五课走向 FFT、Whisper、RAG 和终局整合的实战路线。",
  "openingLessons": [
    {
      "code": "L01",
      "path": "0_foundation/L01_motivation",
      "title": "Aurora 动机、11 模块路线图、月通关标志、check_imports、environment_report"
    },
    {
      "code": "L02",
      "path": "0_foundation/L02_sound_digital",
      "title": "声音数字表示、samples_count/make_time_axis/make_sine/signal_summary，先手算再验证"
    },
    {
      "code": "L03",
      "path": "0_foundation/L03_spectrogram",
      "title": "谱图直觉（纯音/和弦/扫频/噪声），不推公式，为 FFT 种下视觉印象"
    },
    {
      "code": "L04",
      "path": "1_complex_trig/L04_trig",
      "title": "正弦三要素 A·sin(2πft+φ)，实现 sinusoid，和弦叠加 demo"
    },
    {
      "code": "L05",
      "path": "1_complex_trig/L05_complex_numbers",
      "title": "复数模与相位，实现 magnitude_phase，FFT 输出复数预览"
    }
  ],
  "foundationTracks": [
    {
      "path": "1_complex_trig/",
      "range": "L06–L08",
      "title": "欧拉公式、傅里叶直觉、可视化",
      "service": "DSP / FFT"
    },
    {
      "path": "2_linear_algebra/",
      "range": "L09–L21",
      "title": "向量、点积、矩阵、SVD",
      "service": "几乎所有模块"
    },
    {
      "path": "3_calculus/",
      "range": "L22–L26",
      "title": "导数、梯度、链式、梯度下降",
      "service": "深度学习训练"
    },
    {
      "path": "4_probability/",
      "range": "L27–L31",
      "title": "随机、分布、softmax、交叉熵",
      "service": "ML 损失与生成"
    }
  ],
  "monthlyPhases": [
    {
      "month": 1,
      "title": "数学 + DSP 地基",
      "deliverable": "Audio Analysis Engine",
      "checkpoint": "能从空白文件重写 FFT/STFT/mel/MFCC"
    },
    {
      "month": 2,
      "title": "ML / 深度学习地基",
      "deliverable": "从零 autograd + 语音命令分类器",
      "checkpoint": "能手推反向传播；用自己的 mel 特征训出模型"
    },
    {
      "month": 3,
      "title": "Speech Core (ASR)",
      "deliverable": "微调 Whisper-small + WER 评估",
      "checkpoint": "能转录真实音频并讲清 CTC/注意力"
    },
    {
      "month": 4,
      "title": "Music Core（你的优势区）",
      "deliverable": "音乐 embedding + 相似推荐",
      "checkpoint": "歌→向量→推荐跑通"
    },
    {
      "month": 5,
      "title": "LLM + RAG + Agent",
      "deliverable": "Podcast 智能引擎",
      "checkpoint": "本地推理 + LoRA + RAG 跑通"
    },
    {
      "month": 6,
      "title": "整合 + 1 个 Demo + MLOps",
      "deliverable": "Aurora v1 + 面试材料",
      "checkpoint": "一个打磨好的端到端 demo"
    }
  ],
  "weeklyCheckpoints": [
    {
      "file": "docs/current/course/week-01-checklist.md",
      "heading": "L32–L36 逐日打卡 — 信号、复数、numpy 流畅度",
      "range": "L32–L36",
      "title": "信号、复数、numpy 流畅度",
      "target": "建立\"数字信号\"的直觉，掌握复数与欧拉公式，把 numpy 用顺，能完整读懂 `src/aurora/audio/io.py` 和 `windows.py` 的每一行。每天结束前 `git commit`。打勾方式：把 `[ ]` 改成 `[x]`。",
      "lessons": [
        {
          "range": "L32",
          "title": "numpy 流畅度"
        },
        {
          "range": "L33",
          "title": "正弦波与采样"
        },
        {
          "range": "L34",
          "title": "Nyquist 与混叠（aliasing）"
        },
        {
          "range": "L35",
          "title": "复数与欧拉公式（FFT 的命根子）"
        },
        {
          "range": "L36",
          "title": "读懂 io.py / windows.py，整周收口"
        }
      ]
    },
    {
      "file": "docs/current/course/week-02-checklist.md",
      "heading": "L37–L42 逐日打卡 — 傅里叶变换（FFT）",
      "range": "L37–L42",
      "title": "傅里叶变换（FFT）",
      "target": "从数学定义出发彻底理解 DFT，手写蝶形迭代 FFT（Cooley-Tukey 位反转）并通过 numpy.fft 验证，能完整读懂 `src/aurora/audio/transforms.py` 的每一行，并用 FFT 做真实信号的频谱分析。每天结束前 `git commit`。打勾方式：把 `[ ]` 改成 `[x]`。",
      "lessons": [
        {
          "range": "L37",
          "title": "DFT 定义"
        },
        {
          "range": "L38",
          "title": "蝶形运算与分治"
        },
        {
          "range": "L39",
          "title": "从零手写递归 FFT"
        },
        {
          "range": "L40",
          "title": "频谱分析实战"
        },
        {
          "range": "L41",
          "title": "加窗 + 完整流程整合"
        },
        {
          "range": "L42",
          "title": "视觉化 FFT"
        }
      ]
    },
    {
      "file": "docs/current/course/week-03-checklist.md",
      "heading": "L53–L58 逐日打卡 — 计算图与 MLP",
      "range": "L53–L58",
      "title": "计算图与 MLP",
      "target": "",
      "lessons": [
        {
          "range": "L53",
          "title": "MFCC 图形化（若未结业）"
        },
        {
          "range": "L54",
          "title": "Value 计算图"
        },
        {
          "range": "L55",
          "title": "Value 算子补全"
        }
      ]
    },
    {
      "file": "docs/current/course/week-04-checklist.md",
      "heading": "L67–L71 逐日打卡 — CTC 与 Whisper 入门",
      "range": "L67–L71",
      "title": "CTC 与 Whisper 入门",
      "target": "",
      "lessons": [
        {
          "range": "L67",
          "title": "Edit Distance"
        },
        {
          "range": "L68",
          "title": "CTC 对齐"
        },
        {
          "range": "L69",
          "title": "CTC 前向算法"
        },
        {
          "range": "L70",
          "title": "Whisper 架构"
        }
      ]
    }
  ],
  "sourceFiles": [
    "docs/current/course/LEARNING_PLAN.md",
    "docs/current/course/GETTING_STARTED.md",
    "docs/current/course/week-01-checklist.md",
    "docs/current/course/week-02-checklist.md",
    "docs/current/course/week-03-checklist.md",
    "docs/current/course/week-04-checklist.md"
  ]
};

export default courseSnapshot;
