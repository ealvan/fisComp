from data import CONSTANTE_GRAVITACIONAL,DATA
import math

#EJERCICIO 3:
#tercera ley de kepler
#Formula para obtener el periodo de un
#Planeta alrededor del sol
#ejemplo la tierra da una vuelta en 365 segundos

# Formula:
#     K = (4*pi)/(G*Ms)
    # Ms = masa del sol (kg)
    # G = constante universal (N*m^2)/(kg^2)
# Formula: 
#     T^2 = K * Rp^3
    # Rp = distancia entre sol y planeta desde sus centros (metros)
    # K = constante K en (s^2/m^3)
    # T = periodo (segundos)

K = 0 # constante K
R = 0 # Rp distancia al sol
toSun = 0#distancia al sol Ms
sol = {
        "masa": 1.989*10**30,
        "radio": 696340*10**3
}
def getPeriodPlanet(planet):
    
    planet_data = DATA[planet]
    planet_radio = planet_data["radio"]
    toSun = planet_data["sunDistancia"]
    G = CONSTANTE_GRAVITACIONAL
    sqrt = math.sqrt 
    pi = math.pi
    K = (4*pi**2)/(G*sol["masa"])
    #distancia del sol al planeta
    R = sol["radio"]+toSun+planet_radio
    periodo = sqrt(K*R**3)
    return periodo

def printData(planet,period):
    #K T Ms Rp
    magnitug = "dias"
    if(period/(3600*24) >= 400):
        period = period/(3.1536*10**7)
        magnitug = "años"
    else:
        period = period/(3600*24)
        magnitug = "días"
    str1 = f"""---------------------------------------------
Planeta : {planet}
K = {K} s^2*m^-3
R = {R} metros
Masa del Sol = {sol["masa"]} kg
G = {CONSTANTE_GRAVITACIONAL} (N*m^2)/(kg^2)

Respuesta => Periodo({planet}) = {round(period,4)} {magnitug}
---------------------------------------------"""
    print(str1)


def main():
    for planet in DATA.keys():
        period = getPeriodPlanet(planet)
        printData(planet,period)
    print("Lista de Periodos por planeta.")
    for planet in DATA.keys():
        period = getPeriodPlanet(planet)
        magnitug = "dias"
        if(period/(3600*24) >= 400):
            period = period/(3.1536*10**7)
            magnitug = "años"
        else:
            period = period/(3600*24)
            magnitug = "días"
        print(f"Periodo({planet}) = {round(period,3)} {magnitug}")
        
if __name__ == "__main__":
    main()
