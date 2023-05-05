#Um aplicativo pode usar um laço de repetição "for" 
#para percorrer a lista de usuários e enviar uma notificação para cada um.
#usuarios = ['Ana', 'João', 'Pedro', 'Maria']

usuarios = ['Ana', 'João', 'Pedro', 'Maria']
mensagem = "Temos descontos amanhã - 30/04"

for usuario in usuarios:
    print("{},{}".format(usuario, mensagem))
