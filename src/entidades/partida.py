from util.data import Data
from entidades.jogador import obter_jogadores, Jogador, inserir_jogador

partidas = {}


def obter_partidas():
    return partidas


def inserir_partida(partida):
    if partida.id not in partidas.keys():
        partidas[partida.id] = partida
        return
    print(f"Partida {partida.id} já cadastrada!")


class Partida:

    def __init__(self, data: Data) -> None:
        self.data = data
        self.jogadores = {}
        self._id = ""

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, new_value):
        if not obter_partidas():
            self._id = 1
            return
        self._id = obter_partidas()[-1].id + 1

    def __str__(self) -> str:
        if len(self.jogadores) < 2:
            return 'Adicione 2 jogadores na partida!'

        # Assuming you have a way to represent each jogador (player)
        jogador1 = list(self.jogadores.values())[0].nome
        jogador2 = list(self.jogadores.values())[1].nome

        return f"{jogador1} vs {jogador2} | {self.data}"

    def inserir_jogadores(self, jogadores: list):
        for jogador in jogadores:
            if isinstance(jogador, Jogador):
                self.jogadores[jogador.nome] = jogador
                continue
            print(f"Objeto inválido: {jogador}. Esperava um objeto Jogador.")


if "__main__" == __name__:
    partida1 = Partida(data=Data(5, 12, 2024))

    jogador1 = Jogador(nome='Artur Fonseca', rating_atual=2000, estrangeiro=False)
    jogador2 = Jogador('Sara Megumi Sakai dos Santos', rating_atual=2100, estrangeiro=True)

    inserir_jogador(jogador1)
    inserir_jogador(jogador2)
    inserir_partida(partida1)

    partida1.inserir_jogadores([jogador1, jogador2])

    print(partida1)

