// 增长与分享 —— 两个伴生页面（Aurora Quest / 视频资料库）共用的 Star 按钮、分享面板与
// 「点个 Star」提示。
//
// 硬规则（见 docs/current/course 与仓库 README）：
//   · 不设任何门槛：课程免费、无需注册，Star 永远是可选的，从不把它当作任何内容的前置条件。
//   · 不登录 GitHub、不埋点、不引第三方脚本。唯一外部请求是公开的 GitHub REST
//     端点 https://api.github.com/repos/djzoom/AURORA，只读 stargazers_count，
//     localStorage 缓存 1 小时；离线 / 限流时静默退回成不带数字的静态按钮。
//   · 只提供「分享到平台」，不提供「关注作者」。
//
// 文案都集中在下面的 GROWTH 数据块里，作者直接改字就行。

export const GROWTH = {
  repo: "djzoom/AURORA",
  repoUrl: "https://github.com/djzoom/AURORA",
  apiUrl: "https://api.github.com/repos/djzoom/AURORA",
  site: "https://djzoom.github.io/AURORA/",
  pages: {
    quest: {
      url: "https://djzoom.github.io/AURORA/",
      title: "Aurora Quest | AURORA 辅助课程 RPG",
      image: "https://djzoom.github.io/AURORA/og/quest.png",
      qr: "./og/qr-quest.png",
      // 微博 share intent 的一句话（微博带链接，文案可短）
      weibo: "Aurora Quest：把 99 课免费开源的音频 AI 课程打成一场 8-bit 冒险，答题打 Boss，算法全部 NumPy 手写。",
      // 复制推荐语：面向小红书 / 微信 / B 站评论区——这些平台不带外链，所以用文字报仓库名。
      // {url} 会被替换成当前页面地址。随机抽一条，避免大家发出来一模一样。
      copy: [
        "发现一门免费的音频 AI 课：99 课从一条正弦波手写到 Whisper，FFT、梅尔滤波器、注意力、CTC 全部用 NumPy 亲手实现，MIT 开源，不用注册。还配了个 8-bit 小游戏，答题打败 7 个黑盒 Boss 就算通关。\nGitHub 搜 djzoom/AURORA\n在线玩：{url}",
        "把 99 课音频 AI 课程打成一场 8-bit 冒险：答题打 Boss，掉落的不是分数，是“我知道它为什么 work”的底气。课程中文讲解、全部免费、MIT 开源，每一课都能跑通。\nGitHub 搜 djzoom/AURORA\n{url}",
        "想从零搞懂语音识别？这门 99 课的开源课把 FFT 到 Whisper 全部亲手写一遍，每课都过两遍执行验证，免费、MIT、不用注册。配套 Aurora Quest 小游戏，边答题边复习。\nGitHub 搜 djzoom/AURORA\n{url}",
      ],
    },
    videos: {
      url: "https://djzoom.github.io/AURORA/video-library.html",
      title: "视频资料库 | AURORA Video Library",
      image: "https://djzoom.github.io/AURORA/og/videos.png",
      qr: "./og/qr-videos.png",
      weibo: "AURORA 视频资料库：92 条音频 AI 名师课（Karpathy · 3Blue1Brown · 李宏毅 · MIT…）逐条对齐一门 99 课的免费开源课程，可筛选、可打卡。",
      copy: [
        "整理了 92 条音频 AI 名师课（Karpathy、3Blue1Brown、李宏毅、MIT…），逐条对齐一门 99 课的免费开源课程 L01–L99，可按课号、难度、语言筛选，看完打卡记进度。\nGitHub 搜 djzoom/AURORA\n{url}",
        "学音频 AI 卡住了？按课号找视频：92 条 YouTube 教程按正弦波 → FFT → 梅尔 → Transformer → Whisper 排好，先看直觉课，再看手写实现课，再回 notebook 自己写。配套课程 99 课全部免费、MIT 开源。\nGitHub 搜 djzoom/AURORA\n{url}",
        "从正弦波刷到 Whisper 的 92 条视频清单，自带打卡、连续天数和奖章，进度只存在本机浏览器里。课程本体 99 课、NumPy 手写、免费开源、不用注册。\nGitHub 搜 djzoom/AURORA\n{url}",
      ],
    },
  },
  // 视频资料库里「点个 Star」提示：刷到 5 条和 20 条时各提示一次，关掉就不再出现。
  toast: {
    thresholds: [5, 20],
    text: "觉得有用？在 GitHub 上点个 Star，能让更多人找到这门课。",
    dismiss: "不用了",
  },
  starLabel: "Star on GitHub",
  starAria: "在 GitHub 上给 djzoom/AURORA 点 Star（新窗口打开）",
};

