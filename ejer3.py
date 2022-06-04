import math
#Ley de kepler #2
#areas iguales en tiempos iguales
from data import CONSTANTE_GRAVITACIONAL, DATA
from ejer4 import getPeriodPlanet

# Implementar un código computacional 
# para la solución de la segunda
# ley de Kepler.

#FORMULAS
    # L = I * w
    # I = Mp*(r^2)
    # w = (2*pi) / (1 anio en segs)
    # A = (L / 2*Mp)*t

#Significados y Unidades
    # t = tiempo en (segundos) 
    # L = momento angular((Kg*m^2)/s)
    # Mp= Masa del Planeta (Kg)
    # I = inercia (Kg*m^2)
    # r = distancia del sol al planeta desde sus centros (metros)
w = 0 #velocida angular
L = 0 # momento angular
I = 0 #inercia
def getAngularMomentum(planet):
    global w,I,L
    # L = I*w
    # I = m*r^2
    # w = 2*pi / 1 anio en segundos
    planet_data = DATA[planet]
    I = planet_data["masa"]*(planet_data["sunDistancia"])**2
    pi = math.pi
    period = getPeriodPlanet(planet)
    # period = period*60*60*24
    w = (2*pi)/(planet_data["periodo"]*24*60*60)
    L = I*w
    return L

def getAreaKepler2law(planet,tiempo):
    # A = (L / 2*Mp)*t
    if(tiempo < 0):
        print("El tiempo debe ser positivo")
        exit(1)
    L = getAngularMomentum(planet)
    masaPlaneta = DATA[planet]["masa"]
    area = (L/(2*masaPlaneta))*tiempo
    return area

def printData(planet,time,area):
    planet_data = DATA[planet]
    masa = planet_data["masa"]
    distanciaSol = planet_data["sunDistancia"]
    str1 = f"""
---------------------------------------------------
L = {float(f"{L:.3e}")} (kg*m^2)/s
I = {float(f"{I:.3e}")} kg*m^2
t = {time} segs
masa = {masa} kg
w = {float(f"{w:.3e}")} rad/s
r = {distanciaSol} metros

Respuesta => Área({planet}) en {time} segs = {round(area,4)} m^2
---------------------------------------------------
"""    
    print(str1)

def main():
    print("FORMULA: \nA = (L / 2*Mp)*t")
    print("Descripción:\nCalcula cuanto de área barre el planeta\nen \"t\" segundos")
    for k in DATA.keys():
        h = input(f"Ingrese el tiempo que recorrera(planeta {k}):")
        if(h == "exit"):
            print("Usted ha salido con exito del programa...")
            exit(0)
        h = float(h)
        while(h < 0):
            print("La distancia no puede ser negativa...")
            h = input(f"Ingrese el tiempo que recorrera(planeta {k}):")
            if(h == "exit"):
                print("Usted ha salido con exito del programa...")
                exit(0)
            h = float(h)
        area = getAreaKepler2law(k,h)
        printData(k,h,area)
    for planet in DATA.keys():
        momentum = getAngularMomentum(planet)
        area = getAreaKepler2law(planet,1)
        print(f"{planet}/L es: {float('{:0.2e}'.format(momentum))} (kg*m^2)/s")
        print(f"{planet}/Área es: {round(area,3)} m^2\n")

if __name__ == "__main__":
    main()

