"""
KL divergence between two discrete distributions
"""
import numpy as np

def kl_divergence(p, q):
    p = np.array(p)
    q = np.array(q)
    mask = (p > 0) & (q > 0)
    return np.sum(p[mask] * np.log2(p[mask] / q[mask]))

p = [0.4, 0.6]
q = [0.5, 0.5]
print(f"KL divergence D(p||q): {kl_divergence(p, q):.3f} bits")
