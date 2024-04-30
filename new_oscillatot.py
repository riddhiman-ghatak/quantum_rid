import numpy as np
import matplotlib.pyplot as plt

def f(x, p):
    return p, -x

def rk4(x0, p0, h):
    steps = 200
    x = x0
    p = p0
    xs = [x0]
    ps = [p0]
    for _ in range(steps):
        s1x, s1p = f(x, p)
        s2x, s2p = f(x + 0.5 * h * s1x, p + 0.5 * h * s1p)
        s3x, s3p = f(x + 0.5 * h * s2x, p + 0.5 * h * s2p)
        s4x, s4p = f(x + h * s3x, p + h * s3p)
        x += h * (s1x + 2 * s2x + 2 * s3x + s4x) / 6
        p += h * (s1p + 2 * s2p + 2 * s3p + s4p) / 6
        xs.append(x)
        ps.append(p)
    return xs, ps

x0 = 1
p0 = 0
h = 0.01 * 2 * np.pi

xs, ps = rk4(x0, p0, h)

plt.plot(xs, ps)
plt.xlabel('x')
plt.ylabel('p')
plt.title('Phase Portrait (RK4 Method)')
plt.show()