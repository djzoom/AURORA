"""Day 4 — 复数与欧拉公式：FFT 的命根子。

今日目标
--------
吃透  e^{iθ} = cos θ + i·sin θ  —— 复指数就是单位圆上的旋转。
这正是 FFT 里旋转因子（twiddle）e^{-2πi·k·n/N} 的来源。

跑法：  python scripts/learn/d4_euler.py
"""

import numpy as np


def euler(theta: np.ndarray) -> np.ndarray:
    """用 cos / sin **手动**拼出 e^{iθ}，不要直接用 np.exp(1j*theta)。

    返回一个复数数组，实部 = cos θ，虚部 = sin θ。

    提示：
      - np.cos(theta) + 1j * np.sin(theta)
    """
    # TODO(Day4): 用 cos 和 sin 手动构造复指数
    raise NotImplementedError("TODO: 返回 cosθ + i·sinθ")


def twiddle(k: int, n: int, N: int) -> complex:
    """FFT 旋转因子 W = e^{-2πi·k·n/N}。理解它"转了多少圈"。

    提示：
      - 角度 = -2π · k · n / N
      - 复用上面的 euler，或直接 cos/sin 构造
    """
    # TODO(Day4): 返回旋转因子（complex）
    raise NotImplementedError("TODO: 返回 e^{-2πi·k·n/N}")


def main() -> None:
    theta = np.linspace(0, 2 * np.pi, 9)  # 0..360°，9 个点
    z = euler(theta)

    # 自检 1：euler 应与 numpy 的 np.exp(1j*theta) 一致
    ref = np.exp(1j * theta)
    assert np.max(np.abs(z - ref)) < 1e-12, "euler 应等于 np.exp(1j*theta)"
    # 自检 2：单位圆上每个点模长都是 1
    assert np.allclose(np.abs(z), 1.0), "e^{iθ} 落在单位圆上，模长恒为 1"

    print("θ (度) | e^{iθ} = cosθ + i·sinθ")
    for ang, val in zip(np.degrees(theta), z):
        print(f"{ang:6.0f} | {val.real:+.3f} {val.imag:+.3f}i")

    # twiddle 自检：n=0 时不旋转（=1）；转 N 步回到起点
    assert abs(twiddle(0, 0, 8) - 1) < 1e-12, "k·n=0 时旋转因子应为 1"
    print("\n✅ 你理解了：复指数 = 旋转，twiddle = FFT 里的旋转因子。")

    try:
        import matplotlib.pyplot as plt
        from pathlib import Path

        figs = Path(__file__).parent / "figs"
        figs.mkdir(exist_ok=True)
        fine = euler(np.linspace(0, 2 * np.pi, 200))
        plt.figure(figsize=(4.5, 4.5))
        plt.plot(fine.real, fine.imag, "-", lw=1)
        plt.plot(z.real, z.imag, "o")
        plt.gca().set_aspect("equal")
        plt.title("e^{iθ} traces the unit circle")
        plt.xlabel("Re"); plt.ylabel("Im")
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        out = figs / "d4_euler.png"
        plt.savefig(out, dpi=120)
        print(f"📈 已保存单位圆图: {out}")
    except ImportError:
        print("（装了 matplotlib 才会画图: pip install matplotlib）")


if __name__ == "__main__":
    main()
