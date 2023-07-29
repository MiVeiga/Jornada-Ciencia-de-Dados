# Crie um módulo chamado "lista_numeros" 
# que contenha uma lista de números. 
# Em seguida, crie um programa principal que 
# importe esse módulo e imprima a soma e o maior número 

#Miguel
from modulos import lista_numeros

quantidade = int(input("Digite a quantidade de números que deseja inserir: "))
lista = []

for i in range(quantidade):
    numero = float(input(f"Digite o número {i + 1}: "))
    lista.append(numero)

print("Soma da lista:", lista_numeros.soma(lista))
print("Maior número da lista:", lista_numeros.maiorNumero(lista))