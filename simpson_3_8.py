

import time

def simpsons_three_eighth_rule(f, a, b, n):
    """
    Simpson's 3/8 rule for numerical integration.

    Parameters:
    - f: The integrand function.
    - a: The lower limit of integration.
    - b: The upper limit of integration.
    - n: The number of subintervals (must be multiple of 3).

    Returns:
    - The approximate value of the integral.
    """
    if n % 3 != 0:
        raise ValueError("Number of subintervals must be multiple of 3.")

    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    fx = [f(x_i) for x_i in x]

    integral_approx = fx[0] + 3 * sum(fx[i] for i in range(1, n, 3)) + 3 * sum(fx[i] for i in range(2, n, 3)) + fx[-1]
    integral_approx *= 3 * h / 8

    return integral_approx

# Define the function to be integrated
def f(x):
    return x**3

# Integration limits
a = 0
b = 1

# Number of subintervals (must be multiple of 3)
n = 6

# Measure time taken for computation
start_time = time.time()

# Perform integration
result = simpsons_three_eighth_rule(f, a, b, n)

# Calculate elapsed time
elapsed_time = time.time() - start_time

print("Approximated integral using Simpson's 3/8 rule:", result)
print("Time taken:", elapsed_time, "seconds")
