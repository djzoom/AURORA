"""ASR evaluation metrics — from-scratch, no external dependencies.

Implements:
  edit_distance(a, b)  — Levenshtein DP on any indexable sequence
  wer(reference, hypothesis)  — Word Error Rate delegating to edit_distance
"""

from __future__ import annotations

from typing import Sequence


def edit_distance(a: Sequence, b: Sequence) -> int:
    """Levenshtein edit distance between two indexable sequences.

    Works on strings (character-level) and word lists (word-level) alike.
    Space: O(n) — only two DP rows are kept at a time.

    Args:
        a: Source sequence (str or list).
        b: Target sequence (str or list).

    Returns:
        Minimum number of insertions, deletions, and substitutions to
        transform *a* into *b*.
    """
    m, n = len(a), len(b)
    # O(n) space optimisation: keep only the previous and current row.
    prev = list(range(n + 1))
    curr = [0] * (n + 1)
    for i in range(1, m + 1):
        curr[0] = i
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                curr[j] = prev[j - 1]
            else:
                curr[j] = 1 + min(prev[j], curr[j - 1], prev[j - 1])
        prev, curr = curr, prev
    return prev[n]


def wer(reference: str, hypothesis: str) -> float:
    """Word Error Rate = word-level edit distance / number of reference words.

    Delegates to :func:`edit_distance` on word lists — no duplicated DP loop.

    Args:
        reference:  Ground-truth transcript string.
        hypothesis: ASR output string.

    Returns:
        WER in [0, inf).  Returns 0.0 for two empty strings and
        ``float('inf')`` when *reference* is empty but *hypothesis* is not.
    """
    ref_words = reference.lower().split()
    hyp_words = hypothesis.lower().split()
    if len(ref_words) == 0:
        return 0.0 if len(hyp_words) == 0 else float("inf")
    return edit_distance(ref_words, hyp_words) / len(ref_words)


def corpus_wer(references: list[str], hypotheses: list[str]) -> float:
    """Corpus-level WER: total word errors / total reference words.

    Args:
        references:  List of ground-truth transcript strings.
        hypotheses:  List of ASR output strings (same length).

    Returns:
        Corpus WER in [0, inf).
    """
    if len(references) != len(hypotheses):
        raise ValueError("references and hypotheses must have the same length")
    total_errors = 0
    total_words = 0
    for ref, hyp in zip(references, hypotheses):
        ref_words = ref.lower().split()
        hyp_words = hyp.lower().split()
        total_words += len(ref_words)
        total_errors += edit_distance(ref_words, hyp_words)
    if total_words == 0:
        return 0.0
    return total_errors / total_words
