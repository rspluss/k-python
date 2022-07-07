# Działa: program i test
m1 = [
    [1, 2],
    [3, 4],
]
lista = []


def flatten(m1: list) -> list:
    for x in m1:
        for y in x:
            lista.append(y)
    return lista


print(flatten(m1))
