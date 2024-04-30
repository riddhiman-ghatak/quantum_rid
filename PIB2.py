import numpy as np
import matplotlib.pyplot as plt

m=1
hbar=1
start=0
end=5
points=100
dx=(end-start)/(points-1)
t=1/(2*(dx**2))

point_arr=np.linspace(0,5,100)

H=np.zeros((points,points))


def Crdel(i,j):
    if i==j:
        return 1
    return 0

for i in range(points):
    for j in range(points):
        H[i,j]=Crdel(i,j)*2-Crdel(i,j-1)-Crdel(i,j+1)

       
b=0.01
for i in range(points):
    H[i,i]=H[i,i]+b*point_arr[i]
    
    

H=H*t
E,pis=np.linalg.eigh(H)




plt.plot(point_arr,pis[:,0])
plt.plot(point_arr,E)
plt.show()

