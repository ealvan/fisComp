import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np 


# def mean() hara el trabajo de media


def fillMatrix(arr,xu,xd,yl,yr):
    arr[0,:] = xu
    arr[arr.shape[0]-1,:] = xd
    arr[0:,0] = yl
    arr[:,arr.shape[1]-1] = yr
    arr[1,:arr.shape[1]-2]
    arr[1:arr.shape[0]-1,1:arr.shape[1]-1] = (xu+xd+yl+yr)/4

def calculate(arr):
    for i in range(1,arr.shape[0]-1):
        for j in range(1,arr.shape[1]-1):
            arr[i,j] = 0.25*(arr[i+1][j]+arr[i-1][j]+arr[i][j+1]+arr[i][j-1])

def getCalorMap(arr):
    plt.imshow(arr,cmap='hot',interpolation='nearest')
    plt.show()

def main():
    a = 16
    b = 16
    x_upper = 4
    x_down = 0
    l_left = 0
    l_right= 4
    malla = np.zeros((a,b))
    fillMatrix(malla,x_upper,x_down,l_left,l_right)
    calculate(malla)
    getCalorMap(malla)
    # print(malla)

if __name__ == "__main__":
    main()





