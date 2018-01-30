import numpy as np # Vamos a tratar la lista de puertas como una matriz y aplicar operaciones de matrices

#Leer el número de puertas
num_puertas = int(input())

#Leer las líneas con las operaciones
acciones = input()
acciones = acciones.split()
#print (acciones)

''' 
T : Cierra TODAS las puertas.

I : Abre todas las cerradas y cierra todas las abiertas (INVERTIR).

C : Abre todas las cerraduras cuyo identificador es divisible por CUATRO.

S : Cierra todas las cerraduras que tienen un identificador divisible por SIETE.

U : Abre la ÚLTIMA puerta que esté cerrada (última según el número identificador). Si no hay ninguna cerrada, no hace nada.

P : Cierra la PRIMERA puerta que esté abierta (primera según el número identificador). Si no hay ninguna abierta, no hace nada.

M : MUESTRA por pantalla n caracteres A (abierta) o C (cerrada) en función del estado de cada puerta. Deben ir separados por un espacio.

F : FINALIZAR.

Puerta abierta A=1 / Puerta cerrada C=0
'''    
#Crea todas las puertas abiertas

puertas = [1] * num_puertas
#print(puertas)
puertas = np.matrix(puertas) #La convertimos a una matriz para trabajar con una matriz booleana (1's y 0's <--> abiertas y cerradas)
#print(puertas)

#print(puertas[0])
#puertas[0, 0] = 0
#print(puertas[0])
#print(puertas[0, 0], "   ", puertas [0, 1])


for accion in acciones:
    #print(accion)
    if accion == 'T': # Cierra TODAS las puertas.
            puertas = 0*puertas
            #print(accion, " --> ", puertas)
    elif accion == 'I': #Invertir todas
            puertas = np.logical_not(puertas)
            #print(accion, " --> ", puertas)
    elif accion == 'C': #Abre todas las cerraduras cuyo identificador es divisible por CUATRO.
            for i in range(0, num_puertas, 4): # range([start], stop[, step]). eg. range(3) == [0, 1, 2]. 
                puertas[0, i] = 1
    elif accion == 'S': #Cierra todas las cerraduras que tienen un identificador divisible por SIETE.
            for i in range(0, num_puertas, 7): # EL cero es divisible por cualquier numero natural
                puertas[0, i] = 0
    elif accion == 'U': #Abre la ÚLTIMA puerta que esté cerrada (última según el número identificador). Si no hay ninguna cerrada, no hace nada.
            for i in range(num_puertas-1, -1, -1):
                if puertas[0, i] == 0:
                    puertas[0, i] = 1
                    break
    elif accion == 'P': #Cierra la PRIMERA puerta que esté abierta (primera según el número identificador). Si no hay ninguna abierta, no hace nada.
            for i in range(0, num_puertas, 1):
                if puertas[0, i] == 1:
                    puertas[0, i] = 0
                    break
    elif accion == 'M': #MUESTRA por pantalla n caracteres A (abierta) o C (cerrada) en función del estado de cada puerta. Deben ir separados por un espacio.
            salida = ""
            for i in range(0, num_puertas, 1):
                if puertas[0, i] == 1:
                    salida = salida + "A "
                    #salida = salida + str(i) + " A "
                elif puertas[0, i] == 0:
                    salida = salida + "C "
                    #salida = salida + str(i) + " C "
                else:
                    print("Error puerta ", i, " = ",puertas[0, i])
            print(salida)
    elif accion == 'F': #FINALIZAR
            break
    else:
        print("Error accion ", accion) 

# Ejemplo del enunciado: 9 -- M T C U M I S P M F 
# Resultado: 
# A A A A A A A A A 
# A C C C A C C A A 
# C C A A C A A C C
