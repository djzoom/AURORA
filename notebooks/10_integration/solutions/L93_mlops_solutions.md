# 参考实现 — L93_mlops

> ⚠️ 请先独立完成练习，再查看参考实现。

本课的动手练习是补全 `setup_experiment()`：接收一份超参配置字典，在 **disabled 模式**下
初始化一次 W&B run（不联网、不产生任何外部调用），并返回 run 对象供后续 `wandb.log()` 使用。

## 参考实现 — `setup_experiment()`

```python
def setup_experiment(cfg: dict):
    """
    初始化一次 W&B 实验 run（disabled 模式，无需联网）。

    参数：
        cfg: 超参配置字典，至少包含 'project'、'run_name'、'n_mels' 键
    返回：
        wandb.Run 对象；若环境未安装 wandb 则返回 None
    """
    # 用 HAS_WANDB 守卫：没装 wandb 时不应抛异常，直接返回 None
    if not HAS_WANDB:
        return None

    # mode='disabled' 让 wandb 完全离线：不建 run 目录、不联网、不上传，
    # 但 run.config / run.log() 接口照常可用，非常适合教学与 CI。
    run = wandb.init(
        project=cfg["project"],
        name=cfg["run_name"],
        config=cfg,          # 整份超参一次性写入 config，保证可复现
        mode="disabled",
    )
    return run
```

## 讲解

1. **为什么先判空 `HAS_WANDB`**：本课所有涉及 W&B 的代码都被 `HAS_WANDB` 守卫包裹，
   目的是让没装 `wandb` 的读者也能一路跑到结尾。`setup_experiment()` 遵循同样约定——
   缺库时返回 `None` 而不是抛 `ImportError`，把「是否继续」的决定权交给调用方。

2. **`mode="disabled"` 是关键**：它让 `wandb.init()` 不写本地 run 目录、不联网、不需要
   `WANDB_API_KEY`，因此在 notebook、单元测试、CI 里都能安全执行。若要真正上传，改成
   `mode="online"`（默认）并配置好 API key 即可，函数其余部分无需改动。

3. **`config=cfg` 一次性写入**：把学习率、`n_mels`、`batch_size` 等超参整体交给 `config`，
   之后可用 `run.config['n_mels']` 读回——这正是验证单元断言的字段，也是「实验可复现」的
   核心：超参与 run 绑定，不再散落在脚本各处。

4. **返回 run 对象**：训练循环里继续用它 `run.log({...})` 记录指标，结束时 `run.finish()`
   关闭。返回而非在函数内部消费，符合「初始化与使用分离」的工程习惯。

## 验证要点

`setup_experiment(test_cfg)` 后，验证单元会断言：

```python
assert run is not None
assert run.config['n_mels'] == test_cfg['n_mels']   # 64
assert run.config['lr']     == test_cfg['lr']        # 1e-3
```

即 config 中的超参能被原样读回。注意：只有在 `HAS_WANDB` 为真时验证单元才会执行；
未安装 `wandb` 的环境会打印「跳过」提示并直接通过——这是刻意设计，确保本课**无外部依赖也能整篇跑通**。

## 延伸练习

- 把 `mode` 提成 `setup_experiment(cfg, mode="disabled")` 参数，让同一函数既能离线演示、
  又能在真机上联网上传。
- 在返回前追加 `run.define_metric("val_acc", summary="max")`，让 Dashboard 自动记录最优
  `val_acc`，配合本课第 3 节的 grid search 对比使用。
