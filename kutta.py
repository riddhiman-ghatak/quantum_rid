import numpy as np

def f(x, y):
   
    return -2*y + x +4

def runge_kutta_4th_order(x0, y0, h, target_x):
    
    steps = int((target_x - x0) / h)
    x = x0
    y = y0
    for _ in range(steps):
        k1 = h * f(x, y)
        k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(x + 0.5 * h, y + 0.5 * k2)
        k4 = h * f(x + h, y + k3)
        
        y += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x += h
    
    return y
def euler_method(x0, y0, h, target_x):
    
    steps = int((target_x - x0) / h)
    x = x0
    y = y0
    for _ in range(steps):
        y += h * f(x, y)
        x += h
    
    return y

def heuns_method(x0, y0, h, target_x):
    
    steps = int((target_x - x0) / h)
    x = x0
    y = y0
    for _ in range(steps):
        k1 = h * f(x, y)
        k2 = h * f(x + h, y + k1)
        
        y += 0.5 * (k1 + k2)
        x += h
    
    return y

# Initial conditions
x0 = 0
y0 = 1

# Step size
h = 0.2

# Target x value
target_x = 0.2

# Estimate y(0.4)
y_04 = runge_kutta_4th_order(x0, y0, h, target_x)
print("Estimated value using kutta:", y_04)
