class programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.likes}'


class Filme(programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome,ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.duracao} minutos - {self.likes}'


class Serie(programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.temporadas} temporadas - {self.likes}'

class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self.programas = programas

    def __getitem__(self, item):
        return self.programas[item]

    def __len__(self):
        return len(self.programas)


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
todo_mundo_em_panico = Filme('todo mundo em pânico', 2000, 80)
demolidor = Serie('demolidor', 2015, 3)

filmes_programas = [vingadores, atlanta, todo_mundo_em_panico, demolidor]
danilist = Playlist('fim de semana', filmes_programas)

print(f'Essa playlist tem {len(danilist)} itens')

#para cada programa dentro de filmes_programas
for programa in danilist:
    print(programa)