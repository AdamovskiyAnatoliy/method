import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline
from scipy import interpolate

x_data = np.array([-3, -2, 1, 4], float)
y_data = np.array([2, 0, 3, 1], float)

xs = np.arange(x_data[0], x_data[-1], 0.01)
cs = CubicSpline(x_data, y_data, bc_type=((1, -1), (1, 1)))

plt.plot(xs, cs(xs), label="S")
# plt.plot(xs, cs(xs, 1), label="S'")
plt.plot(x_data, y_data, 'o', alpha=0.7, label='Data')

a = cs.c

print(a)



def corect_sustem(x):
    for i in range(len(x)-1):
        x_new = np.linspace(x[i], x[i+1], 4)
        y_new = cs(x_new)

        lag_polynom = interpolate.lagrange(x_new, y_new)

        t = np.arange(x[i], x[i+1], 0.01)
        plt.plot(t, lag_polynom(t))
        print(lag_polynom)

# corect_sustem(x_data)
# real_sustem(x_data, a)

plt.legend()
plt.grid(True)
plt.show()
