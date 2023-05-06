
#Faça um programa que solicite ao usuário uma senha. 
#O usuário tem três tentativas para digitar a senha correta. 
#O programa deve exibir uma mensagem de erro caso a senha esteja incorreta 
#e uma mensagem de sucesso caso a senha esteja correta ou o usuário 
# tenha esgotado as tentativas.

#Douglas
"""
senha = "abcde123" 
tentativas = 3 

while tentativas > 0: 
    entrada = input("Digite a senha: ") 
    if entrada == senha:
         print("Senha correta!") 
         break 
    else: 
        tentativas -= 1 
        print(f"Senha você tem mais {tentativas} tentativas.") 

if tentativas == 0: 
    print("Suas tentativas passaram. Acesso negado.")
"""


#Vanessa

"""
senha_correta = "minhasenha" 
tentativas = 3 
while tentativas > 0: 
    senha = input("Digite sua senha: ") 
    if senha == senha_correta: 
        print("Bem vindo ao Sistema") 
        break 
    else: 
        tentativas -= 1 
    if tentativas > 0 : 
        print("Senha incorreta. Tente novamente. Tentativas restantes:", tentativas) 
    else: 
        print("Tentativas esgotadas. Acesso negado.")
"""


#Amanda

"""
senha = input("DIGITE AQUI SUA SENHA: ") 
login = input("Faça seu login") 
for i in range (1, 3): 
    if(login==senha): 
        print("Bem vindo") 
        break
    else: 
        print("Digite a senha novamente") 
        login = input("Faça seu login: ") 
        if i==2: 
         print("Você excedeu o limite de tentativas.")

"""


#Guilherme/Willian
"""
contador = 0 
while contador < 3: 
    senha = input('Digite a senha: ') 
    if senha != '12345!': 
        print('Senha incorreta') 
        contador += 1 
    else:
         print('Logado') 
         break 
    if contador == 3: 
       print('Excedeu o limite de 3 tentativas') 
       break
"""


#Miguel
"""""
senhaUsuario = "1234" 
tentativa = 0 
while (tentativa < 3): 
    senha = input("Digite sua senha? \n") 
    if (senha == senhaUsuario): 
        print("Bem-Vindo") 
        break 
    print("Senha incorreta !") 
    tentativa = tentativa + 1 

if (tentativa == 3): 
    print("Bloqueando o usuário")
"""

#Helyaby

"""
senha = "abcd" 
tentativas = 3 
while tentativas > 0: 
    entrada = input("Digite a senha: ") 
    if entrada == senha: 
        print("Senha correta. Login sucedido") 
        break 
    else: 
        tentativas -= 1 
        print(f"Senha incorretamente.Login não sucedido Você tem mais {tentativas} tentativas.") 
if tentativas == 0: 
    print("Suas tentativas tentaram.E vc n acertou a senha então acesso negado")
"""





