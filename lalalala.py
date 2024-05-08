import numpy as np
from scipy.fft import fft, ifft
import matplotlib.pyplot as plt


hbar = 1.0  
m = 1.0  
xmin = -5.0 
xmax = 25.0  
nx = 1024  
dx = (xmax - xmin) / (nx - 1)  
x = np.linspace(xmin, xmax, nx)  

sigma = 1.0  # Gaussian wave packet exponent
x0 = -0.5  # Initial position of the wave packet
p0 = 0.0  # Initial momentum of the particle
k0 = p0  # Initial wave vector (hbar = 1)

# Potential parameters
D = 8.0  # Dissociation energy
alpha = np.sqrt(m * (1.0**2))  # Force constant
xe = 0.0  # Equilibrium position

# Morse potential
def V(x):
    return D * (1 - np.exp(-alpha * (x - xe)))**2

# Initial wave function
psi0 = (1 / np.pi**0.25 / sigma**0.5) * np.exp(-(x - x0)**2 / (2 * sigma**2)) * np.exp(1j * k0 * x)

# Kinetic energy operator in momentum space
k = np.fft.fftfreq(nx, dx / (2 * np.pi))
T = (hbar**2 / (2 * m)) * k**2

# Time propagation
dt = 0.2  # Time step
nt = 500  # Number of time steps

# Output files
wavepacket_files = [100, 200, 300, 400, 500]
expectation_file = "expect.out"


with open(expectation_file, "w") as f:
    f.write("# t\t<x>\t<p>\tC(t)\n")

    for it in range(nt + 1):
        t = it * dt

        # Split-operator method
        psi = psi0.copy()
        psi = ifft(np.exp(-0.5j * dt * T) * fft(psi))
        psi *= np.exp(-1j * dt * V(x) / hbar)
        psi = ifft(np.exp(-0.5j * dt * T) * fft(psi))

        # Compute expectation values
        norm = np.sum(np.abs(psi)**2) * dx
        x_avg = np.sum(x * np.abs(psi)**2) * dx / norm
        p_avg = -1j * hbar * np.sum(psi * np.gradient(psi, dx)) / norm
        C = np.sum(np.conj(psi0) * psi) * dx

        # Write to expectation file
        f.write(f"{t}\t{x_avg}\t{p_avg}\t{np.abs(C)}\n")

        # Save wavepacket
        if it in wavepacket_files:
            filename = f"{it}.dat"
            with open(filename, "w") as f_wp:
                f_wp.write("# x\tabs(psi)**2\n")
                for xval, psi_val in zip(x, np.abs(psi)**2):
                    f_wp.write(f"{xval}\t{psi_val}\n")

        psi0 = psi.copy()