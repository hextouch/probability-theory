"""
Shannon entropy of a discrete distribution
"""
import numpy as np

def entropy(p):
    p = np.array(p)
    p = p[p > 0]
    return -np.sum(p * np.log2(p))

p = [0.5, 0.25, 0.25]
print(f"Entropy: {entropy(p):.3f} bits")
