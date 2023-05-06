
"""
Crie um programa que verifique se um número é par e se é maior que 10 e menor que 50 ao mesmo tempo.
"""


num = int(input("Digite um número: "))

if num % 2 == 0 and num > 10 and num < 50:
    print("O número é par e está entre 10 e 50.")
else:
    print("O número não satisfaz as condições.")
