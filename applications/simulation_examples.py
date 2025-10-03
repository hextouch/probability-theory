import numpy as np

def coin_toss_simulation(n=1000):
    results = np.random.choice(['H', 'T'], size=n)
    heads = np.sum(results == 'H')
    print(f"Heads: {heads}, Tails: {n-heads}")

if __name__ == "__main__":
    coin_toss_simulation()
