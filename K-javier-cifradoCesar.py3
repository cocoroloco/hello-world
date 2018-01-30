num_pruebas = int(input())

texto_original = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num_codigos = len(texto_original) #Números de caracteres a codificar
#print(texto_original)

for caso in range(num_pruebas):
    clave = int(input()) #Desplazamiento usado para cifrar el mensaje
    mensaje = input() #Leemos el mensaje cifrado
    #diccionario_cifrado sera un diccionario con la transcripción para cada letra a su nueva letra cifrada
    diccionario_cifrado = dict() #declaramos diccionario_cifrado como un diccionario (inicialmente vacío)
    for i in range(0, num_codigos): #Añadimos los valores de caracteres y su cifrado
        #print(i, " --> ", texto_original[i])
        dir_elemento = (i + clave) % num_codigos #dirección del elemento a cifrar
        #print(dir_elemento)
        #diccionario_cifrado[texto_original[i]] = texto_original[dir_elemento]
        diccionario_cifrado[texto_original[dir_elemento]] = texto_original[i]
    #print(diccionario_cifrado.items())
    #Desciframos el mensaje
    mensaje_descifrado = ""
    for j in range(len(mensaje)):
        letra_entrada = mensaje[j]
        letra_salida = diccionario_cifrado.get(letra_entrada.upper(), None)
        if letra_salida == None:
            letra_salida = mensaje[j]
        elif mensaje[j].islower(): 
            letra_salida = letra_salida.lower()
        mensaje_descifrado = mensaje_descifrado + letra_salida
    print(mensaje_descifrado)
    caso += 1

'''
3
6
GHIJKLMNOPQRSTUVWXYZABCDEF
15
Thipbdh rtatqgpcsd ta pcxktghpgxd st Ijgxcv.
9
Exh j pjwja nbcn lxwldabx mn yaxpajvjlrxw.
'''
'''ABCDEFGHIJKLMNOPQRSTUVWXYZ
Estamos ceGHIJKLMNOPQRSTUVWXYZABCDEFlebrando el aniversario de Turing.
Voy a ganar este concurso de programacion.'''