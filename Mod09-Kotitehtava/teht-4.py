# Moduuli 09, Tehtävä 4

import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    # Metodi nopeuden muuttamiselle (kiihdytys ja jarrutus)
    def kiihdytä(self, muutos):
        uusi_nopeus = self.tamanhetkinen_nopeus + muutos

        if uusi_nopeus > self.huippunopeus:
            self.tamanhetkinen_nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.tamanhetkinen_nopeus = 0
        else:
            self.tamanhetkinen_nopeus = uusi_nopeus

    def kulje(self, tuntia):
        self.kuljettu_matka += self.tamanhetkinen_nopeus * tuntia

# Pääohjelma
def main():
    # Luodaan lista autoista
    autot = []
    for i in range(1, 11):
        huippunopeus = random.randint(100, 200)
        auto = Auto(f"ABC-{i}", huippunopeus)
        autot.append(auto)

    # Kilpailu alkaa
    kilpailu_kaynnissa = True
    while kilpailu_kaynnissa:
        for auto in autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdytä(nopeuden_muutos)

            # Käsketään autoa kulkemaan 1 tunnin ajan
            auto.kulje(1)

            # Tarkistetaan, onko joku autoista saavuttanut 10000 km
            if auto.kuljettu_matka >= 10000:
                kilpailu_kaynnissa = False
                break  

    # Kilpailu päättynyt, tulostetaan kaikkien autojen ominaisuudet taulukossa
    print(
        f"{'Rekisteritunnus':<15}{'Huippunopeus (km/h)':<20}{'Tämänhetkinen nopeus (km/h)':<30}{'Kuljettu matka (km)':<20}")
    print("=" * 85)
    for auto in autot:
        print(
            f"{auto.rekisteritunnus:<15}{auto.huippunopeus:<20}{auto.tamanhetkinen_nopeus:<30}{auto.kuljettu_matka:<20.2f}")


# Suoritetaan pääohjelma
if __name__ == "__main__":
    main()
