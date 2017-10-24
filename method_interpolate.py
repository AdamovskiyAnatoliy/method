import numpy as np
import scipy.interpolate as inter
import matplotlib.pyplot as plt

# Cos 

x = np.arange(-np.pi, np.pi, 0.01)
t = np.linspace(-np.pi, np.pi, 7) 
y = np.cos(t)

tnew = np.linspace(-np.pi, np.pi, 30)

plt.plot(x, np.cos(x), label='Cos')

kinds = ('nearest', 'zero', 'linear', 'slinear', 'quadratic', 'cubic')


for i in kinds:
	f = inter.interp1d(t,y, kind=i)
	plt.plot(tnew, f(tnew), label=i)

plt.plot(t, y,'o', label='nodes')

plt.legend()
plt.grid(True)
plt.show()