const STAR_CACHE_KEY = "aurora-quest.stars.v1";
const STAR_CACHE_TTL = 60 * 60 * 1000; // 1 小时
const TOAST_KEY = "aurora-quest.star-toast.v1";

// ---- 工具 -------------------------------------------------------------------

function readJson(key) {
  try {
    const raw = window.localStorage.getItem(key);
    return raw ? JSON.parse(raw) : null;
  } catch {
    return null;
  }
}

function writeJson(key, value) {
  try {
    window.localStorage.setItem(key, JSON.stringify(value));
  } catch {
    /* 隐私模式 / 配额用尽：缓存失败不影响功能 */
  }
}

export function formatStars(n) {
  if (!Number.isFinite(n) || n < 0) return "";
  if (n < 1000) return String(n);
  const k = n / 1000;
  return `${k >= 10 ? Math.round(k) : Math.round(k * 10) / 10}k`;
}

// 当前页面地址（去掉 hash / 查询串，分享出去的链接干净一些）。
function pageUrl(page) {
  try {
    const u = new URL(window.location.href);
    if (u.protocol === "http:" || u.protocol === "https:") {
      u.hash = "";
      u.search = "";
      return u.toString();
    }
  } catch {
    /* fall through */
  }
  return GROWTH.pages[page].url;
}

export function pickCopy(page, url, rng = Math.random) {
  const list = GROWTH.pages[page].copy;
  const text = list[Math.floor(rng() * list.length)] ?? list[0];
  return text.replaceAll("{url}", url);
}

async function copyText(text) {
  try {
    await navigator.clipboard.writeText(text);
    return true;
  } catch {
    // 旧浏览器 / 非安全上下文：退回隐藏 textarea + execCommand
    try {
      const ta = document.createElement("textarea");
      ta.value = text;
      ta.setAttribute("readonly", "");
      ta.style.position = "fixed";
      ta.style.opacity = "0";
      document.body.appendChild(ta);
      ta.select();
      const ok = document.execCommand("copy");
      ta.remove();
      return ok;
    } catch {
      return false;
    }
  }
}

function flash(button, text, ms = 2000) {
  if (!button) return;
  const original = button.textContent;
  button.textContent = text;
  button.disabled = true;
  window.setTimeout(() => {
    button.textContent = original;
    button.disabled = false;
  }, ms);
}

// ---- B. Star 按钮（带实时计数）------------------------------------------------

let starCountPromise = null;

// 读取 star 数：先查 1 小时缓存，再请求公开 API；任何失败都返回 null。
export function fetchStarCount({ force = false } = {}) {
  if (starCountPromise && !force) return starCountPromise;
  starCountPromise = (async () => {
    const cached = readJson(STAR_CACHE_KEY);
    if (
      !force &&
      cached &&
      Number.isFinite(cached.count) &&
      Number.isFinite(cached.at) &&
      Date.now() - cached.at < STAR_CACHE_TTL
    ) {
      return cached.count;
    }
    try {
      const res = await fetch(GROWTH.apiUrl, {
        headers: { Accept: "application/vnd.github+json" },
      });
      if (!res.ok) return cached?.count ?? null;
      const data = await res.json();
      const count = Number(data?.stargazers_count);
      if (!Number.isFinite(count)) return cached?.count ?? null;
      writeJson(STAR_CACHE_KEY, { count, at: Date.now() });
      return count;
    } catch {
      return cached?.count ?? null;
    }
  })();
  return starCountPromise;
}

export function createStarButton({ className = "pixel-btn" } = {}) {
  const a = document.createElement("a");
  a.className = `${className} star-btn`;
  a.href = GROWTH.repoUrl;
  a.target = "_blank";
  a.rel = "noopener";
  a.setAttribute("aria-label", GROWTH.starAria);
  const star = document.createElement("span");
  star.className = "star-icon";
  star.setAttribute("aria-hidden", "true");
  star.textContent = "⭐";
  const label = document.createElement("span");
  label.className = "star-label";
  label.textContent = GROWTH.starLabel;
  const count = document.createElement("span");
  count.className = "star-count";
  count.hidden = true;
  a.append(star, label, count);
  return a;
}

