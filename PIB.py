import numpy as np
import matplotlib.pyplot as plt


L = 5      
N = 100    
dx = L / (N + 1) 
h_bar = 1  #(set to 1 for simplicity)
m = 1      #(set to 1 for simplicity)


diagonal_elements = np.ones(N) * (2 / dx**2)
off_diagonal_elements = np.ones(N-1)*(-1 / dx**2)
H = np.diag(diagonal_elements) + np.diag(off_diagonal_elements, k=1) + np.diag(off_diagonal_elements, k=-1)


eigenvalues, eigenvectors = np.linalg.eigh(H)


exact_eigenvalues = [(n**2 * np.pi**2 * h_bar**2) / (2 * m * L**2) for n in range(1, N+1)]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(range(1, N+1), eigenvalues, label='Numerical Eigenvalues')
plt.plot(range(1, N+1), exact_eigenvalues, label='Exact Eigenvalues', linestyle='--')
plt.title('Comparison of Numerical and Exact Eigenvalues')
plt.xlabel('Eigenvalue Index')
plt.ylabel('Eigenvalue')
plt.legend()
plt.grid(True)
plt.show()      
