def mostrar_objeto(indice, objeto) -> None:
    separador = "-"
    ordem = indice + 1
    frase = f"{ordem} {separador} {objeto}"
    print(frase)


def mostrar_objetos(cabecalho, lista, filtros=None) -> None:
    if filtros is not None:
        print(filtros)
    print(cabecalho)
    for indice, objeto in enumerate(lista):
        mostrar_objeto(indice, str(objeto))
