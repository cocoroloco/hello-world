# Preparamos las vocales 
vocales = "aeiou"
'''
#Comprobar cómo es vocales
print(vocales)
print(type(vocales))
print(vocales[0])
'''
#Leemos la linea de entrada
linea_entrada = input() # Ejemplo: PruEba de LIneA de Entrada

for nueva_vocal in vocales:
    #print(vocal)
    linea_salida = linea_entrada #Pone la linea de salida igual a la linea original
    for vocal_actual in vocales: #Sustituye cada vocal en la linea de salida con la nueva_vocal
        linea_salida = linea_salida.replace(vocal_actual, nueva_vocal)
        linea_salida = linea_salida.replace(vocal_actual.upper(), nueva_vocal.upper())
    print(linea_salida) #Imprime la linea de salida con las vocales a la nueva_vocal