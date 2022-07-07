# Działa: program i test
zdanie = "blslada"


def napis(napis: str) -> str:
    if len(napis) % 2 != 0:
        for x in napis:
            wynik = int(len(napis) / 2)
            return napis[wynik]
    else:
        return ""


print(napis(zdanie))
