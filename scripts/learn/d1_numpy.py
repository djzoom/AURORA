"""Day 1 — numpy 流畅度：生成一条时间轴。

今日目标
--------
理解"采样率 sr"和"时长 dur"如何决定采样点的数量与时间刻度，
并能用 numpy 一行生成时间轴。

跑法：  python scripts/learn/d1_numpy.py
"""

import numpy as np


def time_axis(duration: float, sample_rate: int) -> np.ndarray:
    """返回一条时间轴：从 0 开始，每隔 1/sample_rate 秒一个点，覆盖 duration 秒。

    例：duration=1.0, sample_rate=16000  ->  长度 16000 的数组，0, 1/16000, ...

    提示：
      - 采样点个数 n = round(duration * sample_rate)
      - 用 np.arange(n) / sample_rate，或 np.linspace（注意 endpoint）
    """
    # TODO(Day1): 用 numpy 生成并返回时间轴
    raise NotImplementedError("TODO: 返回长度为 duration*sample_rate 的时间轴")


def main() -> None:
    sr = 16000
    t = time_axis(1.0, sr)
    print(f"采样率      : {sr} Hz")
    print(f"采样点个数  : {t.shape[0]}  (期望 {sr})")
    print(f"前 5 个时刻 : {t[:5]}")
    print(f"最后 1 个时刻: {t[-1]:.6f} 秒")

    # 自检
    assert t.shape[0] == sr, "采样点个数应等于采样率（1 秒 × sr）"
    assert abs(t[1] - t[0] - 1 / sr) < 1e-12, "相邻时刻间隔应为 1/sr"
    print("\n✅ 通过：你理解了采样率如何决定时间轴。")


if __name__ == "__main__":
    main()
