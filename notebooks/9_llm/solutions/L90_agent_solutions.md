# 参考实现 — L90_agent

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def podcast_qa(question, rag_index, chunks, embed_fn, llm, history=None):
    if history is None:
        history = []

    # 步骤 1：裁剪历史
    history = truncate_history(history, max_turns=5)

    # 步骤 2：检索最相关片段
    context_chunks = retrieve(question, rag_index, chunks, embed_fn, top_k=3)

    # 步骤 3：组装 prompt
    prompt = build_prompt(context_chunks, history, question)

    # 步骤 4：调用 LLM
    answer = llm.generate(prompt)

    # 步骤 5：格式化来源并返回
    sources = format_sources(context_chunks)
    return answer, sources
```

## 参考实现 2

`run_agent` —— 从零手写的 ReAct 循环（Thought → Action → Observation → … → Final Answer），
无任何 Agent 框架。循环体是真正的执行者：解析 LLM 吐出的 `Action: 工具名[输入]`，
调用对应 Python 函数，把返回值当作 `Observation:` 贴回草稿纸，直到出现 `Final Answer:`。

```python
import re

def run_agent(question, llm, tools, max_steps=5):
    scratchpad = f"Question: {question}\n"
    trace = []
    for _ in range(max_steps):
        # 1. LLM 只决定"下一步做什么"
        step = llm.generate(scratchpad)
        scratchpad += step + "\n"
        trace.append(step)

        # 2. 若宣布最终答案，取其后文本返回
        if "Final Answer:" in step:
            answer = step.split("Final Answer:", 1)[1].strip()
            return answer, trace

        # 3. 否则解析 Action: 工具名[输入]，真正调用工具
        m = re.search(r"Action:\s*(\w+)\[(.*?)\]", step)
        if not m:
            raise RuntimeError(f"无法解析动作：{step!r}")
        tool_name, tool_input = m.group(1), m.group(2)
        if tool_name not in tools:
            observation = f"未知工具 {tool_name}"
        else:
            observation = tools[tool_name](tool_input)

        # 4. 把观察贴回草稿纸，进入下一轮
        obs_line = f"Observation: {observation}"
        scratchpad += obs_line + "\n"
        trace.append(obs_line)

    raise RuntimeError(f"超过 max_steps={max_steps} 仍未得到 Final Answer")
```

**要点**
- **谁在循环**：`llm.generate` 只产出"下一步"（一步 Thought+Action，或 Final Answer）；
  真正执行工具、拼接 Observation 的是循环体代码本身。这正是不用 langchain 也能讲清 Agent 的原因。
- **可复现**：`ScriptedReActLLM` 用"数 Observation 条数"代替语言理解来规划，
  配合从零的 `calculator` 与复用 TF-IDF 的 `search`，全程 CPU、离线、每次结果一致。
- **收敛保护**：`max_steps` 上限防止工具调用死循环——真实 Agent 同样必须有步数/预算上限。

