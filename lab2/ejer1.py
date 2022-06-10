import pprint
A = 0
B = 0
def createMatrix(a,b):
    global A,B
    A = a 
    B = b
    rows, cols = (a, b)
    arr = [[0]*cols]*rows
    # pprint.pprint(arr)
    return arr

def getCoord(arr,a,b):
    c = len(arr[0])-1
    h = [0,0]
    h[0] = b
    h[1] = c-a

    return h

def printMatrix(arr,a,b):
    xd = 1
    xu = 3
    yl = -1
    yu = 5
    count = 0
    for i in range(a):
        for j in range(b):
            count+=1
            x,y = getCoord(arr,i,j)
            # print(count,"x:",x,"y:",y,"i:",i,"j:",j)
            if(y == 0):
                # arr[x][0] = xd
                pass
            elif(y == b-1):
                arr[b-1][x] = xu
                print(b-1,"--",x)
            else:
                arr[i][j] = -1
    # for i in range(a):
    #     for j in range(b):
    #         count+=1
    #         x,y = getCoord(arr,i,j)
    #         if(x == 0):
    #             pass
    #             arr[y][0] = yl
    #         if(x == a-1):
    #             pass
    #             arr[y][x] = yu
    for item in arr:
        print(item,end='\n')
    # pprint.pprint(arr)

def fillInitMatrix(arr,xu,xd,yl,yr):
    printMatrix(arr,4,4)
def main():
    matrix = createMatrix(4,4)
    printMatrix(matrix,4,4)
    # fillInitMatrix(matrix,4,0,0,4)

if __name__ == "__main__":
    main()


