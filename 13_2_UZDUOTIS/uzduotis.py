# 2 Užduotis
# Sukurti paleidžiamąjį failą iš programos, kuri:
# Leistų vartotojui įvesti metus nuo ir metus iki
# Atspausdintų visus keliamuosius metus pagal duotą rėžį
# Paleidžiamasis failas turi turėti norimą ikoną


def rasti_keliamuosius_metus(nuo, iki):
    keliamieji_metai = []

    for metai in range(nuo, iki + 1):
        if (metai % 4 == 0 and metai % 100 != 0) or (metai % 400 == 0):
            keliamieji_metai.append(metai)
    return keliamieji_metai


def paleidziam_metus():
    nuo = int(input("Įveskite metus nuo: "))
    iki = int(input("Įveskite metus iki: "))

    if nuo > iki:
        print("Klaida: Metai nuo negali būti didesni nei metai iki.")
    else:
        keliamieji_metai = rasti_keliamuosius_metus(nuo, iki)

        if keliamieji_metai:
            print("Keliamieji metai šiame intervale:")
            for metai in keliamieji_metai:
                print(metai)
        else:
            print("Nėra keliamųjų metų šiame intervale.")

paleidziam_metus()

input("Norėdami uždaryti spauskite ENTER")

# FAILAS YRA :
# C:\Users\Dell\PycharmProjects\pythonProject2\13_2_UZDUOTIS\dist