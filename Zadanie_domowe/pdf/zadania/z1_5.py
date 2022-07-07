is_anagram = ["typhoon", "opython"]


def anagram(anagram: str) -> bool:
    list1 = list(anagram[0])
    list2 = list(anagram[1])
    list1.sort()
    list2.sort()

    return list1 == list2


print(anagram(is_anagram))
