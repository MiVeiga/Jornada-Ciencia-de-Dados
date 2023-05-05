# Uma clínica médica quer um sistema  para percorrer a lista de pacientes e exibir a idade de cada um.
# pacientes = [{'nome': 'Ana', 'idade': 35}, {'nome': 'João', 'idade': 42}, {'nome': 'Pedro', 'idade': 28}, {'nome': 'Maria', 'idade': 50}]

pacientes = [{'nome': 'Ana', 'idade': 35}, {'nome': 'João', 'idade': 42}, {
    'nome': 'Pedro', 'idade': 28}, {'nome': 'Maria', 'idade': 50}]

#Para cada paciente, montamos sua ficha - William
for paciente in pacientes:
   print('{} tem {} anos'.format(paciente['nome'], paciente['idade']))


#Para cada paciente, montamos sua ficha - Pedro
for dic in pacientes:
    for nome,idade in dic.items():
        print(nome,idade)