#Um programa que simule o jogo de adivinhação, 
#em que o usuário deve tentar adivinhar um número escolhido pelo programa. 
#O programa deve informar ao usuário se o número digitado
#é maior ou menor do que o número escolhido. 
#O jogo deve continuar até que o usuário acerte o número escolhido.

"""
Douglas

import random

print("*********************************")
print("Bem vindo ao jogo da adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1, 101)
tentativas = 0
pontos = 100

print("Escolha uma dificuldade! \n")
print("(1) Fácil, (2) Médio, (3) Difícil \n")

level = int(input("Defina a dificuldade: \n"))
if level == 1:
    tentativas = 20
elif level == 2:
    tentativas = 10
elif level == 3:
    tentativas = 5
else:
    print("Você deve escolher entre 1 a 3. Tente novamente! \n")
    
for rodada in range (1, tentativas + 1):
    print(f"Tentativa {rodada} de {tentativas}!")
    palpite_str = int(input("Digite um número: \n"))
    palpite = int(palpite_str)

    if palpite <1 or palpite > 100:
        print("Você deve escolher um número entre 1 a 100!")
        continue

    correto = palpite == numero_secreto
    maior = palpite > numero_secreto
    menor = palpite < numero_secreto

    if(correto):
        print(f"Parabéns! O número secreto é {numero_secreto}")
        print(f"Sua pontuação é {pontos}")
        break
    else:
        pontos -= 5
        if maior:
            print("O seu palpite foi MAIOR do que o número secreto! Tente novamente! \n")
        elif menor:
            print("O seu palpite foi MENOR que o número secreto! Tente novamente! \n")

print("Fim de jogo!")
"""



"""
William/Guilherme
import random
numero_sorteado = random.randint(1, 10)
numero = 0

while numero != numero_sorteado:
    numero = int(input('Digite um número de 1 a 10: '))
    if numero < numero_sorteado:
        print(f'O número sorteado é maior que {numero}\n')
    elif numero > numero_sorteado:
        print(f'O número sorteado é menor que {numero}\n')
    else:
        print(f'Parabéns, o número sorteado foi {numero}\n')
        break

"""



"""
Jaime

import random
numeroPrograma = random.randint(1, 30)

while True:
    palpite = int(input("Dê seu palpite. Informe um número inteiro até 30: \n"))

    if palpite == numeroPrograma:
        print(f"Acertou miserável!")
        break
    elif palpite > numeroPrograma:
        print(f"Errou! Muito alto! Tente novamente")
    else:
        print(f"Errou! Muito baixo! Tente novamente")
"""

"""
Amanda 

numeroAdivinhar = 7
valorEscolhido = int(input("Escolha um valor e veja se é o da memória do programa: "))
while(valorEscolhido != numeroAdivinhar) :
    if(valorEscolhido>numeroAdivinhar):
        print("O valor digitado é maior do que o número do sistema")
    
    else:
        print("O valor digitado é menor do que o número do sistema")

    valorEscolhido = int(input("Valor inválido, tente novamente: "))
print("Parabéns, o valor escolhido foi {}".format(numeroAdivinhar))
"""

"""
Miguel

import random
escolhido = random.randint(1, 100)
print(escolhido)
tentativa = 1

print(">>>>>>>>>>>>Jogo de Adivinhação<<<<<<<<<<<<<")
print(">>>>>>>>>>>>De 1 à 100<<<<<<<<<<<<<")
resposta = int(input(f"Digite {tentativa}° número? \n"))

if (resposta == escolhido):
    print("Você acertou em", tentativa, "tentaiva(s). O número era", escolhido)
tentativa += 1


while (resposta != escolhido):
    resposta = int(input(f"Digite {tentativa}° número? \n"))
    if (resposta == escolhido):
        print("Você acertou em", tentativa, "tentaiva(s). O número era", escolhido)
        break

    if (tentativa == 5):
        if (escolhido % 2 == 0):
            print("\nÉ um número Par!\n")
        else:
            print("\nÉ um número Ímpar!\n")

    if (tentativa == 10):
        if (escolhido > 0 and escolhido <= 20):
            print("\nO número é maior ou igual a 1 e menor ou igual a 20\n")
        else:
            print("\nO número é maior que 20\n")
    
    if (tentativa == 15):
        if (escolhido > 20 and escolhido <= 40):
            print("\nO número é maior a 20 e menor ou igual a 40\n")
        elif (escolhido > 40 and escolhido <= 60):
            print("\nO número é maior a 40 e menor ou igual a 60\n")
    
    if (tentativa == 20):
        if (escolhido > 60 and escolhido <= 80):
            print("\nO número é maior a 60 e menor ou igual a 80\n")
        elif (escolhido > 80):
            print("\nO número é maior que 80\n")

    tentativa += 1
"""

"""
Marcus
valor = int(input("Digite um Número a ser adivinhado: "))
while True:
    numero = int(input("Digite um Número: "))
    if numero > valor:
        print("O número informado é maior que o número escolhido")
    elif numero < valor:
        print("O número informado é menor que o número escolhido")
    else:
        print("O número informado é o número escolhido")
        break

"""

"""
Elcio
import random

numeroaleaotorio = (random.randint(1, 10))

tentativa = 0

numeroescrito = int

while numeroescrito != numeroaleaotorio:
 numeroescrito = int(input("Digite o numero até acertar.. "))
 tentativa += 1
 
 if numeroescrito < 0 and numeroescrito > 10:
     print("Só serão aceitos Números entre 1 a 10.")
     int(input("Digite denovo..: "))
 
 elif numeroescrito == numeroaleaotorio:
  print("Você acertou o número! Obrigado por participar!")
  break
 elif tentativa == 2:
     print("--------------------------------------------")
     print("Aviso! Você tem mais 1 tentativa sobrando!!")
     print("--------------------------------------------")
 elif tentativa == 3:
     print("--------------------------------------------")
     print("Suas tentativas acabaram >:3")
     print("--------------------------------------------")
     break
"""


