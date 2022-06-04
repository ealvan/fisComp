from data import DATA,CONSTANTE_GRAVITACIONAL
import random
#EJERCICIO 1
# A partir de la segunda ley de movimiento de Newton y 
# la ley de gravitación universal realice un código que 
# permita determinar el valor de la gravedad para 
# cualquier planeta del sistema planetario solar.

#Formula = (G*masaPlaneta)/(R+h)^2

#unidades:
    #masas en Kg
    #G = constante universal (N*m^2)/(kg^2)
    #R y h = Distancias en metros

def getGravity(planet,h):
    planetData =DATA[planet]
    mass = planetData["masa"]
    radius = planetData["radio"]
    if not(mass and radius):
        print("No existe este planeta en nuestra base de datos...")
        exit(1)
    if h > radius:
        print("No puede ser mayor al radio del planeta")
        exit(1)
    G = CONSTANTE_GRAVITACIONAL
    gravity = (G*mass)/((radius+h)**2)
    return gravity 
def printData(planeta,h,gravity):
    G = CONSTANTE_GRAVITACIONAL
    planet_data = DATA[planeta]
    masa = planet_data["masa"]
    R = planet_data["radio"]
    str1 = f"""Planeta : {planeta}
G = {G} (N*m^2)/(kg^2)
R = {R} metros
h = {h} metros
Masa = {masa} kg

RESPUESTA => Gravedad({planeta}): {round(gravity,4)} m/s^2
"""
    print("\n","-"*36,str1,"\n","-"*36)

def main():
    print("FORMULA: \ng = (G*Mp)/(R+h)**2")
    for k in DATA.keys():
        h = input(f"Ingrese una h, de acuerdo a la formula(planeta {k}):")
        if(h == "exit"):
            print("Usted ha salido con exito del programa...")
            exit(0)
        h = int(h)
        while(h < 0):
            print("La distancia no puede ser negativa...")
            h = input(f"Ingrese una h, de acuerdo a la formula(planeta {k}):")
            if(h == "exit"):
                print("Usted ha salido con exito del programa...")
                exit(0)
            h = int(h)
        gravity = getGravity(k,h)
        printData(k,h,gravity)#imprimiendo datos
    for k in DATA.keys():
        print("\n","Planeta = ",k,"Gravedad=",getGravity(k,0),"m/s^2")

if __name__ == "__main__":
    main()
    