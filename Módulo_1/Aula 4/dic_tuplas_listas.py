#Variáveis Compostas ou Coleções

"""
#TUPLAS
-Imutáveis
- Representados por () ou no python três apenas por sequência separadas por vírgulas

Algumas operações comuns em tuplas são:
index(): retorna o índice da primeira ocorrência de um elemento na tupla
count(): retorna o número de ocorrências de um elemento na tupla

EXEMPLO: 
tupla = (1, 2, 3, "quatro", "cinco")
print(tupla.index("quatro")) # saída: 3
print(tupla.count(2)) # saída: 1
"""
#---------------------------------------------------------------------------------

"""
#Listas
- Mutáveis
- Representados por []

Algumas operações comuns em listas são:

append(): adiciona um elemento ao final da lista
insert(): adiciona um elemento em uma posição específica da lista
remove(): remove a primeira ocorrência de um elemento na lista
pop(): remove o último elemento da lista e o retorna
index(): retorna o índice da primeira ocorrência de um elemento na lista
count(): retorna o número de ocorrências de um elemento na lista

EXEMPLO:

lista = [1, 2, 3, "quatro", "cinco"]
lista.append("seis")
lista.insert(1, "zero")
lista.remove(2)
valor = lista.pop()
print(lista) # saída: [1, "zero", 3, "quatro", "cinco", "seis"]
print(valor) # saída: cinco
print(lista.index("quatro")) # saída: 3
print(lista.count("zero")) # saída: 1

""
#---------------------------------------------------------------------------------

""
#Dicionário 
- Representado por {}
- Armazena informções associando uma chave a um valor

EXEMPLO:

dicionario = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
print(dicionario.get("nome")) # saída: João
print(dicionario.keys()) # saÍDA dict_keys(['nome', 'idade', 'cidade'])
"""


