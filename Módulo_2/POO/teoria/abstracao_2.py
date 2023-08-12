#Imagine que em Codeville temos um sistema 
# de pedidos online. Vamos criar um exemplo 
# de abstração com foco nos atributos 
# essenciais dos pedidos:


class Pedido: 
    def __init__(self, numero_pedido, cliente,produtos):
        self.numero_pedido = numero_pedido
        self.cliente = cliente
        self.produtos = produtos
    
    def calcular_total(self):
        total = sum(produto.preco for produto in self.produtos)
        return total
    
    def mostrar_detalhes(self):
        print(f"Número do pedido: {self.numero_pedido}")
        print(f"Cliente: {self.cliente}")
        print(f"Produtos:")
        for produto in self.produtos:
            print(f" - {produto.nome} - R$ {produto.preco}")


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


produto_pedidos = [Produto("Camisa", 20), Produto("Calça", 30), Produto("Suco", 2)]
pedido = Pedido(123, "Maria", produto_pedidos)

# pedido.mostrar_detalhes()
# print(f"{pedido.calcular_total()}")