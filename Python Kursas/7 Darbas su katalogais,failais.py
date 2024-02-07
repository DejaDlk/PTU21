# 1 užduotis
# Sukurti programą, kuri:
# Sukurtų failą „Tekstas.txt“ su pilnu tekstu, gauto python kode paleidus „import this“.
# Atspausdintų tekstą iš sukurto failo
# Paskutinėje sukurto failo eilutėje pridėtų šiandienos datą ir laiką
# Sunumeruotų teksto eilutes (kiekvienos pradžioje pridėtų skaičių).
# Sukurtame faile eilutę "Beautiful is better than ugly." pakeistų į "Gražu yra geriau nei bjauru."
# Atspausdintų visą failo tekstą atbulai
# Atspausdintų, kiek failo tekste yra žodžių, skaičių, didžiųjų ir mažųjų raidžių
# Nukopijuotų visą sukurto failą tekstą į naują failą, tik DIDŽIOSIOMIS RAIDĖMIS Patarimai:
# Naudoti from datetime import datetime, datetime.today()
# Kintamajam priskirti sakinį, kuriuo bus operuojama, eilutėmis
# Kai kur galima panaudoti funkcijas iš praeitų pamokų

# import this
import datetime

a = '''
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
# pirma susikuriam visas f-cijas ir veiksmus ir tada sukuriam nauja .txt faila:
# Atspausdintų visą failo tekstą atbulai

def atbulai(sakinys):
    return sakinys[::-1]

# Atspausdintų, kiek failo tekste yra žodžių, skaičių, didžiųjų ir mažųjų raidžių

tikrinam_zodzius = ""

def tikrinam_zodzius(zodziai):
    zodziai = a
    print("zozdziu kiekis: ", len(zodziai.split()))
    print("skaicius kiekis: ", sum(x.isdigit() for x in zodziai))
    print("didziuju raidziu kiekis: ", sum(x.isupper() for x in zodziai))
    print("mazuju raidziu kiekis: ", sum(x.islower() for x in zodziai))

# Nukopijuotų visą sukurto failą tekstą į naują failą, tik DIDŽIOSIOMIS RAIDĖMIS (antra dalis apacioje):

def didziosios(zodziai):
    return zodziai.upper()

# sukurti faila .txt

with open("Tekstas.txt", "w") as failas:
    failas.write(a)

# atspausdinti:
with open("Tekstas.txt", "r") as failas:
    print(failas.read())

# prideti data ir ja atspausdinti
with open("Tekstas.txt", "a") as failas:
    failas.write(str(datetime.datetime.today()))
# atspausdinti
with open("Tekstas.txt", "r") as failas:
    print(failas.read())

# Sunumeruotų teksto eilutes

numeracija = ""
skaicius = 1

with open("Tekstas.txt", "r") as failas:
    for eilute in failas:
        numeracija += str(skaicius) + " " + eilute
        skaicius += 1

with open("Tekstas.txt", "w") as failas:
    failas.write(numeracija)

# Sukurtame faile eilutę "Beautiful is better than ugly." pakeistų į "Gražu yra geriau nei bjauru."

pakeistas_tekstas = ""

with open("Tekstas.txt", "r", encoding="UTF-8") as failas:
    pakeistas_tekstas = failas.read()

pakeistas_tekstas = pakeistas_tekstas.replace("Beautiful is better than ugly.", "Gražu yra geriau nei bjauru.")

with open("Tekstas.txt", "w", encoding="UTF-8") as failas:
    failas.write(pakeistas_tekstas)

# Atspausdintų visą failo tekstą atbulai (f-jos "atbulai" aprasymas virsuje)

with open("Tekstas.txt", "r",) as failas:
    print(atbulai(failas.read()))

# Atspausdintų, kiek failo tekste yra žodžių, skaičių, didžiųjų ir mažųjų raidžių:

with open("Tekstas.txt", "r",) as failas:
    print(tikrinam_zodzius(failas.read()))

# Nukopijuotų visą sukurto failą tekstą į naują failą, tik DIDŽIOSIOMIS RAIDĖMIS:


with open("Tekstas.txt", "r", encoding="UTF-8") as kopijuojamas_failas:
    with open("Tekstas didziosiomis.txt", "w", encoding="UTF-8") as naujas_failas:
        naujas_failas.write(didziosios(kopijuojamas_failas.read()))

# 2 užduotis
# Sukurti programą, kuri:
# Leistų vartotojui įvesti norimą eilučių kiekį
# Leistų vartotojui įrašyti norimą kuriamo failo pavadinimą
# Įrašytų įvestą tekstą atskiromis eilutėmis į failą
# Patarimai: Sukurti while ciklą, kuris užsibaigtų tik įvedus vartotojui tuščią eilutę (nuspaudus ENTER)

ivestas = []

while True:
    ivestas = input("Iveskite teksta (nieko neirasius ir paspaudus ENTER - veiksmas baigsis): ")
    tekstas = ivestas + '/n'
# if "not" - rasom kai norim gauti oposite (jeigu nepasitvirtina pries tai parasyta salyga - gaunam false tada cikle einam i if not ir break):
    if not ivestas:
        break

pavadinimas = input("Iveskite failo pavadinima: ")

with open(f"{pavadinimas}", "w") as naujas_failas:
    naujas_failas.write(ivestas)


# 3 užduotis
# Sukurti programą, kuri:
# Kompiuterio darbalaukyje (Desktop) sukurtų katalogą „Naujas Katalogas“
# Šiame kataloge sukurtų tekstinį failą, kuriame būtų šiandienos data ir laikas
# Atspausdintų šio tekstinio failo sukūrimo datą ir dydį baitais
# Patarimai: Failo sukūrimo datą galima pasiekti per os.stat(„Failas.txt“).st_ctime

import os
import datetime

#Kaip sužinoti katalogą, kuriame esame:
print(os.getcwd())

# # Kaip pakeisti katalogą, kuriame esame:
os.chdir("C:\\Users\\Dell\\Desktop")
print(os.getcwd())

# Kaip sukurti naują katalogą:
os.mkdir("Naujas Katalogas")

# Šiame kataloge sukurtų tekstinį failą, kuriame būtų šiandienos data ir laikas
os.chdir("C:\\Users\\Dell\\Desktop\\Naujas Katalogas")

with open("Failas.txt", "w") as failas:
    failas.write(str(datetime.datetime.today()))

# Atspausdintų šio tekstinio failo sukūrimo datą ir dydį baitais:
# data:

data = os.stat("Failas.txt").st_mtime
print(datetime.datetime.fromtimestamp(data))

# dydis baitais:
print(os.stat("Failas.txt").st_size)


# 4 užduotis
# Sukurti minibiudžeto programą, kuri:
# Leistų vartotojui įvesti pajamas arba išlaidas (su "-" ženklu)
# Pajamas ir išlaidas saugotų sąraše, o sąrašą pickle faile (uždarius programą, įvesti duomenys nedingtų)
# Atvaizduotų jau įvestas pajamas ir išlaidas
# Atvaizduotų įvestų pajamų ir išlaidų balansą (sudėtų visas pajamas ir išlaidas)
# Patarimas: import pickle

import pickle

while True:
    try:
        with open("biudzetas.pkl", "rb") as pickle_in:
            biudzetas = pickle.load(pickle_in)
            suma = 0
            print("--------Įrašų sąrašas:---------")
            for skaicius, irasas in enumerate(biudzetas):
                suma += irasas
                print(skaicius + 1, irasas)
            print("Biudžeto balansas", suma)
            print("-------------------------------")
    except:
        print("Nepavyko nuskaityti failo")
        biudzetas = []
    print("Norėdami išeiti palikite tuščią lauką ir spauskite ENTER")
    irasas = float(input("Įveskite pajamas arba išlaidas: "))
    if irasas == "":
        break
    biudzetas.append(irasas)

    try:
        with open("biudzetas.pkl", "wb") as pickle_out:
            pickle.dump(biudzetas, pickle_out)
    except FileNotFoundError:
        print("Nepavyko įrašyti failo")
