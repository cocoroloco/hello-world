#Leer los kms del deposito lleno
repostado = int(input())

#Lee el recorrido
distancia = int(input()) #Lee la primera distancia
distancias = [] #Inicia a vacia la lista de distancias

while distancia != 0:
    distancias.append(distancia)
    distancia =  int(input())#Lee la siguiente distancia
#print(distancias)
#print(len(distancias))

salida = ""
sum = distancias[0]
for i in range(len(distancias)-1):
    sum += distancias[i+1]
    if sum >= repostado:
        salida = salida + "1 "
        sum = 0
        #print(i, "  ", salida)
    else:
        salida = salida + "0 "
        #print(i,"  ", salida)

#Salida del resultado de paradas propuestas
print(salida.strip()) # Ejemplo entrada: 50 --- 45  10  34  24  25  0   SOLUCION: 1010