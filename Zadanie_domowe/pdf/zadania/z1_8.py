# Działa: program i test
lista = {"a": "1", "b": "4"}


def sumator(lista):
    suma = 0
    if isinstance(lista, list) or isinstance(lista, tuple) or isinstance(lista, set):
        for x in lista:
            suma += int(x)
        return suma
    elif isinstance(lista, dict):
        for x in lista:
            suma += int(lista[x])
        return suma


print(sumator(lista))
