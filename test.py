import numpy as np
import matplotlib.pyplot as plt
import cmath
import math

xo = -0.5
alpha = 20
hbar = 1
xmin = -2
po = 50
dx = 0.02
dt = 0.1
stepst = 500
stepsx = 256
xmax=xmin+dx*stepsx
m = 14500
L = stepsx*dx
dk = 2*math.pi/L
kgrid = []


def wavefunc(po, x):
    ko = po/hbar

    N = (2*alpha/(math.pi))**0.25
    term1 = cmath.exp((1j)*ko*(x-xo))
    term2 = cmath.exp(-alpha*(x-xo)**2)
    return N*term1*term2



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


def ft(psi_t):
    psi_k=np.zeros(stepsx+1,dtype=np.complex128)

    for i in range(stepsx+1):
        for j in range(stepsx+1):
            psi_k[i]=psi_k[i]+psi_t[j]*np.exp(-1j*kgrid[i]*xgrid[j])
        
        psi_k[i]=(1/np.sqrt(stepsx))*psi_k[i]
    
    return psi_k


def ift(psi_k):
    psi_t=np.zeros(stepsx+1,dtype=np.complex128)

    for i in range(stepsx+1):
        for j in range(stepsx+1):
            psi_t[i]=psi_t[i]+psi_k[j]*np.exp(1j*kgrid[j]*xgrid[i])
        
        psi_t[i]=(1/np.sqrt(stepsx))*psi_t[i]
    
    return psi_t

for t in range(1, stepst + 1):
    for i in range(stepsx + 1):
        psi[t][i] = psi[t-1][i]*cmath.exp((-1j)*vgrid[i]*dt/2)
    psi[t] = ft(psi[t])

    for i in range(stepsx + 1):
        psi[t][i] = psi[t][i]*cmath.exp((-1j)*kgrid[i]**2*dt/(2*m))
        
    psi[t] = ift(psi[t])
    
    for i in range(stepsx + 1):
        psi[t][i] = psi[t][i]*cmath.exp((-1j)*vgrid[i]*dt/2)


# for i in range(0, stepst + 1, 500):
#     plt.plot(xgrid, [abs(p)**2 for p in psi[i]], label=str(i))
#     plt.title(f"Time Step {i}")
#     plt.show()

# Plot the wavefunction at different time steps
for i in range(0, stepst + 1, 500):
    plt.figure()
    plt.plot(xgrid, [abs(p)**2 for p in psi[i]], label=f"Time Step {i}")
    plt.title(f"Time Step {i}")
    plt.xlabel("Position (x)")
    plt.ylabel("Probability Density")
    plt.legend()
    plt.show()
