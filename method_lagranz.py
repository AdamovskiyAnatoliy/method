import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as inter

import method_aproks as mp
import method_newton as mn


# def lagranz(x,y,t):
#     z=0
#     for j in range(len(y)):
#         p1=1
#         p2=1
        
#         for i in range(len(x)):
#             if i==j:
#                 p1=p1*1
#                 p2=p2*1   
#             else: 
#                 p1=p1*(t-x[i])
#                 p2=p2*(x[j]-x[i])
#         z=z+y[j]*p1/p2
#     return z

# n = int(input("Enter nodes: "))
# x, y = mp.enter_nodes(n)

def construction_of_lpolinom(n, l_limit, r_limit):
    x = np.linspace(l_limit, r_limit, n)
    y = np.cos(x)

    lag_polynom = inter.lagrange(x,y)
    return lag_polynom

# print("Polynom lagrange: \n", lag_polynom)
def paint_l(n, l_limit, r_limit):
    x = np.linspace(l_limit, r_limit, n)
    y = np.cos(x)

    t = np.arange(l_limit, r_limit, 0.01)

    lag_polynom = inter.lagrange(x,y)
    # new_polinom = mn.construction_of_npolinom(n,l_limit, r_limit)

    plt.plot(t, lag_polynom(t), label='Lagrange')
    # plt.plot(t, new_polinom(t), label='Newton')
    plt.plot(t,np.cos(t), '--', label='Cos')
    plt.plot(x,y, 'o', label='Nodes', alpha=0.5)

    plt.grid(True)
    plt.legend()
    plt.show()












