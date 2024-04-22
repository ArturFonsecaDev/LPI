from util.gerais import mostrar_objetos


class OrganizacaoRating:

    def __init__(self, nome, cidade, unidade_federativa):
        self.nome = nome
        self.cidade = cidade
        self.unidade_federativa = unidade_federativa

    def __str__(self):
        formato = '{:^6} | {:^4} | {:<20}'
        return formato.format(self.nome, self.unidade_federativa, self.cidade)

    # getter para a variável nome
    @property
    def nome(self):
        return self._nome

    # setter responsável por garantir que o nome da organização esteja dentro das existentes
    @nome.setter
    def nome(self, new_value):
        new_value_upper = new_value.upper()
        if new_value_upper in ['FIDE', 'CBX', 'LBX']:
            self._nome = new_value_upper
            return
        self._nome = 'FIDE'

    @property
    def unidade_federativa(self):
        return self._unidade_federativa

    # setter responsável por garantir que a self.unidade_federativa esteja
    # entre as ufs existentes, e se existir, converte para maiúscula
    @unidade_federativa.setter
    def unidade_federativa(self, new_value):
        new_value_upper = new_value.upper()
        estados = [
            'AC', 'AL', 'AP', 'AM', 'BA',
            'CE', 'DF', 'ES', 'GO', 'MA',
            'MT', 'MS', 'MG', 'PA', 'PB',
            'PR', 'PE', 'PI', 'RJ', 'RN',
            'RS', 'RO', 'RP', 'SC', 'SP',
            'SE', 'TO'
        ]
        if new_value_upper in estados:
            self._unidade_federativa = new_value_upper
            return
        self._unidade_federativa = '--'


organizacoes = []


def obter_orgarnizacoes():
    return organizacoes


def inserir_organizacoes(organizacao):
    organizacoes.append(organizacao)


def _filtrar_por_estado(organizacao, uf_filtro):
    """
    Função para uso interno ajudando o funcionamento da função
    seleciona_organizações. Não é necessário utilizar
    :param organizacao:
    :param uf_filtro:
    :return:
    """
    return uf_filtro is None or organizacao.unidade_federativa == uf_filtro


def _filtrar_por_cidade(organizacao, cidade_filtro):
    '''
    Função para uso interno ajudando o funcionamento da função
    seleciona_organizações. Não é necessário utilizar
    :param organizacao:
    :param cidade_filtro:
    :return:
    '''
    return cidade_filtro is None or organizacao.cidade == cidade_filtro


def _filtrar_por_nome(organizacao, nome_filtro):
    '''
    Função para uso interno ajudando o funcionamento da função
    seleciona_organizações. Não é necessário utilizar
    :param organizacao:
    :param nome_filtro:
    :return:
    '''
    return nome_filtro is None or organizacao.nome == nome_filtro


def _adicionar_filtros(nome=None, unidade_federativa=None, cidade=None):
    '''
    Função para uso interno ajudando o funcionamento da função
    seleciona_organizações. Não é necessário utilizar
    :param nome:
    :param unidade_federativa:
    :param cidade:
    :return:
    '''
    filtros_dict = {
        'Nome': nome,
        'Unidade Federativa': unidade_federativa,
        'Cidade': cidade
    }
    str_filtros = 'Filtros -- '
    for key, filtro in filtros_dict.items():
        if filtro is not None:
            str_filtros += f'{key}: {filtro} -- '
    return str_filtros.rstrip('-- ')


def selecionar_organizacoes(nome=None, unidade_federativa=None, cidade=None):
    organizacoes_selecionadas = []
    str_filtros = _adicionar_filtros(nome, unidade_federativa, cidade)
    filtros = [
        lambda organizacao: _filtrar_por_estado(
            organizacao=organizacao,
            uf_filtro=unidade_federativa),
        lambda organizacao: _filtrar_por_cidade(
            organizacao=organizacao,
            cidade_filtro=cidade),
        lambda organizacao: _filtrar_por_nome(
            organizacao=organizacao,
            nome_filtro=nome)
    ]
    for organizacao in organizacoes:
        if all(filtro(organizacao) for filtro in filtros):
            organizacoes_selecionadas.append(organizacao)
    return organizacoes_selecionadas, str_filtros


if __name__ == '__main__':
    cabecalho = 'Lista de Organizações: Nome -- Unidade Federativa -- Cidade'
    inserir_organizacoes(OrganizacaoRating(
        nome='FIDE', unidade_federativa='MS', cidade='Dourados'))
    inserir_organizacoes(OrganizacaoRating(
        nome='LBX', unidade_federativa='SP', cidade='Presidente Prudente'))
    inserir_organizacoes(OrganizacaoRating(
        nome='CBX', unidade_federativa='SP', cidade='São Paulo'))
    inserir_organizacoes(OrganizacaoRating(
        nome='FIDE', unidade_federativa='MG', cidade='Belo Horizonte'))
    inserir_organizacoes(OrganizacaoRating(
        nome='LBX', unidade_federativa='SP', cidade='Barueri'))
    inserir_organizacoes(OrganizacaoRating(
        nome='LBX', unidade_federativa='MS', cidade='Campo Grande'))
    lista, filtro = selecionar_organizacoes()
    mostrar_objetos(cabecalho, lista, filtro)
    print('\n')
    lista, filtro = selecionar_organizacoes(nome='LBX', unidade_federativa='SP', cidade='Barueri')
    mostrar_objetos(cabecalho, lista, filtro)



