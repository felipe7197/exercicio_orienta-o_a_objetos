class Restaurante:

    def __init__(self, nome, categoria, preco, menu ):
        self.nome = nome
        self.categoria = categoria
        self.ativo = True
        self.preco = preco
        self.menu = menu

    def __str__(self):
        return f'{self.nome} | {self.categoria}| {self.preco} |{self.menu}'
    
class Cliente:

    def __init__(self, nome, cpf, mesa, data):
        self.nome = nome
        self.cpf = cpf
        self.mesa = mesa
        self.data = data

    def __str__(self):
        return f'{self.nome} | {self.cpf} |{self.mesa} |{self.data}'


restaurante1 = Restaurante('Praça', 'Gourmet','15.00', '5 estrelas')
cliente = Cliente('Arthur', '236548582', '45', '23/06/2024')

print(restaurante1)
print(cliente)