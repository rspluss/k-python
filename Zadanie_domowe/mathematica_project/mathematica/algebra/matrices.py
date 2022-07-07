m1 = [
    [1, 2],
    [3, 4],
]

m2 = [
    [3, 4],
    [3, 4],
]


def add_matrices(m1: list, m2: list) -> list:
    m3 = []
    for x, y in zip(m1, m2):
        a = []
        for u, i in zip(x, y):
            a.append(u + i)
        m3.append(a)
    return m3


print(add_matrices(m1, m2))


def sub_matrices(m1: list, m2: list) -> list:
    pass
