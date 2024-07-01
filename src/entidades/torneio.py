torneios = {}


def obter_torneios():
    return torneios


def inserir_torneio(torneio):
    if torneio.nome not in torneios.keys():
        torneios[torneio.nome] = torneio
        return
    print("Torneio já cadastrado!")


class Torneio:

    def __init__(self, nome):
        self.nome = nome
        self.id = None
        self.partidas = {}

    @id
    def id(self):
        return self._id



