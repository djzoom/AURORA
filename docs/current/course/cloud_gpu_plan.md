# 云 GPU 配置与训练教学内容规划

> 纳入课程节点：在 L93（MLOps）中新增「云 GPU 实战」章节；
> L72（Whisper 微调）和 L64（KWS 训练）在练习说明中添加「云环境前置检查」引用。

---

## 一、课程定位

| 课节 | 内容 | GPU 需求 |
|------|------|---------|
| L64  | KWS 训练循环（CNN）| 可用 Colab 免费 T4，~10 min |
| L72  | Whisper-small 微调 | 需 A100/H100，~2–4 h，建议 RunPod/Lambda |
| L93  | MLOps 实战（**新增云GPU章节**）| 演示环境，任意 T4 可 |

---

## 二、L93 新增「云 GPU 实战」章节提纲

### Cell A · 为什么需要云 GPU（Markdown）
- 本地 CPU 训练 Speech Commands（35k 音频）需 ~2h；T4 需 ~8 min
- Whisper fine-tune 在 CPU 不现实（16GB A100 训练 LibriSpeech 子集 ~1h）
- 费用参考：RunPod T4 $0.14/h，A100 $1.99/h；Colab Pro+ $12/月无限 A100 优先

### Cell B · 环境对比（Markdown 表格）
| 平台 | 免费层 | 计费层 | 适合任务 |
|------|--------|--------|---------|
| Google Colab | T4 / 12h | Pro+ A100 | 小实验、快速原型 |
| RunPod | — | 按秒计费，spot 可 5折 | Whisper 微调 |
| Lambda Labs | — | 稳定时租，$1.10/h A10 | 长时训练 |
| Kaggle | 30h/wk T4/P100 | — | 竞赛数据集直接访问 |

### Cell C · Colab 快速接入（Code）
```python
# 检测 GPU 类型和显存
import subprocess
result = subprocess.run(['nvidia-smi', '--query-gpu=name,memory.total',
                        '--format=csv,noheader'], capture_output=True, text=True)
print(result.stdout or "❌ 未检测到 GPU，请在 Colab 菜单选 Runtime → Change runtime type → T4")
```

### Cell D · 复现 Aurora 环境（Code + Markdown）
```bash
# Colab / RunPod 首次设置（在 !shell 格运行）
!git clone https://github.com/djzoom/AURORA.git && cd AURORA
!pip install -e ".[dev,notebooks]" -q
!python scripts/validate_pipeline.py --pipeline   # 验证 aurora.audio 可用
```

### Cell E · 数据同步策略（Markdown + Code）
- **Colab**：`from google.colab import drive; drive.mount('/content/drive')`
- **RunPod**：`rsync -avz --progress ./data/ user@host:/workspace/data/`
- **HuggingFace datasets**：`datasets.load_dataset("speech_commands", "v0.02")`（自动缓存）

```python
# 通用数据路径抽象（本地/云均可用）
import os
DATA_ROOT = os.getenv("AURORA_DATA", "./data")   # 云上设 env var 指向挂载目录
print(f"数据根目录: {DATA_ROOT}")
```

### Cell F · GPU 显存管理（Code）
```python
import torch

def gpu_status():
    if not torch.cuda.is_available():
        print("CPU 模式（训练会慢）")
        return
    name = torch.cuda.get_device_name(0)
    total = torch.cuda.get_device_properties(0).total_memory / 1e9
    used  = torch.cuda.memory_allocated(0) / 1e9
    print(f"GPU: {name} | 总显存: {total:.1f}GB | 已用: {used:.2f}GB")

gpu_status()

# 显存不够时的降级策略
BATCH_SIZE = 32 if torch.cuda.get_device_properties(0).total_memory > 10e9 else 8
USE_FP16   = torch.cuda.is_available()   # 自动半精度
```

### Cell G · 训练监控（W&B 接入）（Code）
```python
import wandb, os

wandb.login(key=os.getenv("WANDB_API_KEY"))   # RunPod: 设 env var；Colab: userdata.get()

run = wandb.init(
    project="aurora-kws",
    config={"batch_size": BATCH_SIZE, "lr": 1e-3, "epochs": 20}
)

# 训练循环内
for epoch in range(config.epochs):
    # ... train ...
    wandb.log({"train/loss": loss.item(), "val/acc": val_acc, "epoch": epoch})

wandb.finish()
```

### Cell H · 断点续训（Code）
```python
import torch
from pathlib import Path

CKPT = Path("checkpoints/kws_best.pt")

def save_checkpoint(model, optimizer, epoch, val_acc):
    torch.save({
        "epoch": epoch, "val_acc": val_acc,
        "model_state": model.state_dict(),
        "optim_state": optimizer.state_dict(),
    }, CKPT)

def load_checkpoint(model, optimizer):
    if CKPT.exists():
        ckpt = torch.load(CKPT, map_location="cuda" if torch.cuda.is_available() else "cpu")
        model.load_state_dict(ckpt["model_state"])
        optimizer.load_state_dict(ckpt["optim_state"])
        print(f"✅ 续训自 epoch {ckpt['epoch']}，val_acc={ckpt['val_acc']:.3f}")
        return ckpt["epoch"]
    return 0

start_epoch = load_checkpoint(model, optimizer)
```

### Cell I · 费用控制与 Spot Instance（Markdown）
- RunPod Spot：比 on-demand 便宜 40–60%，但可能被抢占 → 断点续训是必须的
- 估算 GPU-hours：`n_epochs × n_batches × forward_ms / 1000 / 3600`
- 预算告警：RunPod 支持自动停机；Colab 自动断开防止超用
- 示例：KWS 训练（Speech Commands，20 epoch，T4）≈ $0.02；Whisper 微调（1h A100）≈ $2

### Cell J · 验收 Checklist（Markdown + Code）
```python
# 云环境验收：运行完下面所有检查才算配置成功
checks = {
    "GPU 可用": torch.cuda.is_available(),
    "aurora.audio 可导入": True,   # validate_pipeline.py 已通过
    "W&B 已登录": wandb.api.api_key is not None,
    "数据集路径存在": Path(DATA_ROOT).exists(),
    "checkpoint 目录存在": Path("checkpoints").mkdir(exist_ok=True) or True,
}
for name, ok in checks.items():
    print(f"  {'✅' if ok else '❌'} {name}")
assert all(checks.values()), "请修复上方 ❌ 项后再继续"
```

---

## 三、L64 / L72 前置说明补充

**L64 末尾新增 Markdown cell**：
> 💡 本课训练循环在 CPU 上需 ~2h，建议在 Colab T4 完成。
> 配置步骤见 L93「云 GPU 实战」章节 Cell B–D。

**L72 开头新增 Markdown cell**：
> ⚠️ Whisper-small 微调需至少 8GB 显存（T4/A10/A100）。
> 本地 CPU 不可行。请先完成 L93 云 GPU 配置，再回到本课。
> 推荐平台：Colab Pro+（A100）或 RunPod（$1.99/h A100）。

---

## 四、实施顺序

1. **扩写 L93**（Cell A–J，约 10 个 cell）— 主要工作
2. **L64 末尾添加**提示 cell — 1 个 markdown cell
3. **L72 开头添加**前置警告 cell — 1 个 markdown cell
4. 更新 `notebooks/README.md` 中 L93 的描述行

