# Moduuli 10, tehtävä 2

class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")
        else:
            print("Hissi on jo ylimmässä kerroksessa.")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")
        else:
            print("Hissi on jo alimmassa kerroksessa.")

    def siirry_kerrokseen(self, kohde_kerros):
        if kohde_kerros < self.alin_kerros or kohde_kerros > self.ylin_kerros:
            print("Virhe: kohdekerros on hissin ulkopuolella.")
            return

        print(f"Siirrytään kerrokseen {kohde_kerros}")
        while self.nykyinen_kerros < kohde_kerros:
            self.kerros_ylös()
        while self.nykyinen_kerros > kohde_kerros:
            self.kerros_alas()
        print(f"Hissi on saapunut kerrokseen {kohde_kerros}")

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for _ in range(hissien_lkm)]  # Luo hissit listaan

    def aja_hissiä(self, hissin_numero, kohde_kerros):
        if hissin_numero < 1 or hissin_numero > len(self.hissit):
            print("Virhe: Hissin numero on virheellinen.")
            return
        print(f"Ajetaan hissiä {hissin_numero} kohdekerrokseen {kohde_kerros}")
        self.hissit[hissin_numero - 1].siirry_kerrokseen(kohde_kerros)

# Pääohjelma
talo = Talo(1, 10, 3)
# Ajetaan hissejä eri kerroksiin
talo.aja_hissiä(1, 5)
talo.aja_hissiä(2, 8)
talo.aja_hissiä(3, 3)

talo.aja_hissiä(1, 1)
