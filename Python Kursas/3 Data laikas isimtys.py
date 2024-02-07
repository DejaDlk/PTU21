# 1 užduotis
# Parašyti programą, kuri:
# Leistų vartotojui įvesti sveiką skaičių.
# Atspausdinti True, jei skaičius teigiamas
# Atspausdinti False, jei skaičius neigiamas ar lygus 0
# True/False reikšmei išsaugoti naudoti boolean tipo kintamąjį ar_skaicius_teigiamas
# Patarimas: naudoti input, boolean


# skaicius = int(input("Iveskite sveika skaiciu: "))
# ar_skaicius_teigiamas = skaicius > 0
# print(ar_skaicius_teigiamas)


# 2 užduotis
# Parašyti programą, kuri:
# Atspausdintų dabartinę datą ir laiką
# Atimtų iš dabartinės datos ir laiko 5 dienas ir juos atspausdintų
# Pridėti prie dabartinės datos ir laiko 8 valandas ir juos atspausdintų
# Atspausdintų dabartinę datą ir laiką tokiu formatu: 2019 03 08, 09:57:17
# Patarimas: naudoti datetime, timedelta (from datetime import timedelta)

# import datetime
# now = datetime.datetime.now()
# print(now)
# print(now - datetime.timedelta(days=5))
# print(now + datetime.timedelta(hours=8))
# # paskutinis punktas:
# print(now.strftime("%Y %m %d, %H:%M:%S"))
# # arba
# dabar = datetime.datetime(2024, 1, 24, 10, 42, 53) #kai rasome menesi, nereikia nulio pradzioje, nes mes klaida
# print(dabar)


# 3 užduotis
# Parašyti programą, kuri:
# Leistų vartotojui įvesti norimą datą ir laiką (pvz. gimtadienį)
# Paskaičiuotų ir atspausdintų, kiek nuo įvestos datos ir laiko praėjo: Metų Mėnesių Dienų Valandų Minučių Sekundžių
# Kadangi tiksliai galima paskaičiuoti tik dienas ir sekundes, metus, mėnesius ir t.t. paskaičiuokite apytiksliai.
# Patarimas: naudoti datetime, .days, .total_seconds()
# Skaičių suapvalinimo pavyzdys (kurio gali prireikti šioje užduotyje):
# skaicius = 4.66
# print(round(skaicius))

# import datetime
#
# ivesta = input("Iveskite metus (YYYY-MM-DD HH:MM:SS) ")
#
# data = datetime.datetime.strptime(ivesta, "%Y-%m-%d %H:%M:%S")
# skirtumas = (datetime.datetime.now() - data)
# print(skirtumas)
#
# print("Praejo metu: ", skirtumas.days // 365)
# print("Praejo menesiu: ", skirtumas.days // 365 * 12)
# print("Praejo dienu: ", skirtumas.days)
# print("Praejo valandu: ", round(skirtumas.total_seconds() // 3600)) #nes 60 min yra 3600sec
# print("Praejo minuciu: ", round(skirtumas.total_seconds() // 60)) #nes 1 min yra 60sec
# print("Praejo sekundziu: ", round(skirtumas.total_seconds())) #nes sekundes skaiciuoja formule total.seconds()


# 4, 5 užduotys
# Pakeisti 1 ir 3 užduotis taip, kad neteisingai įvedus duomenis ar įvykus klaidoms,
# programos mestų norimas klaidas lietuvių kalba (panaudoti try/except)

# 4.1. UZDUOTIS:


# while True:
#     try:
#         x = (int(input("Iveskite sveika skaiciu: ")) > 0)
#         break
#     except ValueError:
#         print("Ivestas neteisingas skaicius")


# 5.3. UZDUOTIS


# import datetime
#
# while True:
#     try:
#         ivesta = input("Įveskite metus (YYYY-MM-DD HH:MM:SS) ")
#         ivesta_data = datetime.datetime.strptime(ivesta, "%Y-%m-%d %H:%M:%S")
#         break
#     except ValueError:
#         print("Ivestas blogas formatas, naudokites skliausteliuose nurodytu pvz")
#
# # data = datetime.datetime.strptime(ivesta, "%Y-%m-%d %H:%M:%S") - SITOS EILUTES NEREIKIA!!!!
# skirtumas = (datetime.datetime.now() - ivesta_data)
# print(skirtumas)
#
# print("Praejo metu: ", skirtumas.days // 365)
# print("Praejo menesiu: ", skirtumas.days // 365 * 12)
# print("Praejo dienu: ", skirtumas.days)
# print("Praejo valandu: ", round(skirtumas.total_seconds() / 3600))
# print("Praejo minuciu: ", round(skirtumas.total_seconds() / 60))
# print("Praejo sekundziu: ", round(skirtumas.total_seconds()))


