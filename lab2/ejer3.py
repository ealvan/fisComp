from math import pi,sinh,sin
import numpy as np
import matplotlib.pyplot as plt
INFINIT0 = 100

#constantes de la ecuacion
cts = {
    "V2":0, 
    "V1":1,
    "a":1,
    "b":1,
}
#esta funcion implementa la ecuacion del problema 3
def funcion(x,y):
    const = 4/pi
    a = cts["a"]
    b = cts["b"]
    V1 = cts["V1"]
    V2 = cts["V2"]
    general2=0
    for n in range(1,INFINIT0,2):
        c1 = 1/n
        part1 = V2*sinh(((n*pi)/b)*x)
        part2 = V1*sinh(((n*pi)/b)*(a-x))
        denomi = sinh(((n*pi)/b)*a)
        part3 = sin(((n*pi)/b)*y)
        general2 += c1*((part1+part2)/denomi)*part3
    return const*general2

#aqui se itera la matriz y se usa la funcion solucion
def calculate(arr):
    a = cts["a"]
    b = cts["b"]

    x=np.linspace(0,a,arr.shape[0])
    y=np.linspace(0,b,arr.shape[1])

    for i in range(0,arr.shape[0]-1):
        for j in range(0,arr.shape[1]-1):
            #aqui se esta usando la funcion
            arr[i][j] = funcion(x[i],x[j])

#para obtener el mapa de calor.
def getCalorMap(arr):
    plt.imshow(arr,cmap='hot',interpolation='nearest')
    plt.show()

#parte central de los metodos.
def analiticalFuncion(nx,ny):
    malla = np.zeros((nx,ny))
    calculate(malla)
    getCalorMap(malla)

def main():
    filas = 50
    cols = 50
    analiticalFuncion(filas,cols)


if __name__ == "__main__":
    main()



