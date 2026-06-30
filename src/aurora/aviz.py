"""Audio visualization utilities for AURORA course notebooks.

Usage: import aurora.aviz as aviz  (or:  from aurora import aviz)
"""
import matplotlib.pyplot as plt
import numpy as np

_STYLE_APPLIED = False


def style():
    """Apply a clean, readable matplotlib style."""
    plt.rcParams.update({
        'figure.figsize': (10, 4),
        'axes.spines.top': False,
        'axes.spines.right': False,
        'axes.grid': True,
        'grid.alpha': 0.25,
        'font.size': 12,
    })


def waveform(signal, stem=False, title='', sr=16000):
    """Plot a 1-D audio waveform."""
    signal = np.asarray(signal, float)
    t = np.arange(len(signal)) / sr
    fig, ax = plt.subplots()
    if stem:
        markerline, stemlines, baseline = ax.stem(t, signal)
        plt.setp(stemlines, linewidth=0.8)
        plt.setp(markerline, markersize=4)
        plt.setp(baseline, linewidth=0.5, color='k')
    else:
        ax.plot(t, signal)
    ax.set_xlabel('时间 (s)')
    ax.set_ylabel('幅度')
    ax.set_title(title or '波形')
    plt.tight_layout()
    plt.show()


def aliasing(f_signal, f_sample):
    """
    Demonstrate aliasing: f_signal sampled at f_sample Hz.
    Shows the original, aliased, and sampled signals.
    """
    n_periods = 3
    t_fine = np.linspace(0, n_periods / f_sample, 1000)
    t_samp = np.arange(0, n_periods / f_sample, 1 / f_sample)
    f_alias = abs(f_signal - round(f_signal / f_sample) * f_sample)

    y_true = np.sin(2 * np.pi * f_signal * t_fine)
    y_alias = np.sin(2 * np.pi * f_alias * t_fine)
    y_samp = np.sin(2 * np.pi * f_signal * t_samp)

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(t_fine, y_true, 'C0-', lw=2, alpha=0.55,
            label=f'原始信号 {f_signal} Hz')
    ax.plot(t_fine, y_alias, 'C1--', lw=2,
            label=f'混叠频率 {f_alias} Hz')
    ml, sl, bl = ax.stem(t_samp, y_samp, basefmt='k-')
    plt.setp(sl, linewidth=0.8, color='C2', alpha=0.8)
    plt.setp(ml, markersize=6, color='C2', label=f'采样点 @ {f_sample} Hz')
    plt.setp(bl, linewidth=0.5)
    ax.legend(fontsize=10)
    ax.set_xlabel('时间 (s)')
    ax.set_title(
        f'混叠：{f_signal} Hz × {f_sample} Hz 采样率 → 混叠为 {f_alias} Hz'
    )
    plt.tight_layout()
    plt.show()


def twiddles(N):
    """Plot the N twiddle factors e^{-2πik/N} on the complex unit circle."""
    k = np.arange(N)
    tw = np.exp(-2j * np.pi * k / N)

    theta = np.linspace(0, 2 * np.pi, 300)
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.plot(np.cos(theta), np.sin(theta), 'k-', alpha=0.18, lw=1)
    sc = ax.scatter(tw.real, tw.imag, c=k, cmap='hsv', s=90, zorder=5)
    plt.colorbar(sc, ax=ax, label='k')
    for k_i, w in enumerate(tw):
        ax.plot([0, w.real], [0, w.imag], 'k-', alpha=0.2, lw=0.8)
        ax.annotate(f'k={k_i}', xy=(w.real, w.imag),
                    xytext=(8, 4), textcoords='offset points', fontsize=9)
    ax.axhline(0, color='k', lw=0.4)
    ax.axvline(0, color='k', lw=0.4)
    ax.set_aspect('equal')
    ax.set_title(f'N={N} 旋转因子  $e^{{-2\\pi i k/N}}$')
    ax.set_xlabel('实部')
    ax.set_ylabel('虚部')
    plt.tight_layout()
    plt.show()


def windows_overlay(N):
    """Overlay rectangular, Hamming, and Hann window functions."""
    n = np.arange(N)
    rect = np.ones(N)
    hamming = 0.54 - 0.46 * np.cos(2 * np.pi * n / (N - 1))
    hann = 0.5 * (1 - np.cos(2 * np.pi * n / (N - 1)))

    fig, ax = plt.subplots()
    ax.plot(n, rect, 'C2-', lw=2, label='矩形窗', alpha=0.8)
    ax.plot(n, hamming, 'C1-', lw=2, label='Hamming 窗')
    ax.plot(n, hann, 'C0-', lw=2, label='Hann 窗')
    ax.set_xlim(0, N - 1)
    ax.set_ylim(-0.05, 1.12)
    ax.set_xlabel('采样点')
    ax.set_ylabel('幅度')
    ax.set_title(f'窗函数对比（N={N}）')
    ax.legend()
    plt.tight_layout()
    plt.show()


