
"""
Crie um programa que pergunte ao usuário se ele é estudante 
e se tem menos de 18 anos. Se o usuário for estudante e tiver menos de 18 anos, 
imprima "Você tem direito à meia-entrada", caso contrário, 
imprima "Você não tem direito à meia-entrada".
"""

#Pedro

""""
usuario_e_estudante = input("Você é estudante? (sim/não): ").lower().startswith('s') 
usuario_menor_de_18 = input("Você tem menos de 18 anos? (sim/não): ").lower().startswith('s') 
if usuario_e_estudante and usuario_menor_de_18: 
    print("Voce tem direita a meia entrada") 
else: 
    print("Voce não tem direito a meia entrada")
"""


#Guilherme/Willian
""""
estudante = input('É estudante? (s/n):').lower()
idade = int(input('Qual a idade: ')) 
if estudante == 's' and idade < 18: 
    print("Você tem direito à meia-entrada") 
else: 
    print("Você não tem direito à meia-entrada")
"""


#Miguel

"""
usuario = input("Você é estudante? (sim/não)").lower() 
idade = int(input("Quantos anos você tem?"))

if (usuario == "sim" and idade < 18): 
    print ("Você tem direito à meia-entrada") 
else: 
    print("Você não tem direito à meia-entrada")
"""


#Elcio
"""
estudanteIdade = int(input("Quantos Anos você tem?\n")) 
estudanteestuda = input("Você é estudante? (s/n)\n")

if estudanteestuda == "s" and estudanteIdade < 18: 
    print(" Você tem direito a meia entrada!") 
else: 
    print("Você não tem direito a meia entrada")
"""


#Douglas

"""
idade = int(input("Qual a sua idade?").upper()) 
idade_minima = 18 
estudante = input("Você é estudante? (S) ou (N)").upper() 
if idade < idade_minima and estudante == "S": 
    print("Você tem direito à meia-entrada.") 
else: 
    print("Você não tem direito à meia-entrada.")
"""


