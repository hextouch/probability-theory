"""
Bayesian update for a binomial likelihood with a Beta prior
"""
import numpy as np
from scipy.stats import beta

# Prior: Beta(2,2)
a_prior, b_prior = 2, 2
# Data: 7 successes, 3 failures
successes, failures = 7, 3
a_post = a_prior + successes
b_post = b_prior + failures
print(f"Posterior Beta parameters: a={a_post}, b={b_post}")
