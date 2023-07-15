#Crie uma função chamada `calcular_aprovacao` 
# que receba uma lista de notas de alunos em uma 
# rede social e retorne a porcentagem de aprovação. 
# Considere que a nota mínima para aprovação é 7.

lista=[10, 4, 8, 2, 5]

def calcular_aprovacao(notas):
    total_alunos = len(notas)
    aprovados = 0
    for nota in notas:
        if nota >= 7:
            aprovados += 1
    porcentagem_aprovacao = (aprovados / total_alunos) * 100
    return porcentagem_aprovacao

print(calcular_aprovacao(lista))