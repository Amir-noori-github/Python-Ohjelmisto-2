# Moduuli 4, tehtävä 4

import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, muutos):
        self.nopeus = max(0, min(self.huippunopeus, self.nopeus + muutos))

    def kulje(self, tunnit=1):
        self.matka += self.nopeus * tunnit


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            muutos = random.randint(-10, 15)
            auto.kiihdytä(muutos)
            auto.kulje()

    def tulosta_tilanne(self):
        print(f"{'Rekisteritunnus':<15} {'Huippunopeus':<15} {'Nopeus':<10} {'Matka (km)':<10}")
        print("=" * 50)
        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<15} {auto.huippunopeus:<15} {auto.nopeus:<10} {auto.matka:<10.1f}")
        print("\n")

    def kilpailu_ohi(self):
        return any(auto.matka >= self.pituus for auto in self.autot)


# Pääohjelma
autot = [Auto(f"ABC-{i + 1}", random.randint(100, 200)) for i in range(10)]
kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunti = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunti += 1

    if tunti % 10 == 0:
        print(f"Tunti {tunti}")
        kilpailu.tulosta_tilanne()

# Kilpailun päättymisen jälkeen tulostetaan lopullinen tilanne
print("Kilpailu on päättynyt! Lopputilanne:")
kilpailu.tulosta_tilanne()
