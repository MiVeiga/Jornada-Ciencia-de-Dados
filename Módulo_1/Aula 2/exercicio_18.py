 #Desenvolva um programa que leia nome, idade e sexoo de 4 pessoas
#No final do programa, mostre:
 #- A média de idade do grupo
 #- Qual é o nome do homem mais velho
 #- Quantas mulheres têm menos de 20 anos

#Definicao de variaveis
media = 0
somaidade = 0
nome_maisvelho = ""
idade_mulher = 0
counter = 0
maisvelho = 0


for p in range(1, 5):
    #Pega os dados das pessoas
    nome = str(input("Nome: \n"))
    idade = int(input("Idade: \n"))
    sexo = str(input("Sexo [M/F]: \n")).upper()

    #Vejo quem é o homem mais velho
    if sexo == "M":
        if idade > maisvelho:
            maisvelho = idade
            nome_maisvelho = nome
    #Mulheres com menos de 20 anos
    elif sexo == "F":
        if idade < 20:
            idade_mulher +=1
    
    #Media de idade do grupo
    counter +=1
    somaidade += idade
    media = (somaidade/counter)

#respondo as perguntas do enunciado
print("A média é de idade do grupo {}".format(media))
print("O nome do homem mais velho é {}".format(nome_maisvelho))


if idade_mulher == 0:
    print("Nenhuma mulher tem menos de 20 anos")
elif idade_mulher == 1:
    print("{} mulher tem menos de 20 anos".format(idade_mulher))
elif idade_mulher >= 2: 
    print("{} mulhers tem menos de 20 anos".format(idade_mulher))




