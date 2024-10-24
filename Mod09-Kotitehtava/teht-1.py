# Moduuli 09, Tehtävä 1

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0


# Pääohjelma
if __name__ == "__main__":
    auto = Auto("ABC-123", 142)

    # Tulostetaan auton kaikki ominaisuudet
    print(f"Rekisteritunnus: {auto.rekisteritunnus}")
    print(f"Huippunopeus: {auto.huippunopeus} km/h")
    print(f"Tämänhetkinen nopeus: {auto.nopeus} km/h")
    print(f"Kuljettu matka: {auto.kuljettu_matka} km")
