from util.gerais import mostrar_objetos

class Jogador:
    def __init__(self, nome, rating_atual, estrangeiro=False):
        self.nome = nome
        self.rating_atual = rating_atual
        self.titulo_fide = ''
        self.estrangeiro = estrangeiro

    def __str__(self):
        formato = '{:<20} | {:<4} | {:^3} | {:^5} |'
        return formato.format(self.nome, self.rating_atual, self.titulo_fide, 'Sim' if self.estrangeiro else 'Não')

    @property
    def titulo_fide(self):
        return self._titulo_fide

    @property
    def titulo_fide(self):
        return self._titulo_fide

    @titulo_fide.setter
    def titulo_fide(self, new_value):
        if self.rating_atual >= 2500:
            self._titulo_fide = 'GM'
            return
        if self.rating_atual >= 2400:
            self._titulo_fide = 'IM'
            return
        if self.rating_atual >= 2300:
            self._titulo_fide = 'FM'
            return
        if self.rating_atual >= 2100:
            self._titulo_fide = 'CM'
            return
        self._titulo_fide = '--'


# fim da classe


jogadores = []


def obter_jogadores():
    return jogadores


def inserir_jogador(jogador):
    jogadores.append(jogador)


def _filtrar_por_rating(jogador, rating_minimo):
    return rating_minimo is None or jogador.rating_atual >= rating_minimo


def _filtrar_por_prefixo_nome(jogador, prefixo_nome):
    return prefixo_nome is None or jogador.nome.startswith(prefixo_nome)


def _filtrar_por_titulo_fide(jogador, titulo_fide_minimo):
    if titulo_fide_minimo is None:
        return True
    titulo_numerico = {'Sem Título': 0, 'CM': 1, 'FM': 2, 'IM': 3, 'GM': 4}
    jogador_titulo_numerico = titulo_numerico.get(jogador.titulo_fide, 0)
    return jogador_titulo_numerico >= titulo_numerico.get(titulo_fide_minimo, 0)


def _filtrar_por_estrangeiro(jogador, estrangeiro):
    return estrangeiro is None or jogador.estrangeiro == estrangeiro


def _adicionar_filtros(prefixo_nome=None, rating_minimo=None, titulo_fide_min=None, estrangeiro=None):
    str_filtros = 'Filtros -- '
    if prefixo_nome is not None: str_filtros += ' Prefixo Nome --'
    if rating_minimo is not None: str_filtros += ' Mínimo de Rating --'
    if titulo_fide_min is not None: str_filtros += ' Título Fide Mínimo --'
    if estrangeiro is not None: str_filtros += ' Estrangeiro --'
    return str_filtros


def seleciona_jogadores(prefixo_nome=None, rating_minimo=None, titulo_fide_min=None, estrangeiro=None):
    jogadores_selecionados = []
    str_filtros = _adicionar_filtros(prefixo_nome, rating_minimo, titulo_fide_min, estrangeiro)
    filtros = [
        lambda jogador: _filtrar_por_rating(jogador, rating_minimo),
        lambda jogador: _filtrar_por_prefixo_nome(jogador, prefixo_nome),
        lambda jogador: _filtrar_por_titulo_fide(jogador, titulo_fide_min),
        lambda jogador: _filtrar_por_estrangeiro(jogador, estrangeiro)
    ]
    for jogador in jogadores:
        if all(filtro(jogador) for filtro in filtros):
            jogadores_selecionados.append(jogador)
    return jogadores_selecionados, str_filtros


if __name__ == '__main__':
    cabecalho = 'Lista de Jogadores:\nOrdem | Nome | Rating | Título | Estrangeiro'
    inserir_jogador(Jogador('Rafael Correa Viana', 1900, False ))
    inserir_jogador(Jogador('Magnus Carlsen', 2862,  True))
    inserir_jogador(Jogador('Paulo Fonseca', 2400,  False))
    inserir_jogador(Jogador('Artur Fonseca', 2100, False))
    inserir_jogador(Jogador('Sara meu amor', 400, True))
    lista, filtro = seleciona_jogadores()
    mostrar_objetos(cabecalho, lista, filtro)
    print('\n')
    lista, filtro = seleciona_jogadores(titulo_fide_min='IM', rating_minimo=2000)
    mostrar_objetos(cabecalho, lista, filtro)




