import numpy as np
import matplotlib.pyplot as plt


def f(x, y, z, E):
   
   return -2*(1/x)*z - 2*E*y - (2*y)/x


def runge_kutta_4th_order_system(x0, y0, z0, h, target_x, E):
   
   steps = 10000


   #y=y, z= y',  
   x = x0
   y = y0
   z = z0
   ys = []
   for _ in range(steps):
       s1_y = h * z
       s1_z = h * f(x, y, z, E)
       
       s2_y = h * (z + 0.5 * s1_z)
       s2_z = h * f(x + 0.5 * h, y + 0.5 * s1_y, z + 0.5 * s1_z, E)
       
       s3_y = h * (z + 0.5 * s2_z)
       s3_z = h * f(x + 0.5 * h, y + 0.5 * s2_y, z + 0.5 * s2_z, E)
       
       s4_y = h * (z + s3_z)
       s4_z = h * f(x + h, y + s3_y, z + s3_z, E)
       
       y += (s1_y + 2 * s2_y + 2 * s3_y + s4_y) / 6
       z += (s1_z + 2 * s2_z + 2 * s3_z + s4_z) / 6
       x += h
       ys.append(x*x*y*y)
   
   return ys


# Initial conditions
x0 = 0.0005
y0 = 0.000001
z0 = -1000


# Step size
h = (5 - 0.0005) / 10000


start = -0.6
end = -0.4
step = 0.05


# values of E
values_of_E = np.linspace(start, end, 5)


# values of x
value_x = np.linspace(0.0005, 5, 10000)




for E in values_of_E:
   ys = runge_kutta_4th_order_system(x0, y0, z0, h, 10, E)
   plt.plot(value_x, ys, label=f'E={E:.2f}')


plt.xlabel('x')
plt.ylabel('y')
plt.title('Solutions for different values of E')
plt.legend()
plt.show()

