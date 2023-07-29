#Crie um módulo chamado "string_utils" que contenha 
# uma função para contar o número de caracteres em uma string. 
# Em seguida, crie um programa principal que importe esse módulo 
# e peça ao usuário para digitar uma frase. O programa deve imprimir 
# o número de caracteres na frase.


#Modulo  - Miguel 

from modulos import string_utils

frase = input("Digite uma frase: ")

print("Quantidade de caracteres", string_utils.lenCaracteres(frase))