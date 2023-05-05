#Faça um programa que peça o nome do usuário e verifique se ele é "admin", 
# ele é admin ser for Lucas ou Pedro.

#Receber o nome do usário

user = input("Usuario: ").upper()

#Verificando se o user é adm
if (user == 'PEDRO' or user == 'LUCAS'):
    print(f"Bem-Vindo,Admin!")
else:
    print(f"Bem-Vindo,{user}")