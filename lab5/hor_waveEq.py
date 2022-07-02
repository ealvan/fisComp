import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np
import math as m
import time

def waveEq(nx,nt,b,tf,f,g):
    a = 0
    t0 = 0
    dx = (b-a)/(nx-1)
    dt = (tf-t0)/(nt-1)

    x = np.linspace(a,b,nx)
    t = np.linspace(t0,tf,nt)
    
    s = (dt**2)/(dx**2)

    malla = np.zeros((nx,nt))
    for i in range(malla.shape[0]):
        malla[i,0] = f(x[i])
        malla[i,1] = g(x[i])#*dt + f(x[i]) + 
 
    # malla[:,0] = np.sin(m.pi*x)
    # malla[:,1] = np.sin(m.pi*x)*(1+dt)

    for j in range(1,malla.shape[1]-1):# tiempo t
        for i in range(1,malla.shape[0]-1): # espacio x
            malla[i,j+1] = s*(malla[i-1,j] -2*malla[i,j] + malla[i+1,j]) + 2*malla[i,j] - malla[i,j-1]

    # print(malla[:,1])

    fig = plt.figure()

    getCalorMap(malla,fig,t0,tf)
    plt.show()



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

def getCalorMap(malla,fig,t0,tf):
    ax = fig.add_subplot(111)

    dark_jet = cmap_map(lambda x: x*1, matplotlib.cm.jet)
    # ax = plt.subplot()
    im = ax.imshow(malla,cmap=dark_jet,aspect='auto')

    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)
    
    fig.colorbar(im,cax = cax,orientation='vertical')

def main():
    #nx < nt
    nx = 100
    nt = 300
    b = 1
    tf = 1
    f = lambda x: m.sin(2*x)
    g = lambda x: 2*m.sin(x)
    # malla[:,0] = np.sin(m.pi*x)
    # malla[:,1] = np.sin(m.pi*x)*(1+dt)
    #def waveEq(nx,nt,b,tf):
    waveEq(nx,nt,b,tf,f,g)
    pass

if __name__ == "__main__":
    main()
