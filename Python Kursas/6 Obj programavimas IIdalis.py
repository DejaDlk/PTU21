# 1 užduotis
# Sukurti programą, kuri:
# Turėtų klasę Automobilis
# Automobilis turėtų savybes: metai, modelis, kuro_tipas
# Automobilis turėtų metodus: vaziuoti, stoveti, pildyti_degalu, kurie atitinkamai atspausdintų „Važiuoja“, „Priparkuota“, „Degalai įpilti“
# Sukūrus objektą, automatiškai atspausdintų automobilio metus, modelį ir kuro tipą
# Turėtų klasę Elektromobilis (jo tėvinis objektas – Automobilis) *Elektromobilis pakeistų Automobilio metodą pildyti_degalu taip, kad jis atspausdintų „Baterija įkrauta“
# Elektromobilis turėtų metodą vaziuoti_autonomiskai, kuris spausdintų „Važiuoja autonomiškai“
# Sukurti norimą Automobilio objektą
# Sukurti norimą Elektromobilio objektą
# Su sukurtu Automobilio objektu paleisti funkcijas vaziuoti, stoveti, pildyti_degalu
# Su sukurtu Elektromobilio objektu paleisti funkcijas vaziuoti, stoveti, pildyti_degalu, vaziuoti_autonomiskai

class Automobilis():
    def __init__(self, metai, modelis, kuro_tipas):
        self.metai = metai
        self.modelis = modelis
        self.kuro_tipas = kuro_tipas
        print("Metai:", self.metai, "Modelis:", self.modelis, "Tipas:", self.kuro_tipas)

    def vaziuoti(self):
        print("Važiuoja")
    def stoveti(self):
        print("Priparkuota")
    def pildyti_degalu(self):
        print("Degalai įpilti")


honda = Automobilis(2020, "Honda Civic", "Dyzelinas")

honda.vaziuoti()
honda.stoveti()
honda.pildyti_degalu()

class Elektromobilis(Automobilis):
    def pildyti_degalu(self):
        print("Baterija įkrauta")
    def vaziuoti_autonomiskai(self):
        print("Važiuoja autonomiškai")
    def informacija(self):
        print("Metai:", self.metai, "Modelis:", self.modelis, "Tipas:", self.kuro_tipas)

tesla = Elektromobilis(2023,"Tesla Model X", "Elektra")

tesla.vaziuoti()
tesla.stoveti()
tesla.pildyti_degalu()
tesla.vaziuoti_autonomiskai()
tesla.informacija()


# 2 užduotis
# Sukurti programą, kuri:
# Turėtų klasę Darbuotojas
# Darbuotojas turėtų savybes: vardas, valandos_ikainis, dirba_nuo
# Turėtų privatų metodą kuris paskaičiuotų, kiek darbuotojas nudirbo dienų nuo įvestos dienos (dirba_nuo) iki šiandien (turint omeny, kad darbuotojas dirba 7 dienas per savaitę)
# Turėtų metodą paskaiciuoti_atlyginima, kuris panaudodamas aukščiau aprašytu metodu, paskaičiuotų bendrą atlyginimą (turint omeny, kad darbuotojas dirba 8 valandas per dieną)
# Turėtų klasę NormalusDarbuotojas, kuri pakeistų Darbuotojo klasę taip, kad ji skaičiuotų atlyginimą turint omeny, kad darbuotojas dirba 5 dienas per savaitę (o ne 7, kaip įprastas darbuotojas).
# Sukurti norimą Darbuotojo objektą
# Sukurti norimą NormalusDarbuotojas objektą
# Su abiem objektais paleisti funkciją paskaiciuoti_atlyginima


import datetime


class Darbuotojas:
    def __init__(self, vardas, valandos_ikainis, dirba_nuo):
        self.vardas = vardas
        self.valandos_ikainis = valandos_ikainis
        self.dirba_nuo = dirba_nuo
        self.dirba_nuo_data = datetime.datetime.strptime(dirba_nuo, "%Y-%m-%d")
        print(f"Darbuotojo vardas: {vardas}, valandos įkainis: {valandos_ikainis} ir nuo kada jis dirba: {dirba_nuo}")

    def dirbta_dienu(self):
        skirtumas = datetime.datetime.today() - self.dirba_nuo_data
        return skirtumas.days

    def paskaiciuoti_atlyginima(self):
        return self.dirbta_dienu() * 8 * self.valandos_ikainis


darbuotojas_x = Darbuotojas("Tadas", 15, "2019-09-01")
print("Darbuotojas dirba:", darbuotojas_x.dirbta_dienu())
print("Atlyginimas", darbuotojas_x.paskaiciuoti_atlyginima())


class NormalusDarbuotojas(Darbuotojas):
    def dirbta_dienu(self):
        # Funkcija super() grąžina objektą, kuris atstovauja pirminę klasę, siuo atveju i DARBUOTOJO KLASE ir nudirbta_dienu:
        return super().dirbta_dienu() / 7 * 5
        return super().paskaiciuoti_atlyginima()

darbuotojas_normalus = NormalusDarbuotojas("Dainius", 15, "2019-09-01")
print(round(darbuotojas_normalus.dirbta_dienu()))
print(round(darbuotojas_normalus.paskaiciuoti_atlyginima()))

# 3 užduotis
# Patobulinti objektinio programavimo 1 pamokos biudžeto programą:
# Sukurti tėvinę klasę Irasas, kurioje būtų savybės suma , iš kurios klasės PajamuIrasas ir IslaiduIrasas paveldėtų visas savybes.
# Į klasę PajamuIrasas papildomai pridėti savybes siuntejas ir papildoma_informacija, kurias vartotojas galėtų įrašyti.
# Į klasę IslaiduIrasas papildomai pridėti savybes atsiskaitymo_budas ir isigyta_preke_paslauga, kurias vartotojas galėtų įrašyti.
# Atitinkamai perdaryti klasės Biudzetas metodus gauti_balansa ir parodyti_ataskaita kad pasiėmus įrašą iš žurnalo, atpažintų, ar tai yra pajamos ar išlaidos (pvz., panaudojus isinstance() metodą) ir atitinkamai atliktų veiksmus.
# Padaryti, kad vartotojui (per konsolę) būtų leidžiama įrašyti pajamų ir išlaidų įrašus, peržiūrėti balansą ir ataskaitą.


# Funkcija isinstance() grąžina True, jei nurodytas objektas yra nurodyto tipo, kitu atveju False.
# __init__-metodas/konstruktorius, naudojamas klasės objektams inicijuoti.
# Metodas pasirenka objektą kaip savo pirmąjį argumentą (aš), o po to pateikia visus papildomus argumentus, kuriuos jam reikia perduoti.

class Irasas:

    def __init__(self, suma):
        self.suma = suma

class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas, info):
# Funkcija super() grąžina objektą, kuris atstovauja pirminę klasę, siuo atveju i IRASO KLASE ir SUMA:
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.info = info

    def __str__(self):
        return f"Pajamos: {self.suma} (Siuntėjas - {self.siuntejas}, Informacija - {self.info})"


class IslaiduIrasas(Irasas):
    def __init__(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        super().__init__(suma)
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.isigyta_preke_paslauga = isigyta_preke_paslauga

    def __str__(self):
        return f"Išlaidos: {self.suma} (Atsiskaitymo būdas - {self.atsiskaitymo_budas}, Įsigyta - {self.isigyta_preke_paslauga})"


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