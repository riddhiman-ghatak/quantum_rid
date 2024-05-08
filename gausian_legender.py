import numpy as np
import time

def gaussian_legendre_integration(f, a, b, n):
    
    x, w = np.polynomial.legendre.leggauss(n)
    
    
    t = 0.5 * (x + 1)  # Map points from [-1, 1] to [0, 1]
    x_transformed = a * (1 - t) + b * t
    
    
    integral_approx = np.sum(w * f(x_transformed)) * 0.5 * (b - a)
    
    return integral_approx


def f(x):
    return (9.8*68.1/12.5)*(1-np.exp(-(12.5/68.1)*x))


a = 0
b = 10

# Number of points
n = 2


# Perform integration
result = gaussian_legendre_integration(f, a, b, n)



print("Approximated integral:", result)

import numpy as np
import time

def gaussian_legendre_integration(f, a, b, n):
    x, w = np.polynomial.legendre.leggauss(n)
    t = 0.5 * (x + 1)  # Map points from [-1, 1] to [0, 1]
    x_transformed = a * (1 - t) + b * t
    integral_approx = np.sum(w * f(x_transformed)) * 0.5 * (b - a)
    return integral_approx

def f(x):
    return (9.8 * 68.1 / 12.5) * (1 - np.exp(-(12.5 / 68.1) * x))

a = 0
b = 10
# Number of points
n = 2

# Perform integration
result = gaussian_legendre_integration(f, a, b, n)

print("Approximated integral:", result)