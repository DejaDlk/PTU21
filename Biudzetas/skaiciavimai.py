from Biudzetas.pajamos_islaidos import PajamuIrasas, IslaiduIrasas


class Biudzetukas:
    def __init__(self):
        self.zurnalas = []

    def ivesti_pajamas(self):
        suma = float(input("Suma: "))
        siuntejas = input("Siuntėjas: ")
        info = input("Papildoma informacija: ")
        irasas = PajamuIrasas(suma, siuntejas, info)
        self.zurnalas.append(irasas)

    def ivesti_islaidas(self):
        suma = float(input("Suma: "))
        atsiskaitymo_budas = input("Atsiskaitymo būdas: ")
        isigyta_preke_paslauga = input("Įsigyta prekė/paslauga: ")
        irasas = IslaiduIrasas(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
        self.zurnalas.append(irasas)

    def ataskaita(self):
        print("ATASKAITA : ")
        for irasas in self.zurnalas:
            print(irasas)

    def balansas(self):
        suma = 0
        for irasas in self.zurnalas:
# TYPE dedam todel, kad niekur kitur nepriskyriau sito ir jeigu neidedam "type"- neskaiciuoja, type priima argumenta ir inputa
# klausiam koks mano objekto (irasas), tipas? ar tiesa
            if type(irasas) is PajamuIrasas:
                suma += irasas.suma
            if type(irasas) is IslaiduIrasas:
                suma -= irasas.suma
        print("Balansas", suma)


biudzetas = Biudzetukas()


while True:
    pasirinkimas = int(input("1 - įvesti pajamas, \n2 - įvesti išlaidas, \n3 - gauti balansą, \n4 - parodyti ataskaitą, \n5 - išeiti iš programos"))
    if pasirinkimas == 1:
        biudzetas.ivesti_pajamas()
    if pasirinkimas == 2:
        biudzetas.ivesti_islaidas()
    if pasirinkimas == 3:
        biudzetas.balansas()
    if pasirinkimas == 4:
        biudzetas.ataskaita()
    if pasirinkimas == 5:
        print("Viso gero")
        break