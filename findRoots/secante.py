import math as m

def f(x):
    fx = lambda x: 10*m.e**(x/2)*m.cos(2*x)-4
    return fx(x)

def secante(a,b):
    p1 = f(b)
    p2 = a-b
    p3 = f(a) - f(b)
    result = b - p1*p2/p3
    return result

def secanteMethod(guesses):
    print("Metodo de la Secante")
    mystr = ""
    a = guesses[0]
    b = guesses[1]
    error = 10**-10
    current_error = error*2
    init = 0
    iterMax=13
    i=0
    while not current_error <= error:
        sig = secante(a,b)
        if(sig == 0):
            mystr += "\nEl numero siguiente es 0.\n"
            return mystr

        current_error = round(abs((sig-b)/sig),5)
        mystr += (f'''Iteracion #{i+1})\n''')
        mystr += (f"""a={round(a,8)} 
b={round(b,8)} 
f(a)={round(f(a),8)} 
f(b)={round(f(b),8)} 
siguiente b={round(sig,8)} 
error={current_error}%\n\n""")
        a = b
        b = sig
        
        if(iterMax == 0):
            mystr += ("Numero Max de Iteraciones alcanzado \n")
            break
        if current_error <= error:
            return mystr
        i+=1
        iterMax-=1

if __name__ == "__main__":
    mystr = secanteMethod([-1,0.1])
    print(mystr)