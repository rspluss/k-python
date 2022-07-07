pomidor = {"kCal": 19, "bialko": 1, "tluszcze": 0, "wegle": 4, "cena": 5.7}
ser_mozarella = {"kCal": 248, "bialko": 18, "tluszcze": 19, "wegle": 2, "cena": 38.32}
salata = {"kCal": 13, "bialko": 1, "tluszcze": 0, "wegle": 2, "cena": 3.15}


s_pomidory = 350
s_ser_mozarella = 325
s_salata = 350

wynikPomidory = []
wynikSer = []
wynikSalata = []


for el in pomidor:
    wartoscPomidory = s_pomidory * pomidor[el] / 100
    wynikPomidory.append(wartoscPomidory)

for el in ser_mozarella:
    wartoscSer = s_ser_mozarella * ser_mozarella[el] / 100
    wynikSer.append(wartoscSer)

for el in salata:
    wartoscSalata = s_salata * salata[el] / 100
    wynikSalata.append(wartoscSalata)

produkty = ["Pomidor", "Ser", "Sałata"]
waga = [350, 325, 350]
razemWaga = 0
for x in waga:
    razemWaga += x

tablica = [wynikPomidory, wynikSer, wynikSalata]
i = 0
razemKalorie = 0
razemB = 0
razemT = 0
razemW = 0
razemKoszt = 0

for el in tablica:
    print(
        f"{produkty[i]}, Kalorie: {el[0]}, b: {el[1]}, t: {el[2]}, w: {el[3]} waga: {waga[i]}, Koszt: {round((el[4]/10), 2)}"
    )
    print("{:<10} {:<6.2f}".format(produkty[i], 1))
    i += 1

    razemKalorie += el[0]
    razemB += el[1]
    razemT += el[2]
    razemW += el[3]
    razemKoszt += el[4]

print(
    "================================================================================"
)
print(
    f"Suma: Kalorie: {razemKalorie}, b: {razemB}, t: {razemT}, w: {razemW} waga: {razemWaga}, Koszt: {round(razemKoszt, 2)}"
)
