
entrada = input()

vocales = ["a", "e", "i", "o", "u"]
buscada = ["a", "e", "i", "o", "u"]
vocales_M = ["A", "E", "I", "O", "U"]
buscada_M = ["A", "E", "I", "O", "U"]


for letra in vocales:
    i = entrada
    for letra_buscada in buscada:
        i = i.replace(letra_buscada, letra)
        print(i)
        for letra_M in vocales_M:
            for letra_buscada_M in buscada_M:
                i = i.replace(letra_buscada_M, letra_M)
        if letra_buscada == "u":
            print(i)



'''while x != 5:
    i = i.replace("o", "a")
    i = i.replace("e", "a")
    i = i.replace("i", "a")
    i = i.replace("u", "a")
    x +=1
    print(i)'''

'''for letra in vocales:
    i = i.replace("a", letra)
    i = i.replace("e", letra)
    i = i.replace("o", letra)
    i = i.replace("i", letra)
    i = i.replace("u", letra)
    print(i)'''
#MUrcielagO