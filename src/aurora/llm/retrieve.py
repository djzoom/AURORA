"""aurora.llm.retrieve — TF-IDF sparse retrieval, pure Python + NumPy.

No faiss. No sentence-transformers. No pretrained models.
"""
import numpy as np
import re
from collections import Counter


def tokenize(text: str) -> list:
    """Whitespace + punctuation tokenizer supporting CJK and ASCII."""
    return re.findall(r"[a-zA-Z]+|[一-鿿]", text.lower())


def build_tfidf(docs: list) -> tuple:
    """Build a TF-IDF matrix for a list of documents.

    TF(t,d)  = count(t in d) / len(d)              (relative frequency)
    IDF(t)   = log((N+1) / (df(t)+1)) + 1          (smoothed to avoid zero)
    TF-IDF   = TF × IDF

    Args:
        docs: list of raw document strings.

    Returns:
        (matrix, vocab):
          matrix — (n_docs, vocab_size) float32 TF-IDF matrix
          vocab  — list of terms in column order
    """
    tokenized = [tokenize(d) for d in docs]
    all_terms = sorted({t for tokens in tokenized for t in tokens})
    word_idx = {w: i for i, w in enumerate(all_terms)}

    tf = np.zeros((len(docs), len(all_terms)), dtype=np.float32)
    for i, tokens in enumerate(tokenized):
        counts = Counter(tokens)
        total = max(len(tokens), 1)
        for word, count in counts.items():
            if word in word_idx:
                tf[i, word_idx[word]] = count / total

    df = (tf > 0).sum(axis=0).astype(np.float32)
    N = len(docs)
    idf = np.log((N + 1.0) / (df + 1.0)) + 1.0  # smoothed IDF

    return (tf * idf), all_terms


def cosine_retrieve(
    query: str,
    tfidf_matrix: np.ndarray,
    vocab: list,
    docs: list,
    top_k: int = 3,
) -> list:
    """Retrieve top-k documents by TF-IDF cosine similarity.

    Args:
        query:         raw query string.
        tfidf_matrix:  (n_docs, vocab_size) from build_tfidf().
        vocab:         list of terms from build_tfidf().
        docs:          original document strings.
        top_k:         number of results to return.

    Returns:
        List of (doc_string, score) tuples, sorted by descending similarity.
    """
    word_idx = {w: i for i, w in enumerate(vocab)}
    tokens = tokenize(query)
    counts = Counter(tokens)
    total = max(len(tokens), 1)

    q_vec = np.zeros(len(vocab), dtype=np.float32)
    for word, count in counts.items():
        if word in word_idx:
            q_vec[word_idx[word]] = count / total

    q_norm = float(np.linalg.norm(q_vec))
    if q_norm < 1e-8:
        return [(docs[i], 0.0) for i in range(min(top_k, len(docs)))]

    d_norms = np.linalg.norm(tfidf_matrix, axis=1).astype(np.float32)
    d_norms = np.maximum(d_norms, 1e-8)
    scores = (tfidf_matrix @ q_vec) / (d_norms * q_norm)

    k = min(top_k, len(docs))
    part = np.argpartition(scores, -k)[-k:]
    order = np.argsort(scores[part])[::-1]
    idx = part[order]
    return [(docs[i], float(scores[i])) for i in idx]
