# Robiliśmy na zajęciach. Test działa.


def is_palindrom(text: str) -> bool:
    tmp = ""
    for sign in text.lower():
        if sign.isalnum():
            tmp += sign
    return tmp == tmp[::-1]


print(is_palindrom("kajak"))
