"""Aurora LLM Core — from-scratch LLM inference primitives.

Public API
----------
KVCache                  — key-value cache for autoregressive inference
softmax                  — temperature-scaled softmax
greedy_decode            — argmax decoding
top_k_sample             — top-k sampling
top_p_sample             — nucleus (top-p) sampling
build_tfidf              — TF-IDF index construction (pure NumPy, no faiss)
cosine_retrieve          — sparse retrieval by cosine similarity
tokenize                 — simple ASCII + CJK tokenizer
"""
from aurora.llm.kvcache import KVCache
from aurora.llm.sample import softmax, softmax_cross_entropy, greedy_decode, top_k_sample, top_p_sample
from aurora.llm.retrieve import build_tfidf, cosine_retrieve, tokenize

__all__ = [
    "KVCache",
    "softmax",
    "softmax_cross_entropy",
    "greedy_decode",
    "top_k_sample",
    "top_p_sample",
    "build_tfidf",
    "cosine_retrieve",
    "tokenize",
]
