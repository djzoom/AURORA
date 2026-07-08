# 老陈 — L70 学习日志

## 我理解了什么

Whisper 把整个语音识别流水线压缩成一个架构：**音频 → 80维log-Mel特征 → 卷积+Transformer编码 → Transformer解码器 → BPE token**。最绝的是一个模型用不同前缀token（如`<transcribe>`、`<translate>`）就能完成多个任务，不需要多个模型。

我也看懂了编码器的三个层级：固定30秒输入 → 两层卷积降采样2倍（3000→1500帧） → Transformer处理1500步的上下文向量。

## 遇到的困难和问题

### 【理解】为什么要固定30秒且恰好降采样到1500步
课程说"固定30秒窗口统一输入形状"，这我懂。但为什么不是20秒或40秒？为什么降采样后必须是1500步？只是巧合吗，还是有算力/性能的考量？降采样2倍（而不是3倍或4倍）对解码器的计算量有什么具体影响？

### 【理解】log-Mel归一化为什么这样设计
notebook第8个cell给出了这个公式：
```python
log_mel = log10(max(mel_power, 1e-10))
log_mel = max(log_mel, log_mel.max() - 8.0)
log_mel = (log_mel + 4.0) / 4.0
```
我理解第一行是压缩动态范围。但第二行"max(log_mel, log_mel.max() - 8.0)"——这是在做什么？为什么是减8.0而不是减10.0？最后为什么加4.0再除4.0才能得到[-1, 1]？这个公式怎么推导出来的？

### 【推演】Conv1d输出公式的来源
cell 20演示了这个公式：
```python
def conv1d_out(L_in, kernel, stride=1, padding=1):
    return (L_in + 2*padding - kernel) // stride + 1
```
我没学过CNN，不知道这个公式怎么来的。为什么是 `+2*padding` 而不是其他？为什么要减kernel再除stride？能从几何角度解释一遍吗？

### 【理解】Conv1d第一层为什么stride=1、第二层stride=2
课程说"Conv1d层1保持3000帧，层2压缩到1500帧"，我看代码确实是这样。但这个设计选择是怎么来的？为什么不干脆在第一层就用stride=2，然后第二层stride=1？或者两层都stride=2？这样设计对性能/质量有什么影响吗？

### 【理解】自注意力 vs 交叉注意力
notebook有cross-attention的代码示意，我看到了Q来自decoder、K/V来自encoder。但为什么要这样设计？跟自注意力相比有什么优势？decoder为什么要"看"所有1500步的encoder输出？如果只看最相关的几步会怎样？

### 【推演】scaled dot-product attention中的scale是怎么来的
cell 13代码里有 `scale = head_dim ** 0.5`，然后用这个scale除以attention weight。为什么是 `sqrt(d_k)` 而不是 `d_k` 或其他值？为什么要缩放？如果不缩放会发生什么？

### 【理解】多任务头的token前缀为什么有效
notebook第14个cell说用不同前缀token就能让同一个模型做转写/翻译/语言识别。但模型怎么"知道"prefix中的`<transcribe>`意思是"我要做转写而不是翻译"？是因为training data里混了这些label吗？那validation set如果给反了前缀会发生什么？

### 【实践】whisper_preprocess实现的细节问题
步骤2要做"log归一化"，但课程只说了Whisper风格的公式。`power_to_db`是Aurora自己的函数，我需要在它输出的基础上再做Whisper风格的归一化吗？还是我应该直接用np.log10代替power_to_db？

还有，步骤3说"pad或truncate到3000帧"，但mel_spectrogram因为center=True会返回3001帧。我应该先转置到(80, 3001)，然后截掉最后1帧到(80, 3000)？还是有其他顺序？

### 【计算】30秒→3000帧的除法为什么这样算
30秒×16kHz=480000样本，hop=160→480000÷160=3000帧。我理解这是说每160个采样点产生1帧。但为什么hop=160恰好产生3000帧而不是任意数字？这是设计者故意选的吗？

### 【理解】PyTorch和NumPy的shape格式混乱
mel_spectrogram返回(T, 80)（时间在行），但PyTorch Conv1d期望(B, C, T)（时间在最后）。所以要.T转置成(80, T)。但在notebook的几个cell里，有时候是(B, channels, time)有时候是(B, time, channels)。什么时候用哪种格式？有没有一个统一的规则？
