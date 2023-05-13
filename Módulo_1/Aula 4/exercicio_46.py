"""
Crie um programa onde o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista.

Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

"""

lista = []

while True:
    num = int(input("Digite um número: \n"))
    if num in lista:
        print("O número já está na lista.")
    else:
        lista.append(num)
        print("Item adicionado com sucesso")
    
    continuar = str(input("Quer continuar? SIM/NÃO")).strip().upper()
    if continuar[0] == "N":
        break
    elif continuar[0] == "S":
        print("Continuando então...")
    else:
        print("Digite apenas sim ou não")

lista.sort()
print(f"Você digitou esses valores {lista}!")