"""
Cross-entropy loss between true and predicted distributions
"""
import numpy as np

def cross_entropy(p, q):
    p = np.array(p)
    q = np.array(q)
    mask = (p > 0) & (q > 0)
    return -np.sum(p[mask] * np.log2(q[mask]))

p = [1, 0, 0]
q = [0.7, 0.2, 0.1]
print(f"Cross-entropy loss: {cross_entropy(p, q):.3f} bits")
