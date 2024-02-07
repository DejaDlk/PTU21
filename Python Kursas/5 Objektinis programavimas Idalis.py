# 1 užduotis:
# Parašyti klasę Sakinys, kuri turi savybę tekstas ir metodus, kurie:

# class Sakinys:
#         # init - metodas, konstruktorius, jame inicijuojamos savybes, paleidziami metodai:
#     def __init__(self, tekstas= "Laba diena su Vistiena 888"):
#         self.tekstas = tekstas
#
#     def atbulai(self):
#         return self.tekstas[::-1]
#
#     def mazosios(self):
#         return self.tekstas.lower()
#
#     def didziosios(self):
#         return self.tekstas.upper()
#
#     def zodis(self):
#         return self.tekstas[:4]
#
#     def simboliai(self,skaiciuoti):
#         return self.tekstas.count(skaiciuoti)
#
#     def pakeisti(self, pirmas, antras):
#         return self.tekstas.replace(pirmas, antras)

# def pakeisti(self, senas, naujas):
#     return self.tekstas.replace(senas, naujas)
#
#     def skaiciavimai(self):
#         zodziai = len(self.tekstas.split())
#
#         didziosios = 0
#         mazosios = 0
#         skaiciai = 0
#
#         for simbolis in self.tekstas:
#             if simbolis.isupper():
#                 didziosios += 1
#             elif simbolis.islower():
#                 mazosios += 1
#             elif simbolis.isnumeric():
#                 skaiciai += 1
#                 return (f"Zodziu kiekis: {zodziai}, didziosios: {didziosios}, mazosios: {mazosios}, skaiciai: {skaiciai}")
#
# ilgas_sakinys = Sakinys()

# # Gražina tekstą atbulai
# print(ilgas_sakinys.atbulai())
# # Gražina tekstą mažosiomis raidėmis
# print(ilgas_sakinys.mazosios())
# # Gražina tekstą didžiosiomis raidėmis
# print(ilgas_sakinys.didziosios())
# # Gražina žodį pagal nurodytą eilės numerį
# print(ilgas_sakinys.zodis())
# # Gražina, kiek tekste yra nurodytų simbolių arba žodžių
# print(ilgas_sakinys.simboliai(skaiciuoti="a"))
# # Gražina tekstą su pakeistu nurodytu žodžiu arba simboliu
# print(ilgas_sakinys.pakeisti(pirmas ="Vistiena", antras = "Kiauliena"))
# # Atspausdina, kiek sakinyje yra žodžių, skaičių, didžiųjų ir mažųjų raidžių
# # jeigu nenorim gauti NONE reiksmes nepanaudojant RETURN, tada dedam antra varianta spausdinimo be print :
# print(ilgas_sakinys.skaiciavimai())
# # Susikurti kelis klasės objektus ir išbandyti visus metodus
# ??????????????????????



# 2 užduotis:
# Sukurti klasę Sukaktis, kuri turėtų savybę data (galima atskirai įvesti metus, mėnesius ir kt.) ir metodus, kurie:
# Atspausdina, kiek nuo įvestos datos praėjo metų, savaičių, dienų, valandų, minučių, sekundžių
# Gražina, ar nurodytos datos metai buvo keliamieji
# Atima iš nurodytos datos nurodytą kiekį dienų ir gražina naują datą
# Prideda prie nurodytos datos nurodytą kiekį dienų ir gražina naują datą

# import datetime
# import calendar
#
#
# class Sukaktis:
#     def __init__(self, metai=2000, menuo=12, diena=12, valandos=12, minutes=12):
#         self.metai = metai
#         self.menuo = menuo
#         self.diena = diena
#         self.valandos = valandos
#         self.minutes = minutes
#         self.data = datetime.datetime(metai, menuo, diena, valandos, minutes)
#
#     def smulkiai(self):
#         now = datetime.datetime.now()
#         skirtumas = now - self.data
#         print(f"Praėjo metų: ", skirtumas.days // 365)
#         print("Praėjo mėnesių: ", skirtumas.days / 365 * 12)
#         print("Praėjo savaičių: ", skirtumas.days / 7)
#         print("Praėjo dienų: ", skirtumas.days)
#         print("Praėjo valandų: ", skirtumas.total_seconds() / 3600)
#         print("Praėjo minučių: ", skirtumas.total_seconds() / 60)
#         print("Praėjo sekundžių: ", skirtumas.total_seconds())
#
#     def arKeliamieji(self):
#         if calendar.isleap(self.metai):
#             print("Keliamieji metai")
#
#     def atimtiDienas(self, dienos):
#         return self.data - datetime.timedelta(days=dienos)
#
#     def pridetiDienas(self, dienos):
#         return self.data + datetime.timedelta(days=dienos)
#
#     def __str__(self):
#         return (
#             f"Data: {self.metai}-{self.menuo}-{self.diena} {self.valandos}:{self.minutes}")
#
#
# data1 = Sukaktis(2000, 1, 1, 12, 12)
# data1.arKeliamieji()
# data1.smulkiai()
# print(data1.atimtiDienas(5))
# print(data1.pridetiDienas(45))
# print(data1)


