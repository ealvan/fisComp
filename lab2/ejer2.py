import matplotlib.pyplot as plt
import numpy as np 
#LAPLACE -> 
#Ua= Yl
#Ub= Yr
#Uc= Xd
#Ud= Xu
#N = a
#M = b
#H = 1000 iterations
#Error: 0.0001 error
# def mean() hara el trabajo de media

def fillMatrix(arr,xu,xd,yl,yr):
    arr[0,:] = xu
    arr[arr.shape[0]-1,:] = xd
    arr[0:,0] = yl
    arr[:,arr.shape[1]-1] = yr
    arr[1,:arr.shape[1]-2]
    arr[1:arr.shape[0]-1,1:arr.shape[1]-1] = (xu+xd+yl+yr)/4

def calculate(arr,times,error):
    convergencia = 0
    contador = 0
    # tmp = arr
    while(contador < times and convergencia == 0):
        tmp = arr
        for i in range(1,arr.shape[0]-1):
            for j in range(1,arr.shape[1]-1):
                arr[i,j] = 0.25*(arr[i+1][j]+arr[i-1][j]+arr[i][j+1]+arr[i][j-1])
        # if(np.linalg.norm(arr-tmp,np.inf)/np.linalg.norm(arr,np.inf) < error):
        #     convergencia = 1
        contador+=1
    # if(convergencia == 1):
    getCalorMap(arr)
    print(f"contador:{contador}\n[arr-tmp]={np.linalg.norm( tmp)}\n[arr]={np.linalg.norm(arr)}")
    # print(arr[:int(arr.shape[0]/2),:int(arr.shape[1]/2)])

def getCalorMap(arr):
    plt.imshow(arr,cmap='hot',interpolation='nearest')
    plt.show()

def Laplace(arriba,abajo,izq,dere, filas, cols,h,error):
    malla = np.zeros((filas,cols))#creando malla
    fillMatrix(malla,arriba,abajo,izq,dere)#llenando malla
    calculate(malla,h,error)

def main():
    filas = 100
    cols = 100
    x_upper = 0
    x_down = 80
    l_left = 20
    l_right= 300
    times = 500
    error=0.001
    Laplace(x_upper, x_down, l_left, l_right, filas, cols, times, error)
    # print(malla)

if __name__ == "__main__":
    main()