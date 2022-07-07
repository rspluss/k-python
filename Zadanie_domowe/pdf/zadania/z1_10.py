# Niestety z małą pomocą google. Nie mogłem zrozumieć, na czym polega Trójkąt Pascala :/
# Test działa

import math


def silnia(x, y):
    return int((math.factorial(x)) / ((math.factorial(y)) * math.factorial(x - y)))


def pascals_triangle(n):
    wynik = []
    for i in range(n):
        lista = []
        for j in range(i + 1):
            lista.append(silnia(i, j))
        wynik.append(lista)
    return wynik


for a in pascals_triangle(3):
    print(a)
