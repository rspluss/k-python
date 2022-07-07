# Działa: program i test


def perfect_number(x):
    list = []
    suma = 0
    for i in range(1, (int(x / 2) + 1)):
        if x % 2 == 0:
            list.append(i)

    for a in list:
        suma += a
        if suma == x:
            return True


print(perfect_number(27))
