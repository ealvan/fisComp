import math 

from data import DATA,CONSTANTE_GRAVITACIONAL
from ejer1 import getGravity

def getDensity(planet):
    planetdata = DATA[planet]
    radio = planetdata.get("radio")
    if(not(planetdata and radio)):
        print("El planeta {planet} o su radio de {radio} metros no existe...")
        exit(1)
    gravity = getGravity(planet,0)
    pi = math.pi
    G = CONSTANTE_GRAVITACIONAL
    densidad = (3/4)*((gravity)/(G*pi*radio))
    densidad = densidad*(10**-3)
    densidad = round(densidad,4)
    return densidad

def main():
    print("FORMULA:\n Densidad = (3/4)*(g/(G*pi*radio))")
    for k in DATA.keys():
        density = getDensity(k)
        print(f"La densidad del planeta {k} es : {density} kg/m3")
    
if __name__ == "__main__":
    main()