import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh_tridiagonal


h_bar = 1  #  (set to 1 for simplicity)
m = 1      # (set to 1 for simplicity)
L = 5      
N = 1000   
dx = L / (N + 1)
x = np.linspace(0, L, N+2)  


def V(x, b):
    return x*b


def solve_eigenvalue(b):
    
    diagonal = np.ones(N) * (2 / dx**2) + V(x[1:N+1], b)
    off_diagonal = np.ones(N-1)*(-1 / dx**2)
    H = np.diag(diagonal) + np.diag(off_diagonal, k=1) + np.diag(off_diagonal, k=-1)

    
    eigenvalues, eigenvectors = np.linalg.eigh(H)

    
    ground_state = eigenvectors[:, 0]
    
    
    norm = np.sqrt(np.trapz(ground_state**2, x[1:N+1]))
    ground_state /= norm
    
    return ground_state

# Values of b
b_values = [0.01, 0.1, 1, 10]

# Plotting
plt.figure(figsize=(12, 8))
for b in b_values:
    wavefunction = solve_eigenvalue(b)
    plt.plot(x[1:N+1], wavefunction, label=f'b={b}')

plt.title('Wavefunction for Particle in a Box with Linear Ramp')
plt.xlabel('Position')
plt.ylabel('Wavefunction')
plt.legend()
plt.grid(True)
plt.show()