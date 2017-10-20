import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([4.2, 8.8, 16.3, 24.6, 36.5, 48.4])

x0 = 6

t = np.linspace(x[0], x[-1], 1000)
z = np.linspace(x[-1], x0, 1000)


# x = np.array([19.76, 38.09, 40.95, 41.08, 56.29, 68.51, 
# 			  75.01, 89.05, 91.13, 91.26, 99.84, 108.55])
# y = np.array([0.24, 0.31, 0.55, 0.48, 0.78, 0.98,
# 			  0.94, 1.21, 1.29, 1.12, 1.29, 1.49])

#lin

# a = [[sum(x**i) for i in range(j+1, j-1,-1)] for j in range(1,-1,-1)]
# b = [sum(x*y), sum(y)]

# print(np.linalg.solve(a,b))


def search_a(x, y):

	return (len(x)*sum(x*y) - sum(x)*sum(y))/( len(x)*sum(x**2) - (sum(x))**2)


def search_b(x, y, a):

	return sum(y)/len(y) - a * sum(x)/len(x) 


a = search_a(x,y)
b = search_b(x,y,a)

f1_in_x0 = a * x0 + b
f1_in_x = a * x + b

max_lin = max(abs(f1_in_x - y))
print("\nФункція: {}x+{}".format(a,b))
print("Найбільше відхилення використовуючи лінійну апроксимацію: {}".format(max_lin))
print("Прогноз в точці x = 6 використовуючи лінійну апроксимацію: {}".format(f1_in_x0))


plt.plot(x,y, 'o', alpha=0.7, label='Nodes')
plt.plot(t, a*t+b, label='Lin')
plt.plot(z, a*z+b,'--', label='Lin_forecast')
plt.plot([x0],[f1_in_x0], 'x')


#Pow2

a = [[sum(x**i) for i in range(j+2, j-1,-1)] for j in range(2,-1,-1)]
b = [sum(x**2*y), sum(x*y), sum(y)]

print(a)
print(b)


a_b_c = np.linalg.solve(a,b)
polynom = np.poly1d(a_b_c)

f2_pow_x0 = polynom(x0)
f2_in_x = polynom(x)

max_pow = max(abs(f2_in_x-y))

print("\nФункція: {}x^2+{}x+{}".format(a_b_c[0], a_b_c[1], a_b_c[2]))
print("Найбільше відхилення використовуючи квадратичну апроксимацію: {}".format(max_pow))
print("Прогноз в точці x = 6 використовуючи квадратичну апроксимацію: {}\n".format(f2_pow_x0))


plt.plot(t, polynom(t), label='Pow2')
plt.plot(z, polynom(z),'--', label='Pow2_forecast')
plt.plot([x0],[f2_pow_x0], 'x')


plt.grid(True)
plt.title("Approximation")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()


