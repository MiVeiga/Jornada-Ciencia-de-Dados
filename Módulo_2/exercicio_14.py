#A NASA está desenvolvendo um software para simular o pouso lunar. 
# Crie um  programa que verifica se a altitude de um módulo lunar é segura para o pouso. 
# Ela tem que ser menor que 50


altitude = float(input("Digite uma altitude: \n"))

if altitude < 50:
    print("Seguro para pouso")
else:
    print("Não é seguro para pouso")