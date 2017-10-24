import math  
import matplotlib.pyplot as plt
import numpy as np
from LUdecomp3 import *
from scipy.interpolate import CubicSpline

from scipy import interpolate
# x = np.array([-3, -2, 1, 4])
# y = np.array([2, 0, 3, 1])

# s_a = -1
# s_b = 1


# def curvatures(xData,yData):
# 	n = len(xData) - 1
# 	c = np.zeros(n)
# 	d = np.ones(n+1)
# 	e = np.zeros(n)
# 	k = np.zeros(n+1)
# 	c[0:n-1] = xData[0:n-1] - xData[1:n]
# 	d[1:n] = 2.0*(xData[0:n-1] - xData[2:n+1])
# 	e[1:n] = xData[1:n] - xData[2:n+1]
# 	k[1:n] =6.0*(yData[0:n-1] - yData[1:n]) \
# 				/(xData[0:n-1] - xData[1:n]) \
# 			 -6.0*(yData[1:n] - yData[2:n+1]) \
# 				/(xData[1:n] - xData[2:n+1])
# 	LUdecomp3(c,d,e)
# 	LUsolve3(c,d,e,k)
# 	return k

# def evalSpline(xData,yData,k,x):
# 	def findSegment(xData,x):
# 		iLeft = 0
# 		iRight = len(xData)- 1
# 		while True:
# 			if (iRight-iLeft) <= 1:
# 				return iLeft
# 			i = int((iLeft + iRight)/2)

# 			if x < xData[i]: 
# 				iRight = i
# 			else: 
# 				iLeft = i


# 	i = findSegment(xData,x)
# 	h = xData[i] - xData[i+1]
# 	y = ((x - xData[i+1])**3/h - (x - xData[i+1])*h)*k[i]/6.0 \
# 	- ((x - xData[i])**3/h - (x - xData[i])*h)*k[i+1]/6.0 \
# 	+ (yData[i]*(x - xData[i+1]) \
# 	- yData[i+1]*(x - xData[i]))/h
# 	return y



xData = np.array([-3,-2,1,4],float)
yData = np.array([2,0,3,1],float)
# k = curvatures(xData,yData)


xs = np.arange(xData[0], xData[-1], 0.01)
# ys = np.array([evalSpline(xData,yData,k,i) for i in xs])
# plt.plot(xs,ys, label='Cubic spline')





cs = CubicSpline(xData, yData,   bc_type=((1, -1), (1, 1)))
# plt.plot(xData, yData, 'o', label='data')

# print(cs.derivative())
# print(cs.antiderivative())
# print(cs.roots())




# tck = interpolate.splrep(xData, yData, s=0)

# ynew = interpolate.splev(xs, tck, der=0)
# plt.plot(xs, ynew, label='Cubic spline') 


# plt.plot(xData, yData,'--', label='Lin spline')


plt.plot(xs, cs(xs), label="S")
# plt.plot(xs, cs(xs, 1), label="S'")
# plt.plot(xs, cs(xs, 2), label="S''")
# plt.plot(xs, cs(xs, 3), label="S'''")
plt.plot(xData, yData, 'o',alpha=0.7, label='Data') 


def corect_sustem(x):
	for i in range(len(x)-1): 
		x_new = np.linspace(x[i], x[i+1], 4)
		y_new = cs(x_new)

		lag_polynom = interpolate.lagrange(x_new,y_new)
		
		t = np.arange(x[i], x[i+1], 0.01)
		plt.plot(t, lag_polynom(t))

		# print("[{},{}]".format(x[i], x[i+1]))
		print(lag_polynom)

corect_sustem(xData)





plt.legend()
plt.grid(True)
plt.show()

# while True:
# 	try: 
# 		x = float(input("\nx ==> "))
# 	except SyntaxError: 
# 		break
# 	print("y =",evalSpline(xData,yData,k,x))
# input("Done. Press return to exit")