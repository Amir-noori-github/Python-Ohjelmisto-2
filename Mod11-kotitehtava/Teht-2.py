# Moduuli 11, Tehtävä 2

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matkamittari = 0

    def aseta_nopeus(self, nopeus):
        if nopeus <= self.huippunopeus:
            self.nopeus = nopeus
        else:
            self.nopeus = self.huippunopeus

    def aja(self, tunnit):
        self.matkamittari += self.nopeus * tunnit

class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankki = bensatankki

# Pääohjelma
if __name__ == "__main__":

    sahkoauto = Sahkoauto("ABC-15", 180, 52.5)
    polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

    # Asetetaan autojen nopeudet
    sahkoauto.aseta_nopeus(100)
    polttomoottoriauto.aseta_nopeus(130)

    # Ajetaan autoilla 3 tuntia
    sahkoauto.aja(3)
    polttomoottoriauto.aja(3)

    print(f"Sähköauton matkamittarilukema: {sahkoauto.matkamittari} km")
    print(f"Polttomoottoriauton matkamittarilukema: {polttomoottoriauto.matkamittari} km")
