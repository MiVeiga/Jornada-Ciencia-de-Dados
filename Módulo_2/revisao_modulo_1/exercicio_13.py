#Crie uma função que receba uma tupla de números 
# e retorne o menor valor dessa tupla.
# numeros = (5, 2, 10, 1, 8)

#Pedro
numeros = (5, 2, 10, 1, 8)
def menor(lista):
    menor = lista[0]
    for i in lista:
        if i < menor:
            menor = i
    return menor

print(menor(numeros))