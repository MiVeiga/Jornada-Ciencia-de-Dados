
#Faça um programa que simule uma corrida entre dois carros. 
#O programa deve solicitar ao usuário a velocidade dos carros 
#e a distância da pista. O laço deve continuar até que 
#um dos carros chegue ao final da pista. Ao finalizar a corrida, o programa deve exibir o vencedor.


distância = float(input("Digite a distância da pista: \n"))
velocidade1= float(input("Digite a velocidade do carro 1 \n"))
velocidade2 = float(input("Digite a velocidade do carro 2 \n"))

posicao1 = 0
posicao2 = 0

while  posicao1 < distância and posicao2 < distância:
    posicao1 +=velocidade1
    posicao2 +=velocidade2

if posicao1 > posicao2:
    print("O carro 1 venceu!")
elif posicao2 > posicao1: 
    print("O carro 2 venceu!")
else:
    print("Empate!")




