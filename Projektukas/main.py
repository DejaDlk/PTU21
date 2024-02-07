from Projektukas import modulis

# kai paprastas kintamasis, rasom su print, kreipiames i projekta.py ir i kintamaji:
print(modulis.kintamasis)

# kai yra f-ja: rasome pvz.: kreipiames i moduli ir i funkcija aprasyta jame (jis nukreipiamam projekte.py jau turi print f-cja):
# print duoda non reiksme, tai geriau be print
print(modulis.funkcija())
modulis.funkcija()

# kai turime klase, tada turime susikurti nauja kintamaji ir priskirti ji klasei, taip atspausdins reiksmes(jis kitame faile jau turi print f-cja):

importuojam_klase = modulis.Objektas()
