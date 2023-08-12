# Crie um módulo chamado "operacoes_matematicas" que
# contenha funções para calcular a potência e
# a raiz quadrada de um número. Em seguida,
# crie um programa principal que importe esse
# módulo e peça ao usuário para digitar um número
# e a operação desejada (potência ou raiz quadrada).
# O programa deve imprimir o resultado da operação.


# Codigo princial - Miguel

from modulos import operacoes_matematicas

operacao = input(
    "Digite qual o operação deseja usar (** ou r(raiz quadrada)):")

if operacao == "**":
    num = int(input("Digite um número:"))
    potencia = int(input("Digite a potência que deseja: "))
    resul = operacoes_matematicas.potencia(num, potencia)
    print("Resultado da Potencia:", resul)
elif operacao == "r":
    num = int(input("Digite um número:"))
    resul = operacoes_matematicas.raizQuadrada(num)
    print("Resultado da Raiz Quadrada:", resul)
else:
    print("Operação inserida inválida")

