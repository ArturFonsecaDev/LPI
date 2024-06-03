from util.data import Data

partidas = {}


def get_partidas():
    return partidas


def inserir_partida(partida):
    if partida.nome not in partidas.keys():
        partidas[partida.nome] = partida
        return
    print(f"Partida {partida.nome} já cadastrada!")


class Partida:

    def __init__(self, data: Data, jogadores: list) -> None:
        self.data = data
        self.jogadores = jogadores

    @property
    def jogadores(self):
        return self._jogadores

    @jogadores.setter
    def jogadores(self, new_value):
        jogadores_str = [str(jogador) for jogador in self.jogadores]
        jogador1 = jogadores_str[0] if jogadores_str else "Anonymous"
        jogador2 = jogadores_str[1] if len(jogadores_str) > 1 else "Anonymous"
        self._jogadores = [jogador1, jogador2]
        return

    def __str__(self) -> str:
        formato = "{}'X'{} | {}"
        return formato.format(self.jogador1, self.jogador2, self.data)


if "__main__" == __name__:
    jogadores = ["Artur de Oliveira", "Hikaru Nakamura"]
    partida1 = Partida(data=(5, 12, 2024), jogadores=jogadores)
    print(partida1)
