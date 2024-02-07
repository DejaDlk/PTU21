class Kursas:
    def __init__(self, pavadinimas, destytojas, trukme):
        self.pavadinimas = pavadinimas
        self.destytojas = destytojas
        self.trukme = trukme

    def __repr__(self):
        return (f"({self.pavadinimas}, {self.destytojas}, {self.trukme})")

    def destyti(self):
        print("Vyksta mokymas!")
        







