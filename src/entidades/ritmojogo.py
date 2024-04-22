from util.gerais import mostrar_objetos

class RitmoJogo:
    def __init__(self, tempo_inicial, acrescimo):
        """
        Inicializa um objeto RitmoJogo com o tempo inicial e o acréscimo especificados.

        :param tempo_inicial: O tempo inicial do jogo no formato 'minutos:segundos' ou 'minutos'.
        :param acrescimo: O acréscimo de tempo para cada jogada.
        """
        self.tempo_inicial = self.modificar_tempo(tempo_inicial)
        self.acrescimo = acrescimo

    @staticmethod
    def modificar_tempo(tempo):
        """
        Método estático que modifica o tempo para o formato de segundos.

        :param tempo: O tempo no formato 'minutos:segundos' ou 'minutos'.
        :return: O tempo convertido para segundos.
        """
        try:
            if ':' in tempo:
                minutos, segundos = map(int, tempo.split(':'))
                return minutos * 60 + segundos
            return int(tempo)
        except ValueError:
            print("Formato de tempo inválido. Use o formato 'minutos:segundos' ou 'minutos'.")
            return None

    def formatar_tempo_inicial(self):
        """
        Formata o tempo inicial para o formato 'minutos:segundos'.

        :return: O tempo inicial formatado.
        """
        minutos = self.tempo_inicial // 60
        segundos = self.tempo_inicial % 60
        return f'{minutos:02d}:{segundos:02d}'

    def __str__(self):
        """
        Retorna uma representação em string do objeto RitmoJogo.

        :return: A representação em string do objeto.
        """
        tempo_formatado = self.formatar_tempo_inicial()
        formato = '|{:^7}|{:^5}|'
        return formato.format(tempo_formatado, '+' + str(self.acrescimo))


ritmos_de_jogo = []


def obter_ritmos_de_jogo():
    """
    Retorna uma lista contendo todos os ritmos de jogo inseridos.

    :return: A lista de ritmos de jogo.
    """
    return ritmos_de_jogo


def inserir_ritmos_de_jogo(ritmo_de_jogo):
    """
    Insere um ritmo de jogo na lista de ritmos.

    :param ritmo_de_jogo: O ritmo de jogo a ser inserido.
    """
    ritmos_de_jogo.append(ritmo_de_jogo)


def _filtrar_por_tempo_inicial_minimo(ritmo_de_jogo, tempo_minimo_inicial):
    """
    Função interna para filtrar os ritmos de jogo com base no tempo inicial mínimo.

    :param ritmo_de_jogo: O ritmo de jogo a ser filtrado.
    :param tempo_minimo_inicial: O tempo mínimo inicial desejado.
    :return: True se o ritmo de jogo atender ao critério de filtro, False caso contrário.
    """
    if tempo_minimo_inicial is None:
        return True
    tempo_minimo_segundos = RitmoJogo.modificar_tempo(tempo_minimo_inicial)
    return ritmo_de_jogo.tempo_inicial >= tempo_minimo_segundos


def _filtrar_por_acrescimo_maximo(ritmo_de_jogo, acrescimo_maximo):
    """
    Função interna para filtrar os ritmos de jogo com base no acréscimo máximo.

    :param ritmo_de_jogo: O ritmo de jogo a ser filtrado.
    :param acrescimo_maximo: O acréscimo máximo desejado.
    :return: True se o ritmo de jogo atender ao critério de filtro, False caso contrário.
    """
    return acrescimo_maximo is None or ritmo_de_jogo.acrescimo <= acrescimo_maximo


def _filtrar_por_tempo_inicial_maximo(ritmo_de_jogo, tempo_maximo_inicial):
    '''
    Função interna para filtrar os ritmos de jogo com base no tempo máximo inicial.
    :param ritmo_de_jogo:
    :param tempo_maximo_inicial:
    :return:
    '''
    if tempo_maximo_inicial is None:
        return True
    tempo_maximo_segundos = RitmoJogo.modificar_tempo(tempo_maximo_inicial)
    return ritmo_de_jogo.tempo_inicial <= tempo_maximo_segundos


def _adicionar_filtro(tempo_minimo_inicial=None, tempo_maximo_inicial=None, acrescimo_maximo=None):
    """
    Adiciona filtros aplicados à seleção de ritmos de jogo.

    :param tempo_minimo_inicial: O tempo mínimo inicial desejado.
    :param acrescimo_maximo: O acréscimo máximo desejado.
    :return: Uma string representando os filtros aplicados.
    """
    filtros_dict = {
        'Tempo Mínimo Inicial': tempo_minimo_inicial,
        'Tempo Máximo Inicial': tempo_maximo_inicial,
        'Acréscimo Máximo': acrescimo_maximo
    }
    str_filtros = 'Filtros -- '
    for key, filtro in filtros_dict.items():
        if filtro is not None:
            str_filtros += f'{key}: {filtro} -- '
    return str_filtros.rstrip(' -- ')


def selecionar_ritmos_de_jogo(tempo_minimo_inicial=None, tempo_maximo_inicial=None, acrescimo_maximo=None):
    """
    Seleciona os ritmos de jogo com base nos filtros especificados.

    :param tempo_minimo_inicial: O tempo mínimo inicial desejado.
    :param tempo_maximo_inicial: O tempo máximo inicial desejado.
    :param acrescimo_maximo: O acréscimo máximo desejado.
    :return: Uma lista dos ritmos de jogo selecionados e uma string representando os filtros aplicados.
    """
    ritmos_selecionados = []
    str_filtros = _adicionar_filtro(tempo_minimo_inicial, tempo_maximo_inicial, acrescimo_maximo)
    filtros = [
        lambda ritmo: _filtrar_por_tempo_inicial_minimo(
            ritmo_de_jogo=ritmo,
            tempo_minimo_inicial=tempo_minimo_inicial
        ),
        lambda ritmo: _filtrar_por_acrescimo_maximo(
            ritmo_de_jogo=ritmo,
            acrescimo_maximo=acrescimo_maximo
        ),
        lambda ritmo: _filtrar_por_tempo_inicial_maximo(
            ritmo_de_jogo=ritmo,
            tempo_maximo_inicial=tempo_maximo_inicial
        )
    ]
    for ritmo in ritmos_de_jogo:
        if all(filtro(ritmo) for filtro in filtros):
            ritmos_selecionados.append(ritmo)
    return ritmos_selecionados, str_filtros



if __name__ == '__main__':
    cabecalho = 'Lista de Ritmos de Jogo: Tempo Inicial -- Acréscimo'
    inserir_ritmos_de_jogo(RitmoJogo(tempo_inicial='5:00', acrescimo=0))
    inserir_ritmos_de_jogo(RitmoJogo('10:00', 0))
    inserir_ritmos_de_jogo(RitmoJogo('1:00', 1))
    inserir_ritmos_de_jogo(RitmoJogo('12:00', 2))
    inserir_ritmos_de_jogo(RitmoJogo('21:00', 0))
    inserir_ritmos_de_jogo(RitmoJogo('30:00', 15))
    lista, filtro = selecionar_ritmos_de_jogo()
    mostrar_objetos(cabecalho, lista, filtro)
    print('\n')
    lista,filtro = selecionar_ritmos_de_jogo(tempo_minimo_inicial='5:00', tempo_maximo_inicial='10:00')
    mostrar_objetos(cabecalho, lista, filtro)
