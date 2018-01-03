#import sys #No necesario si usamos break en el bucle while
import numpy as np #Permite obtener el producto de las combinaciones de rotores de cada máquina en una sola sentencia

'''
#Pruebas con matrices
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
print(np.multiply(a,b)) #Producto elemento a elemento
print(np.dot(a,b)) #Producto de matrices

m = [1, 2, 3, 4]
m = np.array(m)
a = 3+m
b = 3*m
c = m/3
d = 3/m
print(a, b, c, d)
'''
# Leer el numero de lineas
num_maquinas = int(input())
num_lineas = num_maquinas

#Para cada linea leo los datos de la máquina y obtengo las combinaciones
while num_lineas > 0:
    #Leemos los datos de la máquina actual
    desc_maquina = input()
    #print(desc_maquina)    
    #Los datos de la máquina los separamos en una matriz de cadenas de números
    dm = desc_maquina.split()
    #print(dm)    
    #Pasamos las cadenas a enteros
    dm = list(map(int, dm))
    #Quitamos el primer dato que es el número de rotores
    n_rotores = dm.pop(0) #dm queda ya sólo con los datos de los rotores
    #print(n_rotores)
    #print(dm)
    #Comprobamos que tenemos las combinaciones de todos los rotores
    if n_rotores != len(dm):
        print("Error en los datos de la máquina ", num_maquinas-num_lineas+1)
        break
        #sys.exit(0)
    # Imprimimos el producto de las combinaciones de todos los rotores  
    print(np.prod(dm))    
    #Decrementamos el número de líneas
    num_lineas = num_lineas - 1

# Fin del programa