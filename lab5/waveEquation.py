import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np
import math as m
import time

def waveEquation(xf,tf,v,f,g,phi1,phi2,nx,nt):
    x0 = 0
    t0 = 0
    dx = (xf-x0)/nx
    dt = (tf-t0)/nt
    r = (dt**2)/(dx**2)
    r_2 = r*v**2

    var_graf = 0.1

    x_axis = np.linspace(x0,xf,nx)
    t_axis = np.linspace(t0,tf,nt)

    dx_test = abs(x_axis[0]-x_axis[1])
    dt_test = abs(t_axis[0]-t_axis[1])
    # print(dx_test,"<->"*2,dx)
    # print(dt_test,"<->"*2,dt)

    malla = np.zeros((nt,nx))
    # print(len(t_axis),"--"*3,len(malla[:,0]))
    for j in range(len(t_axis)):
        malla[j, 0] = phi1(t_axis[j])
        malla[j,malla.shape[1]-1] = phi2(t_axis[j]) 

    # print(len(x_axis),"--"*3,len(malla[0,:]))
    for i in range(len(x_axis)):
        malla[malla.shape[0]-1,i] = f(x_axis[i]) # parte t = 0
        malla[malla.shape[0]-2,i] = g(x_axis[i])#*dt + f(x_axis[i]) #t = 1
    
    # print(malla[malla.shape[0]-2,:])
    
    for j in range(malla.shape[0]-2,0,-1):# tiempo t
        for i in range(1,malla.shape[1]-2):# espacio x
            malla[j-1,i] = r*(malla[j,i-1] - 2*malla[j,i] + malla[j,i+1]) + 2*malla[j,i] - malla[j+1,i]
            # malla[j,i+1] = r*(malla[j-1,i] - 2*malla[j,i] + malla[j+1,i]) + 2*malla[j,i] -malla[j,i-1]

# r_2*(malla[j+1,i]+malla[j-1,i]) + 2*(1-r_2)*malla[j,i] - malla[j,i-1]

    # print(malla)
    # print(malla[malla.shape[0]-2,:])

    # print(malla[:,malla.shape[1]-1])
    # print(malla[:,malla.shape[1]-2])
    # print(malla[:,malla.shape[1]-3])
    
    

    fig = plt.figure()

    getCalorMap(malla,fig,t0,tf)
    getplot(t_axis,malla,var_graf,dt,tf,nt,fig)
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


def getplot(x,malla,var_graf,dx,xf,nx,fig):
    bx = fig.add_subplot(122)
    for i in range(1,malla.shape[1]):
        if(i % (var_graf/dx) == 0):
            bx.plot(x,malla[:,malla.shape[1]-i],label="T=" + str(round(x[malla.shape[1]-i],3)) + 'x')
    #malla.shape[0]-i,: #i*xf/malla.shape[1]
    bx.legend()
    bx.grid()

def getCalorMap(malla,fig,t0,tf):
    ax = fig.add_subplot(121)

    dark_jet = cmap_map(lambda x: x*1, matplotlib.cm.jet)
    # ax = plt.subplot()
    im = ax.imshow(malla,cmap=dark_jet,aspect='auto')

    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)
    # im.set_clim(t0,tf)
    fig.colorbar(im,cax = cax,orientation='vertical')

#def waveEquation(xf,tf,v,f,g,phi1,phi2,nx,nt):

def main():
    xf = 1
    tf = 3
    v = 1
    #nx < nt
    nx = 100
    nt = 300
    f = lambda x: m.sin(2*x)
    g = lambda x: 2*m.sin(x)
    phi1 =lambda x: 0
    phi2 = lambda x: 0
    waveEquation(xf,tf,v,f,g,phi1,phi2,nx,nt)

if __name__ == "__main__":
    main()