import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

def enter_nodes(n):
	x = []
	y = []
	for i in range(n):
		current_x = float(input("Enter the value of the " + str(i+1) + " argument: "))
		current_y = float(input("Enter the value of the " + str(i+1) + " function: "))
		x.append(current_x)
		y.append(current_y)
	return np.array(x), np.array(y)

def construction_of_equation(x):
	equation = [[x[i]**j for j in range(len(x)) ] for i in range(len(x))]
	return np.array(equation)

if __name__ == '__main__':
	
	l_limit = float(input('Enter L limit: '))
	r_limit = float(input('Enter R limit: '))

	n = int(input("Enter nodes: "))
	# x, y = enter_nodes(n)
	x = np.linspace(l_limit, r_limit, n)
	y = np.cos(x)

	equation = construction_of_equation(x)
	ai = np.linalg.solve(equation, y)

	polynom = np.poly1d(ai[::-1])
	
	print("Polynom: \n", polynom)
	t = np.arange(l_limit, r_limit, 0.01)

	plt.plot(t, np.cos(t), label="Cos")
	plt.plot(t, polynom(t), label="My")
	plt.plot(x, y, 'o', label="Nodes", alpha=0.5)

	plt.legend()
	plt.grid(True)
	plt.show()

