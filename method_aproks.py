import numpy as np
import matplotlib.pyplot as plt

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

	x = np.arange(-np.pi, 2*np.pi+np.pi/2, np.pi/4)
	y = np.cos(x)

	equation = construction_of_equation(x)
	ai = np.linalg.solve(equation, y)

	polynom = np.poly1d(ai[::-1])
	
	print(polynom)
	t = np.arange(-np.pi, 2*np.pi, 0.01)

	plt.plot(t, np.cos(t), label="Cos")
	plt.plot(t, polynom(t), label="My")
	plt.legend()
	plt.grid(True)
	plt.show()


