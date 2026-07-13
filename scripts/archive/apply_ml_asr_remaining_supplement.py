#!/usr/bin/env python3
"""Apply the remaining ML / ASR supplement updates.

This script patches the remaining notebook bridges, solutions files,
domain-card navigation, and course-plan status updates for:
- L52 / L53 MFCC exit and bridge into L54
- L54 Value autograd bridge and half-step
- L55 / L58 / L59 opening bridges
- L24 / L25 / L30 forward references
- L66 / L67 / L68 / L69 / L70 bridge and cleanup
- docs/current/obsidian/domains/deep-learning.md
- docs/current/obsidian/domains/asr.md
- docs/current/course/*gap-supplement-plan.md
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from textwrap import dedent

import nbformat
from nbformat.v4 import new_code_cell, new_markdown_cell


REPO = Path(__file__).resolve().parent.parent

DSP_L52 = REPO / "notebooks" / "5_audio_dsp" / "L52_features_done.ipynb"
DSP_L53 = REPO / "notebooks" / "5_audio_dsp" / "L53_visual_mfcc.ipynb"

DL_L24 = REPO / "notebooks" / "3_calculus" / "L24_chain_rule.ipynb"
DL_L25 = REPO / "notebooks" / "3_calculus" / "L25_gradient_descent.ipynb"
DL_L30 = REPO / "notebooks" / "4_probability" / "L30_softmax_crossentropy.ipynb"

DL_L54 = REPO / "notebooks" / "6_deep_learning" / "L54_value_autograd.ipynb"
DL_L55 = REPO / "notebooks" / "6_deep_learning" / "L55_forward_pass.ipynb"
DL_L58 = REPO / "notebooks" / "6_deep_learning" / "L58_training_loop.ipynb"
DL_L59 = REPO / "notebooks" / "6_deep_learning" / "L59_tensor_basics.ipynb"

ASR_L66 = REPO / "notebooks" / "7_asr" / "L66_asr_overview.ipynb"
ASR_L67 = REPO / "notebooks" / "7_asr" / "L67_edit_distance.ipynb"
ASR_L68 = REPO / "notebooks" / "7_asr" / "L68_ctc_alignment.ipynb"
ASR_L69 = REPO / "notebooks" / "7_asr" / "L69_ctc_forward.ipynb"
ASR_L70 = REPO / "notebooks" / "7_asr" / "L70_whisper_arch.ipynb"

ML_SOLUTIONS = REPO / "notebooks" / "6_deep_learning" / "solutions"
ASR_SOLUTIONS = REPO / "notebooks" / "7_asr" / "solutions"

ML_PLAN = REPO / "docs" / "current" / "course" / "ml-gap-supplement-plan.md"
ASR_PLAN = REPO / "docs" / "current" / "course" / "asr-gap-supplement-plan.md"
INDEX_PLAN = REPO / "docs" / "current" / "course" / "gap-supplement-plan.md"
DEEP_DOMAIN = REPO / "docs" / "current" / "obsidian" / "domains" / "deep-learning.md"
ASR_DOMAIN = REPO / "docs" / "current" / "obsidian" / "domains" / "asr.md"


def _read_nb(path: Path) -> nbformat.NotebookNode:
    with path.open("r", encoding="utf-8") as fh:
        return nbformat.read(fh, as_version=4)


def _write_nb(path: Path, nb: nbformat.NotebookNode) -> None:
    tmp_path = path.with_suffix(path.suffix + ".tmp")
    tmp_path.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")
    tmp_path.replace(path)


def _cell_source(cell: nbformat.NotebookNode) -> str:
    source = cell.get("source", "")
    if isinstance(source, list):
        return "".join(source)
    return source


def _mk_md(text: str, cell_id: str) -> nbformat.NotebookNode:
    cell = new_markdown_cell(dedent(text).strip())
    cell["id"] = cell_id
    return cell


def _mk_code(text: str, cell_id: str) -> nbformat.NotebookNode:
    cell = new_code_cell(dedent(text).strip("\n"))
    cell["id"] = cell_id
    return cell


def _contains_marker(nb: nbformat.NotebookNode, marker: str) -> bool:
    return any(marker in _cell_source(cell) for cell in nb.cells)


def _insert_before_first(
    nb: nbformat.NotebookNode,
    predicate,
    new_cells: list[nbformat.NotebookNode],
) -> bool:
    if not new_cells:
        return False
    if any(_cell_source(cell).strip() == _cell_source(new_cells[0]).strip() for cell in nb.cells):
        return False
    for idx, cell in enumerate(nb.cells):
        if predicate(cell):
            nb.cells[idx:idx] = new_cells
            return True
    raise RuntimeError("anchor cell not found")


def _replace_cell_source(
    nb: nbformat.NotebookNode,
    marker: str,
    new_source: str,
) -> bool:
    for cell in nb.cells:
        if marker in _cell_source(cell):
            if _cell_source(cell).strip() == dedent(new_source).strip():
                return False
            cell["source"] = dedent(new_source).strip("\n")
            if cell.get("cell_type") == "code":
                cell["outputs"] = []
                cell["execution_count"] = None
            return True
    raise RuntimeError(f"cell containing marker not found: {marker}")


def _append_to_cell_source(
    nb: nbformat.NotebookNode,
    marker: str,
    addition: str,
) -> bool:
    for cell in nb.cells:
        if marker in _cell_source(cell):
            source = _cell_source(cell).rstrip()
            addition_text = dedent(addition).strip()
            if addition_text in source:
                return False
            appended = source + "\n\n" + addition_text
            if source == appended:
                return False
            cell["source"] = appended
            if cell.get("cell_type") == "code":
                cell["outputs"] = []
                cell["execution_count"] = None
            return True
    raise RuntimeError(f"cell containing marker not found: {marker}")


def _write_text_if_changed(path: Path, content: str) -> bool:
    current = path.read_text(encoding="utf-8") if path.exists() else ""
    if current == content:
        return False
    path.write_text(content, encoding="utf-8")
    return True


def _replace_text(path: Path, replacements: list[tuple[str, str]]) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text
    for old, new in replacements:
        text = text.replace(old, new)
    if text == original:
        return False
    path.write_text(text, encoding="utf-8")
    return True


def _replace_text_regex(path: Path, replacements: list[tuple[str, str]]) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text
    for pattern, new in replacements:
        text = re.sub(pattern, new, text, flags=re.MULTILINE)
    if text == original:
        return False
    path.write_text(text, encoding="utf-8")
    return True


def _update_l52() -> bool:
    nb = _read_nb(DSP_L52)
    if _contains_marker(nb, "## 附录 · Audio Core 结业：你已具备的能力清单"):
        return False

    appendix = _mk_md(
        """
        ## 附录 · Audio Core 结业：你已具备的能力清单

        - [ ] 能从空白重写 `fft` / `stft` / `mel_filterbank` / `mfcc`（口述 + 白板）
        - [ ] `make test` audio 全绿
        - [ ] 能解释 MFCC 五段 shape：`(T, n_mels)` → `(T, 13)`
        - [ ] **下一步不是更多 DSP**，而是 **L54：学模型如何从新数据中学习**

        > 这张清单不是额外作业，而是 Month 1 的收束：四项都能口述后，再切到深度学习入口就不会断层。
        """,
        "l52-audio-core-checklist",
    )
    return _insert_before_first(
        nb,
        lambda cell: cell.get("cell_type") == "markdown" and "## 本课收束" in _cell_source(cell),
        [appendix],
    ) and (_write_nb(DSP_L52, nb) or True)


def _update_l53() -> bool:
    nb = _read_nb(DSP_L53)
    if _contains_marker(nb, "## 附录 A · 进入深度学习：从「前向特征」到「反向学习」"):
        return False

    appendix_a = _mk_md(
        """
        ## 附录 A · 进入深度学习：从「前向特征」到「反向学习」（必读，10 分钟）

        1. **L32–L53 你在做什么**：固定变换（FFT / Mel / MFCC）——输入音频，输出向量；**权重不变**。
        2. **L54 起你在做什么**：带**可学习参数**的模型；用**损失函数**衡量错多少；用**梯度**告诉参数往哪改。
        3. **同一门数学**：L53 的 DCT 是前向矩阵乘法；L54 的 `backward()` 是问「若损失变一点，哪个参数该动」——也就是 L24 链式法则的代码版。
        4. **不必先学 PyTorch**：L54–L58 用自写 `Value` 理解 `loss.backward()`；L59 才切 PyTorch。
        5. **心理句**：`我学完 MFCC，是为了给 L62 的 CNN 准备输入；我学完 L54，是为了让 CNN 能从错误中学习。`

        ```python
        # 感受「学习」与「特征」的区别（无需实现）
        # 特征：y = mfcc(x)           — 无参数
        # 学习：loss = (w*x - y)**2   — 要算 dL/dw
        ```
        """,
        "l53-appendix-a",
    )
    appendix_b = _mk_md(
        """
        ## 附录 B · MFCC 流水线最后一眼（回调 L50）

        `waveform → spectrogram → mel_spectrogram → log → dct_ii → mfcc`

        口诀：`(T, 80)` 先压到 `(T, 40)`，再压到 `(T, 13)`；L54 之后就不再处理音频数组，而是处理标量计算图。
        """,
        "l53-appendix-b",
    )
    nav = _mk_md(
        """
        ---

        → **下一课**　[L54 · Value 计算图](../6_deep_learning/L54_value_autograd.ipynb)

        > **模块切换**：先读 L54 开篇「链式法则复习」，再开始 `Value` 实现。若感到突兀，回到本课附录 A。
        """,
        "nav-l53-clos",
    )

    inserted = _insert_before_first(
        nb,
        lambda cell: cell.get("cell_type") == "markdown" and "## 本课收束" in _cell_source(cell),
        [appendix_a, appendix_b],
    )
    replaced_nav = _replace_cell_source(nb, "→ **下一课**　[L54 · Value 计算图]", _cell_source(nav))
    if inserted or replaced_nav:
        _write_nb(DSP_L53, nb)
    return inserted or replaced_nav


def _update_l24() -> bool:
    nb = _read_nb(DL_L24)
    cell_source = """
    ## 本课收束

    现在能调用 `composite_derivative(x)` 得到 `sin(x²)` 在任意点的导数，数值误差在 `1e-9` 量级内。这个"外层导数 × 内层导数"的结构对应 `autograd.backward()`：每个节点缓存局部导数，沿计算图向输入方向连乘。Month 2 实现 autograd 时，`composite_derivative` 的分拆方式会直接变成计算图的边和节点设计。

    下一课：**L25**（梯度下降）把今天得到的导数当方向信号，把参数沿负梯度方向推动一步。

    下一课（L54）会把这条链式法则直接变成 `Value.backward()`，用计算图自动完成同样的乘法。
    """
    return _replace_cell_source(nb, "## 本课收束", cell_source) and (_write_nb(DL_L24, nb) or True)


def _update_l25() -> bool:
    nb = _read_nb(DL_L25)
    cell_source = """
    ## 本课收束

    现在能调用 `gd_step(x, grad_value, lr)` 逐步更新 `x`，在 `f(x) = (x−3)²` 上验证收敛过程。这对应 `aurora.train` 训练循环里每一步的参数更新。下一节（L26）将通过 cviz 等高线图展示梯度下降的收敛轨迹，直观对比不同学习率和起点下的收敛速度。

    下一步会在 L58 的训练循环里，把这条更新公式和 `Value` 的梯度传播合在一起，变成完整的参数更新一步。
    """
    return _replace_cell_source(nb, "## 本课收束", cell_source) and (_write_nb(DL_L25, nb) or True)


def _update_l30() -> bool:
    nb = _read_nb(DL_L30)
    cell_source = """
    ## 本课收束

    现在能用 `softmax(z)` 把任意 logits 向量转成概率分布，用 `cross_entropy(probs, target)` 得到一个标量损失。两个函数合在一起就是分类器「分数 → 概率 → 损失」的完整流程。Month 2 的关键词分类器会直接复用这套代码，Month 3 的 ASR 在 token 级别按相同方式计算训练损失。下一阶段（梯度下降篇）会用交叉熵对参数的导数指导权重更新，届时这里的 `loss` 标量就是起点。

    下一课（L31）将把今天的 softmax、交叉熵和 Shannon 熵全部可视化，建立直觉后进入 Week 2 的音频 DSP。

    **下一课 L31** 会把 softmax、交叉熵与 Shannon 熵画成图；读完后进入 Audio DSP（L32）前，建议先完成 L31 末尾的模块切换清单。

    交叉熵的梯度不会停留在公式里，L58 的训练循环会把它真正接到参数更新上；后面序列损失（如 L69 的 CTC）只是另一种视角。
    """
    return _replace_cell_source(nb, "## 本课收束", cell_source) and (_write_nb(DL_L30, nb) or True)


def _update_l54() -> bool:
    nb = _read_nb(DL_L54)
    changed = False

    if not _contains_marker(nb, "## 复习桥 · L24 链式法则（5 分钟，不跳过）"):
        bridge_md = _mk_md(
            """
            ## 复习桥 · L24 链式法则（5 分钟，不跳过）

            - 公式：`z = f(g(x))` → `dz/dx = (dz/dg) · (dg/dx)`
            - 手算例：`z = x*y + y²`，`x=3, y=2` → `dz/dx = 2`，`dz/dy = 7`
            - 本课要做的事：把这两步乘法交给 `Value.backward()` 自动完成
            """,
            "l54-chain-rule-bridge",
        )
        bridge_code = _mk_code(
            """
            x, y = 3.0, 2.0
            z = x * y + y**2
            dz_dx = y
            dz_dy = x + 2 * y
            assert z == 10 and dz_dx == 2 and dz_dy == 7
            print("链式法则手算与 L54 断言一致")
            """,
            "l54-chain-rule-bridge-check",
        )
        mode_table = _mk_md(
            """
            ## 模式对照表

            | | L53 MFCC | L54 Value |
            |---|---|---|
            | 数据类型 | `ndarray (T, 13)` | 标量 `float` |
            | 方向 | 仅前向 | 前向 + 反向 |
            | 目标 | 压缩表示 | 自动求 `dL/d参数` |
            | 库 | `aurora.audio` | 本课自写（L59 换 PyTorch） |

            记忆点：L53 是「特征提取」，L54 是「让参数从错误中学习」。
            """,
            "l54-mode-table",
        )
        changed = _insert_before_first(
            nb,
            lambda cell: cell.get("cell_type") == "markdown" and "## 本课剧情" in _cell_source(cell),
            [bridge_md, bridge_code, mode_table],
        ) or changed

    if not _contains_marker(nb, "## 半步练习 A · 只做前向（15 分钟）"):
        halfstep = _mk_md(
            """
            ## 半步练习 A · 只做前向（15 分钟）

            先只完成 `__init__`、`__add__`、`__mul__`，不要急着补 `__pow__` 和 `backward()`。
            目标是先让前向值跑通，再去补反向传播，这样不会在同一层 cliff 上同时处理两种难点。
            """,
            "l54-halfstep-forward",
        )
        changed = _insert_before_first(
            nb,
            lambda cell: cell.get("cell_type") == "markdown"
            and "## 4. ✏️ 实现 `class Value`" in _cell_source(cell),
            [halfstep],
        ) or changed

    value_task_source = """
    ## 4. ✏️ 实现 `class Value`

    **三个核心字段**：

    | 字段 | 含义 | 初始值 |
    |---|---|---|
    | `data` | 标量前向值 | 构造时传入 |
    | `grad` | 对最终损失的梯度 | 0.0（等待反向传播填写） |
    | `_backward` | 该算子的反向函数 | `lambda: None` |

    **四步实现路线**：

    | 步骤 | 方法 | backward 公式 |
    |---|---|---|
    | 1 | `__init__` | — |
    | 2 | `__add__` | `a.grad += out.grad`，`b.grad += out.grad` |
    | 3 | `__mul__` | `a.grad += b.data * out.grad`，`b.grad += a.data * out.grad` |
    | 4 | `backward()` | 拓扑排序 → 逆序调用每个节点的 `_backward()` |

    **验收标准**：
    - `(Value(2) + Value(3)).data == 5`
    - `L = a*b + b**2`，`L.backward()`，`a.grad == b.data`（对a的偏导=b）

    **铺垫**：先完成上面的半步练习 A，再补 `__pow__` 和 `backward()`；前向断言先通，反向断言后通。
    """
    changed = _replace_cell_source(nb, "## 4. ✏️ 实现 `class Value`", value_task_source) or changed

    cell12_source = """
    # 前向半步：只要 __init__ / __add__ / __mul__ 完成，这段就应先通过
    a = Value(2.0)
    b = Value(3.0)
    c = a + b
    assert c.data == 5.0, f"期望 5.0，得到 {c.data}"
    print("✅ a + b 前向正确：", c)

    d = a * b
    assert d.data == 6.0, f"期望 6.0，得到 {d.data}"
    print("✅ a * b 前向正确：", d)

    # 完整 backward：如果 __pow__ / backward 还没补完，这段会友好提示
    try:
        a2 = Value(2.0)
        b2 = Value(3.0)
        out = a2 * b2
        out.grad = 1.0
        out._backward()
        assert a2.grad == 3.0, f"期望 a.grad=3.0，得到 {a2.grad}"
        assert b2.grad == 2.0, f"期望 b.grad=2.0，得到 {b2.grad}"
        print("✅ __mul__ _backward 正确：a.grad=", a2.grad, " b.grad=", b2.grad)

        a3 = Value(4.0)
        b3 = Value(2.0)
        L = a3 * b3 + b3 ** 2   # L = 4*2 + 4 = 12；dL/da=2, dL/db=4+4=8
        L.backward()
        assert a3.grad == 2.0, f"期望 dL/da=2.0，得到 {a3.grad}"
        assert b3.grad == 8.0, f"期望 dL/db=8.0，得到 {b3.grad}"
        print("✅ L=(a*b + b**2) backward() 正确：a.grad=", a3.grad, " b.grad=", b3.grad)
    except NotImplementedError:
        print("⬜ backward / __pow__ 还未完成，先把前向半步补完即可继续。")
    """
    if not _contains_marker(nb, "# 前向半步：只要 __init__ / __add__ / __mul__ 完成，这段就应先通过"):
        changed = _replace_cell_source(nb, "# 检查 __add__ 和 __mul__ 的前向值", cell12_source) or changed

    cell17_source = """
    # 验证：优先使用本 notebook 的 Value；若还没实现完，则回退到 PyTorch 做数值对照
    try:
        x = Value(3.0)
        y = Value(2.0)
        z = x * y + y ** 2
        z.backward()
        dz_dx = x.grad
        dz_dy = y.grad
    except NotImplementedError:
        import torch
        x = torch.tensor(3.0, requires_grad=True)
        y = torch.tensor(2.0, requires_grad=True)
        z = x * y + y ** 2
        z.backward()
        dz_dx, dz_dy = x.grad.item(), y.grad.item()

    # z = xy + y^2 → dz/dx = y = 2, dz/dy = x + 2y = 3 + 4 = 7
    assert abs(dz_dx - 2.0) < 1e-6, f"dz/dx = {dz_dx}，期望 2"
    assert abs(dz_dy - 7.0) < 1e-6, f"dz/dy = {dz_dy}，期望 7"
    print(f"✅ dz/dx = {dz_dx} ✓   dz/dy = {dz_dy} ✓")
    """
    if not _contains_marker(nb, "# 验证：优先使用本 notebook 的 Value；若还没实现完，则回退到 PyTorch 做数值对照"):
        changed = _replace_cell_source(nb, "# 验证：用 aurora Value 类与手算梯度对比", cell17_source) or changed

    if changed:
        _write_nb(DL_L54, nb)
    return changed


def _update_l55() -> bool:
    nb = _read_nb(DL_L55)
    if _contains_marker(nb, "## 开篇回调：L54 的 `Value` 还缺什么？"):
        return False
    bridge = _mk_md(
        """
        ## 开篇回调：L54 的 `Value` 还缺什么？

        L54 已经把 `__add__` / `__mul__` 的梯度规则说清了，但还缺三类“节点动作”：`__pow__`、`relu`、`tanh` / `exp`。
        本课只做一件事：把这些算子补齐，让同一套计算图能表达真正的神经网络前向。
        """,
        "l55-opening-bridge",
    )
    changed = _insert_before_first(
        nb,
        lambda cell: cell.get("cell_type") == "markdown" and "## 本课剧情" in _cell_source(cell),
        [bridge],
    )
    if changed:
        _write_nb(DL_L55, nb)
    return changed


def _update_l58() -> bool:
    nb = _read_nb(DL_L58)
    changed = False
    if not _contains_marker(nb, "## 零件清点：`Value` + `Neuron` + 损失 + 优化器"):
        bridge = _mk_md(
            """
            ## 零件清点：`Value` + `Neuron` + 损失 + 优化器

            - `Value` 提供 `backward()` 和梯度累积
            - `Neuron` / `Layer` 负责前向映射
            - 损失函数把分类目标压成一个标量
            - `optimizer.step()` / `zero_grad()` 把一轮训练闭合

            先把这四个零件在脑中排齐，再读下面的 5 步训练循环。
            """,
            "l58-parts-checklist",
        )
        changed = _insert_before_first(
            nb,
            lambda cell: cell.get("cell_type") == "markdown" and "## 本课剧情" in _cell_source(cell),
            [bridge],
        ) or changed

    cell15_new = """
    ## 本课收束

    `train()` 函数实现了完整的梯度下降（gradient descent，GD）训练循环：`forward → hinge loss → backward → update → zero_grad`，返回每轮的损失数值列表。月牙形数据集上 100 轮后准确率超过 85%，损失曲线验证了收敛正常。这个循环与 `src/aurora/` 中 Month 2 PyTorch 版本完全同构——参数更新逻辑、zero_grad 时机、loss 聚合方式一字不差。下一节（L59）将进入 PyTorch 世界：从 `torch.Tensor` 开始，掌握张量操作、dtype 转换与设备管理，为后续 `nn.Module` 构建做好基础。
    """
    changed = _replace_cell_source(nb, "## 本课收束", cell15_new) or changed

    if changed:
        _write_nb(DL_L58, nb)
    return changed


def _update_l59() -> bool:
    nb = _read_nb(DL_L59)
    if _contains_marker(nb, "## 模式切换：从自写 autograd 回到 PyTorch Tensor"):
        return False
    bridge = _mk_md(
        """
        ## 模式切换：从自写 autograd 回到 PyTorch Tensor

        L54–L58 你已经用 `Value` 手写了计算图和训练循环；本课开始切到 `torch.Tensor`，把同样的概念映射到真正的框架接口：

        - `ndarray` → `Tensor`
        - `requires_grad` → autograd
        - `device` → CPU / GPU

        这不是换主题，而是把同一套思维搬进生产级工具。
        """,
        "l59-module-switch-bridge",
    )
    changed = _insert_before_first(
        nb,
        lambda cell: cell.get("cell_type") == "markdown" and "## 本课剧情" in _cell_source(cell),
        [bridge],
    )
    if changed:
        _write_nb(DL_L59, nb)
    return changed


def _update_l66() -> bool:
    nb = _read_nb(ASR_L66)
    cell_source = """
    ## 本课收束

    本节实现了 `compute_wer`，它通过 Levenshtein 动态规划计算词级编辑距离，输出 `(S+D+I)/N` 浮点 WER 值。该指标将贯穿 `aurora.speech` 模块的全部训练与评测循环。下一课：**L67** 将从零实现 Levenshtein 编辑距离动态规划算法，建立 WER 的数学基础。

    `compute_wer` 依赖下一课的编辑距离 DP；如果先想实现 WER 练习，记得把 L67 看完再回头做。
    """
    changed = _replace_cell_source(nb, "## 本课收束", cell_source)
    if changed:
        _write_nb(ASR_L66, nb)
    return changed


def _update_l67() -> bool:
    nb = _read_nb(ASR_L67)
    cell_source = """
    ## 本课收束

    | 概念 | 要记住的 |
    |---|---|
    | 编辑距离 | 3 种操作，DP 表 (m+1)×(n+1) |
    | WER | = 词级编辑距离 / 参考词数，可以 > 1.0 |
    | 回溯 | 从 dp[m][n] 往左上角走，还原对齐路径 |
    | L68 | CTC 对齐——同样是"所有对齐路径"思想，但面对的是连续帧 |

    下一课（L68）将用 CTC 对齐代替手动标注：`ctc_alignment` 把声学帧序列与目标词序列自动对齐，服务于 CTC 系列模型（如 wav2vec 2.0、DeepSpeech）的训练目标。

    L69 的 CTC 前向算法也是同一种“填表递推”思想，只是把最小化编辑代价换成 log 概率求和。
    """
    changed = _replace_cell_source(nb, "## 本课收束", cell_source)
    if changed:
        _write_nb(ASR_L67, nb)
    return changed


def _update_l68() -> bool:
    nb = _read_nb(ASR_L68)
    changed = False

    if _contains_marker(nb, "import torch"):
        changed = _replace_cell_source(
            nb,
            "import numpy as np\nimport torch",
            "import numpy as np",
        ) or changed

    if not _contains_marker(nb, "## 附录 C · 从贪婪解码到前向算法：L69 预习（8 分钟）"):
        appendix = _mk_md(
            """
            ## 附录 C · 从贪婪解码到前向算法：L69 预习（8 分钟）

            1. **L68 做了什么**：找**一条**最优路径（贪婪近似）。
            2. **L69 要做什么**：对**所有**合法路径的概率**求和**（精确训练损失）。
            3. **为何需要 DP**：路径数 O(V^T)；DP 降到 O(T·S)，其中 `S = 2L + 1`。
            4. **与 L67 的关系**：编辑距离 DP 也是“填表递推”；CTC 只是把表里的值换成 log 概率。
            5. **log 域一句**：概率相乘 → log 域用 `logaddexp` 做“log 下的加法”。

            ```text
                    s=0   s=1   s=2   …   (扩展标签轴)
            t=0     α     ·     ·
            t=1     ·     ·     ·
            …
            ```
            """,
            "l68-appendix-c",
        )
        demo = _mk_code(
            """
            from itertools import product

            toy_labels = [1, 2]  # a b
            toy_paths = [
                path
                for path in product(range(3), repeat=3)
                if collapse(path, blank=0) == toy_labels
            ]
            print("T=3 时的合法路径数：", len(toy_paths))
            print("前 5 条路径：", toy_paths[:5])
            print("精确求和要等 L69 的 ctc_forward；L68 这里只先看路径空间怎么长出来。")
            """,
            "l68-appendix-c-demo",
        )
        changed = _insert_before_first(
            nb,
            lambda cell: cell.get("cell_type") == "markdown" and "## 本课收束" in _cell_source(cell),
            [appendix, demo],
        ) or changed

    greedy_decode_source = """
    def ctc_greedy_decode(logits: np.ndarray, blank: int = 0) -> list:
        \"\"\"CTC 贪婪解码：argmax 每帧，去相邻重复，去 blank。

        Args:
            logits: shape (T, V) numpy 数组（未经 softmax 的原始得分）
            blank:  blank 符号的 token id，默认 0
        Returns:
            解码后的 token id 列表
        \"\"\"
        # ✏️ TODO: 第1步——每帧取 argmax
        preds = None

        # ✏️ TODO: 第2步——去相邻重复（保留第一个，后续只保留与前一个不同的）
        deduped = None

        # ✏️ TODO: 第3步——去掉 blank，返回 list[int]
        raise NotImplementedError(\"请先完成上方三个 TODO 步骤，再运行检验 cell；卡住可看 solutions/L68_ctc_alignment_solutions.md\")
    """
    changed = _replace_cell_source(
        nb,
        "raise NotImplementedError(\"请先完成上方三个 TODO 步骤，再运行检验 cell；卡住可看 solutions/L68_ctc_alignment_solutions.md\")",
        greedy_decode_source,
    ) or changed

    changed = _replace_cell_source(
        nb,
        "## 本课收束",
        """
        ## 本课收束

        本节实现了 `ctc_greedy_decode`，它输出一个 `list[int]`（压缩后的 token id 序列），对应 CTC 路径的近似最优解。
        该函数直接服务于 `aurora.speech` 推理管线——在 `torch.nn.CTCLoss` 训练完成后，贪婪解码是最快的线上解码方式。
        本课附录 C 已把 L69 的前向算法预热：先看路径空间，再看 log 域递推，就不会在下一节突然掉进 cliff。
        下一节（L69）将实现 CTC 前向算法的完整动态规划，追踪 blank-skip 和标签折叠两条合法路径，计算序列概率。
        L69 之后还将讨论 Whisper 选择交叉熵而非 CTC 的原因。
        """,
    ) or changed

    nav_update = _replace_cell_source(
        nb,
        "→ **下一课**　[L69 · CTC 前向算法](L69_ctc_forward.ipynb)",
        """
        ---

        → **下一课**　[L69 · CTC 前向算法](L69_ctc_forward.ipynb)

        > 下节课将学习 **CTC 前向算法**：所有路径概率求和，O(T·S) 纯 NumPy 实现。先读本课附录 C，再回到 L67 的 DP 填表逻辑。
        """,
    )
    changed = nav_update or changed

    if changed:
        _write_nb(ASR_L68, nb)
    return changed


def _update_l69() -> bool:
    nb = _read_nb(ASR_L69)
    changed = False

    title_source = """
    # 第69课 · CTC（Connectionist Temporal Classification，CTC） 前向算法（forward algorithm） — 所有路径概率求和，O(T·S) 纯 NumPy 实现

    **学习目标**
    - 理解 CTC 的核心挑战：不知道字符在哪一帧对齐（alignment）
    - 掌握前向变量（forward variable，alpha） α 的递推定义
    - 用纯 NumPy 实现 CTC 前向算法并数值验证
    """
    changed = _replace_cell_source(
        nb,
        "# 第69课 · CTC（Connectionist Temporal Classification，CTC） 前向算法（forward algorithm）",
        title_source,
    ) or changed

    story_source = """
    ## 本课剧情：为什么朴素的路径枚举会\"爆炸\"？

    上节课学了 CTC 的直觉：blank 符号让一个目标序列对应指数级多条路径。

    但问题来了：**若要精确计算 P(\"ab\" | 6帧)，我们需要枚举 3⁶=729 条路径，逐一压缩验证，再相加**。T=100帧时就是 3¹⁰⁰条路径——彻底不可行。

    **前向算法（Forward Algorithm）**的解法：用动态规划，把\"枚举→求和\"变成\"递推→合并\"。

    **关键设计**：把目标序列 `[\"a\",\"b\"]` 扩展为包含 blank 的序列 `l' = [∅, a, ∅, b, ∅]`（每个字符前后插 blank），长度 `S = 2L+1`。

    **前向变量** α[t][s] = \"在第 t 帧结束时，以 l'[s] 结束的所有合法路径的概率和\"。

    **递推关系（三种情况）**：
    ```
    情况1：l'[s] = blank，或与前2步字符相同
       α[t][s] = (α[t-1][s] + α[t-1][s-1]) × P(l'[s] | t)

    情况2：l'[s] = 字符，且 l'[s] ≠ l'[s-2]
       α[t][s] = (α[t-1][s] + α[t-1][s-1] + α[t-1][s-2]) × P(l'[s] | t)
    ```

    最终：`log P(label | logits) = logsumexp(α[T-1][S-1], α[T-1][S-2])`

    复杂度从指数 → **O(T·S)**，其中 `S = 2L + 1`；训练 ASR 成为可能。
    """
    changed = _replace_cell_source(
        nb,
        "## 本课剧情：为什么朴素的路径枚举会\"爆炸\"？",
        story_source,
    ) or changed

    if not _contains_marker(nb, "### Log 域等价（实现用此式）"):
        log_md = _mk_md(
            """
            ### Log 域等价（实现用此式）

            ```text
            log α[t, s] = log p[t, l'[s]] + logaddexp(
                log α[t-1, s],      # 停留
                log α[t-1, s-1],    # 跳一步
                log α[t-1, s-2]     # 跳两步（仅当 l'[s] ≠ l'[s-2]）
            )
            ```

            `np.logaddexp(a, b)` = `log(exp(a) + exp(b))`，数值稳定；三路前驱可用两次 `logaddexp` 叠出来。
            """,
            "l69-log-domain",
        )
        log_demo = _mk_code(
            """
            a, b = np.log([0.3, 0.7])
            assert np.isclose(np.logaddexp(a, b), np.log(1.0))
            print("✅ logaddexp 演示：log(exp(a)+exp(b)) 在 log 域里能稳定相加")
            """,
            "l69-logaddexp-demo",
        )
        log_softmax = _mk_code(
            """
            def log_softmax(logits, axis=-1):
                m = logits.max(axis=axis, keepdims=True)
                shifted = logits - m
                return shifted - np.log(np.exp(shifted).sum(axis=axis, keepdims=True))
            """,
            "l69-log-softmax-helper",
        )
        changed = _insert_before_first(
            nb,
            lambda cell: cell.get("cell_type") == "code" and "def ctc_forward(log_probs" in _cell_source(cell),
            [log_md, log_demo, log_softmax],
        ) or changed

    if not _contains_marker(nb, "## 半步练习 B · ctc_forward_brute_force（先写/先读此函数）"):
        halfstep = _mk_md(
            """
            ## 半步练习 B · ctc_forward_brute_force（先写 / 先读此函数）

            先把“求和的对象”弄明白，再写 DP。暴力枚举只在 T 很小时能跑，所以它是验证器，不是训练器。
            """,
            "l69-halfstep-bruteforce",
        )
        changed = _insert_before_first(
            nb,
            lambda cell: cell.get("cell_type") == "code" and "def ctc_forward_brute_force" in _cell_source(cell),
            [halfstep],
        ) or changed

    cell5_source = """
    ## ✏️ 实现 CTC 前向算法

    **签名**：
    ```python
    def ctc_forward(log_probs: np.ndarray, labels: list, blank: int = 0) -> float:
        # log_probs: (T, V) 对数概率矩阵
        # labels: list[int] 目标序列（不含 blank）
        # 返回: float  log P(labels | log_probs)
    ```

    **5步实现路线**：

    | 步骤 | 操作 | 关键点 |
    |---|---|---|
    | 1 | 构造扩展标签 `l'` | `[blank, L[0], blank, L[1], ..., blank]`，长度 `2L+1` |
    | 2 | 初始化 α：`-inf`，设 `α[0][0]` 和 `α[0][1]` | 第0帧只能是 blank 或第1个字符 |
    | 3 | 对 t=1..T-1：对 s=0..S-1 递推 | 情况1（blank/重复）取2项，情况2取3项 |
    | 4 | 用 log-space 加法避免下溢 | `logsumexp(a, b) = a + log(1 + exp(b-a))` |
    | 5 | 返回 `logsumexp(α[T-1][S-1], α[T-1][S-2])` | 两种结尾方式的概率和 |

    **验收标准**：
    - 与暴力枚举（`ctc_forward_brute_force`）结果误差 < 1e-5
    - `T=6, L=["a","b"]` 时返回有限 float（不是 -inf）

    **实现前先记一句**：`S = 2L + 1`，本课复杂度是 `O(T·S)`，不是 `O(T×2L)`。
    """
    changed = _replace_cell_source(nb, "## ✏️ 实现 CTC 前向算法", cell5_source) or changed

    cell6_source = '''
    def ctc_forward(log_probs: np.ndarray, labels: list, blank: int = 0) -> float:
        """CTC 前向算法：计算 log P(labels | log_probs)。

        Args:
            log_probs: (T, vocab_size) log-probability matrix.
            labels:    list of integer label ids (without blanks).
            blank:     blank token index.
                       注意：本笔记本 BLANK=2，请显式传入 blank=BLANK；
                       函数默认值 0 是 CTC 论文惯例，不适用于本例。

        Returns:
            log probability of the label sequence under CTC.
        """
        T, V = log_probs.shape
        L = len(labels)

        # 扩展标签：blank + label + blank + label + ... + blank
        lprime = [blank]
        for c in labels:
            lprime.append(c)
            lprime.append(blank)
        S = len(lprime)   # = 2L + 1

        NEG_INF = -1e30
        alpha = np.full((T, S), NEG_INF)

        # ✏️ TODO 步骤1：初始条件
        # 第 0 帧只能从扩展标签的前两个位置出发（blank 或第一个字符）
        # alpha[0, 0] = log_probs[0, lprime[0]]
        # if S > 1: alpha[0, 1] = log_probs[0, lprime[1]]

        # ✏️ TODO 步骤2：t=1..T-1 的递推（三个合法前驱）
        # for t in range(1, T):
        #     for s in range(S):
        #         val = alpha[t-1, s]                                   # 停留
        #         if s > 0:
        #             val = np.logaddexp(val, alpha[t-1, s-1])          # 跳1
        #         if s > 1 and lprime[s] != lprime[s-2]:                # 跳2（仅字符位）
        #             val = np.logaddexp(val, alpha[t-1, s-2])
        #         alpha[t, s] = val + log_probs[t, lprime[s]]

        # ✏️ TODO 步骤3：返回终态 log-sum
        # 最后一帧可停在位置 S-1（字符）或 S-2（blank），取 logaddexp
        # return np.logaddexp(alpha[-1, -1], alpha[-1, -2])

        raise NotImplementedError  # 完成步骤1-3后删除此行
    '''
    changed = _replace_cell_source(
        nb,
        "\"\"\"CTC 前向算法：计算 log P(labels | log_probs)。",
        cell6_source,
    ) or changed

    cell7_source = '''
    def ctc_forward_brute_force(log_probs: np.ndarray, labels: list, blank: int = 0) -> float:
        """暴力枚举版 CTC（仅用于验证，T 较小时可用）。
        枚举所有长度为 T 的路径，保留折叠后等于 labels 的路径，用 logsumexp 聚合。
        """
        from itertools import product
        T, V = log_probs.shape

        def collapse(path):
            """去掉 blank、合并重复字符 → 等价于 CTC collapse。"""
            result, prev = [], None
            for c in path:
                if c == blank:
                    prev = None
                elif c != prev:
                    result.append(c)
                    prev = c
            return result

        log_p_list = []
        for path in product(range(V), repeat=T):
            if collapse(list(path)) == list(labels):
                lp = sum(log_probs[t, path[t]] for t in range(T))
                log_p_list.append(lp)

        if not log_p_list:
            return -1e30

        arr = np.array(log_p_list)
        m = arr.max()
        return float(m + np.log(np.exp(arr - m).sum()))


    # 快速自检（T=4 时暴力枚举可在 < 1 秒内完成）
    np.random.seed(42)
    _lp4 = log_softmax(np.random.randn(4, VOCAB_SIZE))
    _ref = ctc_forward_brute_force(_lp4, LABELS, blank=BLANK)
    print(f"暴力枚举参考值（T=4）: {_ref:.4f}  → 用于断言 DP 实现正确性")
    '''
    changed = _replace_cell_source(nb, "def ctc_forward_brute_force(log_probs: np.ndarray, labels: list, blank: int = 0) -> float:", cell7_source) or changed

    cell11_source = """
    ## 本课收束

    | 概念 | 要记住的 |
    |---|---|
    | 扩展标签 l' | blank 插在每个标签之间，长度 2L+1 |
    | 前向变量 α[t][s] | log 域递推，避免下溢 |
    | 三个前驱 | 停留、跳 1、跳 2（限字符不同时）|
    | 复杂度 | O(T·S) — 其中 `S = 2L + 1`，与暴力枚举路径的指数复杂度相比快得多 |
    | L70 | Whisper 用 Attention 解码，但仍然是 token-by-token 的自回归过程 |

    下一课（L70）从代码层面解剖 Whisper 架构：音频编码器（encoder）、交叉注意力（cross-attention）和文本解码器的完整实现。先把本课的 log 域 DP 和 L67 的填表思维串起来，再去看 Whisper。
    """
    changed = _replace_cell_source(nb, "## 本课收束", cell11_source) or changed

    nav = _replace_cell_source(
        nb,
        "→ **下一课**　[L70 · Whisper 架构解析](L70_whisper_arch.ipynb)",
        """
        ---

        → **下一课**　[L70 · Whisper 架构解析](L70_whisper_arch.ipynb)

        > 下节课将学习 **Whisper 架构解析**：Log-Mel 输入、Transformer Encoder-Decoder、多任务头。先看本课附录与 L67 复习桥，再去读 Whisper。
        """,
    )
    changed = nav or changed

    if changed:
        _write_nb(ASR_L69, nb)
    return changed


def _update_l70() -> bool:
    nb = _read_nb(ASR_L70)
    if _contains_marker(nb, "## Whisper / CTC 连接提示"):
        return False
    bridge = _mk_md(
        """
        ## Whisper / CTC 连接提示

        Whisper 用的是交叉熵（cross-entropy）训练，而不是 CTC；L68–L69 则是理解“序列对齐基线”的前一站。
        先把 CTC 的单调路径和 log 域 DP 看懂，再看 Whisper 就会知道它为什么选择 token-by-token 的自回归解码。
        """,
        "l70-whisper-bridge",
    )
    changed = _insert_before_first(
        nb,
        lambda cell: cell.get("cell_type") == "markdown" and "## 本课剧情" in _cell_source(cell),
        [bridge],
    )
    if changed:
        _write_nb(ASR_L70, nb)
    return changed


def _update_ml_solutions() -> bool:
    path = ML_SOLUTIONS / "L54_value_autograd_solutions.md"
    content = dedent(
        """
        # 参考实现 — L54_value_autograd

        > ⚠️ 请先独立完成练习，再查看参考实现。

        ## 参考实现 1

        ```python
        class Value:
            def __init__(self, data, _children=(), _op=""):
                self.data = float(data)
                self.grad = 0.0
                self._backward = lambda: None
                self._prev = set(_children)
                self._op = _op

            def __repr__(self):
                return f"Value(data={self.data:.4f}, grad={self.grad:.4f})"

            def __add__(self, other):
                other = other if isinstance(other, Value) else Value(other)
                out = Value(self.data + other.data, (self, other), "+")

                def _backward():
                    self.grad += out.grad
                    other.grad += out.grad

                out._backward = _backward
                return out

            def __radd__(self, other):
                return self + other

            def __mul__(self, other):
                other = other if isinstance(other, Value) else Value(other)
                out = Value(self.data * other.data, (self, other), "*")

                def _backward():
                    self.grad += other.data * out.grad
                    other.grad += self.data * out.grad

                out._backward = _backward
                return out

            def __rmul__(self, other):
                return self * other

            def __pow__(self, other):
                assert isinstance(other, (int, float)), "指数必须是标量"
                out = Value(self.data**other, (self,), f"**{other}")

                def _backward():
                    self.grad += other * (self.data ** (other - 1)) * out.grad

                out._backward = _backward
                return out

            def __neg__(self):
                return self * -1

            def __sub__(self, other):
                return self + (-other)

            def __rsub__(self, other):
                return other + (-self)

            def __truediv__(self, other):
                return self * other**-1

            def backward(self):
                topo = []
                visited = set()

                def build(v):
                    if v not in visited:
                        visited.add(v)
                        for child in v._prev:
                            build(child)
                        topo.append(v)

                build(self)
                self.grad = 1.0
                for node in reversed(topo):
                    node._backward()
        ```
        """
    ).strip()
    return _write_text_if_changed(path, content)


def _update_asr_solutions() -> bool:
    path = ASR_SOLUTIONS / "L69_ctc_forward_solutions.md"
    content = dedent(
        """
        # 参考实现 — L69_ctc_forward

        > ⚠️ 请先独立完成练习，再查看参考实现。

        ## 参考实现 1

        ```python
        def log_softmax(logits, axis=-1):
            m = logits.max(axis=axis, keepdims=True)
            shifted = logits - m
            return shifted - np.log(np.exp(shifted).sum(axis=axis, keepdims=True))


        def ctc_forward(log_probs: np.ndarray, labels: list, blank: int = 0) -> float:
            T, V = log_probs.shape
            lprime = [blank]
            for c in labels:
                lprime.append(c)
                lprime.append(blank)
            S = len(lprime)

            NEG_INF = -1e30
            alpha = np.full((T, S), NEG_INF)
            alpha[0, 0] = log_probs[0, lprime[0]]
            if S > 1:
                alpha[0, 1] = log_probs[0, lprime[1]]

            for t in range(1, T):
                for s in range(S):
                    val = alpha[t - 1, s]
                    if s > 0:
                        val = np.logaddexp(val, alpha[t - 1, s - 1])
                    if s > 1 and lprime[s] != lprime[s - 2]:
                        val = np.logaddexp(val, alpha[t - 1, s - 2])
                    alpha[t, s] = val + log_probs[t, lprime[s]]

            return float(np.logaddexp(alpha[-1, -1], alpha[-1, -2]))


        def ctc_forward_brute_force(log_probs: np.ndarray, labels: list, blank: int = 0) -> float:
            from itertools import product

            T, V = log_probs.shape

            def collapse(path):
                result, prev = [], None
                for c in path:
                    if c == blank:
                        prev = None
                    elif c != prev:
                        result.append(c)
                        prev = c
                return result

            log_p_list = []
            for path in product(range(V), repeat=T):
                if collapse(list(path)) == list(labels):
                    lp = sum(log_probs[t, path[t]] for t in range(T))
                    log_p_list.append(lp)

            if not log_p_list:
                return -1e30

            arr = np.array(log_p_list)
            m = arr.max()
            return float(m + np.log(np.exp(arr - m).sum()))
        ```
        """
    ).strip()
    return _write_text_if_changed(path, content)


def _update_ml_plan() -> bool:
    return _replace_text_regex(
        ML_PLAN,
        [
            (
                r"^> \*\*状态\*\*：(?:📋 下一步计划（2026-07-01）|🟡 已落地待复审（2026-07-01）— L53→L54 / L55–L59 / week-03 / deep-learning 导航已回写)$",
                "> **状态**：🟡 已落地待复审（2026-07-01）— L53→L54 / L55–L59 / week-03 / deep-learning 导航已回写",
            ),
            (
                r"^周 5：L53 附录 A/B \+ L54 复习桥 \+ 半步 A \+ solutions/L54(?: — ✅ 已落地待复审（2026-07-01）)*$",
                "周 5：L53 附录 A/B + L54 复习桥 + 半步 A + solutions/L54 — ✅ 已落地待复审（2026-07-01）",
            ),
            (
                r"^周 6：L54 边界测试 \+ Aurora 连接文案 \+ week-03-checklist \+ L55/L58 衔接(?: — ✅ 已落地待复审（2026-07-01）)*$",
                "周 6：L54 边界测试 + Aurora 连接文案 + week-03-checklist + L55/L58 衔接 — ✅ 已落地待复审（2026-07-01）",
            ),
        ],
    )


def _update_asr_plan() -> bool:
    return _replace_text_regex(
        ASR_PLAN,
        [
            (
                r"^> \*\*状态\*\*：(?:📋 下一步计划（2026-07-01）|🟡 已落地待复审（2026-07-01）— L68→L69 / L66→L70 / week-04 / asr 导航已回写)$",
                "> **状态**：🟡 已落地待复审（2026-07-01）— L68→L69 / L66→L70 / week-04 / asr 导航已回写",
            ),
            (
                r"^周 7：L68 附录 C \+ 降泄漏 \+ L69 复习桥 \+ log 域 \+ 半步 B(?: — ✅ 已落地待复审（2026-07-01）)*$",
                "周 7：L68 附录 C + 降泄漏 + L69 复习桥 + log 域 + 半步 B — ✅ 已落地待复审（2026-07-01）",
            ),
            (
                r"^周 8：L69 三段 TODO 验证 \+ 边界 \+ week-04-checklist \+ L66/L67/L70 衔接(?: — ✅ 已落地待复审（2026-07-01）)*$",
                "周 8：L69 三段 TODO 验证 + 边界 + week-04-checklist + L66/L67/L70 衔接 — ✅ 已落地待复审（2026-07-01）",
            ),
        ],
    )


def _update_index_plan() -> bool:
    return _replace_text_regex(
        INDEX_PLAN,
        [
            (
                r"^> \*\*状态\*\*：(?:📋 下一步计划（2026-07-01）|🟡 执行中（2026-07-01）(?:— DSP / ML / ASR 三份分计划已落地待复审)+)$",
                "> **状态**：🟡 执行中（2026-07-01）— DSP / ML / ASR 三份分计划已落地待复审",
            ),
            (
                r"^\| \[`ml-gap-supplement-plan\.md`\]\(ml-gap-supplement-plan\.md\) \| \*\*Phase 2\*\* \| L22–L25、L53–L58 \| \*\*L53→L54\*\*（全课最陡，Δ=3） \| (?:📋 待落地|🟡 已落地待复审) \|$",
                "| [`ml-gap-supplement-plan.md`](ml-gap-supplement-plan.md) | **Phase 2** | L22–L25、L53–L58 | **L53→L54**（全课最陡，Δ=3） | 🟡 已落地待复审 |",
            ),
            (
                r"^\| \[`asr-gap-supplement-plan\.md`\]\(asr-gap-supplement-plan\.md\) \| \*\*Phase 3\*\* \| L24、L27、L67–L71 \| \*\*L68→L69\*\*（数学密度最高） \| (?:📋 待落地|🟡 已落地待复审) \|$",
                "| [`asr-gap-supplement-plan.md`](asr-gap-supplement-plan.md) | **Phase 3** | L24、L27、L67–L71 | **L68→L69**（数学密度最高） | 🟡 已落地待复审 |",
            ),
        ],
    )


def _update_deep_domain() -> bool:
    text = DEEP_DOMAIN.read_text(encoding="utf-8")
    if "## 跃升点导航" in text:
        return False
    needle = "Terms drawn from module 6 (Deep Learning, L54–L65).\n\n---\n\n"
    nav_block = dedent(
        """
        ## 跃升点导航

        - `L53` → `L54`：[[../../../notebooks/5_audio_dsp/L53_visual_mfcc.ipynb|L53 附录 A：前向特征 → 反向学习]] → [[../../../notebooks/6_deep_learning/L54_value_autograd.ipynb|L54 复习桥 · L24 链式法则]]
        - `L54` → `L55` → `L58` → `L59`：[[../../../notebooks/6_deep_learning/L54_value_autograd.ipynb|L54 模式对照表]] → [[../../../notebooks/6_deep_learning/L55_forward_pass.ipynb|L55 开篇回调]] → [[../../../notebooks/6_deep_learning/L58_training_loop.ipynb|L58 零件清点]] → [[../../../notebooks/6_deep_learning/L59_tensor_basics.ipynb|L59 模式切换]]
        - Tags: `#跃升点` `#面试高频`

        ---
        """
    ).strip()
    if needle not in text:
        raise RuntimeError("deep-learning domain anchor not found")
    new_text = text.replace(needle, f"Terms drawn from module 6 (Deep Learning, L54–L65).\n\n---\n\n{nav_block}\n\n", 1)
    return _write_text_if_changed(DEEP_DOMAIN, new_text)


def _update_asr_domain() -> bool:
    text = ASR_DOMAIN.read_text(encoding="utf-8")
    if "## 跃升点导航" in text:
        return False
    needle = "Terms drawn from module 7 (ASR, L66–L75).\n\n---\n\n"
    nav_block = dedent(
        """
        ## 跃升点导航

        - `L67` → `L68` → `L69` → `L70`：[[../../../notebooks/7_asr/L67_edit_distance.ipynb|L67 编辑距离]] → [[../../../notebooks/7_asr/L68_ctc_alignment.ipynb|L68 附录 C：L69 预习]] → [[../../../notebooks/7_asr/L69_ctc_forward.ipynb|L69 复习桥]] → [[../../../notebooks/7_asr/L70_whisper_arch.ipynb|L70 Whisper 架构解析]]
        - Tags: `#跃升点` `#面试高频`

        ---
        """
    ).strip()
    if needle not in text:
        raise RuntimeError("asr domain anchor not found")
    new_text = text.replace(needle, f"Terms drawn from module 7 (ASR, L66–L75).\n\n---\n\n{nav_block}\n\n", 1)
    return _write_text_if_changed(ASR_DOMAIN, new_text)


def main() -> int:
    updates = [
        _update_l52(),
        _update_l53(),
        _update_l24(),
        _update_l25(),
        _update_l30(),
        _update_l54(),
        _update_l55(),
        _update_l58(),
        _update_l59(),
        _update_l66(),
        _update_l67(),
        _update_l68(),
        _update_l69(),
        _update_l70(),
        _update_ml_solutions(),
        _update_asr_solutions(),
        _update_ml_plan(),
        _update_asr_plan(),
        _update_index_plan(),
        _update_deep_domain(),
        _update_asr_domain(),
    ]
    if any(updates):
        print("Applied remaining ML / ASR supplement updates.")
    else:
        print("No changes needed; ML / ASR supplement already applied.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
