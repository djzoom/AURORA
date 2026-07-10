// 8-bit 音效引擎 —— 纯 Web Audio 振荡器手写合成，无音频文件、无库。
// 呼应课程的「no API wrappers」精神：连音效都是方波 + 包络亲手算出来的，
// 而不是加载一段 mp3。本层不持有游戏状态：静音开关由调用方传入。

let audioCtx = null;

function getAudioCtx() {
  if (audioCtx) return audioCtx;
  const AC = window.AudioContext || window.webkitAudioContext;
  if (!AC) return null;
  try {
    audioCtx = new AC();
  } catch {
    audioCtx = null;
  }
  return audioCtx;
}

// 一个带指数衰减包络的方波音符，start/dur 单位为秒。
function blip(freq, start, dur, { type = "square", gain = 0.14 } = {}) {
  const ctx = getAudioCtx();
  if (!ctx) return;
  const t0 = ctx.currentTime + start;
  const osc = ctx.createOscillator();
  const env = ctx.createGain();
  osc.type = type;
  osc.frequency.setValueAtTime(freq, t0);
  env.gain.setValueAtTime(0.0001, t0);
  env.gain.linearRampToValueAtTime(gain, t0 + 0.012);
  env.gain.exponentialRampToValueAtTime(0.0001, t0 + dur);
  osc.connect(env).connect(ctx.destination);
  osc.start(t0);
  osc.stop(t0 + dur + 0.02);
}

const SFX = {
  hit: () => {
    blip(660, 0, 0.09);
    blip(988, 0.07, 0.13);
  },
  miss: () => {
    blip(220, 0, 0.16, { type: "sawtooth", gain: 0.12 });
    blip(150, 0.13, 0.2, { type: "sawtooth", gain: 0.1 });
  },
  clear: () => {
    [523, 659, 784, 1047].forEach((f, i) => blip(f, i * 0.09, 0.17));
  },
  finale: () => {
    [523, 659, 784, 1047, 880, 1047, 1319, 1568].forEach((f, i) =>
      blip(f, i * 0.11, 0.22),
    );
  },
};

export function playSfx(name, muted) {
  if (muted) return;
  if (!SFX[name]) return;
  const ctx = getAudioCtx();
  if (ctx && ctx.state === "suspended") ctx.resume().catch(() => {});
  SFX[name]();
}