# 3 užduotis:
# Perdaryti 1 užduotį taip, kad jei kuriant objektą, nepaduodamas joks tekstas, veiksmai turi būti atliekami su „Zen of Python“ tekstu
# Perdaryti 2 užduotį taip, kad jei kuriant objektą, nepaduodamas jokia data, veiksmai turi būti atliekami su programuotojo gimtadieniu
# 4 užduotis:
# Perdaryti 1 užduotį taip, kad spausdinant sakinio objektą, spausdintų ne objekto adresą, o įvestą tekstą
# Perdaryti 2 užduotį taip, kad spausdinant datos objektą, spausdintų ne objekto adresą, o įvestą datą

# CIA NAUDOTUME __str__
#
#
# 5 uzduotis
class Irasas:
    def __init__(self, tipas, suma):
        self.tipas = tipas
        self.suma = suma
    def __str__(self):
        return f"{self.tipas}: {self.suma}"

class Biudzetas:
    def __init__(self):
        self.zurnalas = []
    def prideti_pajamu_irasa(self, suma):
        pajamos = Irasas("Pajamos", suma)
        self.zurnalas.append(pajamos)
    def prideti_islaidu_irasa(self, suma):
        islaidos = Irasas("Išlaidos", suma)
        self.zurnalas.append(islaidos)
    def gauti_balansa(self):
        suma = 0
        for irasas in self.zurnalas:
            if irasas.tipas == "Pajamos":
                suma += irasas.suma
            if irasas.tipas == "Išlaidos":
                suma -= irasas.suma
        print(suma)
    def parodyti_ataskaita(self):
        for irasas in self.zurnalas:
            print(f"{irasas.tipas}: {irasas.suma}")

biudzetas = Biudzetas()

while True:
    pasirinkimas = int(input("1 - įvesti pajamas, \n2 - įvesti išlaidas, \n3 - gauti balansą, \n4 - parodyti ataskaitą, \n9 - išeiti iš programos"))
    if pasirinkimas == 1:
        suma = float(input("Įveskite pajamų sumą: "))
        biudzetas.prideti_pajamu_irasa(suma)
    if pasirinkimas == 2:
        suma = float(input("Įveskite išlaidų sumą: "))
        biudzetas.prideti_islaidu_irasa(suma)
    if pasirinkimas == 3:
        biudzetas.gauti_balansa()
    if pasirinkimas == 4:
        biudzetas.parodyti_ataskaita()
    if pasirinkimas == 9:
        print("Viso gero")
        break


# ARBA KITAIP
# class Irasas:
#     def __init__(self, suma):
#         self.suma = suma
#
#
# class PajamuIrasas(Irasas):
#     def __init__(self, suma, siuntejas, info):
#         super().__init__(suma)
#         self.siuntejas = siuntejas
#         self.info = info
#
#     def __str__(self):
#         return f"Pajamos: {self.suma} (siuntėjas - {self.siuntejas}, info - {self.info})"
#
#
# class IslaiduIrasas(Irasas):
#     def __init__(self, suma, atsiskaitymo_budas, isigyta, info):
#         super().__init__(suma)
#         self.atsiskaitymo_budas = atsiskaitymo_budas
#         self.isigyta = isigyta
#         self.info = info
#
#     def __str__(self):
#         return f"Išlaidos: {self.suma} (atsiskaitymo būdas - {self.atsiskaitymo_budas}, įsigyta - {self.isigyta}, info - {self.info})"
#
#
# class Biudzetas:
#     def __init__(self):
#         self.zurnalas = []
#
#     def ivesti_pajamas(self):
#         suma = float(input("Suma: "))
#         siuntejas = input("Siuntėjas: ")
#         info = input("Papildoma informacija: ")
#         irasas = PajamuIrasas(suma, siuntejas, info)
#         self.zurnalas.append(irasas)
#
#     def ivesti_islaidas(self):
#         suma = float(input("Suma: "))
#         atsiskaitymo_budas = input("Atsiskaitymo būdas: ")
#         isigyta = input("Įsigyta prekė/paslauga: ")
#         info = input("Papildoma informacija: ")
#         irasas = IslaiduIrasas(suma, atsiskaitymo_budas, isigyta, info)
#         self.zurnalas.append(irasas)
#
#     def ataskaita(self):
#         print("-----------------")
#         for irasas in self.zurnalas:
#             print(irasas)
#
#     def balansas(self):
#         suma = 0
#         for irasas in self.zurnalas:
#             if type(irasas) is PajamuIrasas:
#                 suma += irasas.suma
#             if type(irasas) is IslaiduIrasas:
#                 suma -= irasas.suma
#         print("Balansas", suma)
#
#
# biudzetas = Biudzetas()
#
# while True:
#     veiksmas = int(input("""
#     1 - įvesti pajamas
#     2 - įvesti išlaidas
#     3 - balansas
#     4 - ataskaita
#     5 - išeiti
#     """))
#     match veiksmas:
#         case 1:
#             biudzetas.ivesti_pajamas()
#         case 2:
#             biudzetas.ivesti_islaidas()
#         case 3:
#             biudzetas.balansas()
#         case 4:
#             biudzetas.ataskaita()
#         case 5:
#             break