# Działa kod, jednak mam problem ze stworzeniem testu.

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}


def status(statuses: int) -> int:
    online, offline = 0, 0
    for x in statuses:
        if statuses[x] == "online":
            online += 1
        elif statuses[x] == "offline":
            offline += 1

    return f"Status \nonline: {online}, offline {offline}"


print(status(statuses))
