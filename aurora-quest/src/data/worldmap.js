// 像素世界地图数据 —— 11 个课程阶段（L01–L99）作为地形区块，按 Quest 章节分组。
// 纯数据：改地图布局/文案只动这里；渲染在 ../ui.js，样式在 ../../styles.css。
//
// range = [起, 止] 课号（闭区间）；questIndex 指向 data/quests.js 的章节
// （0=序章 … 6=第6章），区块的解锁/通关状态跟随所属章节。

export const MAP_ZONES = [
  { questIndex: 0, icon: "🏁", name: "基础前导", range: [1, 3] },
  { questIndex: 1, icon: "📐", name: "复数与三角", range: [4, 8] },
  { questIndex: 1, icon: "🔢", name: "线性代数", range: [9, 21] },
  { questIndex: 1, icon: "∂", name: "微积分", range: [22, 26] },
  { questIndex: 1, icon: "🎲", name: "概率统计", range: [27, 31] },
  { questIndex: 1, icon: "🔊", name: "Audio DSP", range: [32, 53] },
  { questIndex: 2, icon: "🧠", name: "深度学习", range: [54, 65] },
  { questIndex: 3, icon: "🎙️", name: "语音识别 ASR", range: [66, 75] },
  { questIndex: 4, icon: "🎵", name: "音乐智能", range: [76, 82] },
  { questIndex: 5, icon: "🤖", name: "LLM · RAG · Agent", range: [83, 91] },
  { questIndex: 6, icon: "🚀", name: "整合 · MLOps", range: [92, 99] },
];
