#c = numero de estudiantes que caben en un laboratorio entre 0 y 100000
#a = numero de estudiantes matriculados entre 0 y 1000000

import sys
while True:
    # leer variables
    v = input()
    c, a = v.split()
    a = int(a)
    c = int(c)

    if c == 0:
        sys.exit()
    else:
        # operaciones
        g = (a // c)  # // da la parte no decimal de una division
        if a % c == 0:
            print(g)
        else:
            print(g + 1)