import numpy as np

def f(x, y):
    """
    Defines the differential equation y'(x) = x^2 + y^2
    """
    return -2*y + x +4

def euler_method(x0, y0, h, target_x):
    """
    Implementation of Euler's method
    """
    steps = int((target_x - x0) / h)
    x = x0
    y = y0
    for _ in range(steps):
        y += h * f(x, y)
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
y_04 = euler_method(x0, y0, h, target_x)
print("Estimated value using Euler's method:", y_04)
