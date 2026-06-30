"""Tests for aurora.llm.sample — decoding strategies."""
import numpy as np
import pytest
from aurora.llm.sample import softmax, greedy_decode, top_k_sample, top_p_sample


def test_softmax_sums_to_one():
    logits = np.array([1.0, 2.0, 3.0])
    probs = softmax(logits)
    assert abs(probs.sum() - 1.0) < 1e-9
    assert np.all(probs >= 0)


def test_softmax_temperature_high_flattens():
    logits = np.array([10.0, 0.0, 0.0])
    p_low = softmax(logits, temperature=0.1)
    p_high = softmax(logits, temperature=10.0)
    # high temperature → more uniform
    assert p_high.max() < p_low.max()
    assert p_high.min() > p_low.min()


def test_greedy_decode_returns_argmax():
    logits = np.array([0.1, 5.0, 0.3])
    assert greedy_decode(logits) == 1


def test_top_k_restricts_vocab():
    logits = np.arange(100, dtype=float)
    k = 5
    samples = [top_k_sample(logits, k=k) for _ in range(200)]
    # All samples must come from top-k indices (95..99)
    top_k_indices = set(range(95, 100))
    assert all(s in top_k_indices for s in samples), \
        f"top_k_sample sampled outside top-{k}: {set(samples) - top_k_indices}"


def test_top_p_within_mass():
    # Concentrated distribution: token 0 has 90%+ mass
    logits = np.array([10.0, 1.0, 0.5, 0.1, 0.1])
    samples = [top_p_sample(logits, p=0.95) for _ in range(500)]
    # Token 0 should dominate
    assert samples.count(0) > 300, "token 0 should be sampled most often"


def test_top_k_k1_is_greedy():
    logits = np.array([1.0, 9.0, 2.0])
    samples = [top_k_sample(logits, k=1) for _ in range(20)]
    assert all(s == 1 for s in samples), "k=1 should always pick argmax"
