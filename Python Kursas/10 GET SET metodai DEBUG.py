# 1 užduotis
# Parašyti klasę "Namas", kuri turėtų savybę "plotas" ir "verte".
# Padaryti taip, kad savybė "verte" koreguojama tik įvedus skaičių. Programoje naudoti dekoratorių @property.

class Namas:
    def __init__(self, plotas, verte):
        self.plotas = plotas
        self._verte = verte
# @property naudojam - kai norim suteikti "ypatingu" f-ju, kad veiktu kaip gaudytojai, nustatytojai arba trynėjai, kai apibrėžiame ypatybes klasėje:
    @property
    def verte(self):
        return self._verte
# @setter/set - naudojamas naujoms ypatybems prideti
    @verte.setter
    def verte(self, naujas):
        try:
            self._verte = int(naujas)  #Paverciam i skaiciu ir nustatom errora
        except ValueError:
            print("Error: Verte turi buti skaicius")


namas1 = Namas(55, 150000)

# print(f"Plotas (kv.m.): {namas1.plotas}")
print(f"Pradine verte (EUR): {namas1.verte}")

# idedam beleka, kad spausdintu klaida:
namas1.verte = "piririri"

# teisinga verte:
namas1.verte = 888888
print(f"Teisinga verte: {namas1.verte} EUR")
