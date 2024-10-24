# Moduuli 09, Tehtävä 3

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):

        uusi_nopeus = self.tamanhetkinen_nopeus + muutos

        if uusi_nopeus > self.huippunopeus:
            self.tamanhetkinen_nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.tamanhetkinen_nopeus = 0
        else:
            self.tamanhetkinen_nopeus = uusi_nopeus

    # Metodi kuljetun matkan kasvattamiseksi
    def kulje(self, tuntia):
        self.kuljettu_matka += self.tamanhetkinen_nopeus * tuntia

# Pääohjelma
def main():
    auto = Auto("ABC-123", 142)

    # Kiihdytetään autoa
    auto.kiihdytä(60)

    auto.kulje(1.5)

    # Tulostetaan tämänhetkinen nopeus ja kuljettu matka
    print(f"Tämänhetkinen nopeus: {auto.tamanhetkinen_nopeus} km/h")
    print(f"Kuljettu matka: {auto.kuljettu_matka} km")

    # Kiihdytetään lisää ja kuljetaan uudelleen
    auto.kiihdytä(50)
    auto.kulje(2)

    print(f"Uusi nopeus: {auto.tamanhetkinen_nopeus} km/h")
    print(f"Kuljettu matka: {auto.kuljettu_matka} km")

# Suoritetaan pääohjelma
if __name__ == "__main__":
    main()
