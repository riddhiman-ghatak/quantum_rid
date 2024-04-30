import numpy as np
import matplotlib.pyplot as plt

def f(x, y, p):
   
   return p, -2*(1/x)*p - 2*(-0.4)*y - (2*y)/x


def eular(x0, y0, p0, h):
    steps = 10000
    x = x0
    y= y0
    p = p0
    xs = [x0]
    ys= [y0]
    ps = [p0]
    for _ in range(steps):
        s1y, s1p = f(x, y, p)
        
        y += s1y
        p += s1p
        x +=h
        xs.append(x)
        ys.append(y)
        ps.append(p)
    return xs, ys, ps






def rk4(x0, y0, p0, h):
    steps = 10000
    x = x0
    y= y0
    p = p0
    xs = [x0]
    ys= [y0]
    ps = [p0]
    for _ in range(steps):
        s1y, s1p = f(x, y, p)
        s2y, s2p = f(x+0.5*h, y + 0.5 * h * s1y, p + 0.5 * h * s1p)
        s3y, s3p = f(x+0.5*h, y + 0.5 * h * s2y, p + 0.5 * h * s2p)
        s4y, s4p = f(x+h ,y + h * s3y, p + h * s3p)
        y += h * (s1y + 2 * s2y + 2 * s3y + s4y) / 6
        p += h * (s1p + 2 * s2p + 2 * s3p + s4p) / 6
        x +=h
        xs.append(x)
        ys.append(y)
        ps.append(p)
    return xs, ys, ps


x0 = 0.0005
y0 = 0.000001
p0 = -1000
h = (5 - 0.0005) / 10000
xs, ys, ps= eular(x0, y0, p0, h)

values_of_E = np.linspace(-0.6, -0.4, 5)
for E in values_of_E:
   ys = rk4(x0, y0, p0, h, 10, E)
   plt.plot(xs, ys, label=f'E={E:.2f}')

plt.plot(xs,ys)
plt.show()