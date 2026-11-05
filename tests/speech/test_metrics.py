"""Tests for edit distance and WER."""

import pytest

from aurora.speech import corpus_wer, edit_distance, wer


def test_edit_distance_classic_cases():
    assert edit_distance("kitten", "sitting") == 3
    assert edit_distance("", "abc") == 3
    assert edit_distance("abc", "abc") == 0
    assert edit_distance(["a", "b"], ["b"]) == 1


def test_edit_distance_is_symmetric():
    assert edit_distance("flaw", "lawn") == edit_distance("lawn", "flaw")


def test_wer_basic():
    assert wer("the cat sat", "the cat sat") == 0.0
    assert wer("the cat sat", "the cat") == pytest.approx(1 / 3)
    assert wer("the cat sat", "the dog sat") == pytest.approx(1 / 3)
    assert wer("THE CAT", "the cat") == 0.0  # case-insensitive


def test_wer_empty_reference():
    assert wer("", "") == 0.0
    assert wer("", "hello") == float("inf")


def test_corpus_wer_pools_errors():
    refs = ["a b c d", "e f"]
    hyps = ["a b c", "e f g"]  # 1 deletion + 1 insertion over 6 words
    assert corpus_wer(refs, hyps) == pytest.approx(2 / 6)
    with pytest.raises(ValueError):
        corpus_wer(["a"], [])
