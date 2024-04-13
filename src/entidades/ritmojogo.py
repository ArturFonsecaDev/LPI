class RitmoJogo:
    def __init__(self, tempo_inicial, acrescimo):
        self._tempo_inicial = tempo_inicial
        self._acrescimo = acrescimo

    def calcular_acrescimo(self):
        self._tempo_inicial += self._acrescimo

    def obter_tempo_inicial(self):
        return self._tempo_inicial


