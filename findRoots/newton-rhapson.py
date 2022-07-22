import math as m

def f(x):
    #f1 = m.e**(-1*x)
    fx = lambda x: x**3 +4*x**2 -10
    return fx(x)

def df(x):
    #f1 = -1*m.e**(-1*x)
    dfx = lambda x: 3*x**2 + 8*x
    return dfx(x)

def newton_raphson(a):
    x = a - f(a)/df(a)
    return x

def newtonRaphson(guess):
    print("Metodo de Newton Raphson")
    mystr = ""
    a = guess
    error = 10**-10
    current_error = error*2
    init = 0
    iterMax=13
    i=0
    bufferr = current_error
    while not current_error <= error:
        sig = newton_raphson(a)
        if(sig == 0):
            mystr += "\nEl numero siguiente es 0.\n"
            return mystr
        
        bufferr = current_error
        current_error = round(abs((sig-a)/sig),5)
        mystr += (f'''Iteracion #{i+1})\n''')
        mystr += (f"""x_i={round(a,8)} 
next x_i+1={round(sig,8)}
error={current_error}%\n\n""")
        a = sig

        # if(bufferr < current_error):
        #     mystr += f"El error actual({round(current_error,4)}%) es mayor "
        #     mystr += f"que el anterior({round(bufferr,4)}%)"
        #     mystr += f"\nSignifica que no se encontro la raiz con el punto {sig}"
        #     mystr += " \no la ecuacion no tiene raices"
        #     return mystr
        
        if(iterMax == 0):
            mystr += ("Numero Max de Iteraciones alcanzado \n")
            mystr += f"Significa que no se encontro la raiz con el punto {sig}"
            return mystr

        if current_error <= error:
            return mystr
        
        i+=1
        iterMax-=1

if __name__ == "__main__":
    mystr = newtonRaphson(2)
    print(mystr)
