import numpy as np
from scipy import sparse
import matplotlib.pyplot as plt
from copy import deepcopy

#dt es el k
#dx es el h

def eqCalor(dt, fun,alfa,beta,t= 1, L = 1, gamma =0.5):
    to = 0
    var_graf = 0.08

    paso = (t-to)/dt

    dx = dt**(1/2)
    N = int(L/dx)

    x = np.linspace(0, L, N)

    print("aca es x")
    print(x)

    mu = gamma*dt/(dx**2)

    dl = mu*np.ones(N-2)
    du = mu*np.ones(N-2)
    d0 = 1-2*mu*np.ones(N-2)
    d = np.vstack((dl, d0, du))
    A = sparse.spdiags(d, (-1, 0, 1), N-2, N-2)

    u0 = np.zeros(N)
    for i in range(len(x)):
        u0[i] = fun(x[i])
    
    #u0 = np.full([N-2, 1], funcion_init)
    u0 = u0[:,None]
    u0 = u0[1:]
    u0 = u0[:-1]
    #Confia :3 <xd
    print("ACA")
    print(u0)


    b = np.zeros([N-2, 1])

    ui = deepcopy(u0)


    plt.figure()
    # x = x[1:]
    # x = x[:-1]
    a = True
    for i in range(int(paso)+1):
        
        if i % (var_graf/dt) == 0:
            u_aux = deepcopy(ui)
            u_aux = np.insert(u_aux, 0, alfa)
            if a:
                print(np.insert(u_aux, 0, alfa))
                a = False
            u_aux = np.append(u_aux, beta)

            plt.plot(x, u_aux, label="T = " + str(i*t/paso) + 's')

        b[0] = mu*alfa
        b[-1] = mu*beta
        ui = A.dot(ui) + b



    plt.xlim(-0.1, L+0.5)
    plt.title("Ecuacion de diferencias finitas ")
    plt.legend()
    plt.grid()
    plt.show()

from math import sin,pi
def fun_Cal2(x):
    n = 0
    return sin(n*pi*x)+sin(n+1)*pi*x

def fun_Cal(x):
    return 4-abs(4*x-1)-abs(4*x-3)

if __name__ == "__main__":
    eqCalor(0.0001, fun_Cal,0.5,3, t= 1, L = 1, gamma =0.20)
