from math import pi,sinh,sin
import numpy as np 
import matplotlib.pyplot as plt
INFINIT0 = 100

#constantes
cts = {
    "V2":0,
    "V1":1,
    "a":1,
    "b":1,
}
#z=
#   z+4*(V2*sinh((N)*pi*x/b)+V1*sinh((N)*pi*(a-x)/b)).*
#   sin((N)*pi*y/b)/(sinh((N)*pi*a/b)*(N)*pi)

def funcion(x,y):
    const = 4/pi
    a = cts["a"]
    b = cts["b"]
    V1 = cts["V1"]
    V2 = cts["V2"]
    general2=0
    for n in range(1,INFINIT0,2):
        # print(f"((n:{n}*pi)/b:{b})*(a:{a}-x:{x})")
        c1 = 1/n
        part1 = V2*sinh(((n*pi)/b)*x)
        part2 = V1*sinh(((n*pi)/b)*(a-x))
        denomi = sinh(((n*pi)/b)*a)
        part3 = sin(((n*pi)/b)*y)
        general2 += c1*((part1+part2)/denomi)*part3
    return const*general2

def fillMatrix(arr,xu,xd,yl,yr):
    arr[0,:] = xu
    arr[arr.shape[0]-1,:] = xd
    arr[0:,0] = yl
    arr[:,arr.shape[1]-1] = yr
    arr[1,:arr.shape[1]-2]
    #(xu+xd+yl+yr)/4
    arr[1:arr.shape[0]-1,1:arr.shape[1]-1] = 0

def calculate(arr):
    a = cts["a"]
    b = cts["b"]

    x=np.linspace(0,a,arr.shape[0])
    y=np.linspace(0,b,arr.shape[1])

    for i in range(0,arr.shape[0]-1):
        for j in range(0,arr.shape[1]-1):
            arr[i][j] = funcion(x[i],x[j])

def getCalorMap(arr):
    plt.imshow(arr,cmap='hot',interpolation='nearest')
    plt.show()

def analiticalFuncion(nx,ny):
    malla = np.zeros((nx,ny))
    # fillMatrix(malla,xu,0,0,yr)
    calculate(malla)
    getCalorMap(malla)

def main():
    filas = 50
    cols = 50
    analiticalFuncion(filas,cols)


if __name__ == "__main__":
    main()



