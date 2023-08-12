# Suponha que em Codeville temos um sistema
# de gerenciamento de biblioteca. Vamos criar
# um exemplo de abstração com foco nos atributos
# essenciais dos livros:

class Livro:
    def __init__(self, titulo,autor, genero):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
    
    def mostrar_info(self):
        print(f"Título:{self.titulo}")
        print(f"Autor:{self.autor}")
        print(f"Genero:{self.genero}")


class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []
    
    def adicionar_livros(self, livro):
        self.livros.append(livro)
    
    def listar_livros(self):
        print(f"Livros disponiveis na biblioteca {self.nome}")
        for livro in self.livros:
            print(f"- {livro.titulo} de {livro.autor}")

livro1 = Livro("Aventura na Floresta", "Joao", "Aventura")
livro2 = Livro("Harry Potter", "J.K", "Magia")

biblioteca = Biblioteca("Biblioteca Central")

biblioteca.adicionar_livros(livro1)
biblioteca.adicionar_livros(livro2)

biblioteca.listar_livros()