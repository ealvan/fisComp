import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np
import math as m
import time

def ecuacionCalor(dt,f,alfa,beta,t=1,L=1,gamma=0.5):
    L0 = 0
    t0 = 0
    var_graf = 0.1
    dx = m.sqrt(2*gamma*dt)#(dt**(1/2))/(2*gamma)
    print("dx= ", dx)
    print("dt= ", dt)
    
    mx = (L -L0)/dx 
    nt = (t - t0)/dt 
    nt = int(nt)
    mx = int(mx)

    x = np.linspace(L0, L, mx)
    print(f"La malla es de {nt}x{mx}")
    s = gamma*(dt/(dx**2))
    print("S es : ", s)
    malla = np.zeros((nt,mx))

    malla[:,0] = alfa
    malla[:,malla.shape[1]-1] = beta
    #Condiciones iniciales al inicio de la barra:
    for j in range(0,malla.shape[1]):
            malla[malla.shape[0]-1, j] = f(x[j])

    for i in range(malla.shape[0]-1, 0,-1):
        for j in range(1,malla.shape[1]-1):            
            try:
                tmp1 = s*(malla[i,j-1]+ malla[i,j+1])
                tmp2 = (1-2*s)*malla[i,j]
                malla[i-1,j] = tmp1+tmp2
            #un try catch si algun valor es muy pequenio
            #que se hace NaN
            except:
                print(f"[{i+1},{j}]")
                print(f"[{i},{j-1}]")
                print(f"[{i},{j+1}]")
                print(f"[{i},{j}]")
                break
    malla = np.nan_to_num(malla) 
    fig = plt.figure()
    getplot(x,malla,var_graf,dt,t,nt,fig)
    getCalorMap(malla,fig,alfa,beta)
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

def getplot(x,malla,var_graf,dt,t,nt,fig):
    bx = fig.add_subplot(122)#ubicar fila 1 col 2
    #cortando verticalmente la malla, para ver el comportamiento
    #por tiempos
    for i in range(1,malla.shape[0]):
        if(i % (var_graf/dt) == 0):
            bx.plot(x,malla[malla.shape[0]-i,:],label="T=" + str(round(i*t/malla.shape[0],3)) + 's')    
    bx.legend()#la legenda de cada funcion
    bx.grid()#los cuadrantes

#el mapa de calor del lado derecho
def getCalorMap(malla,fig,t0,tf):
    ax = fig.add_subplot(121)#ubicar en fila 1 col 1

    dark_jet = cmap_map(lambda x: x*1, matplotlib.cm.jet)
    # ax = plt.subplot()
    im = ax.imshow(malla,cmap=dark_jet,aspect='auto')

    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)
    
    # im.set_clim(-0.7,1)#especificar limites, para que no sean automaticos
    fig.colorbar(im,cax = cax,orientation='vertical')#la barra de colores

def main():
    # f = lambda x: m.sin(x)
    # f_test = lambda x: 0
    n = 0.6
    #1-3
    f1 = lambda x: m.cos(x)#m.sin(n*x)+m.sin(n-1)*x

    ecuacionCalor(0.0001,f1,0,0,t=1,L=1,gamma=0.3)

if __name__ == "__main__":
    main()



    # f2 = lambda x: 4-abs(4*x-1)-abs(4*x-3)
    # f3 = lambda x: m.cos(x)