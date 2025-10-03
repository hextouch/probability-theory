import numpy as np

# Model the probability of cone cell response to different wavelengths

def cone_response(wavelength):
    # Simplified: S, M, L cones (short, medium, long)
    S = np.exp(-((wavelength-420)/20)**2)
    M = np.exp(-((wavelength-534)/30)**2)
    L = np.exp(-((wavelength-564)/30)**2)
    return S, M, L

def main():
    wavelengths = np.linspace(400, 700, 100)
    responses = np.array([cone_response(w) for w in wavelengths])
    import matplotlib.pyplot as plt
    plt.plot(wavelengths, responses[:,0], label='S (Blue)')
    plt.plot(wavelengths, responses[:,1], label='M (Green)')
    plt.plot(wavelengths, responses[:,2], label='L (Red)')
    plt.title('Cone Cell Response Probability')
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Response')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
