import matplotlib.pyplot as plt
import numpy as np 
#LAPLACE -> 
#Ua= Yl izquierda
#Ub= Yr derecha
#Uc= Xd abajo
#Ud= Xu arriba
#N = a 
#M = b
#H = 500 iterations

def fillMatrix(arr,xu,xd,yl,yr):
    arr[0,:] = xu
    arr[arr.shape[0]-1,:] = xd
    arr[0:,0] = yl
    arr[:,arr.shape[1]-1] = yr
    arr[1,:arr.shape[1]-2]
    arr[1:arr.shape[0]-1,1:arr.shape[1]-1] = (xu+xd+yl+yr)/4

def calculate(arr,times):
    convergencia = 0
    contador = 0
    # tmp = arr
    while(contador < times and convergencia == 0):
        tmp = arr
        for i in range(1,arr.shape[0]-1):
            for j in range(1,arr.shape[1]-1):
                arr[i,j] = 0.25*(arr[i+1][j]+arr[i-1][j]+arr[i][j+1]+arr[i][j-1])
        contador+=1

    getCalorMap(arr)

def getCalorMap(arr):
    plt.imshow(arr,cmap='hot',interpolation='nearest')
    plt.show()

def Laplace(arriba,abajo,izq,dere, filas, cols,h):
    malla = np.zeros((filas,cols))#creando malla
    fillMatrix(malla,arriba,abajo,izq,dere)#llenando malla
    calculate(malla,h)


def main():
    filas  = 100 # nro de filas
    cols   = 100 # nro de columnas de la matriz
    x_upper= 300 # contorno de arriba
    x_down = 20 # contorno de abajo
    l_left = 80 # el lado izquierdo
    l_right= 0 # el lador derecho
    times  = 500 # nro de iteraciones
    Laplace(x_upper, x_down, l_left, l_right, filas, cols, times)

if __name__ == "__main__":
    main()