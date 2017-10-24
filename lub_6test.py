from math import ceil

import matplotlib.pyplot as plt


a = 1.2
b = 0.6
l = 0.8
k = 0.3


def fR(t ,R , F):
	return a*R-b*R*F

def fF(t, R, F):
	return -l*F + k*R*F

t = [0]
R = [2]
F = [1] 

h = 0.001
tfinal = 30
N = ceil(tfinal/h)

for i in range(N):
	t += [t[i]+h]

	k1R = fR(t[i], R[i], F[i])
	k1F = fF(t[i], R[i], F[i])

	k2R = fR(t[i]+h/2, R[i]+h*k1R/2, F[i]+h*k1F/2)
	k2F = fF(t[i]+h/2, R[i]+h*k1R/2, F[i]+h*k1F/2)

	k3R = fR(t[i]+h/2, R[i]+h*k2R/2, F[i]+h*k2F/2)
	k3F = fF(t[i]+h/2, R[i]+h*k2R/2, F[i]+h*k2F/2)

	k4R = fR(t[i]+h, R[i]+h*k3R, F[i]+h*k3F)
	k4F = fF(t[i]+h, R[i]+h*k3R, F[i]+h*k3F)

	R += [R[i] + h*(k1R+2*k2R+2*k3R+k4R)/6]
	F += [F[i] + h*(k1F+2*k2F+2*k3F+k4F)/6]



plt.plot(t,R)
plt.plot(t,F)
plt.show()
