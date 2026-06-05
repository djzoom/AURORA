"""Day 5 — 读懂 io.py / windows.py，并把三种窗函数画出来对比。

今日目标
--------
逐行读 src/aurora/audio/io.py 与 windows.py（今天主要是"读"，代码量很小）。
作为通关动作，调用仓库的窗函数把 Hann/Hamming/Blackman 画在一张图上，
观察它们的形状差异——这关系到 Week 3 的"频谱泄漏"。

跑法：  python scripts/learn/d5_read.py
"""

import numpy as np

from aurora.audio import blackman, hamming, hann


def describe_window(name: str, w: np.ndarray) -> None:
    """打印一个窗的关键性质：长度、两端值、峰值位置。

    提示（窗函数通常的性质）：
      - 两端接近 0（Hann 严格为 0），中间最大
      - 关于中心对称
    用 numpy 取 w[0]、w[-1]、w.max()、np.argmax(w) 即可。
    """
    # TODO(Day5): 打印 name、长度、首尾值、峰值与峰值位置
    raise NotImplementedError("TODO: 描述这个窗的形状性质")


def main() -> None:
    N = 64
    windows = {
        "Hann": hann(N),
        "Hamming": hamming(N),
        "Blackman": blackman(N),
    }

    for name, w in windows.items():
        assert w.shape[0] == N, f"{name} 窗长度应为 {N}"
        describe_window(name, w)

    # 观察：Hann 两端为 0，Hamming 两端略高于 0
    assert abs(hann(N)[0]) < 1e-9, "Hann 窗两端应为 0"
    print("\n阅读检查清单（合上代码，能口述吗？）：")
    print("  □ io.sine 里 2π·f·n/sr 每个符号是什么")
    print("  □ io.read_wav 如何把字节解析成样本")
    print("  □ 为什么加窗能减少频谱泄漏（Week 3 会深入）")

    try:
        import matplotlib.pyplot as plt
        from pathlib import Path

        figs = Path(__file__).parent / "figs"
        figs.mkdir(exist_ok=True)
        plt.figure(figsize=(8, 3.5))
        for name, w in windows.items():
            plt.plot(w, label=name)
        plt.title(f"Window functions (N={N})")
        plt.xlabel("sample"); plt.ylabel("weight")
        plt.legend(); plt.grid(True, alpha=0.3)
        plt.tight_layout()
        out = figs / "d5_windows.png"
        plt.savefig(out, dpi=120)
        print(f"\n📈 已保存窗函数对比图: {out}")
    except ImportError:
        print("\n（装了 matplotlib 才会画图: pip install matplotlib）")

    print("\n✅ Week 1 收口：信号 → 采样 → 复数 → 加窗，地基已就位。")


if __name__ == "__main__":
    main()
