# Moduuli 09, Tehtävä 2

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):

        self.nopeus += muutos

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

        elif self.nopeus < 0:
            self.nopeus = 0

# Pääohjelma
auto = Auto("ABC-123", 142)

# Tulostetaan auton ominaisuudet alussa
print(f"Rekisteritunnus: {auto.rekisteritunnus}")
print(f"Huippunopeus: {auto.huippunopeus} km/h")
print(f"Tämänhetkinen nopeus: {auto.nopeus} km/h")
print(f"Kuljettu matka: {auto.kuljettu_matka} km")

# Kiihdytykset
auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)

print(f"Auton nopeus: {auto.nopeus} km/h")

# Hätäjarrutus
auto.kiihdytä(-200)

print(f"Auton nopeus hätäjarrutuksen jälkeen: {auto.nopeus} km/h")
