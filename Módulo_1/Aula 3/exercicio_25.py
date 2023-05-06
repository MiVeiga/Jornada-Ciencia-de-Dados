#Faça um programa que simule uma contagem regressiva de um 
# foguete antes do lançamento para NASA. O usuário deve digitar o número de segundos 
# da contagem regressiva e o programa deve exibir a contagem regressiva em ordem decrescente.

from time import sleep

#Marcus
"""
numero = int(input("Digite o numero para ordem decrecente: ")) 
for i in range(numero, 0,-1): 
    print(i) 
    sleep(1) 
print("LANÇAR")
"""


#Pedro
"""
numero_de_segundos = int(input("Segundos: ")) 
contagem = 0

while numero_de_segundos > contagem: 
    sleep(1) 
    print(numero_de_segundos) 
    numero_de_segundos-=1 
print("Foguete em Lançamento")
"""


#Willian
"""
segundos = int(input('Digite o número de segundos: ')) 
print(f'Lançamento em {segundos} segundos') 
for i in range(segundos, 0, -1): 
    print(i) 
    sleep (1) 
print('Decolar!!!')
"""


