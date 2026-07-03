# 参考实现 — L01_motivation

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

`check_imports`：用 `importlib.util.find_spec` 检测每个包是否可导入。

```python
import importlib.util

def check_imports(names):
    """检测一组包是否可导入。返回 {包名: bool} 字典。"""
    result = {}
    for name in names:
        result[name] = importlib.util.find_spec(name) is not None
    return result
```

## 参考实现 2

`environment_report`：从当前目录逐级向上找到含 `pyproject.toml` 的项目根，
汇总解释器路径、版本、`aurora` 可用性与项目根。

```python
import sys
from pathlib import Path

def environment_report():
    """返回当前运行环境的快照字典。"""
    root = None
    for folder in [Path.cwd(), *Path.cwd().parents]:
        if (folder / 'pyproject.toml').exists():
            root = folder
            break
    return {
        'python_executable': sys.executable,
        'python_version':    sys.version,
        'aurora_available':  check_imports(['aurora'])['aurora'],
        'project_root':      str(root),
    }
```
