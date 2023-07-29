# Crie um módulo chamado "moeda" que 
# contenha uma função para formatar um 
# número como um valor monetário, com duas casas 
# decimais e o símbolo de moeda. Em seguida, crie 
# um programa principal que importe esse módulo e 
# peça ao usuário para digitar um valor numérico. 
# O programa deve imprimir o valor formatado como moeda.

#Miguel 

from modulos import moeda

valor = float(input("Digite um valor: "))

print("Valor formatado da moeda", moeda.moeda(valor))
