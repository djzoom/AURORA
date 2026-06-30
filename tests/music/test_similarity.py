"""Tests for aurora.music.similarity — cosine similarity and k-NN search."""
import numpy as np
import pytest
from aurora.music.similarity import cosine_similarity, pairwise_cosine, knn_search, find_similar


def test_cosine_similarity_identical():
    v = np.array([1.0, 2.0, 3.0])
    assert abs(cosine_similarity(v, v) - 1.0) < 1e-9


def test_cosine_similarity_orthogonal():
    a = np.array([1.0, 0.0])
    b = np.array([0.0, 1.0])
    assert abs(cosine_similarity(a, b)) < 1e-9


def test_cosine_similarity_opposite():
    v = np.array([1.0, 0.0])
    assert abs(cosine_similarity(v, -v) + 1.0) < 1e-9


def test_cosine_similarity_range():
    rng = np.random.default_rng(0)
    for _ in range(20):
        a = rng.standard_normal(16)
        b = rng.standard_normal(16)
        sim = cosine_similarity(a, b)
        assert -1.0 - 1e-9 <= sim <= 1.0 + 1e-9


def test_cosine_similarity_zero_vector():
    v = np.array([1.0, 2.0, 3.0])
    zero = np.zeros(3)
    assert cosine_similarity(v, zero) == 0.0
    assert cosine_similarity(zero, zero) == 0.0


def test_pairwise_cosine_shape():
    X = np.random.randn(5, 8)
    sim = pairwise_cosine(X)
    assert sim.shape == (5, 5)


def test_pairwise_cosine_diagonal_ones():
    X = np.random.randn(4, 8)
    sim = pairwise_cosine(X)
    assert np.allclose(np.diag(sim), 1.0, atol=1e-6)


def test_pairwise_cosine_symmetric():
    X = np.random.randn(4, 8)
    sim = pairwise_cosine(X)
    assert np.allclose(sim, sim.T, atol=1e-9)


def test_knn_search_returns_k():
    db = np.random.randn(20, 8)
    q = np.random.randn(8)
    idx, scores = knn_search(q, db, k=5)
    assert len(idx) == 5
    assert len(scores) == 5


def test_knn_search_descending_order():
    db = np.random.randn(20, 8)
    q = np.random.randn(8)
    _, scores = knn_search(q, db, k=5)
    assert np.all(scores[:-1] >= scores[1:]), "Scores should be non-increasing"


def test_knn_search_self_is_top():
    db = np.eye(5)   # 5 orthogonal unit vectors
    idx, scores = knn_search(db[2], db, k=1)
    assert idx[0] == 2
    assert abs(scores[0] - 1.0) < 1e-6


def test_find_similar_is_knn_alias():
    rng = np.random.default_rng(7)
    db = rng.standard_normal((10, 4))
    q = rng.standard_normal(4)
    idx1, s1 = knn_search(q, db, k=3)
    idx2, s2 = find_similar(q, db, k=3)
    assert np.array_equal(idx1, idx2)
    assert np.allclose(s1, s2)
