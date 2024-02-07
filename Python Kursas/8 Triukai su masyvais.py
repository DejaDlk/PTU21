# 1 užduotis:
# Sukurti programą, kuri:
# Prie kiekvieno sakinio "The Zen of Python" žodžio pridėtų šauktuką ir atspausdintų naują sakinį.
# Patarimai:Naudoti map (su lambda) arba comprehension, " ".join()

sakinys = '''
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

# map - iteratorius, kad grąžintų rezultatą, pritaikius funkciją kiekvienam iteruojamo elemento elementui (tuple, sarasas ir ect.)
# "LAMBDA - 'anonimine f-ja' su argumentais, bet tik viena israiska, pvz dalyba, daugyba ir t.t.:

naujas = map(lambda x: x + "!" , sakinys.split())

# Join metodas - ima visus elementus ir sujungia, bet jam reikia specifikacijos pvz.: tarpas " ". , arba kitaip:  stringas = " ", ir butu stringas.join(naujas):
print(" ".join(naujas))



# 2 užduotis:
# Sukurti programą, kuri:
# Sukurtų sąrašą iš skaičių nuo 0 iki 50
# Su kvadratų sąrašu (nauju kintamuoju) atliktų šiuos veiksmus: atspausdintų sumą, mažiausią ir didžiausią skaičių, vidurkį, medianą
# Surūšiuotų ir atspausdintų kvadratų sąrašą atbulai Patarimai:Naudoti map, filter arba comprehension, sum, min, max, mean, median, %

from statistics import mean, median

sarasas = list(range(51))
# print(sarasas)

# Padaugintų visus sąrašo skaičius iš 10 ir atspausdintų
# map - iteratorius, kad grąžintų rezultatą, pritaikius funkciją kiekvienam iteruojamo elemento elementui (tuple, sarasas ir ect.)
# "LAMBDA - 'anonimine f-ja' su argumentais, bet tik viena israiska, pvz dalyba, daugyba ir t.t.:

daugyba = map(lambda x: x * 10, sarasas)
print(list(daugyba))

# Atrinktų iš sąrašo skaičius, kurie dalinasi iš 7 ir atspausdintų
# "FILTER" f-cija duoda True/False reiksme ir tada daro veiksma, konkrecioms reiksmems, siuo atveju sarasui range (51):

dalyba = filter(lambda x: x % 7 == 0, sarasas)
print(list(dalyba))

# Pakeltų visus sąrašo skaičius kvadratu ir atspausdintų. Šį sąrašą (list masyvą) priskirti naujam kintamajam.
# "MAP" - sutrumpina koda, o esme, kad pritaiko f-ja kiekvienam iteruojamam elementui(sarasas ir ect.), naudojam kaip norim 1 f-jos visiem elementam, pvz:

kvadratu = list(map(lambda x: x ** 2, sarasas))
print(kvadratu)

# Su kvadratų sąrašu (nauju kintamuoju) atliktų šiuos veiksmus: atspausdintų sumą, mažiausią ir didžiausią skaičių, vidurkį, medianą

print(f'skaiciu suma:',sum(kvadratu))
print(f'maziausias skaicius:', min(kvadratu))
print(f'didziausias skaicius:',max(kvadratu))
# MEAN - vidurkis
print(f'vidurkis:', round(mean(kvadratu)))
# MEDIAN - vidurio taško reikšmė
print(f'vidurio tasko reiksme:', median(kvadratu))

# Surūšiuotų ir atspausdintų kvadratų sąrašą atbulai
# "SORT" - PAKEIS SARASA,  turėtų būti naudojamas visada, kai ketinama pakeisti sąrašą ir nepageidautina gauti pradinės elementų tvarkos.
# "SORTED" - SUKURS NAUJA SARASA IS PIRMINIO IR SURUSIUOS, turėtų būti naudojamas, kai rūšiuojamas objektas yra kartojamas:
# (pvz., sąrašas, eilutė, žodynas, eilutė), o norimas rezultatas yra surūšiuotas sąrašas, kuriame yra visi elementai.

kvadratu.sort(reverse=True)
print(list(kvadratu))





# 3 užduotis:
# Duotas sąrašas: sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]
# Sukurti programą, kuri:
# Patarimai:Naudoti filter arba comprehension, sum, " ".join()


sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]

# Paskaičiuotų ir atspausdintų VISU sąrašo skaičių sumą

suma= sum(filter(lambda x: type(x) is int or type(x) is float, sarasas))
print(f'saraso skaiciu suma:', suma)

# Sudėtų ir atspausdintų visus sąrašo žodžius

zodziai = filter(lambda x: type(x) is str, sarasas)
# print(list(zodziai))
print('zodziai:', " ".join(zodziai))

# # Suskaičiuotų ir atspausdintų, kiek sąraše yra loginių (boolean) kintamųjų su True reikšme

boolean_kiekis = sum(type(x) is bool for x in sarasas)
print(boolean_kiekis)




# 4 užduotis:
# Sukurti programą, kuri:
# Turėtų klasę Zmogus, su savybėmis vardas ir amzius
# Klasėje būtų repr metodas, kuris atvaizduotų vardą ir amžių
# Inicijuoti kelis Zmogus objektus su vardais ir amžiais
# Įdėti sukurtus Zmogus objektus į naują sąrašą
# Surūšiuotų ir atspausdintų sąrašo objektus pagal vardą ir pagal amžių (ir atbulai)
# Patarimai: Naudoti sorted, attrgetter, reverse, funkciją repr, from operator import attrgetter

# operator - biblioteka
# attrgetter - f-ja, leidžia gauti objekto atributUS (viena ar kelis):
from operator import attrgetter


class Zmogus:
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius

    def __repr__(self):
        return (f"({self.vardas}, {self.amzius})")

zmogus_1 = Zmogus("Tomas", "25")
zmogus_2 = Zmogus("Monika", "88")
sarasas = [zmogus_1, zmogus_2]
# print(sarasas)

# Surūšiuotų ir atspausdintų sąrašo objektus pagal vardą
surusiuota_vardas = sorted(sarasas, key=attrgetter("vardas"))
print(surusiuota_vardas)
# atbulai
surusiuota_vardas = sorted(sarasas, key=attrgetter("vardas"),reverse=True)
print(surusiuota_vardas)

# Surūšiuotų ir atspausdintų sąrašo objektus pagal amžių
surusiuota_amzius = sorted(sarasas, key=attrgetter("amzius"))
print(surusiuota_amzius)
# atbulai
surusiuota_amzius = sorted(sarasas, key=attrgetter("amzius"), reverse=True)
print(surusiuota_amzius)