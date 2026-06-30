"""Tests for aurora.llm.kvcache."""
import numpy as np
import pytest
from aurora.llm.kvcache import KVCache


def make_kv(n_heads, head_dim):
    rng = np.random.default_rng(0)
    k = rng.standard_normal((n_heads, 1, head_dim))
    v = rng.standard_normal((n_heads, 1, head_dim))
    return k, v


def test_init():
    cache = KVCache(n_heads=4, head_dim=64)
    assert cache.n_heads == 4
    assert cache.head_dim == 64


def test_first_update_returns_one_token():
    cache = KVCache(n_heads=2, head_dim=8)
    k, v = make_kv(2, 8)
    k_out, v_out = cache.update(layer=0, new_k=k, new_v=v)
    assert k_out.shape == (2, 1, 8)
    assert v_out.shape == (2, 1, 8)


def test_cache_grows_with_tokens():
    cache = KVCache(n_heads=2, head_dim=8)
    for step in range(5):
        k, v = make_kv(2, 8)
        k_out, v_out = cache.update(layer=0, new_k=k, new_v=v)
        assert k_out.shape[1] == step + 1, f"step {step}: expected seq_len={step+1}"


def test_multiple_layers_independent():
    cache = KVCache(n_heads=2, head_dim=8)
    for layer in range(3):
        k, v = make_kv(2, 8)
        cache.update(layer=layer, new_k=k, new_v=v)

    # Adding a second token to layer 0 should not affect layers 1/2
    k2, v2 = make_kv(2, 8)
    k0_out, _ = cache.update(layer=0, new_k=k2, new_v=v2)
    assert k0_out.shape[1] == 2

    k1_out, _ = cache.update(layer=1, new_k=k2, new_v=v2)
    assert k1_out.shape[1] == 2


def test_values_preserved():
    cache = KVCache(n_heads=1, head_dim=4)
    k1 = np.ones((1, 1, 4))
    v1 = np.ones((1, 1, 4)) * 2
    k2 = np.ones((1, 1, 4)) * 3
    v2 = np.ones((1, 1, 4)) * 4

    cache.update(layer=0, new_k=k1, new_v=v1)
    k_out, v_out = cache.update(layer=0, new_k=k2, new_v=v2)

    assert np.allclose(k_out[0, 0], 1.0)
    assert np.allclose(k_out[0, 1], 3.0)
    assert np.allclose(v_out[0, 0], 2.0)
    assert np.allclose(v_out[0, 1], 4.0)


def test_accumulated_values_match_concatenation():
    """KVCache must produce identical output to manual np.concatenate along seq dim."""
    cache = KVCache(n_heads=2, head_dim=8)
    rng = np.random.default_rng(42)

    k_tokens, v_tokens = [], []
    for _ in range(5):
        k_new = rng.standard_normal((2, 1, 8))
        v_new = rng.standard_normal((2, 1, 8))
        k_tokens.append(k_new)
        v_tokens.append(v_new)
        k_out, v_out = cache.update(layer=0, new_k=k_new, new_v=v_new)

    k_ref = np.concatenate(k_tokens, axis=1)  # (2, 5, 8)
    v_ref = np.concatenate(v_tokens, axis=1)

    assert k_out.shape == k_ref.shape, f"K shape {k_out.shape} != {k_ref.shape}"
    assert np.allclose(k_out, k_ref, atol=1e-12), "K cache differs from np.concatenate reference"
    assert np.allclose(v_out, v_ref, atol=1e-12), "V cache differs from np.concatenate reference"
