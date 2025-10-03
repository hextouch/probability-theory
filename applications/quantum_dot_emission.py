import numpy as np
import matplotlib.pyplot as plt

# Model photon emission from quantum dots as a Poisson process

def simulate_emission(rate, duration):
    emissions = np.random.poisson(rate, duration)
    return emissions

def main():
    rate = 3  # average photons per ms
    duration = 1000  # ms
    emissions = simulate_emission(rate, duration)
    plt.plot(emissions)
    plt.title('Quantum Dot Photon Emission (Poisson Process)')
    plt.xlabel('Time (ms)')
    plt.ylabel('Photons Emitted')
    plt.show()

if __name__ == "__main__":
    main()
