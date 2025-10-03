import numpy as np
import matplotlib.pyplot as plt

# Model the effect of noise on visual signal detection

def simulate_visual_acuity(trials=1000, signal_strength=5, noise_std=2):
    detections = []
    for _ in range(trials):
        noise = np.random.normal(0, noise_std)
        detected = (signal_strength + noise) > 3  # threshold
        detections.append(detected)
    prob_correct = np.mean(detections)
    return prob_correct

def main():
    probs = [simulate_visual_acuity(noise_std=std) for std in np.linspace(0.5, 5, 20)]
    plt.plot(np.linspace(0.5, 5, 20), probs)
    plt.title('Probability of Correct Visual Detection vs. Noise')
    plt.xlabel('Noise Std Dev')
    plt.ylabel('Probability of Correct Detection')
    plt.show()

if __name__ == "__main__":
    main()
