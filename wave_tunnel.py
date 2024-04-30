import numpy as np
import matplotlib.pyplot as plt

# Constants
ℏ = 1
m = 1
dx = 0.01

# Potential function
def V(x):
    if x < 4:
        return 0
    elif 4 <= x <= 5:
        return 9
    else:
        return 0

# Finite difference method to solve Schrödinger equation
def solve_schrodinger(E):
    N = int(10 / dx) + 1
    ψ = np.zeros(N, dtype=np.complex128)
    k = np.sqrt(2 * m * (E - V(0)) / ℏ ** 2)
    ψ[0] = 1
    ψ[1] = np.exp(-1j * k * dx)
    
    for j in range(1, N - 1):
        ψ[j + 1] = (2 - 2 * m * (E - V(j * dx)) * dx ** 2 / ℏ ** 2) * ψ[j] - ψ[j - 1]
    
    return ψ

# Main function
if __name__ == "__main__":
    E = 9  # Energy in eV
    ψ = solve_schrodinger(E)

    # Plot real and imaginary parts of the wavefunction
    x = np.arange(0, 10 + dx, dx)
    plt.plot(x, ψ.real, label='Real part')
    plt.plot(x, ψ.imag, label='Imaginary part')
    plt.xlabel('Position (x)')
    plt.ylabel('Wavefunction')
    plt.title('Wavefunction for E = 9 eV')
    plt.legend()
    plt.grid(True)
    plt.show()
