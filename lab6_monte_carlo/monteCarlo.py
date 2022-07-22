from scipy import random
import matplotlib.pyplot as plt 
import math as m 
#a = limite de inicio de la integral
#b = limite final
#f = la funcion a aplicar en la integral
#N = el rango de numeros aleatorios entre a y b
def calcularArea_MonteCarlo(a,b,f,N):
    areas = []
    barras = 30#numero de barras a mostrar
    colors = ['tomato', 'blue', 'lime']#colores para el grafico
    for i in range(N):
        #esta funcion genera numeros aleatorios 
        #entre a y b, y lo hacen N veces
        equis = random.uniform(a,b,N)#numeros aleatorios
        integral = 0.0
        for i in range(N):
            integral += f(equis[i])

        answer = (b-a)/float(N)*integral
        #crear lista de todas las
        #areas que nos dan, con diferentes 
        #numeros aleatorios
        areas.append(answer)
    print("La integral es: ",answer)
    plt.title("Distribucion de Areas Calculadas",fontweight ="bold")

    plt.hist(areas, barras, density = True,
    histtype ='bar',
    color = colors[1],
    label="Cantidad de resultados",
    rwidth = 0.5)
    plt.legend(prop ={'size': 10})
    plt.xlabel("Areas")
    plt.show()

def main():
    a = -1
    b = 0
    f = lambda x: (1-(m.e**x)**2)**(1/2)
    N = 1000
    calcularArea_MonteCarlo(a,b,f,N)

if __name__ == "__main__":
    main()