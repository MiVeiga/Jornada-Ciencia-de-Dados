#Crie uma função chamada `verificar_amigos` que 
# receba uma lista de nomes de usuários de uma rede social 
# e verifique se algum desses usuários são amigos no sistema.

amigos = ["Pedro", "João", "Maria", "Gabi"]
def verificar_amigos(usuarios):
    for usuario in amigos:
        if usuarios in amigos:
            return True
    return False


print(verificar_amigos("Maria"))

