import numpy as np
import matplotlib.pyplot as plt

# Model reliability of nanoscale devices using exponential distribution

def simulate_device_lifetime(rate, n_devices):
    lifetimes = np.random.exponential(1/rate, n_devices)
    return lifetimes

def main():
    rate = 0.1  # failure rate per hour
    n_devices = 1000
    lifetimes = simulate_device_lifetime(rate, n_devices)
    plt.hist(lifetimes, bins=30, alpha=0.7)
    plt.title('Nanoscale Device Lifetime (Exponential)')
    plt.xlabel('Lifetime (hours)')
    plt.ylabel('Count')
    plt.show()

if __name__ == "__main__":
    main()
