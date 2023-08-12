# Crie um módulo chamado "conversor" 
# que contenha duas funções: uma para 
# converter graus Celsius para Fahrenheit e 
# outra para converter graus Fahrenheit para Celsius.
#  Em seguida, crie um programa principal que importe 
#  esse módulo e peça ao usuário para digitar uma temperatura 
#  e a unidade de medida (C ou F). O programa deve imprimir a 
#  temperatura convertida para a outra unidade.


# Codigo principal do modulo - Miguel
from modulos import conversor 
temperatura = float(input("Digite uma temperatura: ")) 
unidade = input("Qual a unidade de medida (c ou f): ") 
if unidade == "c": 
    resultado = conversor.celsius(temperatura)
elif unidade == "f": 
    resultado = conversor.fahrenheit(temperatura)
else: 
    resultado = ""
    print("Unidade transmitida não identificada")

print("Temperatura transmitida em",unidade, "igual a", resultado)