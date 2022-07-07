# Działa: program i test

text = "żółćęśąźń"
tresc = "Pchnąć w tę łódź jeża lub ośm skrzyń fig"


def pangram(tresc: str) -> bool:
    a = []
    for x in tresc:
        for y in text:
            if x == y:
                a.append(x)
            if len(a) == 9:
                return True


print(pangram(tresc))
