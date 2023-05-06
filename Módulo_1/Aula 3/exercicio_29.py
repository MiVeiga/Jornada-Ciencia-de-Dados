#Hospital: Faça um programa que simule um hospital. 
#O usuário deverá digitar o nome e a idade de cada paciente, até que o usuário decida encerrar o cadastro.
#O programa deve exibir uma mensagem de alerta caso o paciente tenha mais de 60 anos.

while True:

    nome = input("Digite o nome do paciente: \n")
    idade = int(input("Digite a idade do paciente \n"))

    if idade > 60:
        print(f"Atenção!{nome} tem mais de 60 anos")
    
    opcao = input("Deseja cadastrar outro paciente? (s/n) \n")
    if opcao.lower() != "s":
        print("Cadastro com sucesso")
        break
