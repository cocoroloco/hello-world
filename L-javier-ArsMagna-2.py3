
# Python function to print permutations of a given list
def permutation(lst):
 
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []
 
    # If there is only one element in lst then, only
    # one permuatation is possible
    if len(lst) == 1:
        return [lst]
 
    # Find the permutations for lst if there are
    # more than 1 characters
 
    l = [] # empty list that will store current permutation
 
    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
       m = lst[i]
 
       # Extract lst[i] or m from the list.  remLst is
       # remaining list
       remLst = lst[:i] + lst[i+1:]
 
       # Generating all permutations where m is first
       # element
       for p in permutation(remLst):
           l.append([m] + p)
    return l
 
# Driver program to test above function
#data = list('123')
#for p in permutation(data):
#    print (p)
    
#Numero de cadenas a permutar
num_cadenas = int(input())

for i in (range(num_cadenas)):
    cadena = list(input()) # Cadena a permutar --> Transformada en lista de caracteres
    permutaciones = permutation(cadena)
    #print(permutaciones)
    salidas = [] #Forma la lista de palabras a ordenar
    for permutacion in permutaciones:
        cadena = ""
        salidas.append(cadena.join(permutacion))
    #print(salidas)
    salidas.sort() #Ordena la lista de cadenas de salida
    #sorted(salidas, key=lambda cadena: len(cadena), reverse=True)
    #print(salidas)
    for i in salidas:
        print(i) #Imprime linea en blanco antes de la nueva secuencia de permutaciones
    print() #Imprimir linea en blanco
    
#print("FIN")