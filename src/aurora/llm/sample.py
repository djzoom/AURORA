"""aurora.llm.sample — decoding strategies for autoregressive language models."""
import numpy as np


def softmax(logits: np.ndarray, temperature: float = 1.0) -> np.ndarray:
    """Numerically stable softmax with temperature scaling.

    temperature < 1  → sharper distribution (more confident / greedy-like)
    temperature > 1  → flatter distribution (more random / exploratory)
    temperature → 0  → equivalent to argmax
    temperature → ∞  → uniform distribution
    """
    logits = np.asarray(logits, dtype=np.float64)
    logits = logits / max(float(temperature), 1e-8)
    logits -= logits.max()  # subtract max for numerical stability before exp
    exp = np.exp(logits)
    return exp / exp.sum()


def greedy_decode(logits: np.ndarray) -> int:
    """Pick the single token with the highest logit (deterministic)."""
    return int(np.argmax(logits))


def top_k_sample(logits: np.ndarray, k: int = 50, temperature: float = 1.0) -> int:
    """Sample from the top-k highest-logit tokens.

    Algorithm:
      1. Keep only the k tokens with the largest logits; set the rest to -inf.
      2. Apply temperature scaling and softmax.
      3. Draw one sample from the resulting categorical distribution.

    k=1 is equivalent to greedy decoding.
    k=vocab_size is equivalent to unconstrained sampling.
    """
    logits = np.asarray(logits, dtype=np.float64)
    k = max(1, min(k, len(logits)))
    top_idx = np.argpartition(logits, -k)[-k:]
    masked = np.full_like(logits, -np.inf)
    masked[top_idx] = logits[top_idx]
    probs = softmax(masked, temperature)
    return int(np.random.choice(len(probs), p=probs))


def top_p_sample(logits: np.ndarray, p: float = 0.9, temperature: float = 1.0) -> int:
    """Nucleus sampling: sample from the smallest set of tokens summing to probability p.

    Algorithm (Holtzman et al. 2020 "The Curious Case of Neural Text Degeneration"):
      1. Sort tokens by probability descending.
      2. Find the minimal prefix whose cumulative probability ≥ p.
      3. Renormalise the nucleus and sample.

    The nucleus adapts to model confidence: high-confidence → small nucleus;
    uncertain → larger nucleus, naturally injecting more diversity when needed.
    """
    logits = np.asarray(logits, dtype=np.float64)
    probs = softmax(logits, temperature)
    sorted_idx = np.argsort(probs)[::-1]
    sorted_probs = probs[sorted_idx]
    cumulative = np.cumsum(sorted_probs)
    cutoff = int(np.searchsorted(cumulative, p)) + 1
    cutoff = max(1, min(cutoff, len(sorted_idx)))
    nucleus_idx = sorted_idx[:cutoff]
    nucleus_probs = probs[nucleus_idx]
    nucleus_probs = nucleus_probs / nucleus_probs.sum()  # renormalise
    return int(np.random.choice(nucleus_idx, p=nucleus_probs))
