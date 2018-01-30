import sys

#Altura de la pirámide
altura = int(input())
if (altura < 1) or (altura > 9):
    print("Error de la altura")
    sys.exit(0)

if altura == 1:
    print(1)
    sys.exit(0)

#Creamos la base de la pirámide 
salida = ""
for i in list(range(1, altura+1)):
    salida = salida + str(i)
for i in list(range(1, altura)):
    salida = salida + str(altura-i)

#Imprimimos la piramide invertida, guardando cada linea en la pila piramide
print(salida)
piramide = []
piramide.insert(0, salida)

for i in list(range(1, altura)):
    salida = salida.replace(str(i)," ")
    print(salida)
    piramide.insert(0, salida)

#Imprimimos la piramide invertida
for i in list(range(1, len(piramide))):
    print(piramide[i])