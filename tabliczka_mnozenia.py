# out = []
# a = 10
#
# i = [x for x in range(1, 11)]
# j = [i[x] * x for x in range(10)]
#
# print(j)

# Zadanie 1
var = [[i * j for i in range(1, 11)] for j in range(1, 10)]

# Zadanie 2
liczby = [1, 11, 2, 15, 4, 8, 11, 21, 34]
liczby_pierwsze = []


for x in liczby:
    if x % x == 0:
        liczby_pierwsze.append(x)

print(liczby_pierwsze)
