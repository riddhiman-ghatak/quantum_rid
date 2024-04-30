import numpy as np
import matplotlib.pyplot as plt

ohm=2/3
k=1
gamma=0.5
q=1.06



def f(x, y, p):
    return p, -k*np.sin((y)) - gamma*p + q*np.sin((x*ohm))



def rk4(x0, y0, p0, h):
    steps = 250
    x = x0
    y = y0
    p = p0
    xs = [x0]
    ys = [y0]
    ps = [p0]
    for _ in range(steps):
        s1y, s1p = f(x, y, p)
        s2y, s2p = f(x + 0.5 * h, y + 0.5 * h * s1y, p + 0.5 * h * s1p)
        s3y, s3p = f(x + 0.5 * h, y + 0.5 * h * s2y, p + 0.5 * h * s2p)
        s4y, s4p = f(x + h, y + h * s3y, p + h * s3p)
        y += h * (s1y + 2 * s2y + 2 * s3y + s4y) / 6
        p += h * (s1p + 2 * s2p + 2 * s3p + s4p) / 6
        x += h
        xs.append(x)
        ys.append(y)
        ps.append(p)
    return xs, ys, ps

x0 = 0
y0 = 1
p0 = 0
h = 0.02*2*np.pi

xs, ys, ps = rk4(x0, y0, p0, h)

plt.plot(xs,ys)
plt.plot(xs,ps)
plt.show()

