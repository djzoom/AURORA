// 像素世界地图数据 —— 课程结构(11 阶段 · L01–L99)到 RPG 地理的比喻映射。
// 纯数据:改地图布局/文案只动这里;渲染在 ../ui.js,样式在 ../../styles.css。
//
// 比喻映射(依据 LEARNING_PLAN.md §2 的依赖链):
//   数学(复数/线代) ─┐
//                     ├─→ DSP(频谱之海)──→ 音频特征 ─┐
//   微积分·概率 ──────┴─→ ML/DL(反传熔炉)───────────┴─→ ASR / Music / LLM 三王国 ─→ 终局城堡
// 地图上:并列 = 可并行学的同层地基;上下相连 = 依赖;三岔 = 熔炉之后的三个应用王国;
// 汇聚 = 一切在「极光城堡」(Aurora v1)合流。deps 在区块上渲染成「◀ 承接」注记。
//
// range = [起, 止] 课号(闭区间);questIndex 指向 data/quests.js 的章节,
// 区块的解锁/通关状态跟随所属章节;gate 表示该区块自带章节城门。

export const MAP_ZONES = {
  camp: {
    questIndex: 0,
    gate: 0,
    icon: "🏕️",
    terrain: "出发营地",
    name: "基础前导",
    range: [1, 3],
    deps: [],
    flavor: "装好行囊:环境、声音的数字化、谱图直觉。",
  },
  trig: {
    questIndex: 1,
    icon: "🌀",
    terrain: "旋转风车岭",
    name: "复数与三角",
    range: [4, 8],
    deps: ["camp"],
    flavor: "欧拉公式:一切旋转的起点。",
  },
  linalg: {
    questIndex: 1,
    icon: "⛏️",
    terrain: "矩阵矿脉",
    name: "线性代数",
    range: [9, 21],
    deps: ["camp"],
    flavor: "矩阵即变换——DFT/Mel 都是从这里挖出的矿。",
  },
  calc: {
    questIndex: 1,
    icon: "⛰️",
    terrain: "梯度坡道",
    name: "微积分",
    range: [22, 26],
    deps: ["camp"],
    flavor: "顺着最陡的坡往下走,就是训练。",
  },
  prob: {
    questIndex: 1,
    icon: "🎲",
    terrain: "骰子荒原",
    name: "概率统计",
    range: [27, 31],
    deps: ["camp"],
    flavor: "softmax 与交叉熵在荒原尽头等你。",
  },
  dsp: {
    questIndex: 1,
    icon: "🌊",
    terrain: "频谱之海",
    name: "Audio DSP",
    range: [32, 53],
    deps: ["trig", "linalg"],
    flavor: "四条山溪在此汇流:手写 FFT → STFT → Mel → MFCC。",
  },
  dl: {
    questIndex: 2,
    gate: 2,
    icon: "🌋",
    terrain: "反传熔炉",
    name: "深度学习",
    range: [54, 65],
    deps: ["calc", "prob", "dsp"],
    flavor: "用梯度锻造模型:micrograd → PyTorch → 音频 CNN。",
  },
  asr: {
    questIndex: 3,
    gate: 3,
    icon: "🗣️",
    terrain: "听风峡谷",
    name: "语音识别 ASR",
    range: [66, 75],
    deps: ["dsp", "dl"],
    flavor: "把风声译成文字:CTC、Whisper、beam search。",
  },
  music: {
    questIndex: 4,
    gate: 4,
    icon: "🎵",
    terrain: "节拍绿洲",
    name: "音乐智能",
    range: [76, 82],
    deps: ["dsp", "dl"],
    flavor: "chroma、beat、嵌入与推荐,在绿洲里成歌。",
  },
  llm: {
    questIndex: 5,
    gate: 5,
    icon: "🗼",
    terrain: "注意力高塔",
    name: "LLM · RAG",
    range: [83, 91],
    deps: ["dl", "prob"],
    flavor: "塔的每一层都是注意力:Transformer → KV-Cache → RAG。",
  },
  ops: {
    questIndex: 6,
    gate: 6,
    icon: "🏰",
    terrain: "极光城堡",
    name: "整合 · MLOps",
    range: [92, 99],
    deps: ["asr", "music", "llm"],
    flavor: "三条大道在此合流:mic → ASR → LLM,Aurora v1 点亮极光。",
  },
};

// 地图版面:自上而下逐行渲染。
//   { zones: [...] }          一行地形区(多个 = 并列/可并行)
//   { gate: questIndex }      一行整宽章节城门
//   { flow: "字符" }          一行流线(纯装饰,体现依赖走向)
export const MAP_LAYOUT = [
  { zones: ["camp"] },
  { flow: "│" },
  { gate: 1 },
  { zones: ["trig", "linalg"] },
  { zones: ["calc", "prob"] },
  { flow: "╲  ╱" },
  { zones: ["dsp"] },
  { flow: "│" },
  { zones: ["dl"] },
  { flow: "╱  │  ╲" },
  { zones: ["asr", "music", "llm"] },
  { flow: "╲  │  ╱" },
  { zones: ["ops"] },
];
