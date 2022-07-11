import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np
import math as m
import time


def getAnaliticalPlot(f,x_items,y_items,a=0,b=1):
    a = 0
    b = 1
    t0=0
    tf=10
    f = lambda x,t: m.sin(m.pi*x)*( m.cos(m.pi*t) + m.sin(m.pi*t)/m.pi )

    x_axis = np.linspace(a,b,x_items)
    y_axis = np.linspace(t0,tf,y_items)

    malla = np.zeros((x_items,y_items))
    def getCalorMap(arr):
        plt.imshow(arr,cmap='hot',interpolation='nearest')
        plt.show()
    
    for i in range(0,malla.shape[0]-1):
        for j in range(0,malla.shape[1]-1):
            malla[i][j] = f(x_axis[i],y_axis[j])

    getCalorMap(malla)
#xf: longitud final
#tf: tiempo final
#v: velocidad
#Condiciones Iniciales: (a <= x <= b)
    #f: funcion f(x) = u0(x,t)
    #g: funcion g(x) = u1(x,t)
#Condiciones Frontera: (t >= 0)
#phi1: u(a,t)
#phi1: u(b,t)
def ecuacionOnda(xf,tf,v,f,g,phi1,phi2,nx,nt):
    x0 = 0#longitud inicial
    t0 = 0#tiempo inicial
    dx = (xf-x0)/nx#es la diferencial en x 
    dt = (tf-t0)/nt#es la diferencial en t

    r = (dt**2)/(dx**2) #r es la que junta las constantes
    r_2 = r*v**2 #multiplicando por la velocidad^2

    #numero de graficos para la segunda grafica
    var_graf = 0.01
    #creando los eje T(tiempo) y eje X(longitud)
    x_axis = np.linspace(x0,xf,nx)
    t_axis = np.linspace(t0,tf,nt)

    #para probar es dx = dx_test
    # dx_test = abs(x_axis[0]-x_axis[1])
    # dt_test = abs(t_axis[0]-t_axis[1])

    malla = np.zeros((nt,nx))
    #comprobando el numero de elementos
    # print(len(t_axis),"--"*3,len(malla[:,0]))

    #evaluando las funciones phi1 y phi2
    for j in range(len(t_axis)):
        malla[j, 0] = phi1(t_axis[j])
        malla[j,malla.shape[1]-1] = phi2(t_axis[j]) 

    #comprobando el numero de elementos
    # print(len(x_axis),"--"*3,len(malla[0,:]))

    #evaluando la primera y la antepenultima fila...
    for i in range(len(x_axis)):
        malla[malla.shape[0]-1,i] = f(x_axis[i]) # parte t = 0
        malla[malla.shape[0]-2,i] = g(x_axis[i])#*dt + f(x_axis[i]) #t = 1
        
    #implementado la funcion numerica de la ecuacion de onda
    for j in range(malla.shape[0]-2,0,-1):# tiempo t
        for i in range(1,malla.shape[1]-2):# espacio x
            p1 = r*(malla[j,i-1] - 2*malla[j,i] + malla[j,i+1]) 
            p2 = 2*malla[j,i] - malla[j+1,i]
            malla[j-1,i] = p1 + p2

    #una figura para tener dos subgraficos
    fig = plt.figure()
    #poniendo las dos graficas
    getCalorMap(malla,fig,t0,tf)
    getplot(t_axis,malla,var_graf,dt,tf,nt,fig)
    #mostrar grafica
    plt.show()

#funcion sacada de la documentacion de matplotlib
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

#para lograr el 2do grafico
def getplot(x,malla,var_graf,dx,xf,nx,fig):
    bx = fig.add_subplot(122)#colocarlo a la derecha

    for i in range(1,malla.shape[1]):
        if(i % (var_graf/dx) == 0):
            bx.plot(x,malla[:,malla.shape[1]-i])
    bx.set_xlabel('X(eje x)')
    bx.set_ylabel("T(tiempo)")
    bx.set_title("Mapa de Transversal de la Ecuacion de Onda.")

    # bx.legend()#mostrar las leyendas de cada funcion
    bx.grid()#modo malla

#para lograr el 1er grafico
def getCalorMap(malla,fig,t0,tf):
    ax = fig.add_subplot(121)#primero a la izquierda
    #elegir los colores para el mapa de calor
    dark_jet = cmap_map(lambda x: x*1, matplotlib.cm.jet)
    im = ax.imshow(malla,cmap=dark_jet,aspect='auto')
    #para hacer la barra de colores
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)
    # im.set_clim(t0,tf)#para especificar el maximo y minimo de la barra de colores
    
    ax.set_xlabel('X(eje x)')
    ax.set_ylabel("T(tiempo)")
    ax.set_title("Mapa de Calor de la Ecuacion de Onda.")
    fig.colorbar(im,cax = cax,orientation='vertical')

def main():
    xf = 1#longitud final
    tf = 1#tiempo final
    v = 1#velocidad 
    #nx < nt
    #malla
    nx = 100#cols
    nt = 300#filas
    #condiciones frontera e iniciales
    f = lambda x: abs(4*x-1)
    g = lambda x: 0
    phi1 =lambda x: 0
    phi2 = lambda x: 0
    #ecuacion de onda
    ecuacionOnda(xf,tf,v,f,g,phi1,phi2,nx,nt)

if __name__ == "__main__":
    # main()
    #def getAnaliticalPlot(f,x_items,y_items,a=0,b=1):
    getAnaliticalPlot(None,100,300,0,1)