def framing(signal, frame_len=256, hop=128, n_frames=5):
    """Visualize overlapping STFT frames on the waveform."""
    signal = np.asarray(signal, float)
    colors = plt.cm.tab10(np.linspace(0, 0.5, n_frames))
    t = np.arange(len(signal))

    fig, ax = plt.subplots(figsize=(12, 3))
    ax.plot(t, signal, 'k-', lw=0.8, alpha=0.4)
    max_frames = (len(signal) - frame_len) // hop + 1
    for i in range(min(n_frames, max_frames)):
        start = i * hop
        end = min(start + frame_len, len(signal))
        ax.axvspan(start, end, alpha=0.18, color=colors[i])
        ax.plot(range(start, end), signal[start:end],
                color=colors[i], lw=1.5, label=f'帧 {i}')
    ax.set_xlabel('采样点')
    ax.set_ylabel('幅度')
    ax.set_title(f'STFT 分帧：frame_len={frame_len}, hop={hop}')
    ax.legend(loc='upper right', fontsize=9, ncol=2)
    plt.tight_layout()
    plt.show()


def spectrogram(signal, sr=16000):
    """Plot the power spectrogram of a signal (numpy FFT, Hann window)."""
    signal = np.asarray(signal, float)
    frame_len, hop = 256, 128
    win = 0.5 * (1 - np.cos(2 * np.pi * np.arange(frame_len) / (frame_len - 1)))

    frames = np.array([
        signal[i * hop: i * hop + frame_len]
        for i in range((len(signal) - frame_len) // hop + 1)
        if i * hop + frame_len <= len(signal)
    ])
    if frames.size == 0:
        print('信号太短，无法生成频谱图。')
        return

    spec = np.abs(np.fft.rfft(frames * win, axis=1)) ** 2
    spec_db = 10 * np.log10(spec.T + 1e-10)
    freqs = np.fft.rfftfreq(frame_len, 1 / sr)
    times = np.arange(len(frames)) * hop / sr

    fig, ax = plt.subplots(figsize=(10, 4))
    im = ax.imshow(
        spec_db, origin='lower', aspect='auto', cmap='magma',
        extent=[times[0], times[-1], freqs[0], freqs[-1]],
    )
    plt.colorbar(im, ax=ax, label='dB')
    ax.set_xlabel('时间 (s)')
    ax.set_ylabel('频率 (Hz)')
    ax.set_title('功率谱图')
    plt.tight_layout()
    plt.show()


def mel_filterbank_plot(n_mels, n_fft, sr):
    """Plot the mel filterbank as overlapping triangular filters."""
    def _hz_mel(f):
        return 2595 * np.log10(1 + f / 700)

    def _mel_hz(m):
        return 700 * (10 ** (m / 2595) - 1)

    m_min, m_max = _hz_mel(0), _hz_mel(sr / 2)
    mel_pts = np.linspace(m_min, m_max, n_mels + 2)
    hz_pts = _mel_hz(mel_pts)
    bins = np.floor(hz_pts / (sr / n_fft)).astype(int)

    fig, ax = plt.subplots(figsize=(10, 4))
    colors = plt.cm.viridis(np.linspace(0, 1, n_mels))
    for m in range(n_mels):
        xs = [bins[m], bins[m + 1], bins[m + 2]]
        ys = [0, 1, 0]
        ax.plot(xs, ys, color=colors[m], alpha=0.75, lw=1.5)
        ax.fill_between(xs, ys, alpha=0.08, color=colors[m])
    ax.set_xlabel('FFT bin')
    ax.set_ylabel('幅度')
    ax.set_title(f'Mel 滤波器组：{n_mels} 个滤波器，n_fft={n_fft}，sr={sr} Hz')
    plt.tight_layout()
    plt.show()


def mel_spectrogram_plot(signal, sr, n_mels):
    """Plot the mel spectrogram of a signal."""
    signal = np.asarray(signal, float)
    frame_len, hop = 256, 128
    win = 0.5 * (1 - np.cos(2 * np.pi * np.arange(frame_len) / (frame_len - 1)))

    frames = np.array([
        signal[i * hop: i * hop + frame_len]
        for i in range((len(signal) - frame_len) // hop + 1)
        if i * hop + frame_len <= len(signal)
    ])
    if frames.size == 0:
        print('信号太短，无法生成 Mel 频谱图。')
        return

    spec = np.abs(np.fft.rfft(frames * win, axis=1)) ** 2
    n_bins = frame_len // 2 + 1

    def _hz_mel(f):
        return 2595 * np.log10(1 + f / 700)

    def _mel_hz(m):
        return 700 * (10 ** (m / 2595) - 1)

    m_min, m_max = _hz_mel(0), _hz_mel(sr / 2)
    mel_pts = np.linspace(m_min, m_max, n_mels + 2)
    hz_pts = _mel_hz(mel_pts)
    bins = np.floor(hz_pts / (sr / frame_len)).astype(int)

    fb = np.zeros((n_mels, n_bins))
    for m in range(n_mels):
        s, c, e = bins[m], bins[m + 1], bins[m + 2]
        if c > s:
            fb[m, s:c] = np.linspace(0, 1, c - s)
        if e > c:
            fb[m, c:e] = np.linspace(1, 0, e - c)

    mel_spec_db = 10 * np.log10(spec @ fb.T + 1e-10)
    times = np.arange(len(frames)) * hop / sr

    fig, ax = plt.subplots(figsize=(10, 4))
    im = ax.imshow(
        mel_spec_db.T, origin='lower', aspect='auto', cmap='magma',
        extent=[times[0], times[-1], 0, n_mels],
    )
    plt.colorbar(im, ax=ax, label='dB')
    ax.set_xlabel('时间 (s)')
    ax.set_ylabel('Mel 滤波器')
    ax.set_title(f'Mel 频谱图：{n_mels} 个滤波器')
    plt.tight_layout()
    plt.show()
