
def is_palindrom(text: str) -> bool:
    tmp = ""
    for sign in text.lower():
        if sign.isalnum():
            tmp += sign
#     if tmp == tmp[::-1]
#         return True
#     else:
#         return False

    return tmp == tmp[::-1]
    
assert is_palindrom("kajak")
