import numpy as np
import matplotlib.pyplot as plt
import cmath
import copy
import math

def wavefunc(po, x):
   return (1.0/np.pi)**0.25*(np.exp(-1j*0))*np.exp(-(0.5*(x+0.5)**2))

xmin = -5
po = 0
dx = 30/1024
dt = 0.2
stepst = 500
stepsx = 1024
m = 1
L = stepsx*dx
dk = 2*math.pi/L
kgrid = []

for i in range(stepsx + 1):
    if i < stepsx/2:
        kgrid.append(2*math.pi*i/L)
    else:
        kgrid.append(2*math.pi*(i - stepsx)/L)

xgrid = []
for i in range(stepsx + 1):
    xgrid.append(xmin + i*dx)

def potential(x):
     return 8*(1-np.exp(-np.sqrt(1/(2*8))*(x)))**2
    
vgrid = []
for i in range(stepsx + 1):
    vgrid.append(potential(xgrid[i]))

psi = np.zeros((stepst + 1, stepsx + 1), dtype=complex)
# print(psi.shape, len(xgrid), len(kgrid), len(vgrid))

for i in range(stepsx + 1):
    psi[0][i] = wavefunc(po, xgrid[i])

for t in range(1, stepst + 1):
    for i in range(stepsx + 1):
        psi[t][i] = psi[t-1][i]*cmath.exp((-1j)*vgrid[i]*dt/2)
    psi[t] = np.fft.fft(psi[t])
    for i in range(stepsx + 1):
        psi[t][i] = psi[t][i]*cmath.exp((-1j)*kgrid[i]**2*dt/(2*m))
    psi[t] = np.fft.ifft(psi[t])
    for i in range(stepsx + 1):
        psi[t][i] = psi[t][i]*cmath.exp((-1j)*vgrid[i]*dt/2)


for i in range(0, stepst + 1, 100):
    plt.plot(xgrid, [abs(p)**2 for p in psi[i]], label=str(i))
    plt.title(f"Time Step {i}")
    plt.show()

