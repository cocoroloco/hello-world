def Comprobar_Fibonacci (x): #Comprueba si el número x es Fibonacci o no, devuelve texto como respuesta
    fib1 = 0
    fib2 = 1
    fib = fib1 + fib2
    while x >= fib:
        if x == fib:
            return("Fibonacci")
        fib1 = fib2
        fib2 = fib
        fib = fib1 + fib2
    return("No Fibonacci")

# print(Comprobar_Fibonacci(5)) #Comprobar que funciona la funcion

#Leer el número de entradas
num_lineas = int(input())

while num_lineas > 0:
    numero = int(input())
    print(Comprobar_Fibonacci(numero))
    # num_lineas = num_lineas - 1 # En Python es más común usar += -= *= /=
    num_lineas -= 1
    