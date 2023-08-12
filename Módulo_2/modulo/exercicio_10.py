#Crie um módulo chamado "media_numeros" que contenha 
# uma função para calcular a média de uma lista de números.
#  Em seguida, crie um programa principal que importe esse 
# módulo e peça ao usuário para digitar uma lista de números 
# separados por espaço. O programa deve imprimir a média dos números.


from modulos import media_numeros

quantidade = int(input("Digite a quantidade de números que deseja inserir: "))
lista = []

for i in range(quantidade):
    numero = float(input(f"Digite o número {i + 1}: "))
    lista.append(numero)

print("Média da lista:", media_numeros.media(lista))