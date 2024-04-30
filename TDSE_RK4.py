import numpy as np
import matplotlib.pyplot as plt


hbar = 1.0  
m = 1.0  


x_min = 0.0
x_max = 10.0
N = 1000  
dx = (x_max - x_min) / (N - 1)
x = np.linspace(x_min, x_max, N)

dt = 0.0001  
num_time_steps = 300  
times = [150, 300]  

sigma = 0.1
k = 20.0
x0 = 5.0
alpha = 20.0
N_const = (2 * alpha / np.pi) ** 0.25


psi_init = N_const * np.exp(-((x - x0) ** 2) / (2 * sigma ** 2)) * np.exp(-1j * k * x)

# Potential function
V = x*0  


def rk4_step(psi, V):
    f1 = (-1j * hbar / (2 * m)) * (np.roll(psi, 1) - 2 * psi + np.roll(psi, -1)) / dx ** 2 - V * psi
    k1 = dt * f1
    f2 = (-1j * hbar / (2 * m)) * (np.roll(psi + k1 / 2, 1) - 2 * (psi + k1 / 2) + np.roll(psi + k1 / 2, -1)) / dx ** 2 - V * (psi + k1 / 2)
    k2 = dt * f2
    f3 = (-1j * hbar / (2 * m)) * (np.roll(psi + k2 / 2, 1) - 2 * (psi + k2 / 2) + np.roll(psi + k2 / 2, -1)) / dx ** 2 - V * (psi + k2 / 2)
    k3 = dt * f3
    f4 = (-1j * hbar / (2 * m)) * (np.roll(psi + k3, 1) - 2 * (psi + k3) + np.roll(psi + k3, -1)) / dx ** 2 - V * (psi + k3)
    k4 = dt * f4
    return psi + (k1 + 2 * k2 + 2 * k3 + k4) / 6

# Time evolution
psi = psi_init.copy()
psi_squared = [np.abs(psi) ** 2]

for i in range(num_time_steps):
    psi = rk4_step(psi, V)
    if i + 1 in times:
        psi_squared.append(np.abs(psi) ** 2)



# # Plot the initial wavefunction
plt.plot(x, np.abs(psi_init) ** 2, label='t = 0')



for i ,time in enumerate(times):
    plt.plot(x, psi_squared[i+1], label=f't = {time} iterations')

plt.show()    