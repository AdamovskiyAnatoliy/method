import numpy as np

def LUdecomp(a):
	n = len(a)
	for k in range(0,n-1):
		for i in range(k+1,n):
			if a[i,k] != 0.0:
				lam = a[i,k]/a[k,k]
				a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
				a[i,k] = lam
	return a

def LUsolve(a,b):
	n = len(a)
	for k in range(1,n):
		b[k] = b[k] - np.dot(a[k,0:k],b[0:k])
	b[n-1] = b[n-1]/a[n-1,n-1]
	for k in range(n-2,-1,-1):
		b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
	return b

def LUdecomp3(c,d,e):
	n = len(d)
	for k in range(1,n):
		lam = c[k-1]/d[k-1]
		d[k] = d[k] - lam*e[k-1]
		c[k-1] = lam
	return c,d,e

def LUsolve3(c,d,e,b):
	n = len(d)
	for k in range(1,n):
		b[k] = b[k] - c[k-1]*b[k-1]
	b[n-1] = b[n-1]/d[n-1]
	for k in range(n-2,-1,-1):
		b[k] = (b[k] - e[k]*b[k+1])/d[k]
	return b