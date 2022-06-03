from data import DATA,CONSTANTE_GRAVITACIONAL
import random

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
        # h = int(h)
        gravity = getGravity(k,h)
        print(f"El planeta {k} tiene una gravedad de {gravity} m/s^2")

if __name__ == "__main__":
    main()
    