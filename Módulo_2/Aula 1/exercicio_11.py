# Durante uma missão espacial, a NASA precisa
# verificar se os níveis de oxigênio na estação
# espacial estão dentro do limite seguro.
# O programa deve  receber o valor atual de oxigênio
# em percentual e imprimir uma mensagem informando
# se é necessário tomar medidas de precaução ou não.
# Oxigenio entre 21 e 25 = O nível de oxigênio está dentro do limite seguro.
# Oxigenio menor que 21 = Nível de oxigênio baixo. Tomar medidas de precaução.
# Oxigenio maior que 25 = "Nível de oxigênio alto. Tomar medidas de precaução.

# Pedro
import random

nivel_oxigenio = random.randint(10, 40)

if nivel_oxigenio < 21:
    print(f" {nivel_oxigenio} Oxigenio BAIXO, Necessario Ativar Medida de Precaução")
elif nivel_oxigenio > 25:
    print(f" {nivel_oxigenio} Oxigenio ALTO, Necessario Ativar Medida de Precaução")
else:
    print(f" {nivel_oxigenio} Oxigenio Dentro do Limite Seguro")

