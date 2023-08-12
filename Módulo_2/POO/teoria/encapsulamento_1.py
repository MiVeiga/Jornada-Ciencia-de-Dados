# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.

# Em Codeville, temos uma fábrica com processos
#  internos complexos. Usamos encapsulamento
# para ocultar os detalhes internos
# e fornecer uma interface pública.

class Fabrica:
    def __init__(self):
        self.public_info = "Isso é público"
        self._protected_info = "Isso é protegido"
        self.__private_info = "Isso é privado"
    
    def iniciar_producao(self):
        print("Produção iniciada")

    def parar_producao(self):
        print("Produção parada")
    
    def _detalhes_protegido(self):  #Metodo protegido
        return self._protected_info
    
    def __detalhes_privados(self):  #Metodo privado
        return self.__private_info

class Fornecedora(Fabrica):
    def mostrar_detalhes(self):
        print(self.public_info)
        print(self.protected_info)
        # print(self.private_info)


fabrica = Fabrica()
fornecedor = Fornecedora()

# print("Detalhes públicos")
# print(fabrica.public_info)
# print(fornecedor.public_info)

# print("Detalhes protegidos")
# print(fabrica._protected_info)
# print(fornecedor._protected_info)
# print(fornecedor._detalhes_protegido())

# print("Detalhes privados")
# print(fabrica.__private_info)