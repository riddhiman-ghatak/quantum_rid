import numpy as np
import matplotlib.pyplot as plt

# Constants
alpha = 20.0  
x0 = -0.5     #
p0 = 20.0     # 
mass = 14500.0  # 
xmin = -2.0   
dx = 0.02    
dt = 0.1      
total_steps = 5000  

# Potential function
def V(x):
    return np.where(x >= 0, 1, 0)

# Initialize grid
N = int((abs(xmin) * 2) / dx) + 1
x = np.linspace(xmin, -xmin, N)

# Initialize wave function
psi = np.sqrt(2 * alpha / np.pi) * np.exp(1j * p0 * (x - x0)) * np.exp(-alpha * (x - x0) ** 2)


def finite_difference_second_derivative(psi, dx):
    return np.gradient(np.gradient(psi, dx), dx)


def fourier_transform_second_derivative(psi, dx):
    k = np.fft.fftfreq(len(psi), d=dx) * 2 * np.pi
    psi_k = np.fft.fft(psi)
    psi_k_second_derivative = (1j * k) ** 2 * psi_k
    return np.fft.ifft(psi_k_second_derivative).real


for i in range(1, total_steps + 1):
    psi_new = psi + (1j * dt / 2) * (finite_difference_second_derivative(psi, dx) / mass - V(x) * psi)
    psi = psi_new

    
    if i % 1000 == 0:
        plt.plot(x, abs(psi) ** 2)
        plt.title(f"Time Step {i}")
        plt.xlabel("Position (au)")
        plt.ylabel("Probability Density")
        #plt.savefig(f"wavepacket_timestep_{i}.png")
        plt.show()
        plt.close()


