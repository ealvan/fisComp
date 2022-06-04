import math 

from data import DATA,CONSTANTE_GRAVITACIONAL
from ejer1 import getGravity

# EJERCICIO 2:
#  Del problema anterior realice un codigo 
#  para poder determinar la densidad de 
#  cualquier planeta del sistema planetario solar.

# densidad = (3/4)*(g/(G*pi*R))

#Unidades:
    # g = gravedad (m/s^2)
    # G = constante universal (N*m^2)/(kg^2)
    # R = radio del planeta en (metros)
#DENSIDAD en kg/m^3 -> g/cm^3
gravity = 0
def getDensity(planet):
    planetdata = DATA[planet]
    radio = planetdata.get("radio")
    if(not(planetdata and radio)):
        print("El planeta {planet} o su radio de {radio} metros no existe...")
        exit(1)
    global gravity
    gravity = getGravity(planet,0)
    pi = math.pi
    G = CONSTANTE_GRAVITACIONAL
    densidad = (3/4)*((gravity)/(G*pi*radio))
    #cambiando de  kg/m^3 -> g/cm^3  con (10^-3)
    densidad = densidad*(10**-3)
    densidad = round(densidad,4) #redondeo de 4 decimales
    return densidad

def printData(planeta,densidad):
    G = CONSTANTE_GRAVITACIONAL
    planet_data = DATA[planeta]
    R = planet_data["radio"]
    str1 = f"""Planeta : {planeta}
G = {G} (N*m^2)/(kg^2) (constante Universal)
Radio = {R} metros
g = {gravity} m/s^2

RESPUESTA => Densidad({planeta}): {round(densidad,2)} g/cm^3
"""
    print("-"*36,str1,"-"*36)

def main():
    print("FORMULA:\n Densidad = (3/4)*(g/(G*pi*radio))")
    for k in DATA.keys():
        density = getDensity(k)
        printData(k,density)
    print("Lista por Planeta:")
    for k in DATA.keys():
        density = getDensity(k)
        print(f"Densidad({k}) = {round(density,3)} g/cm^3")

if __name__ == "__main__":
    main()