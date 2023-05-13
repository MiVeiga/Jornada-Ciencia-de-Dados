"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho
e cadastre-os (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de zero, o dicionário receberá também
o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos
a pessoa vai se aposentar.

Obs.: aposentadoria em 35 anos de contribuição.
"""

from datetime import date

cadastros = []

while True:
    nome = input("Digite o nome:")
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    carteira_trabalho = int(input("Digite o número da carteira de trabalho(0 caso você não tenha)"))

    idade = date.today().year - ano_nascimento

    if carteira_trabalho != 0:
        ano_contratacao = int(input("Digite o ano da sua primeira contratação:"))
        salario = float(input("Digite o salário:"))
        contribuicao = date.today().year - ano_contratacao

        aposentadoria = (35-contribuicao) + idade

        cadastro = {
            "nome": nome,
            "ano_nascimento":ano_nascimento,
            "carteira_trabalho" :carteira_trabalho,
            "ano_contratacao": ano_contratacao,
            "salario":salario,
            "idade": idade,
            "aposentadoria":aposentadoria
        }
    else:
        cadastro ={
            "nome":nome,
            "ano_nascimento":ano_nascimento,
            "cateira_trabalho":carteira_trabalho,
            "idade": idade
        }
    cadastros.append(cadastro)

    continuar = input("Deseja continuar? (S/N) \n")

    if continuar.upper() != "S":
        break

print(cadastros)

