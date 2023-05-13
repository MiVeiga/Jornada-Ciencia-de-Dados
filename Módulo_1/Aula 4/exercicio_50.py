"""
Suponha que você tenha uma lista contendo os números de telefone 
de uma agenda, por exemplo: ["(11) 9999-9999", "(21) 8888-8888", "(31) 7777-7777"].
Remova o segundo número de telefone da lista e 
salve-o em uma variável chamada "numero".
"""

agenda = ["(11) 9999-9999", "(21) 8888-8888", "(31) 7777-7777"]
numero = agenda.pop(1)
print(numero)
print(agenda)