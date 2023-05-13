
""""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f

(Caractere)(><^)(quantidade)
> Esquerda
< Direita
^ Centro

Interpolação básica de strings
s - string
d e i - int
f - float

"""
variavel = 'banana'
print(f'{variavel}')
# 1 qtd de casas decimais f se é int,ou float
print(f'{1000.4873648123746:.1f}')
#aparece até atingir o numero de caracteres que eu quero
print(f'{variavel:+>20}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')

nome = 'Luiz'
preco = 1000.95897643

variavel = '%s, o preço é R$%.2f' % (nome, preco)
variavelFormat = '{}, o preço é R${:.2f}'.format(nome, preco)
print(variavel)
print(variavelFormat)

