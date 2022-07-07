# Nie wiem dokładnie jak użyć tutaj funkcji mapy.
# Po stworzeniu map(count_words, napis) tworzyli listę z każdą literą oddzielnie.

napis = "kobyła ma mały bok! Bok"
napis2 = "C'est la vie, -- c'est la vie! closed-door"

slownik = dict()


def count_words(napis):
    list = napis.lower().replace("!", "").split(" ")
    for x in list:
        if x not in slownik:
            slownik[x] = 0
        if x in slownik:
            slownik[x] += 1
    return slownik


print(count_words(napis))
