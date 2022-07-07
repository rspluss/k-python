a = "Cześć"


def local():
    b = " wszystkim"
    global a
    a = "siema"
    print(a, b)


local()
