# 1 užduotis
# Sukurkite ir išsibandykite funkcijas, kurios:
# 1 Gražinti trijų paduotų skaičių sumą:

# def skaiciai(x1, x2, x3):
#     suma = (x1 + x2 + x3)
#     return (suma)
#
# print(skaiciai(2, 5, 10))


# # 2 Gražintų paduoto sąrašo iš skaičių, sumą:

# def skaiciai(x1=5, x2=5, x3=5):
#     suma = (x1 + x2 + x3)
#     return (suma)
#
# print(skaiciai())

# arba:
# def saraso_suma(sarasas):
#     atsakymas = 0
#     for skaicius in sarasas:
#         atsakymas += skaicius
#     return atsakymas
#
#
# sarasas = [10, 5, 20, 100]
# print(saraso_suma(sarasas))


# 3 Atspausdintų didžiausią iš kelių paduotų skaičių (panaudojant *args):

# def maximumas(*args):
#     rezultatas = args[0]
#     for skaicius in args:
#         if skaicius > rezultatas:
#             rezultatas = skaicius
#     return rezultatas
#
# print(maximumas(10, 500, 888))

# arba:
# def maximumas(*args):
#     return max(args)
#
# print(maximumas(5, 10, 800, 950, 888))

# 4 Gražintų paduotą stringą atbulai.

# zodziai = "Labas vakaras"
# print(zodziai[::-1])

# arba su def:

# def atbulai(zodziai):
#     return zodziai[::-1]
#
# print(atbulai("Labas vakaras"))


# 5 Atspausdintų, kiek paduotame stringe yra žodžių, didžiųjų ir mažųjų raidžių, skaičių.

# def sakinys(stringas):
#     print(f"Siame sakinyje yra {len(stringas.split())} zodziai")
#     didziosios = 0
#     mazosios = 0
#     skaiciai = 0
#     for simbolis in stringas:
#         if simbolis.isupper():
#             didziosios += 1
#         if simbolis.islower():
#             mazosios += 1
#         if simbolis.isnumeric():
#             skaiciai += 1
#     print(f"Didziosios: {didziosios}, mazosios: {mazosios}, skaiciai: {skaiciai}")
#
# sakinys("Vakar buvome 5 patiekalu degustacineje vakarieneje Vilniuje")

# 6 Gražintų sąrašą tik su nepasikartojančiais paduoto sąrašo elementais.

# # susikuriam lista skaiciu:
# skaiciai = [1, 3, 15, 555, 999, 555, 15, 1]
# # sukurta lista mes perkeliam i f-ja
# def unikalus_sarasas(skaiciai):
# # susikuriam tuscia lista, kuris rezultate duos unikalius skaicius
#     listas =[]
# # tada naudojam SET, kad istrauktume unikalius skaicius
#     unikalus_skaiciai = set(skaiciai)
# # jau turiu unikalius numerius, dabar reikia juos prideti prie listo is SET f-jos: pridejimo f-ja yra APPEND
#     for skaicius in unikalus_skaiciai:
#             listas.append(skaicius)
#     return listas
#
# print(unikalus_sarasas(skaiciai))

# 7 Gražintų, ar paduotas skaičius yra pirminis.
# ar while ciklas naudojamas po def f? galima, po def galima beleka naudot if, for, while ir t.t.
# naudojame range todel, kad tai yra LISTAS ir su for mums tinka
# kodel skliausteliuose 2? todel, kad pirminis skaicius(dalinasi is pacio saves ir daugiau uz 1) pradedamas nuo 2, "skaicius" - kur sustoti

# ivestas_skaicius = int(input("Iveskite skaiciu: "))
#
# def ar_skaicius_pirminis(skaicius):
#     if skaicius > 1:
#         for pirminis in range(2, skaicius):
#             if skaicius % pirminis == 0:
#                 return False
#         return True
#
# print(ar_skaicius_pirminis(ivestas_skaicius))


# 8 Išrikiuotų paduoto stringo žodžius nuo paskutinio iki pirmojo

# def isrikiuoti(sakinys):
#     zodziai = sakinys.split()
#     return zodziai[::-1]
#
# print("".join(isrikiuoti("laba diena su vistiena")))



# 9 Gražina, ar paduoti metai yra keliamieji, ar ne.

# metai = int(input("Iveskite metus:"))
#
# def patikrinimas(metai):
#     if (metai % 4 ==0) or (metai % 100 == 0) or (metai % 400 == 0): #skliaustai nera butini
#         print("keliamieji metai")
#     else:
#      print("nekeliamieji metai")
#
# print(patikrinimas(metai))


# 10 Atspausdina, kiek nuo paduotos sukakties praėjo metų, mėnesių, dienų, valandų, minučių, sekundžių.

# import datetime
#
#
# def tikrinam_data(sukaktis):
#     ivesta_data = datetime.datetime.strptime(sukaktis, "%Y-%m-%d %H:%M:%S")
#     dabar = datetime.datetime.now()
#     skirtumas = dabar - ivesta_data
#
#     print("Praejo metu: ", skirtumas.days // 365)
#     print("Praejo menesiu: ", skirtumas.days // 365 * 12)
#     print("Praejo dienu: ", skirtumas.days)
#     print("Praejo valandu: ", skirtumas.total_seconds() / 3600)
#     print("Praejo minuciu: ", skirtumas.total_seconds() / 60)
#     print("Praejo sekundziu: ", skirtumas.total_seconds())
#
# print(tikrinam_data("1997-09-12 11:11:11"))

# 2 užduotis
# Sukurti funkciją, kuri patikrintų, ar paduotas Lietuvos piliečio asmens kodas yra validus.
# Padaryti, kad programa sugeneruotų teisingą asmens kodą (panaudojus anksčiau sukurtą funkciją) pagal įvestą lytį, gimimo datą ir eilės numerį).

# class Sakinys:
#     def __init__(self, tekstas="Zen of Python"):
#         self.tekstas = tekstas
#
#     def atbulai(self):
#         return self.tekstas[::-1]
#
#     def didziosiomis(self):
#         return self.tekstas.upper()
#
#     def mazosiomis(self):
#         return self.tekstas.lower()
#
#     def ieskoti(self, ieskomas):
#         return self.tekstas.count(ieskomas)
#
#     def pakeisti(self, senas, naujas):
#         return self.tekstas.replace(senas, naujas)
#
#     def atspausdintiZodi(self, skaicius):
#         suskirstytas = self.tekstas.split()
#         return suskirstytas[skaicius]
#
#     def info(self):
#         zodziu_kiekis = len(self.tekstas.split())
#         skaiciai = sum(i.isnumeric() for i in self.tekstas)
#         didziosios = sum(i.isupper() for i in self.tekstas)
#         mazosios = sum(i.islower() for i in self.tekstas)
#         print(
#             f"Žodžių kiekis: {zodziu_kiekis}, Skaičiai: {skaiciai}, Didžiosios: {didziosios}, Mažosios: {mazosios}")
#
#     def __str__(self):
#         return ("Tekstas: " + self.tekstas)
#
#
# mano_sakinys = Sakinys("Mano tekstas yra toks")
# print(mano_sakinys.atbulai())
# print(mano_sakinys.mazosiomis())
# print(mano_sakinys.didziosiomis())
# print(mano_sakinys.ieskoti("a"))
# print(mano_sakinys.pakeisti("Mano", "Savo"))
# print(mano_sakinys.atspausdintiZodi(2))
# mano_sakinys.info()
# print(mano_sakinys)