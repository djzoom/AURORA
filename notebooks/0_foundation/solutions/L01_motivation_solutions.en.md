# Reference implementations — L01_motivation

> ⚠️ Work through the exercises on your own first, then look at the reference implementations.

## Reference implementation 0 · Example answers for `course_purpose` (the Section 6 exercise)

This question has no single correct answer — what it tests is "can you connect each module to Aurora,"
not whether you can recite the roadmap. Below are two kinds of sample, so you know what "a passing answer" looks like.

**Sample A: the concrete version** (good for early-to-middle modules you already have some feel for) —
both X and Y in the sentence are pinned down, and Y always points to a specific thing in Aurora:

```python
'2_linear_algebra': 'I am learning linear algebra so I can see that the DFT is really just one matrix multiplication — '
                    'multiply a stretch of sound by a fixed table and you get its spectrum',
'5_audio_dsp':      'I am learning audio DSP so I can write FFT/STFT/Mel myself, '
                    'and build the "sound recipe table" at the input of Whisper from scratch',
```

**Sample B: the acceptable vague version** (good for modules like `8_music` and `9_llm` that you know almost nothing about yet) —
honestly note "I don't know yet," add a promise to "come back and rewrite this," and that's a passing answer:

```python
'8_music': 'I do not know yet what a music embedding is exactly, only that it can turn a song '
           'into a sequence of numbers; when I reach L76 I will come back and make this concrete',
```

**Two self-checks**:
1. Can you find X (what you're learning) and Y (what you'll do in Aurora) in the sentence? Y can't be empty talk like "build music-related features" —
   either pin it to something specific (Sample A), or honestly mark it "to be rewritten once I've learned it" (Sample B).
2. This list is a living document: each time you enter a new module, come back and upgrade its entry from Sample B to Sample A.

## Reference implementation 1

`check_imports`: use `importlib.util.find_spec` to check whether each package can be imported.

```python
import importlib.util

def check_imports(names):
    """Check whether a list of packages can be imported. Returns a {package name: bool} dict."""
    result = {}
    for name in names:
        result[name] = importlib.util.find_spec(name) is not None
    return result
```

## Reference implementation 2

`environment_report`: starting from the current directory, walk upward to find the project root containing `pyproject.toml`,
then gather the interpreter path, the version, whether `aurora` is available, and the project root.

```python
import sys
from pathlib import Path

def environment_report():
    """Return a snapshot dict of the current runtime environment."""
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
