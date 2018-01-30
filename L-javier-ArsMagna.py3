#import itertools as it 
from itertools import combinations, permutations
#print(list(combinations([1,2,3,4],3))) #Combinaciones 
#print(list(permutations(['a','b','c','d'],3))) #Permutaciones
#print(list(combinations(['chocolate', 'fresa','limón','naranja','vainilla'],3))) #Combinaciones: Helados de 3 sabores posibles 
#print(list(permutations(['Cáceres', 'Mérida', 'Navalmoral', 'Plasencia'],3))) #Permutaciones: Recorridos de visitas a 3 ciudades de Extremadura

#Numero de cadenas a permutar
num_cadenas = int(input())

for i in (range(num_cadenas)):
    cadena = input() # Cadena a permutar
    if len(cadena) == 1:
        print(cadena)
        print()
        continue
    permutaciones = list(permutations(cadena,len(cadena))) #Lista con todas las permutaciones de la cadena de entrada
    #print(permutaciones)
    salidas = [] #Forma la lista de palabras a ordenar
    for permutacion in permutaciones:
        cadena = ""
        salidas.append(cadena.join(permutacion))
    '''    for permutacion in permutaciones: #Imprime en una cadena los caracteres de cada lista de permutacion
            salida = ""
            for j in range(len(permutacion)):
                salida = salida + permutacion[j]
            salidas.append(salida)
    ''' 
    #print(salidas)
    salidas.sort() #Ordena la lista de cadenas de salida
    #sorted(salidas, key=lambda cadena: len(cadena), reverse=True)
    #print(salidas)
    for i in salidas:
        print(i) #Imprime linea en blanco antes de la nueva secuencia de permutaciones
    print() #Imprimir linea en blanco
    
#print("FIN")