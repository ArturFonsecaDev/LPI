
class Jogador:
    def __init__(self, nome, rating_atual, titulo_fide=None, estrangeiro=False):
        self.nome = nome
        self.rating_atual = rating_atual
        self.titulo_fide = titulo_fide if titulo_fide in {
            'CM', 'FM', 'IM', 'GM'} else 'Sem Título'
        self.estrangeiro = estrangeiro

    def __str__(self):
        formato = '{:<20} | {:<4} | {:<3} | {:<3} |'
        return formato.format(self.nome, self.rating_atual, self.titulo_fide, 'Sim' if self.estrangeiro else 'Não')



jogadores = []


def get_jogadores():
    return jogadores


def set_jogador(jogador):
    jogadores.append(jogador)


def filtrar_por_rating(jogador, rating_minimo):
    return rating_minimo is None or jogador.rating_atual >= rating_minimo


def filtrar_por_prefixo_nome(jogador, prefixo_nome):
    return prefixo_nome is None or jogador.nome.startswith(prefixo_nome)


def filtrar_por_titulo_fide(jogador, titulo_fide_min):
    if titulo_fide_min is None:
        return True
    titulo_numerico = {'Sem Título': 0, 'CM': 1, 'FM': 2, 'IM': 3, 'GM': 4}
    jogador_titulo_numerico = titulo_numerico.get(jogador.titulo_fide, 0)
    return jogador_titulo_numerico >= titulo_numerico.get(titulo_fide_min, 0)


def filtrar_por_estrangeiro(jogador, estrangeiro):
    return estrangeiro is None or jogador.estrangeiro == estrangeiro


def seleciona_jogadores(prefixo_nome=None, rating_minimo=None, titulo_fide_min=None, estrangeiro=None):
    jogadores_selecionados = []
    filtros = [
        lambda jogador: filtrar_por_rating(jogador, rating_minimo),
        lambda jogador: filtrar_por_prefixo_nome(jogador, prefixo_nome),
        lambda jogador: filtrar_por_titulo_fide(jogador, titulo_fide_min),
        lambda jogador: filtrar_por_estrangeiro(jogador, estrangeiro)
    ]
    for jogador in jogadores:
        if all(filtro(jogador) for filtro in filtros):
            jogadores_selecionados.append(jogador)


