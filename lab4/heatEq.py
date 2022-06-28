import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np
import math as m


def createMalla(m,n):
    return np.zeros((m,n))

#funcion para obtener los colores para nuestra
#imagen(obtenida de la documentacion de python)
def cmap_map(function, cmap):
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
def fillMalla(malla,g1,g2):
    # x = a:dx:b es un array 
    # x_f = np.array([f(item) for item in x])
    # malla[:,0] = x_f
    # print(malla)
    malla[:,0] = g1
    malla[:,malla.shape[0]-1] = g2

def calculate(malla,dx,dt):
    s = (dt)/(dx**2)#por el momento... dt/dx^2
    # for _ in range(40):
    for j in range(0,malla.shape[1]-1):
        for i in range(1,malla.shape[0]-1):
            malla[i,j+1] = s*malla[i-1,j] + (1-2*s)*(malla[i,j]) + malla[i+1,j]*s

def getCalorMap(arr):
    dark_jet = cmap_map(lambda x: x*1, matplotlib.cm.jet)
    ax = plt.subplot()
    im = ax.imshow(arr,cmap=dark_jet,aspect='auto')
    # cs = ax.contourf(arr, levels=np.linspace(0, 1, 25))
    # divider = make_axes_locatable(ax)
    # cax = divider.append_axes("right", size="5%", pad=0.05)
    im.set_clim(0,1)
    # plt.colorbar(im,cax = cax)
    plt.show()

def ecuacionCalor(a,b,t0,tf,f,mx,ny,g1,g2):
    malla = createMalla(mx,ny)
    dx = (b-a)/(mx-1)
    dt = (tf-t0)/(ny-1)
    x = np.linspace(a,b,malla.shape[0])
    t = np.linspace(t0,tf, malla.shape[1])
    fillMalla(malla,g1,g2)
    calculate(malla,dx,dt)
    getCalorMap(malla)
    # print(malla[:,malla.shape[0]-1])


def main():
    #malla dimensions
    #x:
    mx = 20
    #y:
    ny = 300
    #for x axis
    a = 0
    b = 1
    dx = (b-a)/(mx-1)
    #for y axis
    t0 = 0
    tf = 0.2
    dt = (tf-t0)/(ny-1)
    #Condicion inicial
    f = lambda x: m.sin(m.pi*x)
    #Condiciones frontera:
    g1 = 1
    g2 = -1
    #ecuacion de calor:
    ecuacionCalor(a,b,t0,tf,f,mx,ny,g1,g2)

if __name__ == "__main__":
    main()