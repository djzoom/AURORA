"""Day 2 — 自己实现正弦波，并和仓库标准实现对答案。

今日目标
--------
吃透公式  x[n] = A · sin(2π · f · n / sr)  的每个符号，亲手实现它，
再和 aurora.audio.sine 对比，确认数值一致。

跑法：  python scripts/learn/d2_sine.py
"""

import numpy as np

from aurora.audio import sine as reference_sine  # 仓库标准实现 = 你的"答案"


def my_sine(
    freq: float,
    duration: float,
    sample_rate: int,
    amplitude: float = 1.0,
) -> np.ndarray:
    """生成一个正弦波，返回 float 数组。

    x[n] = amplitude · sin(2π · freq · n / sample_rate),  n = 0..N-1

    提示：
      - N = round(duration * sample_rate)
      - n = np.arange(N)
      - 角度 = 2 * np.pi * freq * n / sample_rate
      - 返回 amplitude * np.sin(角度)
    """
    # TODO(Day2): 实现正弦波
    raise NotImplementedError("TODO: 按公式实现 my_sine")


def main() -> None:
    freq, dur, sr = 440.0, 1.0, 16000
    mine = my_sine(freq, dur, sr)
    ref = reference_sine(freq, duration=dur, sample_rate=sr)

    print(f"我的实现 shape : {mine.shape}")
    print(f"标准实现 shape : {ref.shape}")
    max_diff = float(np.max(np.abs(mine - ref)))
    print(f"最大逐点误差   : {max_diff:.2e}")

    assert mine.shape == ref.shape, "长度应一致"
    assert max_diff < 1e-6, "数值应几乎完全一致（差异 < 1e-6）"
    print("\n✅ 对答案通过：你的正弦波和仓库实现一致。")

    # 可选：画前 50 个采样点（需要 matplotlib）
    try:
        import matplotlib.pyplot as plt
        from pathlib import Path

        figs = Path(__file__).parent / "figs"
        figs.mkdir(exist_ok=True)
        plt.figure(figsize=(8, 3))
        plt.plot(mine[:50], marker="o", ms=3)
        plt.title("440 Hz sine — first 50 samples")
        plt.xlabel("sample n")
        plt.ylabel("amplitude")
        plt.tight_layout()
        out = figs / "d2_sine.png"
        plt.savefig(out, dpi=120)
        print(f"📈 已保存波形图: {out}")
    except ImportError:
        print("（装了 matplotlib 才会画图: pip install matplotlib）")


if __name__ == "__main__":
    main()
