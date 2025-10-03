import numpy as np

def law_of_large_numbers_demo(n=10000):
    samples = np.random.binomial(1, 0.5, n)
    running_mean = np.cumsum(samples) / np.arange(1, n+1)
    return running_mean

def main():
    running_mean = law_of_large_numbers_demo()
    import matplotlib.pyplot as plt
    plt.plot(running_mean)
    plt.axhline(0.5, color='red', linestyle='--', label='Expected Value')
    plt.title('Law of Large Numbers Demo')
    plt.xlabel('Number of Trials')
    plt.ylabel('Sample Mean')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
