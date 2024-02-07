from Biudzetas.pagrindinis import Irasas


class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas, info):
        # Funkcija super() grąžina objektą, kuris atstovauja pirminę klasę, siuo atveju i IRASO KLASE ir SUMA:
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.info = info

    def __str__(self):
        return f"Pajamos: {self.suma} (Siuntėjas - {self.siuntejas}, Informacija - {self.info})"


class IslaiduIrasas(Irasas):
    def __init__(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        super().__init__(suma)
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.isigyta_preke_paslauga = isigyta_preke_paslauga

    def __str__(self):
        return f"Išlaidos: {self.suma} (Atsiskaitymo būdas - {self.atsiskaitymo_budas}, Įsigyta - {self.isigyta_preke_paslauga})"
