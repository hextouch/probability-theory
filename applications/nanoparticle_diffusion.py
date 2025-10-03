import numpy as np
import matplotlib.pyplot as plt

# Simulate random walk (Brownian motion) of nanoparticles

def random_walk(n_steps, n_particles):
    steps = np.random.normal(0, 1, (n_particles, n_steps))
    positions = np.cumsum(steps, axis=1)
    return positions

def main():
    n_steps = 1000
    n_particles = 10
    positions = random_walk(n_steps, n_particles)
    for i in range(n_particles):
        plt.plot(positions[i], alpha=0.7)
    plt.title('Nanoparticle Diffusion (Random Walk)')
    plt.xlabel('Step')
    plt.ylabel('Position')
    plt.show()

if __name__ == "__main__":
    main()
