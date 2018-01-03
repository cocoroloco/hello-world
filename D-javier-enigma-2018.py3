num_maquinas = int(input())

j=1
while j <= num_maquinas:
    
    linea = input()
    maquina = linea.split()

    rotores = int(maquina[0])

    i = 1
    combinaciones = 1 # Producto de las combinaciones de los rotores
    while i <= rotores:
        a =  int(maquina[i])
        combinaciones = combinaciones * a
        print(i, " -->", maquina[i], rotores)
        i = i + 1
    print(combinaciones)
    j += 1
    