import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np
import math as m

V = 1.1#la constante V de la formula

def createMalla(m,n):
    return np.zeros((m,n))
#funcion para obtener los colores para nuestra
#imagen(obtenida de la documentacion de python)
def cmap_map(function, cmap):
    """ Applies function (which should operate on vectors 
    of shape 3: [r, g, b]), on colormap cmap.
    This routine will break any discontinuous points in a colormap.
    """
    cdict = cmap._segmentdata
    step_dict = {}
    # Firt get the list of points where the segments start or end
    for key in ('red', 'green', 'blue'):
        step_dict[key] = list(map(lambda x: x[0], cdict[key]))
    step_list = sum(step_dict.values(), [])
    step_list = np.array(list(set(step_list)))
    # Then compute the LUT, and apply the function to the LUT
    reduced_cmap = lambda step : np.array(cmap(step)[0:3])
    old_LUT = np.array(list(map(reduced_cmap, step_list)))
    new_LUT = np.array(list(map(function, old_LUT)))
    # Now try to make a minimal segment definition of the new LUT
    cdict = {}
    for i, key in enumerate(['red','green','blue']):
        this_cdict = {}
        for j, step in enumerate(step_list):
            if step in step_dict[key]:
                this_cdict[step] = new_LUT[j, i]
            elif new_LUT[j,i] != old_LUT[j, i]:
                this_cdict[step] = new_LUT[j, i]
        colorvector = list(map(lambda x: x + (x[1], ), this_cdict.items()))
        colorvector.sort()
        cdict[key] = colorvector

    return matplotlib.colors.LinearSegmentedColormap('colormap',cdict,1024)

#f: es una lambda function
#malla: es la matriz
#x: es el array con la condicion inicial
def fillMalla(malla,f,x):
    # x = a:h:b es un array 
    x_f = np.array([f(item) for item in x])
    malla[:,0] = x_f

def calculate(malla,h,k):
    r = (V**2*k)/(h**2)#por el momento... k/h^2
    # for _ in range(40):
    for j in range(0,malla.shape[1]-1):
        for i in range(1,malla.shape[0]-1):
            malla[i,j+1] = r*malla[i-1,j] + (1-2*r)*(malla[i,j]) + malla[i+1,j]*r

def getCalorMap(arr,x,dt):
    malla = arr
    var_graf = 0.001
    # dark_jet = cmap_map(lambda x: x*1, matplotlib.cm.jet)
    # ax = plt.subplot()
    # im = ax.imshow(arr,cmap=dark_jet,aspect='auto')
    # divider = make_axes_locatable(ax)
    # cax = divider.append_axes("right", size="5%", pad=0.05)
    # plt.colorbar(im,cax = cax)
    # print("*"*12)
    # print(arr[:,0])
    # print(arr[:,10])
    # print(arr[:,15])
    plt.figure()
    for i in range(len(malla[:,0])):
        if(i %  (2) == 0):
            plt.plot(x,malla[:,i],label=f"T ={i*dt}segs")
    plt.title("Ecuacion de Calor")
    plt.legend()
    plt.grid()
    plt.show()

def ecuacionCalor(a,b,t0,tf,f,mx,ny):
    malla = createMalla(mx,ny)
    h = (b-a)/(mx-1)
    k = (tf-t0)/(ny-1)
    x = np.linspace(a,b,malla.shape[0])
    t = np.linspace(t0,tf, malla.shape[1])
    fillMalla(malla,f,x)
    calculate(malla,h,k)
    getCalorMap(malla,x,k)
    # print(malla[:,0])
    # print(malla[:,malla.shape[1]-1])

def main():
    #malla dimensions
    #x:
    mx = 40
    #y:
    ny = 300
    #Para x axis
    a = 0
    b = 1.2
    h = (b-a)/(mx-1)
    #Para y axis
    t0 = 0
    tf = 1
    k = (tf-t0)/(ny-1)
    #Condicion inicial
    n = 1
    f = lambda x: m.sin(n*m.pi*x) + m.sin(n+1)*m.pi*x#m.sin(m.pi*x)#
    #ecuacion de calor:
    ecuacionCalor(a,b,t0,tf,f,mx,ny)
    
if __name__ == "__main__":
    main()

