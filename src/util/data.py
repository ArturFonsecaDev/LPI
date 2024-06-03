from datetime import date


class Data:

    def __init__(self, dia, mes, ano) -> None:
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        if len(str(self.dia)) == 1:
            self.dia = '0' + str(self.dia)
        if len(str(self.mes)) == 1:
            self.mes = '0' + str(self.mes)
        formato = '{}/{}/{}'
        return formato.format(self.dia, self.mes, self.ano)

    def __eq__(self, data: object) -> bool:
        return (self.ano, self.mes, self.dia) == (data.ano, data.mes, data.dia)

    def __ne__(self, outra_data: object) -> bool:
        return not self == outra_data

    def __gt__(self, data: object) -> bool:
        return (self.ano, self.mes, self.dia) > (data.ano, data.mes, data.dia)

    def __lt__(self, data: object) -> bool:
        return (self.ano, self.mes, self.dia) < (data.ano, data.mes, data.dia)

    def __ge__(self, data: object) -> bool:
        return not self < data

    def __le__(self, data: object) -> bool:
        return not self > data

    def calcular_idade(self, data_referencia=None):
        if data_referencia is None:
            dia_referencia, mes_referencia, ano_referencia = map(
                int, date.today().strftime("%d/%m/%Y").split("/")
            )
            return
        dia_referencia = data_referencia.dia
        mes_referencia = data_referencia.mes
        ano_referencia = data_referencia.ano

        idade = ano_referencia - self.ano
        if mes_referencia < self.mes or (
            mes_referencia == self.mes and dia_referencia < self.dia
        ):
            idade -= 1

        return idade

if __name__ == '__main__':
    data1 = Data(5, 4, 2024)
    print(data1)