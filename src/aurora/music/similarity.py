"""aurora.music.similarity — vector similarity and k-NN search, pure NumPy."""
import numpy as np


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    """Cosine similarity between two 1D vectors."""
    norm_a = float(np.linalg.norm(a))
    norm_b = float(np.linalg.norm(b))
    if norm_a < 1e-8 or norm_b < 1e-8:
        return 0.0
    return float(np.dot(a, b) / (norm_a * norm_b))


def pairwise_cosine(X: np.ndarray) -> np.ndarray:
    """(n, d) row-stacked embeddings → (n, n) cosine similarity matrix."""
    norms = np.linalg.norm(X, axis=1, keepdims=True)
    norms = np.maximum(norms, 1e-8)
    X_normed = X / norms
    return X_normed @ X_normed.T


def knn_search(query: np.ndarray, database: np.ndarray, k: int = 5) -> tuple:
    """k-nearest neighbours by cosine similarity, pure NumPy O(n·d).

    Args:
        query:    (d,) embedding vector.
        database: (n, d) embedding matrix.
        k:        number of neighbours to return.

    Returns:
        (indices, scores) — both (k,) arrays, sorted by descending similarity.
    """
    q_normed = query / (np.linalg.norm(query) + 1e-8)
    d_norms = np.linalg.norm(database, axis=1, keepdims=True)
    d_normed = database / (d_norms + 1e-8)
    scores = d_normed @ q_normed  # (n,)
    k = min(k, len(scores))
    # argpartition gives top-k in O(n); sorting k items is O(k log k)
    part = np.argpartition(scores, -k)[-k:]
    order = np.argsort(scores[part])[::-1]
    idx = part[order]
    return idx, scores[idx]


find_similar = knn_search  # notebook-facing alias (L80 teaches this name)
