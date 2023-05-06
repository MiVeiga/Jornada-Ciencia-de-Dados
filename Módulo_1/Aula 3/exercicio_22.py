''' Faça um programa que mostre a tabuada de múltiplicação de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo
'''

while True: 
    n = int(input("Qual tabuada você quer?\n"))
    if n < 0:
        break
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
