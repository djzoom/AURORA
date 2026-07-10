// 8-bit Boss 像素精灵 —— 16×16 字符矩阵手绘，Canvas 逐像素渲染，无图片文件。
// 每个字符映射调色板一格：'.' 为透明。改造型只需改字符画。

const PALETTE = {
  K: "#10182e", // 深色主体
  W: "#edf7ff", // 白
  C: "#66e8ff", // 青
  D: "#2a7fa8", // 暗青
  A: "#ffc85e", // 琥珀
  M: "#ff6f91", // 品红
  G: "#8ff3a5", // 绿
  P: "#b48cff", // 紫
};

export const SPRITES = {
  // 黑盒守门人：一只咧嘴的密封黑箱
  blackbox: [
    "................",
    "...WWWWWWWWWW...",
    "..WKKKKKKKKKKW..",
    "..WKKKKKKKKKKW..",
    "..WKAAKKKKAAKW..",
    "..WKAAKKKKAAKW..",
    "..WKKKKKKKKKKW..",
    "..WKMKKKKKKMKW..",
    "..WKKMMMMMMKKW..",
    "..WKKKKKKKKKKW..",
    "..WKKKKKKKKKKW..",
    "...WWWWWWWWWW...",
    "....C......C....",
    "...CC......CC...",
    "................",
    "................",
  ],
  // 频谱守门人：体内长着频谱条纹的波形幽灵
  spectrum: [
    "................",
    ".....CCCCCC.....",
    "....CCCCCCCC....",
    "...CCCCCCCCCC...",
    "...CWWCCCCWWC...",
    "...CWKCCCCWKC...",
    "...CCCCCCCCCC...",
    "...CCCCCCCCCC...",
    "...CDCDCDCDCD...",
    "...CDCDCDCDCD...",
    "...CCCCCCCCCC...",
    "...CCCCCCCCCC...",
    "...CC.CC.CC.CC..",
    "................",
    "................",
    "................",
  ],
  // 反向传播骑士：琥珀目缝的头盔骑士，胸口链式徽记
  knight: [
    "................",
    "......MM........",
    ".....MMMM.......",
    "....WWWWWW......",
    "...WWWWWWWW.....",
    "...WWWWWWWW.....",
    "...WKAAAAKW.....",
    "...WWWWWWWW.....",
    "...WWWWWWWW.....",
    "....WDDDDW......",
    "....DDDDDD......",
    "...DDDDDDDD.....",
    "...DD.WW.DD.....",
    "...DD.WW.DD.....",
    "................",
    "................",
  ],
  // 对齐裁判：黑白条纹衫
  judge: [
    "................",
    ".....WWWWWW.....",
    "....WWWWWWWW....",
    "....WKWWWWKW....",
    "....WWWWWWWW....",
    "....WWKKKKWW....",
    ".....WWWWWW.....",
    "....KWKWKWKW....",
    "...KWKWKWKWKW...",
    "...WKWKWKWKWK...",
    "...KWKWKWKWKW...",
    "...WKWKWKWKWK...",
    "....KK....KK....",
    "................",
    "................",
    "................",
  ],
  // 旋律机灵鬼：一枚长了脸的八分音符
  melody: [
    "................",
    ".........AAA....",
    ".........AAAA...",
    ".........A..A...",
    ".........A......",
    ".........A......",
    ".........A......",
    ".........A......",
    "......AAAA......",
    ".....AAAAAA.....",
    "....AAAAAAAA....",
    "....AKAAAAKA....",
    "....AAAAAAAA....",
    "....AAMMMMAA....",
    ".....AAAAAA.....",
    "......AAAA......",
  ],
  // 检索图书馆长：戴眼镜的绿皮厚书
  librarian: [
    "................",
    "..GGGGGGGGGGGG..",
    "..GGGGGGGGGGGG..",
    "..GGKKKKKKKKGG..",
    "..GGKWKGGKWKGG..",
    "..GGKKKGGKKKGG..",
    "..GGGGGGGGGGGG..",
    "..GGGGMMMMGGGG..",
    "..GGGGGGGGGGGG..",
    "..GGGGGGGGGGGG..",
    "..GWWWWWWWWWWG..",
    "..GWWWWWWWWWWG..",
    "..GGGGGGGGGGGG..",
    "................",
    "................",
    "................",
  ],
  // 终局总工：头顶星标、戴安全帽的紫色机器人
  architect: [
    "................",
    ".......WW.......",
    "......WWWW......",
    ".......WW.......",
    "....AAAAAAAA....",
    "...AAAAAAAAAA...",
    "...PPPPPPPPPP...",
    "...PCCPPPPCCP...",
    "...PCCPPPPCCP...",
    "...PPPPPPPPPP...",
    "...PGGGGGGGGP...",
    "...PPPPPPPPPP...",
    "....P..PP..P....",
    "................",
    "................",
    "................",
  ],
};

// quest.id → 精灵键；题库数据保持纯净，映射集中在这里。
export const SPRITE_BY_QUEST = {
  prologue: "blackbox",
  "phase-1": "spectrum",
  "phase-2": "knight",
  "phase-3": "judge",
  "phase-4": "melody",
  "phase-5": "librarian",
  "phase-6": "architect",
};

export function drawSprite(canvas, key) {
  if (!canvas?.getContext) return;
  const ctx = canvas.getContext("2d");
  if (!ctx) return;
  const rows = SPRITES[key] ?? SPRITES.blackbox;
  canvas.width = 16;
  canvas.height = 16;
  ctx.clearRect(0, 0, 16, 16);
  rows.forEach((row, y) => {
    for (let x = 0; x < row.length; x += 1) {
      const color = PALETTE[row[x]];
      if (!color) continue;
      ctx.fillStyle = color;
      ctx.fillRect(x, y, 1, 1);
    }
  });
}
