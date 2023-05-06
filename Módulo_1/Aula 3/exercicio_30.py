#Faça um programa que simule um salão de beleza. 
#O usuário deverá digitar o nome e o serviço desejado (corte de cabelo ou manicure). 
#O programa deve exibir uma mensagem confirmando o serviço escolhido e perguntar 
#se o usuário deseja agendar outro serviço. 
#O laço deve continuar até que o usuário decida encerrar o atendimento.


while True:
    nome = input("Digite seu nome: \n")
    servico = input("Digite o serviço que você deseja: corte de cabelo ou manicure: \n")

    print(f"O serviço de {servico} foi marcado para {nome}")

    opcao = input("Deseja agendar outro serviço ? (s/n) \n")
    if opcao.lower() != "s":
        break