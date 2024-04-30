import time

def trapezoidal_rule(f, a, b, n):
    """
    Trapezoidal rule for numerical integration.

    Parameters:
    - f: The integrand function.
    - a: The lower limit of integration.
    - b: The upper limit of integration.
    - n: The number of subintervals.

    Returns:
    - The approximate value of the integral.
    """
    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    fx = [f(x_i) for x_i in x]

    integral_approx = 0.5 * (fx[0] + fx[-1]) + sum(fx[1:-1])
    integral_approx *= h

    return integral_approx

# Define the function to be integrated
def f(x):
    return x**3

# Integration limits
a = 0
b = 1

# Number of subintervals
n = 10

# Measure time taken for computation
start_time = time.time()

# Perform integration
result = trapezoidal_rule(f, a, b, n)

# Calculate elapsed time
elapsed_time = time.time() - start_time

print("Approximated integral using Trapezoidal rule:", result)
print("Time taken:", elapsed_time, "seconds")
