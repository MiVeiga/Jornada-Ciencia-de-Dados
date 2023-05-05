''' Crie um programa que leia o ano de nascimento de sete pessoas
No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores'''


#Marcus Vinicius
#declarou contadores
menores = 0
maiores = 0

for i in range(1,8):
    ano = int(input("Digite seu ano de nascimento: "))
    if(2023 - ano < 18):
        menores += 1
    else:
        maiores += 1 
print("{} são maiores de idade e {} são menores de idade".format(maiores, menores))