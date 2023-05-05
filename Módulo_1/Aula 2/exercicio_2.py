# Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Louvor", se a média for igual a dez.


nota1 = float(input("Digite a primeira nota: \n"))
nota2 = float(input("Digite a segunda nota: \n"))

media = (nota1+nota2)/2
print(f"A média desse aluno é: {media}")

#if media>=7:
#    print("Aprovado")
#elif media == 10:
 #  print("Aprovado com louvor")
#else:
  #  print("Reprovado")

if media == 10:
    print("Aprovado com Louvor")
elif media >= 7:
    print('Aprovado')
else:
    print('Reprovado')