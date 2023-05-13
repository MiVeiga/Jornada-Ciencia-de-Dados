
"""
Uma escola precisa gerar boletins de notas para os alunos.
 Escreva um programa em Python que receba o nome e as notas de cada aluno 
 em três disciplinas diferentes (Matemática, Português e Ciências)
e calcule a média final de cada aluno. O programa deve imprimir o boletim de 
cada aluno com o nome, as notas e a média final.

"""

alunos = []
while True:
  nome = input("Digite o nome do aluno (ou digite 'sair' para encerrar): ")
  if nome == "sair":
    break
  matematica = float(input("Digite a nota do aluno em Matemática: "))
  portugues = float(input("Digite a nota do aluno em Português: "))
  ciencias = float(input("Digite a nota do aluno em Ciências: "))
  media = (matematica + portugues + ciencias) / 3
  aluno = {"nome": nome, "Matemática": matematica, "Português": portugues, "Ciências": ciencias, "Média": media}
  alunos.append(aluno)
print("Boletim de Notas")
for aluno in alunos:
  print(f"Aluno: {aluno['nome']}")
  print(f"Matemática: {aluno['Matemática']}")
  print(f"Português: {aluno['Português']}")
  print(f"Ciências: {aluno['Ciências']}")
  print(f"Média Final: {aluno['Média']:.2f}")
  print()
