import numpy as np
import matplotlib.pyplot as plt

# Simulate photon arrivals at the retina using a Poisson process

def simulate_photon_arrivals(rate, duration):
    arrivals = np.random.poisson(rate, duration)
    return arrivals

def main():
    rate = 2  # average photons per ms
    duration = 1000  # ms
    arrivals = simulate_photon_arrivals(rate, duration)
    plt.plot(arrivals)
    plt.title('Photon Arrivals at Retina (Poisson Process)')
    plt.xlabel('Time (ms)')
    plt.ylabel('Photons Arrived')
    plt.show()

if __name__ == "__main__":
    main()
