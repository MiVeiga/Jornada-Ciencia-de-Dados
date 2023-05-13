"""
Uma escola precisa verificar se um aluno foi aprovado ou
 reprovado em uma disciplina, considerando que a nota mínima para aprovação é 7,0. 
Escreva um programa em Python que receba a nota do aluno 
e verifique se ele foi aprovado ou reprovado.
"""

nota_aluno = float(input("Digite a nota do aluno: "))
if nota_aluno >= 7.0:
  print("O aluno foi aprovado.")
else:
  print("O aluno foi reprovado.")