function applyStarCount(count) {
  if (!Number.isFinite(count)) return;
  const label = formatStars(count);
  for (const el of document.querySelectorAll(".star-btn")) {
    const c = el.querySelector(".star-count");
    if (!c) continue;
    c.textContent = `· ${label}`;
    c.hidden = false;
    el.setAttribute("aria-label", `${GROWTH.starAria}，目前 ${count} 个 Star`);
  }
}

// 把 Star 按钮挂到所有 [data-star-slot] 容器里，然后异步补上计数。
export function mountStarButtons(root = document) {
  for (const slot of root.querySelectorAll("[data-star-slot]")) {
    if (slot.querySelector(".star-btn")) continue;
    slot.appendChild(createStarButton({ className: slot.dataset.starSlot || "pixel-btn" }));
  }
  fetchStarCount().then(applyStarCount);
}

// ---- C. 分享面板 ---------------------------------------------------------------

let panel = null;
let lastTrigger = null;

function buildPanel(page) {
  const cfg = GROWTH.pages[page];
  const url = pageUrl(page);

  const backdrop = document.createElement("div");
  backdrop.className = "share-backdrop";
  backdrop.hidden = true;

  const box = document.createElement("div");
  box.className = "share-panel pixel-panel";
  box.setAttribute("role", "dialog");
  box.setAttribute("aria-modal", "true");
  box.setAttribute("aria-labelledby", "share-panel-title");

  box.innerHTML = `
    <div class="share-head">
      <h2 class="share-title" id="share-panel-title">分享本页</h2>
      <button class="share-close" type="button" aria-label="关闭分享面板">✕</button>
    </div>
    <p class="share-note">小红书 / 微信 / B 站不带外链——推荐语里直接写了“GitHub 搜 djzoom/AURORA”，配二维码更好认。</p>
    <textarea class="share-text" rows="5" readonly aria-label="推荐语" spellcheck="false"></textarea>
    <div class="share-actions">
      <button class="pixel-btn primary" type="button" data-share="copy-text">复制推荐语</button>
      <button class="pixel-btn ghost" type="button" data-share="shuffle">换一条</button>
      <button class="pixel-btn" type="button" data-share="copy-link">复制链接</button>
      <a class="pixel-btn" data-share="weibo" target="_blank" rel="noopener">分享到微博</a>
      <button class="pixel-btn" type="button" data-share="qr" aria-expanded="false" aria-controls="share-qr">显示二维码</button>
      <button class="pixel-btn" type="button" data-share="native" hidden>系统分享…</button>
    </div>
    <figure class="share-qr" id="share-qr" hidden>
      <img alt="本页链接的二维码" width="200" height="200" loading="lazy" />
      <figcaption>微信扫一扫打开本页 · 或长按保存图片</figcaption>
    </figure>
    <div class="share-foot" data-star-slot="pixel-btn"></div>
  `;

  const textarea = box.querySelector(".share-text");
  const setCopy = () => {
    textarea.value = pickCopy(page, url);
  };
  setCopy();

  const weibo = box.querySelector('[data-share="weibo"]');
  const weiboParams = new URLSearchParams({ url, title: cfg.weibo, pic: cfg.image });
  weibo.href = `https://service.weibo.com/share/share.php?${weiboParams.toString()}`;

  const qrImg = box.querySelector(".share-qr img");
  qrImg.src = cfg.qr;

  const nativeBtn = box.querySelector('[data-share="native"]');
  if (typeof navigator.share === "function") nativeBtn.hidden = false;

  box.addEventListener("click", async (event) => {
    const btn = event.target.closest("[data-share], .share-close");
    if (!btn) return;
    if (btn.classList.contains("share-close")) {
      closeSharePanel();
      return;
    }
    switch (btn.dataset.share) {
      case "copy-text":
        flash(btn, (await copyText(textarea.value)) ? "✓ 已复制，去发吧" : "复制失败，请手动选择");
        break;
      case "shuffle":
        setCopy();
        break;
      case "copy-link":
        flash(btn, (await copyText(url)) ? "✓ 已复制链接" : "复制失败");
        break;
      case "qr": {
        const fig = box.querySelector(".share-qr");
        fig.hidden = !fig.hidden;
        btn.setAttribute("aria-expanded", String(!fig.hidden));
        btn.textContent = fig.hidden ? "显示二维码" : "收起二维码";
        break;
      }
      case "native":
        try {
          await navigator.share({ title: cfg.title, text: textarea.value, url });
        } catch {
          /* 用户取消，静默 */
        }
        break;
      default:
        break;
    }
  });

  // 键盘：Esc 关闭；Tab 在面板内循环
  box.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      event.preventDefault();
      closeSharePanel();
      return;
    }
    if (event.key === "Tab") {
      const focusables = [...box.querySelectorAll("button:not([hidden]):not(:disabled), a[href], textarea")];
      if (!focusables.length) return;
      const first = focusables[0];
      const last = focusables[focusables.length - 1];
      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
    }
  });

  backdrop.addEventListener("click", (event) => {
    if (event.target === backdrop) closeSharePanel();
  });

  backdrop.appendChild(box);
  document.body.appendChild(backdrop);
  mountStarButtons(box);
  return backdrop;
}

