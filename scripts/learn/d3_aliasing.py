"""Day 3 — Nyquist 与混叠（aliasing）：亲眼看到高频"伪装"成低频。

今日目标
--------
理解为什么 sample_rate 必须 > 2 × 最高频率。用一个故意过低的采样率去采一个
高频正弦，画出来观察它变成了另一个低频。

跑法：  python scripts/learn/d3_aliasing.py
"""

import numpy as np

from aurora.audio import sine


def predict_alias_freq(freq: float, sample_rate: int) -> float:
    """预测：用 sample_rate 去采 freq Hz 的信号，实际会"看起来像"多少 Hz？

    当 freq > sample_rate/2（Nyquist 频率）时会发生混叠。
    折叠公式（单次折叠的简化版）：alias = |freq - sample_rate · round(freq/sample_rate)|

    提示：
      - k = round(freq / sample_rate)
      - 返回 abs(freq - k * sample_rate)
    """
    # TODO(Day3): 实现折叠频率预测
    raise NotImplementedError("TODO: 返回混叠后的视在频率")


def main() -> None:
    sr = 8000          # 故意偏低的采样率，Nyquist = 4000 Hz
    true_freq = 6000   # 高于 Nyquist -> 会混叠
    alias = predict_alias_freq(true_freq, sr)

    print(f"采样率        : {sr} Hz  (Nyquist = {sr // 2} Hz)")
    print(f"真实频率      : {true_freq} Hz  -> 高于 Nyquist，会混叠")
    print(f"预测视在频率  : {alias} Hz")
    assert 0 <= alias <= sr / 2, "混叠后的视在频率应落在 0..Nyquist 之间"

    # 用真实频率采样，再和"预测的低频"叠在一起对比
    x_aliased = sine(true_freq, duration=0.01, sample_rate=sr)
    x_lowfreq = sine(alias, duration=0.01, sample_rate=sr)

    match = float(np.max(np.abs(x_aliased - x_lowfreq)))
    print(f"采样点与低频版差异: {match:.2e}  (越接近 0，说明混叠成立)")

    try:
        import matplotlib.pyplot as plt
        from pathlib import Path

        figs = Path(__file__).parent / "figs"
        figs.mkdir(exist_ok=True)
        plt.figure(figsize=(9, 3))
        plt.plot(x_aliased, "o-", ms=4, label=f"sampled {true_freq} Hz @ {sr} Hz")
        plt.plot(x_lowfreq, "x--", ms=5, label=f"pure {alias:.0f} Hz")
        plt.title("Aliasing: a 6 kHz tone masquerades as a low tone")
        plt.xlabel("sample n")
        plt.legend()
        plt.tight_layout()
        out = figs / "d3_aliasing.png"
        plt.savefig(out, dpi=120)
        print(f"📈 已保存混叠对比图: {out}")
    except ImportError:
        print("（装了 matplotlib 才会画图: pip install matplotlib）")

    print("\n✅ 你亲眼验证了混叠：欠采样让高频伪装成低频。")


if __name__ == "__main__":
    main()
