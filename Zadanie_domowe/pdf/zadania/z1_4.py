# Działa: program i test
double_letters = "Helo"


def double(double_letters: str) -> bool:
    for x in range(len(double_letters)):
        if double_letters[x] == double_letters[x + 1]:
            return True
        else:
            return False


print(double(double_letters))
