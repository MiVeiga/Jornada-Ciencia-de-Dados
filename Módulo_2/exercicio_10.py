#Crie uma função chamada `adicionar_amigo` que receba uma
# lista de amigos de um usuário em uma rede social e um novo amigo, 
# e adicione esse novo amigo na lista.

#Amanda
def adicionar_amigo(lista, novoAmigo):
    lista.append(novoAmigo)
    return lista

amigos = ['jose', 'Maria', 'joao']
novo_amigo = 'Carlos'
amigosAtualizado = adicionar_amigo(amigos, novo_amigo)
print(amigosAtualizado)


