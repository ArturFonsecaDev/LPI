from util.gerais import mostrar_objetos
from entidades.jogador import *
from entidades.ritmojogo import *
from entidades.organizacao_rating import *

def cadastro_jogadores():
    inserir_jogador(Jogador(nome='Rafael Correa Viana', rating_atual=2435, estrangeiro=False))
    inserir_jogador(Jogador('Magnus Carlsen', 2862, True))
    inserir_jogador(Jogador('Paulo Fonseca', 1850, False))
    inserir_jogador(Jogador('Artur Fonseca', 2700, False))
    inserir_jogador(Jogador('Sara Sakai', 2000, True))
    inserir_jogador(Jogador('Tigran Petrosian', 2652, True))
    inserir_jogador(Jogador('Mikhail Tal', 2700, True))
    inserir_jogador(Jogador('Hikaru Nakamura', 2795, True))


def cadastro_organizacoes():
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


def cadastro_ritmo_jogo():
    inserir_ritmos_de_jogo(RitmoJogo(tempo_inicial='5:00', acrescimo=5))
    inserir_ritmos_de_jogo(RitmoJogo('10:00', 0))
    inserir_ritmos_de_jogo(RitmoJogo('1:00', 1))
    inserir_ritmos_de_jogo(RitmoJogo('12:00', 2))
    inserir_ritmos_de_jogo(RitmoJogo('21:00', 0))
    inserir_ritmos_de_jogo(RitmoJogo('30:00', 15))
    inserir_ritmos_de_jogo(RitmoJogo('0:30', 2))


if __name__ == '__main__':
    # cadastro dos jogadores
    cadastro_jogadores()
    cabecalho = 'Lista de Jogadores: Nome | Rating | Título | Estrangeiro'
    lista, filtro = selecionar_jogadores()
    mostrar_objetos(cabecalho=cabecalho, lista=lista, filtros=filtro)
    print('\n')
    lista, filtro = selecionar_jogadores(rating_minimo=1900)
    mostrar_objetos(cabecalho, lista, filtro)
    print('\n')
    lista, filtro = selecionar_jogadores(rating_minimo=1900, titulo_fide_min='GM')
    mostrar_objetos(cabecalho, lista, filtro)
    print('\n')
    lista, filtro = selecionar_jogadores(rating_minimo=1900, titulo_fide_min='GM', estrangeiro = True)
    mostrar_objetos(cabecalho, lista, filtro)
    print('\n')
    lista, filtro = selecionar_jogadores(rating_minimo=1900, titulo_fide_min='GM', estrangeiro = True, prefixo_nome ='H')
    mostrar_objetos(cabecalho, lista, filtro)

    # cadastro das organizações
    cadastro_organizacoes()
    cabecalho = 'Lista de Organizações: Nome -- Unidade Federativa -- Cidade'
    lista, filtro = selecionar_organizacoes()
    mostrar_objetos(cabecalho, lista, filtro)
    print('\n')
    lista, filtro = selecionar_organizacoes(nome='LBX')
    mostrar_objetos(cabecalho, lista, filtro)
    print('\n')
    lista, filtro = selecionar_organizacoes('LBX', unidade_federativa='SP')
    mostrar_objetos(cabecalho, lista, filtro)
    print('\n')
    lista, filtro = selecionar_organizacoes('LBX', 'SP', cidade='Barueri')
    mostrar_objetos(cabecalho, lista, filtro)

    # cadastro do ritmo de jogo
    cadastro_ritmo_jogo()
    cabecalho = 'Lista de Ritmos de Jogo: Tempo Inicial -- Acréscimo'
    lista, filtro = selecionar_ritmos_de_jogo()
    mostrar_objetos(cabecalho, lista, filtro)
    print('\n')
    lista, filtro = selecionar_ritmos_de_jogo(tempo_minimo_inicial='1:00')
    mostrar_objetos(cabecalho, lista, filtro)
    print('\n')
    lista, filtro = selecionar_ritmos_de_jogo('1:00', tempo_maximo_inicial='10:00')
    mostrar_objetos(cabecalho, lista, filtro)
    print('\n')
    lista, filtro = selecionar_ritmos_de_jogo('1:00', '10:00', acrescimo_maximo=0)
    mostrar_objetos(cabecalho, lista, filtro)
    print('\n')


