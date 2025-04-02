lista_de_numeros: list[int] = [40, 50, 60, -3473674, 80, 1, 25, 30]
lista_de_numeros_02: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_de_numeros_03: list[int] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


def ordenar_lista(lista: list[int]) -> list[int]:
    lista_ordenada: list[int] = []
    for i in range(len(lista)):
        menor_numero: int = min(lista)
        lista_ordenada.append(menor_numero)
        lista.remove(menor_numero)
    return lista_ordenada

    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i] < lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


nova_lista_numeros: list[int] = ordenar_lista(lista_de_numeros)
nova_lista_numeros_02: list[int] = ordenar_lista(lista_de_numeros_02)
nova_lista_numeros_03: list[int] = ordenar_lista(lista_de_numeros_03)

print(nova_lista_numeros)
print(nova_lista_numeros_02)
print(nova_lista_numeros_03)

