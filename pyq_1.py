import numpy as np
import matplotlib.pyplot as plt


ℏ = 1
m = 1
dx = 0.01


def V(x):
    if x <= 4.5:
        return 9* np.exp((-1)*((x-4.5)/0.6)**2)
    
    else:
        return 5*np.exp((-1)*((x-4.5)/0.6)**2) + 4


def schorindger(E):
    N = int(10 / dx) + 1
    psi = np.zeros(N, dtype=np.complex128)
    k = np.sqrt(2 * m * (E - V(0)) / ℏ ** 2)
    psi[0] = 1
    psi[1] = np.exp(-1j * k * dx)
    
    for j in range(1, N - 1):
        psi[j + 1] = (2 - 2 * m * (E - V(j * dx)) * dx ** 2 / ℏ ** 2) * psi[j] - psi[j - 1]
    
    return psi

def quantum_trans(E):
    psi = schorindger(E)
    Pavg = (np.max(np.abs(psi[600:])) ** 2 + np.min(np.abs(psi[600:])) ** 2) / 2
    t = 2 / (1 + Pavg)
    return t

def classical_trans(E):
    if E>9:
        return 1
    else:
        return 0

def boltzman(k_BT, quantum_probability, energies):
    sum_term = 0
    for i in range(len(energies)):
        sum_term += (0.1/k_BT)*quantum_probability[i] * np.exp(-energies[i] / k_BT)
    return sum_term




if __name__ == "__main__":
    energies = np.arange(1, 15, 0.1)
    quantum_probability = [quantum_trans(E) for E in energies]
    classical_probability=[classical_trans(E) for E in energies]

    with open('transmission_probability_data.txt', 'w') as file:
        for energy, quantum, classical in zip(energies, quantum_probability, classical_probability):
            file.write(f"{energy}\t{quantum}\t{classical}\n")
    
    plt.plot(energies, quantum_probability, label = 'quamtum_probability')
    plt.plot(energies, classical_probability, label='classical_probability')
    plt.xlabel('Kinetic Energy')
    plt.ylabel('Transmission Probability')
    plt.title('Transmission Probability vs Kinetic Energy')
    plt.legend()
    plt.grid(True)
    plt.show()



#calculating boltzman
    k_BT_values = np.arange(0.1, 2.1, 0.1)

    quantum_sums = []
    classical_sums = []
    for k_BT in k_BT_values:
        quantum_sums.append(boltzman(k_BT, quantum_probability, energies))
        classical_sums.append(boltzman(k_BT, classical_probability, energies))
    
    with open('sum vs kbt.txt', 'w') as file:
        for K_BT, quantum, classical in zip(k_BT_values, quantum_sums, classical_sums):
            file.write(f"{K_BT}\t{quantum}\t{classical}\n")    



    plt.plot(k_BT_values, quantum_sums, label='Quantum')
    plt.plot(k_BT_values, classical_sums, label='Classical')
    plt.xlabel('k_BT')
    plt.ylabel('Sum')
    plt.title('Sum vs k_BT')
    plt.legend()
    plt.grid(True)
    plt.show()


#wave function plot for E=10

#if __name__ == "__main__":
    E = 10  
    psi = schorindger(E)
    psi_mag=np.abs(psi)*np.abs(psi)
    x = np.arange(0, 10 + dx, dx)
    with open('wavefunction_magnitude_data.txt', 'w') as file:
        for pos, mag in zip(x, psi_mag):
            file.write(f"{pos}\t{mag}\n")

    
    
    plt.plot(x, psi_mag, label='Magnitude of wave func')
    #plt.plot(x, psi.imag, label='Imaginary part')
    plt.xlabel('Position (x)')
    plt.ylabel('Wavefunction')
    plt.title('Wavefunction for E = 10 eV')
    plt.legend()
    plt.grid(True)
    plt.show()