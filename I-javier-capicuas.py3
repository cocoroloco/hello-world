#Leer la primera entrada
numero = input().strip() # En este problema nos interesa que se considere como una cadena de carcteres
#print(numero)
#print(len(numero))

while numero != "0":
    invertido = ""
    for i in range(len(numero), 0, -1):
        invertido = invertido + numero[i-1] 
    #print(invertido)
    if numero == invertido:
        print("S")
    else: 
        print("N")
    numero = input().strip()
        