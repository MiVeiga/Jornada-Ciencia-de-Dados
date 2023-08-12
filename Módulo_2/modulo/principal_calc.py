
#Crie um módulo chamado Calculadora que 
# tenha os métodos somar, subtrair, multiplicar 
# e dividir. Cada método deve receber dois números 
# como parâmetros e retornar o resultado da operação correspondente.

#Código principal

from modulos import calculadora

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação desejada (+, -, * ou / ): ")

if operacao == "+":
    resultado = calculadora.adicacao(num1, num2)
elif operacao == "-":
    resultado = calculadora.subtracao(num1, num2)
elif operacao == "*":
    resultado = calculadora.multiplicacao(num1, num2)
elif operacao == "/":
    resultado = calculadora.divisao(num1, num2)
else:
    resultado = "Operação inválida"

print("Resultado:", resultado)

