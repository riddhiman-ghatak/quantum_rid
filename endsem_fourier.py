import numpy as np
import matplotlib.pyplot as plt
import cmath
import copy
import math

def wavefunc(po, x):
    xo = -0.5
    alpha = 20
    hbar = 1
    ko = po/hbar

    N = (2*alpha/(math.pi))**0.25
    term1 = cmath.exp((1j)*ko*(x-xo))
    term2 = cmath.exp(-alpha*(x-xo)**2)
    return N*term1*term2

xmin = -2
po = 50
dx = 0.02
dt = 0.1
stepst = 5000
stepsx = 256
m = 14500
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
    if x < 0 or x > 0.5:
        return 0
    else:
        return 0.1
    
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


for i in range(0, stepst + 1, 500):
    plt.plot(xgrid, [abs(p)**2 for p in psi[i]], label=str(i))
    plt.title(f"Time Step {i}")
    plt.show()

