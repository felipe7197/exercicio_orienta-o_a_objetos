class carro:

    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def __str__(self):
        return f'{self.modelo} |{self.cor} | {self.ano}'
        
carro1 = carro(modelo ='SUV',cor ='branca', ano ='2018' )
carro2 = carro (modelo ='Picape',cor ='preto', ano ='2019' )
carro3 = carro(modelo ='Perua',cor ='red', ano ='2020' )

print(carro1)
print(carro2)
print(carro3)