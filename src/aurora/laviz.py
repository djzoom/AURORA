"""Linear-algebra visualization utilities for AURORA course notebooks.

Usage: from aurora.laviz import style, arrows2d, ...
"""
import matplotlib.pyplot as plt
import numpy as np

_PAL = ['#2A9D8F', '#E9C46A', '#F4A261', '#E76F51', '#264653', '#A8DADC']


def style():
    """Apply a clean, readable matplotlib style."""
    plt.rcParams.update({
        'figure.figsize': (6, 6),
        'axes.spines.top': False,
        'axes.spines.right': False,
        'axes.grid': True,
        'grid.alpha': 0.2,
        'font.size': 11,
    })


# ── helpers ────────────────────────────────────────────────────────────────

def _annotate_cells(ax, M, fontsize=9):
    """Write value labels on every cell of an imshow matrix."""
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            ax.text(j, i, f'{M[i, j]:.2g}',
                    ha='center', va='center', fontsize=fontsize)


def _mat_ax(ax, M, title='', color='#264653', fontsize=9, **kw):
    """Draw matrix M on ax with imshow + cell labels and a colored border."""
    vmax = max(abs(M).max(), 1e-9)
    defaults = dict(cmap='RdBu_r', vmin=-vmax, vmax=vmax, aspect='auto')
    defaults.update(kw)
    im = ax.imshow(M, **defaults)
    _annotate_cells(ax, M, fontsize)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(title, fontsize=11, color=color, fontweight='bold')
    for sp in ax.spines.values():
        sp.set_edgecolor(color)
        sp.set_linewidth(2)
    return im


# ── public API ─────────────────────────────────────────────────────────────

def arrows2d(vectors, labels=None, colors=None, title=''):
    """
    Plot 2-D vectors as arrows from the origin.

    vectors : list of [x, y] pairs
    labels  : optional list of annotation strings
    colors  : optional list of color strings
    """
    vecs = np.asarray(vectors, float)
    if vecs.ndim == 1:
        vecs = vecs[None]
    n = len(vecs)
    labels = labels or [f'v{i}' for i in range(n)]
    colors = colors or [_PAL[i % len(_PAL)] for i in range(n)]

    lim = max(np.abs(vecs).max() * 1.35, 1.5)
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.axhline(0, color='k', lw=0.5)
    ax.axvline(0, color='k', lw=0.5)
    ax.set_aspect('equal')

    for vec, lbl, col in zip(vecs, labels, colors, strict=False):
        ax.annotate('', xy=vec, xytext=(0, 0),
                    arrowprops=dict(arrowstyle='->', color=col,
                                   lw=2, mutation_scale=18))
        ax.text(vec[0] * 1.08, vec[1] * 1.08, lbl,
                color=col, fontsize=11, ha='center', va='center')

    ax.set_title(title)
    plt.tight_layout()
    plt.show()


def vec_times_vec(a, b):
    """
    Visualize the outer product a ⊗ bᵀ as a heatmap.
    Left panel = column vector a, right panel = row vector bᵀ,
    centre panel = the (m×n) result.
    """
    a = np.asarray(a, float)
    b = np.asarray(b, float)
    outer = np.outer(a, b)
    vmax = max(abs(outer).max(), 1e-9)
    kw = dict(cmap='RdBu_r', vmin=-vmax, vmax=vmax, aspect='auto')

    fig, axes = plt.subplots(
        1, 3, figsize=(10, 3),
        gridspec_kw={'width_ratios': [1, max(len(b), 2), 1]},
    )

    # Column vector a
    _mat_ax(axes[0], a.reshape(-1, 1), 'a', **kw)
    axes[0].set_title('a', fontsize=11, color='#264653', fontweight='bold')

    # Outer product
    im = _mat_ax(axes[1], outer, 'a ⊗ bᵀ  (外积)', **kw)
    axes[1].set_xlabel('b 的分量 →', fontsize=9)
    axes[1].set_ylabel('← a 的分量', fontsize=9)
    plt.colorbar(im, ax=axes[1], shrink=0.8)

    # Row vector b
    _mat_ax(axes[2], b.reshape(1, -1), 'bᵀ', **kw)

    plt.suptitle('向量外积  a ⊗ bᵀ', fontsize=13)
    plt.tight_layout()
    plt.show()


def mat_times_vec(A, x):
    """
    Visualize A @ x as a linear combination of A's columns.
    Shows each scaled column plus the sum (= result).
    """
    A = np.asarray(A, float)
    x = np.asarray(x, float)
    m, n = A.shape
    result = A @ x

    vmax = max(abs(A).max(), abs(result).max(), 1e-9)
    kw = dict(cmap='RdBu_r', vmin=-vmax, vmax=vmax, aspect='auto')

    # [A] | [x[0]*col0] ... [x[n-1]*col_{n-1}] | [Ax]
    ratios = [n] + [1] * n + [1]
    fig, axes = plt.subplots(1, n + 2, figsize=(2.5 * (n + 2), max(3, m)),
                              gridspec_kw={'width_ratios': ratios})

    _mat_ax(axes[0], A, 'A', **kw)
    axes[0].set_xticks(range(n))
    axes[0].set_yticks([])

    for j in range(n):
        col = (A[:, j] * x[j]).reshape(-1, 1)
        _mat_ax(axes[j + 1], col,
                f'×{x[j]:.2g}\n(列{j})', color=_PAL[j % len(_PAL)], **kw)

    _mat_ax(axes[-1], result.reshape(-1, 1), '= Ax',
            color='#264653', **kw)

    plt.suptitle('矩阵 × 向量 = 各列的线性组合', fontsize=13)
    plt.tight_layout()
    plt.show()


