# 1 užduotis
# Sukurti funkcijas, kurios:
# Gražintų visų paduotų skaičių sumą (su *args argumentu)
# Gražintų paduoto skaičiaus šaknį (panaudoti math.sqrt())
# Gražintų paduoto sakinio simbolių kiekį (su len())
# Gražintų rezultatą, skaičių x padalinus iš y

# Nustatyti standartinį logerį (logging) taip, kad jis:
# Saugotų pranešimus į norimą failą
# Saugotų INFO lygio žinutes
# Pranešimai turi būti tokiu formatu: data/laikas, lygis, žinutė
# Kiekviena funkcija turi sukurti INFO lygio log pranešimą apie tai, ką atliko, pvz.:
# logging.info(f"Skaiciu {args} suma lygi: {sum(args)}")
# Paleisti kiekvieną funkciją su norimais argumentais

# import logging
# import math
#
# logging.basicConfig(filename="uzduotis1.log", level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')
#
#
# def suma(*args):
#     rezultatas = sum(args)
#     logging.info(f"funkcijos skaiciu {args} suma lygi: {rezultatas}")
#     return rezultatas
#
# def saknis(skaicius):
#     rezultatas = math.sqrt(skaicius)
#     logging.info(f"funkcijos saknis is {skaicius} rezultatas: {rezultatas}")
#
# def simboliai(sakinys):
#     rezultatas = len(sakinys)
#     logging.info(f"funkcijos simboliu kiekio {sakinys} rezultatas: {rezultatas}")
#
# def dalyba(x,y):
#     rezultatas = x / y
#     logging.info(f"funkcijos dalybos {x} ir {y} rezultatas: {rezultatas}")
#
# suma(5,5,5)
# saknis(9)
# simboliai("Laba diena su vistiena")
# dalyba(8,2)




# 2 užduotis
# Perdaryti 1 užduoties programą, kad:
# Į šaknies funkciją padavus string tipo argumetrą, į log failą būtų išsaugoma išimties klaida su norimu tekstu
# Į dalybos funkciją antrą argumentą padavus 0, į log failą būtų išsaugoma išimties klaida su norimu tekstu
# Patarimas: panaudoti try/except/else, logging.exception()

# import logging
# import math
#
# logging.basicConfig(filename="uzduotis1.log", encoding="UTF-8", level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')
#
# def suma(*args):
#     rezultatas = sum(args)
#     logging.info(f"funkcijos skaiciu {args} suma lygi: {rezultatas}")
#     return rezultatas
#
# def saknis(skaicius):
#     rezultatas = 0
#     try:
#         rezultatas = math.sqrt(skaicius)
#         logging.info(f"funkcijos saknis is {skaicius} rezultatas: {rezultatas}")
#     except TypeError:
#         logging.exception("Reikia paduoti skaiciu")
#     else:
#         return rezultatas
#
# def simboliai(sakinys):
#     rezultatas = len(sakinys)
#     logging.info(f"funkcijos simboliu kiekio {sakinys} rezultatas: {rezultatas}")
#
#
# def dalyba(x,y):
#     rezultatas = 0
#     try:
#         rezultatas = x / y
#         logging.info(f"funkcijos dalybos {x} ir {y} rezultatas: {rezultatas}")
#     except ZeroDivisionError:
#         logging.exception("Dalyba is 0 negalima")
#     else:
#         return rezultatas
#
# suma(5,5,5)
# saknis(9)
# saknis("labas")
# simboliai("Laba diena su vistiena")
# dalyba(10,2)
# dalyba(10,0)


# 3 užduotis
# Perdaryti 2 užduoties programą, kad:
# Būtų sukurtas savo logeris, kuris fiksuotų visus anksčiau aprašytus pranešimus
# Sukurtas logeris ne tik išsaugotų pranešimus faile, bet ir atvaizduotų juos konsolėje



import logging
import math

# uzregistruojame nauja logeri:
logger = logging.getLogger(__name__)
# suteikiame jam varda:
file_handler = logging.FileHandler(filename="uzduotis3.log")
# suformatuojam koki norim gaut rezultata: laikas, error level, zinute:
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
# uzdedam prie naujo loggerio formata:
file_handler.setFormatter(formatter)
# prie naujo failo pridedam formatavima:
logger.addHandler(file_handler)


# streamhandler - siuncia logginimo i KONSOLE:
stream_handler = logging.StreamHandler()
# suformatuojam kaip norim matyti:
stream_handler.setFormatter(formatter)
# pridedam prie naujai sukurto loggerio:
logger.addHandler(stream_handler)

# nustatome kokius errorus tikrinsime:
logger.setLevel(logging.DEBUG)


def suma(*args):
    rezultatas = sum(args)
    logger.info(f"funkcijos skaiciu {args} suma lygi: {rezultatas}")
    return rezultatas

def saknis(skaicius):
    rezultatas = 0
    try:
        rezultatas = math.sqrt(skaicius)
        logger.info(f"funkcijos saknis is {skaicius} rezultatas: {rezultatas}")
    except TypeError:
        logger.exception("Reikia paduoti skaiciu")
    else:
        return rezultatas

def simboliai(sakinys):
    rezultatas = len(sakinys)
    logger.info(f"funkcijos simboliu kiekio {sakinys} rezultatas: {rezultatas}")


def dalyba(x,y):
    rezultatas = 0
    try:
        rezultatas = x / y
        logger.info(f"funkcijos dalybos {x} ir {y} rezultatas: {rezultatas}")
    except ZeroDivisionError:
        logger.exception("Dalyba is 0 negalima")
    else:
        return rezultatas

suma(5,5,5)
saknis(9)
saknis("labas")
simboliai("Laba diena su vistiena")
dalyba(10,2)
dalyba(10,0)