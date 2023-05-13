"""
Uma loja de roupas precisa gerenciar seu estoque. 
Escreva um programa em Python que permita ao usuário adicionar 
novos itens ao estoque e verificar a quantidade disponível de cada item.
 O programa deve permitir que o usuário adicione um novo item especificando 
 seu nome, preço e quantidade inicial. O usuário também deve 
 poder verificar a quantidade disponível de um item existente.

"""

estoque = {}

while True:
    acao = input("Digite 'adicionar' para adicionar um novo item ou 'verificar' para verificar a quantidade disponível de um item existente: ")

    if acao == "adicionar":
        nome = input("Digite o nome do novo item: ")
        preco = float(input("Digite o preço do novo item: "))
        quantidade = int(input("Digite a quantidade inicial do novo item: "))
        estoque[nome] = {"preço": preco, "quantidade": quantidade}
        print(f"{quantidade} unidades do item {nome} foram adicionadas ao estoque.")
    
    elif acao == "verificar":
        nome = input("Digite o nome do item para verificar a quantidade disponível: ")
        if nome in estoque:
            print(f"Há {estoque[nome]['quantidade']} unidades do item {nome} disponíveis no estoque.")
        else:
            print(f"O item {nome} não está no estoque.")
    
    else:
        print("Ação inválida. Tente novamente.")