def mat_times_mat_rank1(A, B):
    """
    Show A @ B as a sum of rank-1 outer products col_j(A) ⊗ row_j(B).
    """
    A = np.asarray(A, float)
    B = np.asarray(B, float)
    m, k = A.shape
    result = A @ B

    vmax = max(abs(A).max(), abs(B).max(), abs(result).max(), 1e-9)
    kw = dict(cmap='RdBu_r', vmin=-vmax, vmax=vmax, aspect='auto')

    fig, axes = plt.subplots(2, k + 1,
                              figsize=(3 * (k + 1), 6))

    for j in range(k):
        r1 = np.outer(A[:, j], B[j, :])
        _mat_ax(axes[0, j], r1, f'a_{j} ⊗ b_{j}ᵀ  (秩1)',
                color=_PAL[j % len(_PAL)], **kw)
        axes[1, j].bar(range(B.shape[1]), B[j, :],
                       color=_PAL[j % len(_PAL)], alpha=0.75)
        axes[1, j].set_title(f'行 b_{j}', fontsize=9)
        axes[1, j].set_xticks([])

    im = _mat_ax(axes[0, -1], result, 'A @ B  (和)', **kw)
    plt.colorbar(im, ax=axes[0, -1], shrink=0.8)
    axes[1, -1].set_visible(False)

    plt.suptitle(f'矩阵乘法 = {k} 个秩1矩阵之和', fontsize=13)
    plt.tight_layout()
    plt.show()


def matrix_4ways(A):
    """
    Show matrix A in four complementary views:
    ① full heatmap  ② element values  ③ columns highlighted  ④ rows highlighted
    """
    A = np.asarray(A, float)
    m, n = A.shape
    vmax = max(abs(A).max(), 1e-9)
    kw = dict(cmap='RdBu_r', vmin=-vmax, vmax=vmax, aspect='auto')

    fig, axes = plt.subplots(1, 4, figsize=(14, max(3, m)))
    titles = ['① 整体', '② 元素值', '③ 列视角', '④ 行视角']

    for ax, ttl in zip(axes, titles, strict=False):
        ax.imshow(A, **kw)
        ax.set_title(ttl, fontsize=11)
        ax.set_xticks([])
        ax.set_yticks([])

    # ② element values
    _annotate_cells(axes[1], A, fontsize=10)

    # ③ column highlights
    col_colors = plt.cm.tab10(np.linspace(0, 0.9, n))
    for j in range(n):
        axes[2].axvline(j, color=col_colors[j], lw=4, alpha=0.6, label=f'列{j}')
    axes[2].legend(fontsize=8, loc='upper right')

    # ④ row highlights
    row_colors = plt.cm.Set2(np.linspace(0, 1, m))
    for i in range(m):
        axes[3].axhline(i, color=row_colors[i], lw=4, alpha=0.6, label=f'行{i}')
    axes[3].legend(fontsize=8, loc='upper right')

    plt.suptitle('同一矩阵的四种读法', fontsize=13)
    plt.tight_layout()
    plt.show()


def show_factorization(A, factors, labels, modes=None, title=''):
    """
    Visualize A = F0 @ F1 @ ... as side-by-side heatmaps.

    factors : list of 2-D arrays
    labels  : list of label strings (one per factor)
    modes   : optional list of border colors (one per factor)
    """
    A = np.asarray(A, float)
    factors = [np.asarray(F, float) for F in factors]
    if modes is None:
        modes = [_PAL[i % len(_PAL)] for i in range(len(factors))]

    all_mats = [A] + factors
    all_labels = ['A'] + list(labels)
    all_colors = ['#264653'] + list(modes)
    vmax = max(abs(M).max() for M in all_mats)
    kw = dict(cmap='RdBu_r', vmin=-vmax, vmax=vmax, aspect='auto')

    fig, axes = plt.subplots(1, len(all_mats),
                              figsize=(3 * len(all_mats), 4))
    for ax, M, lbl, col in zip(axes, all_mats, all_labels, all_colors, strict=False):
        _mat_ax(ax, M, lbl, color=col, **kw)

    plt.suptitle(title or f'A = {" @ ".join(labels)}', fontsize=13)
    plt.tight_layout()
    plt.show()


def heatmap(A, title='', cmap='viridis', labels=None):
    """
    Plot matrix A as a colour heatmap with annotated cell values.

    labels : optional (row_labels, col_labels) tuple of lists
    """
    A = np.asarray(A, float)
    m, n = A.shape
    fig, ax = plt.subplots(figsize=(max(4, n * 1.2), max(3, m * 1.0)))
    im = ax.imshow(A, cmap=cmap, aspect='auto')
    plt.colorbar(im, ax=ax)

    threshold = A.max() * 0.65
    for i in range(m):
        for j in range(n):
            color = 'white' if A[i, j] > threshold else 'black'
            ax.text(j, i, f'{A[i, j]:.2g}',
                    ha='center', va='center', fontsize=9, color=color)

    if labels:
        row_lbl, col_lbl = labels
        ax.set_yticks(range(m))
        ax.set_yticklabels(row_lbl)
        ax.set_xticks(range(n))
        ax.set_xticklabels(col_lbl, rotation=45, ha='right')
    else:
        ax.set_xticks([])
        ax.set_yticks([])

    ax.set_title(title)
    plt.tight_layout()
    plt.show()
