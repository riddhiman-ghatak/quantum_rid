import numpy as np
import matplotlib.pyplot as plt


ℏ = 1
m = 1
dx = 0.01


def V(x):
    if x < 4:
        return 0
    elif 4 <= x <= 5:
        return 9
    else:
        return 0


def solve_schrodinger(E):
    N = int(10 / dx) + 1
    psi = np.zeros(N, dtype=np.complex128)
    k = np.sqrt(2 * m * (E - V(0)) / ℏ ** 2)
    psi[0] = 1
    psi[1] = np.exp(-1j * k * dx)
    
    for j in range(1, N - 1):
        psi[j + 1] = (2 - 2 * m * (E - V(j * dx)) * dx ** 2 / ℏ ** 2) * psi[j] - psi[j - 1]
    
    return psi

def cal_trans_probability(E):
    psi = solve_schrodinger(E)
    Pavg = (np.max(np.abs(psi[600:])) ** 2 + np.min(np.abs(psi[600:])) ** 2) / 2
    t = 2 / (1 + Pavg)
    return t


if __name__ == "__main__":
    energies = np.arange(1, 26, 0.1)
    transmission_probabilities = [cal_trans_probability(E) for E in energies]

    
    plt.plot(energies, transmission_probabilities)
    plt.xlabel('Incident Kinetic Energy (eV)')
    plt.ylabel('Transmission Probability')
    plt.title('Transmission Probability vs Incident Kinetic Energy')
    plt.grid(True)
    plt.show()


#wave function plot for E=9

if __name__ == "__main__":
    E = 9  
    psi = solve_schrodinger(E)
    psi_mag=np.abs(psi)*np.abs(psi)

    
    x = np.arange(0, 10 + dx, dx)
    plt.plot(x, psi_mag, label='Magnitude of wave func')
    #plt.plot(x, psi.imag, label='Imaginary part')
    plt.xlabel('Position (x)')
    plt.ylabel('Wavefunction')
    plt.title('Wavefunction for E = 9 eV')
    plt.legend()
    plt.grid(True)
    plt.show()