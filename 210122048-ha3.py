
# Hello sir, I am Riddhiman Ghatak(Roll No. 210122048).


import numpy as np
import matplotlib.pyplot as plt


def f(x, p):
    return p, -x


x = 1
p = 0
h = 0.02 * 2 * np.pi
total_steps = 800



# Euler method
x_values = [x]
p_values = [p]
E_values = [p**2 + x**2]


for _ in range(total_steps):
    dx, dp = f(x, p)
    x += h * dx
    p += h * dp
    x_values.append(x)
    p_values.append(p)
    E_values.append(p**2 + x**2)


plt.plot(np.arange(total_steps + 1) * h / (2 * np.pi), E_values)
plt.xlabel('t/period')
plt.ylabel('2E')
plt.title('Energy vs Time (Euler Method)')

plt.show()


plt.plot(x_values, p_values)
plt.xlabel('x')
plt.ylabel('p')
plt.title('P_X (Euler Method)')
plt.show()


plt.plot(np.arange(total_steps + 1) * h / (2 * np.pi), x_values)
plt.xlabel('t/period')
plt.ylabel('x')
plt.title('Position vs Time (Euler Method)')
plt.show()




#RK2
x = 1
p = 0


x_values_rk2 = [x]
p_values_rk2 = [p]
E_values_rk2 = [p**2 + x**2]


for _ in range(total_steps):
    k1x, k1p = f(x, p)
    k2x, k2p = f(x + h * k1x, p + h * k1p)
    x += h * 0.5 * (k1x + k2x)
    p += h * 0.5 * (k1p + k2p)
    x_values_rk2.append(x)
    p_values_rk2.append(p)
    E_values_rk2.append(p**2 + x**2)


plt.plot(np.arange(total_steps + 1) * h / (2 * np.pi), E_values_rk2)
plt.xlabel('t/period')
plt.ylabel('2E')
plt.title('Energy vs Time (RK2 Method)')
plt.ylim(0.955,1.055)
plt.show()


plt.plot(x_values_rk2, p_values_rk2)
plt.xlabel('x')
plt.ylabel('p')
plt.title('P_X Plot (RK2 Method)')
plt.show()


plt.plot(np.arange(total_steps + 1) * h / (2 * np.pi), x_values_rk2)
plt.xlabel('t/period')
plt.ylabel('x')
plt.title('Position vs Time (RK2 Method)')
plt.xlim(0,1)
plt.show()




#RK4
x = 1
p = 0


x_values_rk4 = [x]
p_values_rk4 = [p]
E_values_rk4 = [p**2 + x**2]


for _ in range(total_steps):
    k1x, k1p = f(x, p)
    k2x, k2p = f(x + 0.5 * h * k1x, p + 0.5 * h * k1p)
    k3x, k3p = f(x + 0.5 * h * k2x, p + 0.5 * h * k2p)
    k4x, k4p = f(x + h * k3x, p + h * k3p)
    x += h * (k1x + 2 * k2x + 2 * k3x + k4x) / 6
    p += h * (k1p + 2 * k2p + 2 * k3p + k4p) / 6
    x_values_rk4.append(x)
    p_values_rk4.append(p)
    E_values_rk4.append(p**2 + x**2)


plt.plot(np.arange(total_steps + 1) * h / (2 * np.pi), E_values_rk4)
plt.xlabel('t/period')
plt.ylabel('2E')
plt.title('Energy vs Time (RK4 Method)')
plt.ylim(0, 2)
plt.show()


plt.plot(x_values_rk4, p_values_rk4)
plt.xlabel('x')
plt.ylabel('p')
plt.title('P_X Plot (RK4 Method)')
plt.show()


plt.plot(np.arange(total_steps + 1) * h / (2 * np.pi), x_values_rk4)
plt.xlabel('t/period')
plt.ylabel('x')
plt.title('Position vs Time (RK4 Method)')
plt.xlim(0,1)
plt.show()
