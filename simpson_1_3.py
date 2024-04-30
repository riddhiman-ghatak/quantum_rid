import time

def simpsons_one_third_rule(f, a, b, n):
    """
    Simpson's 1/3 rule for numerical integration.

    Parameters:
    - f: The integrand function.
    - a: The lower limit of integration.
    - b: The upper limit of integration.
    - n: The number of intervals (must be even).

    Returns:
    - The approximate value of the integral.
    """
    if n % 2 != 0:
        raise ValueError("Number of intervals must be even.")

    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    fx = [f(x_i) for x_i in x]

    integral_approx = fx[0] + 4 * sum(fx[i] for i in range(1, n, 2)) + 2 * sum(fx[i] for i in range(2, n - 1, 2)) + fx[-1]
    integral_approx *= h / 3

    return integral_approx

# Define the function to be integrated
def f(x):
    return x**3

# Integration limits
a = 0
b = 1

# Number of intervals (must be even)
n = 4

# Measure time taken for computation
start_time = time.time()

# Perform integration
result = simpsons_one_third_rule(f, a, b, n)

# Calculate elapsed time
elapsed_time = time.time() - start_time

print("Approximated integral using Simpson's 1/3 rule:", result)
print("Time taken:", elapsed_time, "seconds")
