"""
Maximum Likelihood Estimation (MLE) for normal distribution
"""
import numpy as np

np.random.seed(0)
data = np.random.normal(loc=2, scale=1, size=100)
mu_mle = np.mean(data)
sigma_mle = np.std(data, ddof=0)
print(f"MLE mean: {mu_mle:.2f}, MLE std: {sigma_mle:.2f}")
