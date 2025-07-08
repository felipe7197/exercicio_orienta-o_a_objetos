class Musica:
   
   def __init__(self, nome, artista, duracao=0):
      self.nome = nome
      self.artista = artista
      self.duracao = duracao

   def __str__(self):
    return f'{self.nome} | {self.artista} | {self.duracao}'

musica1 = Musica(nome ='Mirror, Mirror', artista = 'Blind Guardian', duracao = 507)
musica2 = Musica(nome ='Bohemian Raphsody', artista = 'Queen', duracao = 820)
musica3 = Musica(nome = 'Ghost opera', artista ='Blind guardian', duracao = 523)


print(musica1)
print(musica2)
print(musica3)
