# 参考实现 — L72_whisper_finetune

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

练习 1：LoRA 参数量计算（对应练习代码单元格 `d_model=512, r=16, num_matrices=3`）。

```python
# ─── 练习 1：LoRA 参数量计算 ───────────────────────────────────────────
d_model = 512
r = 16
num_matrices = 3  # q_proj, k_proj, v_proj

original_params_per_matrix = d_model * d_model          # 512×512 = 262144
lora_params_per_matrix = 2 * d_model * r                # A(d×r)+B(r×d) = 2×512×16 = 16384
total_lora_params = num_matrices * lora_params_per_matrix        # 3×16384 = 49152
total_original_params = num_matrices * original_params_per_matrix  # 3×262144 = 786432
reduction_pct = (1 - total_lora_params / total_original_params) * 100  # ≈ 93.75%

expected_lora = 3 * 2 * 512 * 16  # = 49152
expected_reduction = (1 - expected_lora / (3 * 512 * 512)) * 100  # ≈ 93.75%
assert total_lora_params == expected_lora, f'参数量错误: {total_lora_params}'
assert abs(reduction_pct - expected_reduction) < 0.01, f'降幅错误: {reduction_pct:.2f}%'
print(f'✅ LoRA 参数量: {total_lora_params:,}，降幅 {reduction_pct:.1f}%')
```

## 参考实现 2

练习 2：不依赖 `jiwer` 的简化 WER（词级编辑距离 / 参考词数）。

```python
# ─── 练习 2：不依赖 jiwer 的简化 WER ────────────────────────────────────
def simple_wer(ref: str, hyp: str) -> float:
    """单句词级 WER（编辑距离 / 参考词数），不使用 jiwer。
    ref / hyp 为普通字符串，内部按空格分词。
    """
    r = ref.split()
    h = hyp.split()
    n, m = len(r), len(h)
    # dp[i][j] = r[:i] 变成 h[:j] 的最小编辑距离
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i          # 删除 i 个词
    for j in range(m + 1):
        dp[0][j] = j          # 插入 j 个词
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if r[i - 1] == h[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]           # 匹配，无代价
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # 删除
                    dp[i][j - 1],      # 插入
                    dp[i - 1][j - 1],  # 替换
                )
    # WER = 编辑距离 / 参考词数（ref 为空时按 0 词处理，避免除零）
    return dp[n][m] / max(n, 1)


# 验证
try:
    result = simple_wer("the cat sat on the mat", "the cat sat on a mat")
    assert abs(result - 1/6) < 1e-6, f'WER 错误: {result}'
    print(f'✅ simple_wer 通过: WER = {result:.4f}')
except (NotImplementedError, TypeError):
    print('⏳ 尚未实现 simple_wer，完成 TODO 后重新运行')

# 验收标准自检
assert simple_wer("hello world", "hello world") == 0.0
assert simple_wer("hello world", "hello") == 0.5           # 删 1 词 / 2 词
assert abs(simple_wer("a b c", "x b c") - 1/3) < 1e-9      # 替 1 词 / 3 词
assert simple_wer("good", "this is very very good") == 4.0  # 插 4 词 / 1 词，WER > 1
```
