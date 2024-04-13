from util.gerais import mostrar_objetos


class Jogador:
    def __init__(self, nome, rating_atual, estrangeiro=False):
        self.nome = nome
        self.rating_atual = rating_atual
        # Setter faz a atribuição correta de self.titulo_fide
        # com base na variável rating_atual
        self.titulo_fide = ''
        # fim do comentário
        self.estrangeiro = estrangeiro

    def __str__(self):
        formato = '{:<20} | {:<4} | {:^3} | {:^5} |'
        return formato.format(self.nome, self.rating_atual, self.titulo_fide, 'Sim' if self.estrangeiro else 'Não')

    @property
    def titulo_fide(self):
        return self._titulo_fide

    # Setter responsável pela atribuição e validação do self.titulo_fide
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
    """
    Retorna uma lista contendo todos os jogadores inseridos
    pela função inserir_jogadores().
    :return:
    """
    return jogadores


def inserir_jogador(jogador):
    """
    Insere um jogador numa lista.
    A lista deve ser recuperada a partir da função obter_jogadores()
    :param jogador:
    """
    jogadores.append(jogador)


def _filtrar_por_rating(jogador, rating_minimo):
    """
        Função para uso interno ajudando o funcionamento da função seleciona jogadores.
        Não é necessário utilizar.
        :param jogador:
        :param rating_minimo:
        :return:
        """
    return rating_minimo is None or jogador.rating_atual >= rating_minimo


def _filtrar_por_prefixo_nome(jogador, prefixo_nome):
    """
        Função para uso interno ajudando o funcionamento da função seleciona jogadores.
        Não é necessário utilizar.
        :param jogador:
        :param prefixo_nome:
        :return:
        """
    return prefixo_nome is None or jogador.nome.startswith(prefixo_nome)


def _filtrar_por_titulo_fide(jogador, titulo_fide_minimo):
    """
        Função para uso interno ajudando o funcionamento da função seleciona jogadores.
        Não é necessário utilizar.
        :param jogador:
        :param titulo_fide_minimo:
        :return:
        """
    if titulo_fide_minimo is None:
        return True
    titulo_numerico = {'Sem Título': 0, 'CM': 1, 'FM': 2, 'IM': 3, 'GM': 4}
    jogador_titulo_numerico = titulo_numerico.get(jogador.titulo_fide, 0)
    return jogador_titulo_numerico >= titulo_numerico.get(titulo_fide_minimo, 0)


def _filtrar_por_estrangeiro(jogador, estrangeiro):
    """
    Função para uso interno ajudando o funcionamento da função seleciona jogadores.
    Não é necessário utilizar.
    :param jogador:
    :param estrangeiro:
    :return:
    """
    return estrangeiro is None or jogador.estrangeiro == estrangeiro


def _adicionar_filtros(prefixo_nome=None, rating_minimo=None, titulo_fide_min=None, estrangeiro=None):
    """
    Função para uso interno ajudando o funcionamento da função seleciona jogadores.
    Não é necessário utilizar.
    :param prefixo_nome:
    :param rating_minimo:
    :param titulo_fide_min:
    :param estrangeiro:
    :return:
    """
    filtros_dict = {
        'Prefixo Nome': prefixo_nome,
        'Mínimo de Rating': rating_minimo,
        'Título Fide Mínimo': titulo_fide_min,
        'Estrangeiro': estrangeiro
    }
    str_filtros = 'Filtros -- '
    for filtro, valor in filtros_dict.items():
        if valor is not None:
            str_filtros += f' {filtro}: {valor} -- '
    return str_filtros.rstrip('--')


def seleciona_jogadores(prefixo_nome: str = None, rating_minimo: int = None,
                        titulo_fide_min: str = None, estrangeiro: bool = None) -> list and str:
    """
    Retorna uma lista de jogadores com base nos parâmetros definidos.
    Deve ser utilizada em conjunto com a função inserir_jogador() e obter_jogador()
    :param prefixo_nome:
    :param rating_minimo:
    :param titulo_fide_min:
    :param estrangeiro:
    :return:
    """
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
    inserir_jogador(Jogador('Sara meu amor', 2000, True))
    lista, filtro = seleciona_jogadores()
    mostrar_objetos(cabecalho, lista, filtro)
    print('\n')
    lista, filtro = seleciona_jogadores(titulo_fide_min='IM', rating_minimo=2000)
    mostrar_objetos(cabecalho, lista, filtro)
