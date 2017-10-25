import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from math import ceil

EPS = 1e-3
a = 1.25
b = 0.65
c = 0.85
d = 0.35
x0 = 2.51
y0 = 1.52
start = 1
finish = 31

h = np.sqrt(np.sqrt(EPS))


def f1(t, x, y):
    return a*x-b*x*y


def f2(t, x, y):
    return -c*y+d*x*y

n = ceil(abs(start-finish)/h)
t_p = np.linspace(start, finish, n)


def pend(z, t, a, b, c, d):
    x, y = z
    dydt = [(a*x - b*x*y), (-c*y + d*x*y)]
    return dydt

sol = odeint(pend, [x0, y0], t_p,  args=(a, b, c, d))


def method_runge_kutta(h, x, y, t_0, t_1):
    n = ceil(abs(t_0-t_1)/h)
    t = [t_0]

    for i in range(n):
        t += [t[i]+h]

        k1 = h*f1(t[i], x[i], y[i])
        q1 = h*f2(t[i], x[i], y[i])

        k2 = h*f1(t[i] + h/2, x[i] + k1/2, y[i] + q1/2)
        q2 = h*f2(t[i] + h/2, x[i] + k1/2, y[i] + q1/2)

        k3 = h*f1(t[i] + h/2, x[i] + k2/2, y[i] + q2/2)
        q3 = h*f2(t[i] + h/2, x[i] + k2/2, y[i] + q2/2)

        k4 = h*f1(t[i] + h, x[i] + k3, y[i] + q3)
        q4 = h*f2(t[i] + h, x[i] + k3, y[i] + q3)

        x.append(x[i] + (k1 + 2*k2 + 2*k3 + k4)/6)
        y.append(y[i] + (q1 + 2*q2 + 2*q3 + q4)/6)

    return t, x, y


def runge_rules(t_1, t_2, x_1, x_2):
    r = 0
    for i in range(len(t_2)):
        for j in range(len(t_1)):
            if i/2 == j:
                r = max(r, abs(x_1[i]-x_2[j]))
            else:
                break
    return r


delta = 1
while delta > EPS:
    t_1, x_1, y_1 = method_runge_kutta(h, [x0], [y0], start, finish)
    t_2, x_2, y_2 = method_runge_kutta(h/2, [x0], [y0], start, finish)
    delta = max(runge_rules(t_1, t_2, x_1, x_2),
                runge_rules(t_1, t_2, y_1, y_2))

fig, axes = plt.subplots(1, 2, subplot_kw=dict())

axes[0].plot(t_p, sol[:, 0], label='X_real')
axes[0].plot(t_p, sol[:, 1], label='Y_real')
axes[0].plot(t_1, x_1, '--',  label="X")
axes[0].plot(t_1, y_1, '--',  label="Y")
axes[0].set(title='Original function', xlabel='t', ylabel='F(t)')



axes[1].plot(sol[:, 0], sol[:, 1], label='Real')
axes[1].plot(x_1, y_1, label='My')
axes[1].set(title='Dependence between the original functions', xlabel='x', ylabel='y')


axes[0].grid(True)
axes[1].grid(True)
axes[0].legend()
axes[1].legend()
plt.show()
