import numpy as np
import time

def gaussian_legendre_integration(f, a, b, n):
    # Calculate Gauss-Legendre points and weights
    x, w = np.polynomial.legendre.leggauss(n)
    
    # Transform integration limits
    t = 0.5 * (x + 1)  # Map points from [-1, 1] to [0, 1]
    x_transformed = a * (1 - t) + b * t
    
    # Calculate integral approximation
    integral_approx = np.sum(w * f(x_transformed)) * 0.5 * (b - a)
    
    return integral_approx

# Define the function to be integrated
def f(x):
    return x**3

# Integration limits
a = 0
b = 1

# Number of points
n = 5

# Measure time taken for computation
start_time = time.time()

# Perform integration
result = gaussian_legendre_integration(f, a, b, n)

# Calculate elapsed time
elapsed_time = time.time() - start_time

print("Approximated integral:", result)
print("Time taken:", elapsed_time, "seconds")
