
#Em Codeville, temos diferentes tipos de alunos na 
# escola, mas nos concentramos nos atributos essenciais, 
# como nome e idade, enquanto ocultamos os detalhes internos.

class Aluno:
    def __init__(self, nome, idade, matricula, turma):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
        self.turma = turma
    
    def apresentar(self):
        print(f"Oie, meu nome é {self.nome}, tenho {self.idade} anos e sou da turma {self.turma.nome}")


class Turma:
    def __init__(self, nome, serie):
        self.nome = nome
        self.serie = serie
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def listar_alunos(self):
        print(f"Aluno da turma {self.nome} - Série {self.serie}")
        for aluno in self.alunos:
            print(f"Nome: {aluno.nome}, Matrícula: {aluno.matricula}")


#Criando objetos das classes

turma_a = Turma("A", 8)
aluno_1 = Aluno("João", 13, "72827", turma_a)
aluno_2 = Aluno("Maria", 13, "9182", turma_a)

#Adicionando alunos na Turma
turma_a.adicionar_aluno(aluno_1)
turma_a.adicionar_aluno(aluno_2)


#Apresentação dos alunos

# for aluno in turma_a.alunos:
#     aluno.apresentar()

# turma_a.listar_alunos()

