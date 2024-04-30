import numpy as np
from scipy.fft import fft, ifft

# Input parameters
alpha = 20.0        # Gaussian wavepacket exponent
x0 = -0.5           # Initial position of the wavepacket
p0 = 50.0           # Initial momentum
mass = 14500.0      # Mass of the particle
xmin = -2.0         # Starting point of the grid
dx = 0.02           # Step size in x
dt = 0.1            # Time step size
nsteps = 5000        # Total number of time steps

# Set up the grid and potential
N = int((4.0 - xmin) / dx)  # Number of grid points
x = np.linspace(xmin, 4.0 - dx, N)
V = np.zeros_like(x)
V[x >= 0.0] = 1.0  # Step potential

# Initialize the wavefunction
psi = np.sqrt(alpha / np.pi) * np.exp(-alpha * (x - x0) ** 2 + 1j * p0 * x)

# Precompute kinetic energy operator in momentum space
k = np.fft.fftfreq(len(x), dx)
Ek = 0.5 * (k * np.pi) ** 2 / mass

# Time propagation
for t in range(nsteps):
    # Split-Operator propagation
    psi = np.exp(-0.5j * dt * V) @ psi
    psi_k = np.fft.fft(psi)
    psi_k = np.exp(-1j * dt * Ek) * psi_k
    psi = np.fft.ifft(psi_k)
    psi = np.exp(-0.5j * dt * V) @ psi

    # Plot the wavefunction every 500 steps
    if (t + 1) % 500 == 0:
        print(f"Step: {t + 1}")
        import matplotlib.pyplot as plt
        plt.plot(x, np.abs(psi) ** 2)
        plt.xlabel("x")
        plt.ylabel(r"|$\psi(x, t)$|$^2$")
        plt.show()