import numpy as np
import sympy as sym

from scipy.optimize import minimize_scalar
from scipy.integrate import quad
from numpy.polynomial.legendre import leggauss


EPS = 1e-9

l_lim = np.array([0, 1e-9])
r_lim = np.array([0.5, 1])
x = sym.Symbol('x')

integrative_function = sym.cos(x**2/4)
invalid_function = sym.sin(x)/sym.sqrt(x)


d2y = integrative_function.diff(x).diff(x)
d4y = integrative_function.diff(x).diff(x).diff(x).diff(x)


f = sym.lambdify(x, integrative_function, 'numpy')
z = sym.lambdify(x, invalid_function, 'numpy')
d2f = sym.lambdify(x, d2y, 'numpy')
d4f = sym.lambdify(x, d4y, 'numpy')


def min_d2f(x):
    return -abs(d2f(x))


def min_d4f(x):
    return -abs(d4f(x))


def inverted_z(x):
    return -z(x)


m2 = -minimize_scalar(min_d2f, bounds=[l_lim[0], r_lim[0]],
                      method='bounded').fun
m4 = -minimize_scalar(min_d4f, bounds=[l_lim[0], r_lim[0]],
                      method='bounded').fun
min_z = minimize_scalar(z, bounds=[l_lim[1], r_lim[1]],
                        method='bounded').fun
min_z = min_z if min_z < 0 else 0
max_z = -minimize_scalar(inverted_z,  bounds=[l_lim[1], r_lim[1]],
                         method='bounded').fun


# Trapezoid method


def optimal_h(a, b, m, e):
    return np.sqrt(12*e/(m*abs(b-a)))


def optimal_n(a, b, h):
    return (b-a)/h


def trapezoid_integral(fun, a, b, h, n):
    list_nodes = np.linspace(a, b, n)
    return h*(fun(list_nodes[0]) + 2*sum(fun(list_nodes[1:-1])) +
              fun(list_nodes[-1]))/2


h1 = optimal_h(l_lim[0], r_lim[0], m2, EPS)
n = int(optimal_n(l_lim[0], r_lim[0], h1-EPS)) + 1
trapezoid_integral_value = trapezoid_integral(f, l_lim[0], r_lim[0], h1, n)

print("\n", "-"*10, "\n")
print("Function: ", integrative_function,
      "Left limit: {} Right limit: {}".format(l_lim[0], r_lim[0]))
print("Trapezoid method: ", trapezoid_integral_value)


# Simpson's method


def optimal_h(a, b, h):
    return (b-a)/(2*h)


def simpson_integral(fun, a, b, m):
    h = optimal_h(a, b, m)
    list_nodes = np.linspace(a, b, 2*m)
    partial_amount = fun(list_nodes[0]) + fun(list_nodes[-1])
    for i in range(1, m+1):
        partial_amount += 4*fun(list_nodes[2*i-1])
    for i in range(1, m):
        partial_amount += 2*fun(list_nodes[2*i])
    return h*partial_amount/3


m = 1
delta = 1
h = optimal_h(l_lim[0], r_lim[0], m)

while delta > EPS:
    simpson_integral_value1 = simpson_integral(f, l_lim[0], r_lim[0], m)
    simpson_integral_value2 = simpson_integral(f, l_lim[0], r_lim[0], 2*m)
    delta = abs(simpson_integral_value1 - simpson_integral_value2)/15
    m *= 2

print("Simpson method: ", simpson_integral_value2)


# Gauss method


a = 5
nodes = leggauss(a)


def gauss_integral(func, nodes, a, b):
    return (b-a)*0.5 * sum(nodes[1]*func((b-a)*0.5*nodes[0]+(b+a)*0.5))

gauss_integral_value = gauss_integral(f, nodes, l_lim[0], r_lim[0])

print("Gauss method: ", gauss_integral_value)
print("Real integral: ", quad(f, l_lim[0], r_lim[0])[0])
print("\n", "-"*10, "\n")

# Method Monte Carlo

# n = int(input("Enter len array: "))
n = 1_000_000

a = np.random.uniform(l_lim[1], r_lim[1], n)
b = np.random.uniform(min_z, max_z, n)

num_hits = 0
for i in range(len(a)):
    if z(a[i]) >= b[i]:
        num_hits += 1

monte_сarlo_integral_value = num_hits*abs(l_lim[1]-r_lim[1])*abs(min_z-max_z)/n

print("Function: ",  invalid_function,
      "Left limit: 0 Right limit: {}".format(r_lim[1]))
print("Monte carlo method: ", monte_сarlo_integral_value)
print("Real integral: ", quad(z, 0, r_lim[1])[0])
print("\n", "-"*10, "\n")
