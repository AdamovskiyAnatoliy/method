import random
import math
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-20, 20, 0.01)
y1 = 1/2*np.sqrt(20-5*x**2)  
y2 = -1/2*np.sqrt(20-5*x**2)  

y11 = np.sqrt((1-4*x**2)/5)
y12 = -np.sqrt((1-4*x**2)/5)

plt.plot(x,y1, c='m')
plt.plot(x,y2, c ='m')
plt.plot(x,y11, c ='c')
plt.plot(x,y12, c = 'c')


plt.show()



# def norm_rozpod(n):
# 	for i in range(n):
# 		x1 = -math.sqrt(5)
# 		x2 = math.sqrt(5)

# 		y1 = -2
# 		y2 = 2

# 		x = [ (x2-x1)*random.random()+x1 for i in range(1000)]

# 		y = [ (y2-y1)*random.random()+y1 for i in range(1000)] 

# 		n = 0
		
# 		for i in range(len(x)):
# 			if x[i]**2/4+y[i]**2/5 <= 1 and x[i]**2/0.25+y[i]**2/0.2<=1:
# 				n+=1

# 		print("S = ", 8*(math.sqrt(5))*n/len(x))



		# f = []

		# for i in n:
		# 	f.append(math.exp((-i**2)/2)/(2*math.pi)**(1/2))

		# znachF = (x2-x1)*sum(f)/len(n)

		# print("Integral: ", znachF)

		# a1 = min(n)
		# a2 = max(n)

		# r = a2 - a1
		# k = 7 
		# dx = r / k

		# d = [ a1+i*dx for i in range(k+1)]

		# m = [ 0 for i in range(k)]


		# for i in range(k):	
		# 	for j in n:
		# 		if  d[i] <= j and j <= d[i+1]:
		# 			m[i]+=1


		# v = [ m[i]/len(n) for i in range(k)]

		# w = [ (v[i]-1/k)**2 for i in range(k)]

		# xi = sum(w)*k
		# print("XI^2 = ", xi)

# norm_rozpod(10)