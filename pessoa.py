class pessoa:

    def __init__(self, nome='', idade='0', profissao=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'{self.nome}, {self.idade} anos, {self.profissao}'
    
    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá, sou {self.nome}! Trabalho como {self.profissao}.'
        else:
            return f'Olá, sou {self.nome}!'
        
    def aniversario(self):
        self.idade +=1

#criar as instancias das 3 pessoas
pessoa1 = pessoa(nome='Alice', idade=30, profissao='Bombeira')
pessoa2 = pessoa(nome='Luana', idade=25, profissao='Medica')
pessoa3 = pessoa(nome='Felipe', idade=32)

#imprimir as informações iniciais 
print('Informações iniciais:')
print(pessoa1)
print(pessoa2)
print(pessoa3)
print()

## Utilizando o método de instância aniversario para aumentar a idade de uma pessoa
pessoa1.aniversario()
pessoa3.aniversario()

## Imprimindo informações após aniversário
print('Informações após aniversário:')
print(pessoa1)
print(pessoa3)
print()

# Utilizando o método de classe saudacao para exibir mensagens personalizadas
print(pessoa1.saudacao)
print(pessoa2.saudacao)
print(pessoa3.saudacao)




