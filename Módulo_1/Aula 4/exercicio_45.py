"""
Uma empresa quer saber qual é o seu melhor e pior funcionário 
em relação a vendas em um determinado mês.
funcionarios = (("João", 10000), ("Maria", 5000), ("Pedro", 15000), ("Fernanda", 8000))
"""

funcionarios = (("João", 10000), ("Maria", 5000), ("Pedro", 15000), ("Fernanda", 8000))

melhor_funcionario = max(funcionarios, key=lambda x: x[1])[0]
pior_funcionario = min(funcionarios, key=lambda x: x[1])[0]

print(f"Melhor funcionário: {melhor_funcionario}")
print(f"Pior funcionário: {pior_funcionario}")
