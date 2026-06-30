"""Tests for aurora.llm.retrieve — TF-IDF sparse retrieval."""
import numpy as np

from aurora.llm.retrieve import build_tfidf, cosine_retrieve, tokenize

DOCS = [
    "the cat sat on the mat",
    "the dog ran in the park",
    "cats and dogs are common pets",
    "the park has green grass and trees",
]


def test_tokenize_basic():
    tokens = tokenize("Hello world, foo-bar")
    assert "hello" in tokens
    assert "world" in tokens


def test_build_tfidf_shape():
    matrix, vocab = build_tfidf(DOCS)
    assert matrix.shape[0] == len(DOCS)
    assert matrix.shape[1] == len(vocab)


def test_tfidf_non_negative():
    matrix, _ = build_tfidf(DOCS)
    assert np.all(matrix >= 0)


def test_query_returns_ranked_results():
    matrix, vocab = build_tfidf(DOCS)
    results = cosine_retrieve("cat sat mat", matrix, vocab, DOCS, top_k=2)
    assert len(results) == 2
    # Doc 0 ("the cat sat on the mat") should rank highest
    # cosine_retrieve returns (doc_text, score) tuples
    top_doc = results[0][0] if isinstance(results[0], tuple) else results[0]
    assert any(w in top_doc for w in ("cat", "sat", "mat")), \
        f"Expected doc with cat/sat/mat, got: {top_doc}"


def test_query_top_k_respected():
    matrix, vocab = build_tfidf(DOCS)
    for k in [1, 2, 3]:
        results = cosine_retrieve("dog park", matrix, vocab, DOCS, top_k=k)
        assert len(results) == k


def test_unknown_query_returns_results():
    matrix, vocab = build_tfidf(DOCS)
    # Query with OOV terms should not crash
    results = cosine_retrieve("xyzzy unicorn", matrix, vocab, DOCS, top_k=2)
    assert len(results) == 2
