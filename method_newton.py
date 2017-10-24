import numpy as np
import matplotlib.pyplot as plt

# Cos(x)

def x_newton(v):
	return sum( C[k]*p for k, p in enumerate(newton(v, len(C)) ) )


x = np.linspace(-np.pi, np.pi, 5)
y = np.cos(x)
C = [] 

def newton(val, n):
	mul = 1
	for i in range(n):
		if i: 
			mul *= val - x[i-1]
		yield mul

for n in range(len(x)):
	p = newton( x[n], n+1 )
	C.append( (y[n]-sum(C[k]*next(p) for k in range(n)) )/next(p) )

