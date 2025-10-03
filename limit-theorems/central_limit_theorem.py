import numpy as np
import matplotlib.pyplot as plt

def central_limit_theorem_demo(n_samples=1000, sample_size=30):
    means = [np.mean(np.random.uniform(0, 1, sample_size)) for _ in range(n_samples)]
    plt.hist(means, bins=30, density=True, alpha=0.7)
    plt.title('Central Limit Theorem Demo')
    plt.xlabel('Sample Mean')
    plt.ylabel('Density')
    plt.show()

if __name__ == "__main__":
    central_limit_theorem_demo()
