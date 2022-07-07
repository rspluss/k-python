# Nie wiem, dlaczego wyświetla się tyle razy czas. Wywołuję ją tylko raz :/
# Nie robiłem testu, bo nie wiem, czy dokładnie o to chodzi :/
import datetime
import timeit


def decorator(func):
    func()


def now():
    now = datetime.datetime.now()
    print(now)


a = timeit.timeit(lambda: decorator(now), number=1000)
print(a)
