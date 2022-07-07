class Vegetables:
    def __init__(self, name, kCal, protein, fats, carbs, cost, weight):
        self.name = name
        self.kCal = kCal
        self.protein = protein
        self.fats = fats
        self.carbs = carbs
        self.cost = cost
        self.weight = weight


class StartController:
    def __init__(self):
        self.basket = []
        (
            self.bialko,
            self.tluscz,
            self.wegle,
            self.kalorie,
            self.koszt,
            self.waga_calosc,
        ) = (0, 0, 0, 0, 0, 0)

    def add_Vegetables(self, pomidor, ser_mozarella, salata):
        self.basket = [pomidor, ser_mozarella, salata]

    def show(self):
        for x in self.basket:
            waga = x.weight
            cena = waga * x.cost / 1000
            k = x.kCal / 100 * waga
            b = x.protein / 100 * waga
            t = x.fats / 100 * waga
            w = x.carbs / 100 * waga

            print(
                f"{x.name:15}, Kalorie: {k:5.7}, Białko: {b:5.7}, Tłuszcze: {t:5.7}, Węgle: {w:5.7}, Waga: {waga}, Cena: {cena}"
            )

            self.bialko += b
            self.tluscz += t
            self.wegle += w
            self.kalorie += k
            self.koszt += cena
            self.waga_calosc += waga

        print(f"=" * 80)
        print(
            f"{'Suma':15}, Kalorie: {self.kalorie:5.7}, Białko: {self.bialko:5.7}, Tłuszcze: {self.tluscz:5.7}, Węgle: {self.wegle:5.7}, Waga: {self.waga_calosc}, Cena: {self.koszt}"
        )


class Start(StartController):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.menu()

    def menu(self):
        pomidor = Vegetables("Pomidor", 19, 1, 0, 4, 5.7, 350)
        ser_mozarella = Vegetables("Ser Mozarella", 248, 18, 19, 2, 38.32, 325)
        salata = Vegetables("Sałata", 13, 1, 0, 2, 3.15, 350)
        self.add_Vegetables(pomidor, ser_mozarella, salata)
        self.show()


start = Start("start")
