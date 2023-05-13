"""
Peça ao usuário para digitar seu nome
Se nome  for digitado:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input("Digite seu nome: \n")

if nome: 
    print(f"Seu nome é {nome}")
    print(f"O seu nome invertido é {nome[::-1]}")

    if ' ' in nome:
        print("Seu nome contém espaços")
    else: 
        print("Seu nome não contém espaços")
    
    print(f"Seu nome tem {len(nome)} letras")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A última letra do seu nome é {nome[-1]}")
else:
    print("Digite o nome")
    


