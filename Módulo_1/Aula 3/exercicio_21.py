#Faça um programa que leia o sexo de uma pessoa
#mas só aceite os valores "M" ou "F".
#Caso esteja errado, peça a digitação novamente
#até ter um valor correto.


sexo = str(input("Digite seu sexo, M ou F: \n")).strip().upper()[0]

while sexo not in "MmFf":
    sexo = str(input("Só pode valor M ou F. Digite novamente: \n")).strip().upper()[0]

print("Sexo {} registrado com sucesso.".format(sexo))