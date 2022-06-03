#tercera ley de kepler
from data import CONSTANTE_GRAVITACIONAL,DATA
import math
def getPeriodPlanet(planet):
    sol = {
        "masa": 1.989*10**30,
        "radio": 696340*10**3
    }
    planet_data = DATA[planet]
    planet_radio = planet_data["radio"]
    toSun = planet_data["sunDistancia"]
    # print("SOL distanci: ",toSun)
    # toSun = 1.496*10**11 #metros
    G = CONSTANTE_GRAVITACIONAL
    sqrt = math.sqrt 
    pi = math.pi
    K = (4*pi**2)/(G*sol["masa"])
    R = sol["radio"]+toSun+planet_radio
    periodo = sqrt(K*R**3)
    return periodo

def main():
    for planet in DATA.keys():
        period = getPeriodPlanet(planet)     
        magnitug = "dias"
        if(period/(3600*24) >= 400):
            period = period/(3.1536*10**7)
            magnitug = "años"
        else:
            period = period/(3600*24)
            magnitug = "días"
        print(f"El periodo de {planet} es :{period} {magnitug}")
        

if __name__ == "__main__":
    main()