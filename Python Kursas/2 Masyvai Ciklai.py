# 2 PASKAITA, 1 KLAUSIMAS
# #Sukurti norimą sąrašą ir žodyną ir juose:
# Atspausdinti vieną norimą įrašą
# Pridėti įrašą
# Ištrinti įrašą
# Pakeisti įrašą
# Išbandyti kitas sąrašų ir žodynų funkcijas: clear(), index(), insert(), remove...

# sarasas = [2, 5, 6, {"Karolis": 25}]
# print(sarasas)
#
# print(sarasas[0])
#
# sarasas.append(15)
# print(sarasas)
#
# sarasas.pop(2)
# print(sarasas)
#
# sarasas[0]= 5
# print(sarasas)
#
# sarasas.reverse()
# print(sarasas)
#
# print(len(sarasas))
#
# sarasas.clear()
# print(sarasas)


# 2 KLAUSIMAS:
# Parašyti programą, kuri:
# Leistų vartotojui įvesti skaičių.
# Jei įvestas skaičius yra teigiamas, paprašyti įvesti dar vieną skaičių
# Jei įvestas skaičius neigiamas, nutraukti programą ir atspausdinti visų įvestų teigiamų skaičių sumą
# Patarimas: Naudoti ciklą while, sąlygą if, break

# skaicius = int(input("iveskite skaiciu"))
#
# skaiciu_suma = 0
#
# while skaicius >= 0:
#     skaiciu_suma += skaicius
#     skaicius = int(input("iveskite skaiciu"))
# print(skaiciu_suma)

# ARBA:

# suma = 0
# while True:
#    skaicius = int(input("Iveskite skaiciu: "))
#    if skaicius < 0:
#        break
#    suma += skaicius
# print(suma)


#3 UZDUOTIS
# Sukurti programą, kuri:
# Leistų vartotojui po vieną įvesti 5 žodžius
# Pridėtų įvestus žodžius į sąrašą
# Atspausdintų kiekvieną žodį, jo ilgį ir eilės numerį sąraše (nuo 1)
# Sudėtingiau: kad programa leistų įvesti norimą žodžių kiekį
# Patarimas: Naudoti sąrašą (list), ciklą for, funkcijas len ir index


# zodziai = []
#
# for sarasas in range(5):
#     zodziai.append(input("iveskite zodi:"))
# for zodis in zodziai:
#     print(zodziai,zodis,len(zodis),zodziai.index(zodis))



# 4 užduotis
# Kauliukų žaidimas
# Sukurti programą, kuri:
# Sugeneruotų tris atsitiktinius skaičius nuo 1 iki 6
# Jei vienas iš šių skaičių yra 5, atspausdinti „Pralaimėjai...“
# Kitu atveju atspausdinti „Laimėjai!“
# Patarimas: Naudoti while ciklą, funkciją random.randint (import random), else, break


# import random
#             #random #range nuo 1 iki 6pvz:
# numeris1 = random.randint(1, 6)
# numeris2 = random.randint(1, 6)
# numeris3 = random.randint(1, 6)
# print(numeris1, numeris2, numeris3)
#
# if numeris1 == 5 or numeris2 == 5 or numeris3 == 5:
#     print("pralaimejai..")
# else:
#     print("laimejai!")
#
#
# #arba galima daryti taip:
#
# import random
# for x in range(3):
#     num = random.randint(1, 6)
#     print(num)
#     if num == 5:
#         print("Pralaimėjai...")
# else:
#     print("Laimėjai!")


# 5 užduotis
# Sukurti programą, kuri:
# Leistų vartotojui įvesti metus
# Atspausdintų „Keliamieji metai“, jei taip yra
# Atspausdintų „Nekeliamieji metai“, jei taip yra

# metai = int(input("Iveskite metus:"))
# if (metai % 4 ==0) or (metai % 100 == 0) or (metai % 400 == 0): #skliaustai nera butini
#     print("keliamieji metai")
# else:
#     print("nekeliamieji metai")


# 6 užduotis
# Perdaryti 5 užduoti taip, kad programa atspausdintų visus keliamuosius metus, nuo 1900 iki 2100 metų.
# Keliamieji metai yra kas 4 metus, išskyrus paskutinius amžiaus metus, kurie keliamieji yra tik kas 400 metų

# for metai in range(1900,2100):
#     if metai % 4 == 0:
#         print(metai)
#     elif metai % 400 == 0:
#         print(metai)

#
# for metai in range(1900,2100):
#     if (metai % 4 == 0) or (metai % 400 == 0):
#         print(metai)
