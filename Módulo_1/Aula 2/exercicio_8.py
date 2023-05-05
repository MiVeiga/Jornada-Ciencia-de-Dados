#Verificar se o usuário digitou o login e a senha corretos 
#usuario = miveiga
#senha = 12345!


#Receber login e senha

login = input("Digite seu login: \n")
senha = input("Digite sua senha: \n")

#Verficando se login e senha está correto

if login == "miveiga" and senha == "12345!":
    print("Login realizado com sucesso")
else:
    print("Usuário ou senha incorretos")