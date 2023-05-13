"""
 Uma agência de turismo precisa gerar um itinerário para uma viagem. 
 Escreva um programa em Python que receba o nome e a duração (em dias)
  de cada cidade visitada durante a viagem e imprima o itinerário completo. 
 O programa deve numerar cada cidade na ordem em que é visitada.
"""

itinerario = []
while True:
  cidade = input("Digite o nome da cidade visitada (ou digite 'sair' para encerrar): ")
  if cidade == "sair":
    break
  duracao = int(input("Digite a duração da estadia (em dias): "))
  itinerario.append({"cidade": cidade, "duração": duracao})
print("Itinerário de Viagem")
for i, cidade in enumerate(itinerario):
  print(f"{i+1}. {cidade['cidade']} ({cidade['duração']} dias)")