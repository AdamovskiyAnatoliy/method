import numpy as np
import matplotlib.pyplot as plt
from sympy import diff
from scipy.misc import derivative
from scipy.optimize import minimize


X0 = 2
EPS = 10**-9
H = 0.01




def f(x):
	return 60*x**44 - 32*x**33 + 208*x**4 - 67*x**2 - 65

def real_df(x):
	return 2640*x**43 - 1056*x**32 + 832*x**3 - 134*x

def optemal_H(e,m):
	return (3*e/m)**(1/3)

def optemal_H2(e,m):
	return ((45*e)/(4*m))**(1/5)

def max_diff(a, b, n):
	list_of_a_b = np.linspace(a,b,n)
	list_of_dif_in_point = []
	for i in list_of_a_b:
		list_of_dif_in_point.append(derivative(f, i, n=3, order=5, dx=EPS))
	return max(list_of_dif_in_point)


def f(x):
	return 60*x**44 - 32*x**33 + 208*x**4 - 67*x**2 - 65

def real_df(x):
	return 2640*x**43 - 1056*x**32 + 832*x**3 - 134*x

def df_2(x):
	return 113520*x**42 - 33792*x**31 + 2493*x**2 - 134

def df_3(x):
	return 4767840*x**41 - 1047552*x**30 + 4986*x

def df_4(x):
	return 195481440*x**40 - 31426560*x**29  + 4986

def df_5(x):
	return 7819257600*x**39 - 911370240*x**28

def df_6(x):
	return 304951046400*x**38 - 304951046400*x*27


a = np.zeros(41)
a[0] = 195481440
a[11] = 31426560
a[-1] = 4986
root = np.roots(a)
print("Root1: \n", root)
M=[]

for i in root[0], root[3]:
	M.append(abs(df_3(i)))

M_R1 = max(M)



a = np.zeros(39)
a[0] = 304951046400
a[11] = 304951046400
root = np.roots(a)
print("Root2: \n", root)
M_R2 = abs(df_5(root[0].real))

print("-"*10)
print("Max_df3: ", M_R1)
print("Max_df5: ", M_R2)





def fi(x, h, i):
	return f(x+i*h)




def D(x,h, i):
	return (fi(x, h, i) - fi(x, h, -i))/(2*i*h)

def df(x, h):
	return (4*D(x, h, 1) - D(x, h, 2))/3

print("-"*10)

# print(df(X0, optemal_H(EPS, max_diff(1.999999,2.000001,1000))))	

print("Optemal H1: ", optemal_H(EPS, M_R1))
print("Optemal H2: ", optemal_H2(EPS,M_R2))

print("-"*10)
print("Df O(h^2): ", df(X0, optemal_H(EPS, M_R1)))
print("Df O(h^4): ", df(X0,  optemal_H2(EPS,M_R2)))

print("Real df: ", real_df(X0))