export function openSharePanel(page, trigger = null) {
  if (!panel) panel = buildPanel(page);
  lastTrigger = trigger ?? document.activeElement;
  panel.hidden = false;
  document.body.classList.add("share-open");
  panel.querySelector('[data-share="copy-text"]')?.focus();
}

export function closeSharePanel() {
  if (!panel || panel.hidden) return;
  panel.hidden = true;
  document.body.classList.remove("share-open");
  if (lastTrigger && typeof lastTrigger.focus === "function") lastTrigger.focus();
  lastTrigger = null;
}

export function isSharePanelOpen() {
  return Boolean(panel && !panel.hidden);
}

// ---- D. 「点个 Star」提示（视频资料库）--------------------------------------------

let toastEl = null;

export function toastShown(threshold) {
  const seen = readJson(TOAST_KEY) ?? {};
  return Boolean(seen[String(threshold)]);
}

function markToast(threshold) {
  const seen = readJson(TOAST_KEY) ?? {};
  seen[String(threshold)] = true;
  writeJson(TOAST_KEY, seen);
}

export function showStarToast(threshold) {
  if (toastEl) toastEl.remove();
  const el = document.createElement("div");
  el.className = "star-toast pixel-panel";
  el.setAttribute("role", "status");
  el.setAttribute("aria-live", "polite");
  el.innerHTML = `
    <p class="star-toast-text"></p>
    <div class="star-toast-actions">
      <span data-star-slot="pixel-btn primary"></span>
      <button class="pixel-btn ghost" type="button" data-toast-dismiss>${GROWTH.toast.dismiss}</button>
    </div>
    <button class="share-close" type="button" aria-label="关闭提示" data-toast-dismiss>✕</button>
  `;
  el.querySelector(".star-toast-text").textContent = GROWTH.toast.text;
  const dismiss = () => {
    el.remove();
    if (toastEl === el) toastEl = null;
  };
  el.addEventListener("click", (event) => {
    if (event.target.closest("[data-toast-dismiss]")) dismiss();
    // 点了 Star 按钮（跳 GitHub）也顺手收起提示
    if (event.target.closest(".star-btn")) window.setTimeout(dismiss, 300);
  });
  document.body.appendChild(el);
  mountStarButtons(el);
  toastEl = el;
  markToast(threshold);
  return el;
}

// 打卡数刚到阈值时弹一次；已经提示过的阈值永不再弹。调用方在每次打卡后传入当前数量。
export function maybeStarToast(watchedCount) {
  for (const t of GROWTH.toast.thresholds) {
    if (watchedCount >= t && !toastShown(t)) {
      showStarToast(t);
      return t;
    }
  }
  return null;
}

// ---- 入口 ----------------------------------------------------------------------

// page: "quest" | "videos"。把 Star 按钮挂进所有 [data-star-slot]，把所有
// [data-share-trigger] 接到分享面板。
export function initGrowth({ page }) {
  mountStarButtons(document);
  for (const trigger of document.querySelectorAll("[data-share-trigger]")) {
    trigger.addEventListener("click", (event) => {
      event.preventDefault();
      openSharePanel(page, trigger);
    });
  }
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && isSharePanelOpen()) closeSharePanel();
  });
}
