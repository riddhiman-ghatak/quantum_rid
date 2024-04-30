import numpy as np


# sir I am Riddhiman.I have submitted already 2 days ago.
# But my file name was not in format , so I am submitting again




def f(x):
    ans = 2000 * np.log(140000 / (140000 - 2100 * x)) - 9.8 * x
    return ans

def trapezoid(a, b, n):
    term = 0
    h = (b - a) / n
    for i in range(1, n):
        term += f(a + i * h)
    ans = h * (f(a) / 2 + f(b) / 2 + term)
    return ans

def romberg(j, k, a, b):
    n = max(j + 1, k)
    matrix = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        matrix[i][1] = trapezoid(a, b, 2 ** (i - 1))
    for col in range(2, n + 1):
        for row in range(1, n - col + 2):
            matrix[row][col] = (4 ** (col - 1) * matrix[row + 1][col - 1] - matrix[row][col - 1]) / (4 ** (col - 1) - 1)
    return matrix[j][k]

if __name__ == "__main__":
    print(romberg(1, 4, 8, 30))
    #print(trapezoid(8, 30, 2))
