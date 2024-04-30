import numpy as np
import matplotlib.pyplot as plt




h_bar = 1.0  
m = 14500.0       
times=[0,1500,2500,4500]

def V(x):
   vs=[]
   for x_ll in x:
       if(x_ll<0 or x_ll>0.5):
           vs.append(0)
       else:
           vs.append(0.1)    


   return vs   


def initial_psi(x, x0, k0, alpha):
   return (2 * alpha / np.pi)**0.25 * np.exp(1j * k0 * (x - x0) - alpha * (x - x0)**2)




def d2psi_dx2(psi, dx):
    d2psi = np.zeros_like(psi)
    
    # First point: forward difference
    d2psi[0] = ( psi[0] - 2 * psi[1] + psi[2]) / dx**2
    
    # Interior points: central difference
    for i in range(1, len(psi) - 1):
        d2psi[i] = (psi[i + 1] - 2 * psi[i] + psi[i - 1]) / dx**2
    
    # Last point: backward difference
    d2psi[-1] = ( psi[-1] - 2 * psi[-2] + psi[-3]) / dx**2
    
    return d2psi

def evolve_psi(psi, x, dt):
   dx = x[1] - x[0]
   psi_new = psi + 1j * dt * (h_bar / (2 * m) * d2psi_dx2(psi, dx) - V(x) * psi / h_bar)
   return psi_new




dt = 0.1            
total_time_steps = 5000




xmin = -2.0 
dx= 0.02        
xmax = xmin+(256*dx)
         
x = np.linspace(xmin, xmax+dx, 256)




x0 = -0.5           
k0 = 50.0 / h_bar  
alpha = 20.0        




psi_previous = initial_psi(x, x0, k0, alpha)
psi_current = evolve_psi(psi_previous, x, dt)




for i in range(total_time_steps):
   psi_next = evolve_psi(psi_current, x, dt)
   psi_previous, psi_current = psi_current, psi_next
   
   if i in times:
       plt.plot(x, abs(psi_next) ** 2)
       plt.title(f"Time Step {i}")
       plt.xlabel("Position (au)")
       plt.ylabel("Probability Density")
       
       plt.show()