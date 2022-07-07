# Działa: program i test
list = [2, 5, 7]


def max_of_three(numbers: list) -> int:
    max = 0
    for x in numbers:
        if x > max:
            max = x

    return max


print(max_of_three(list))
