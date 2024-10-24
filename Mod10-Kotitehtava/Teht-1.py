#Moduuli 10, Tehtävä 1
class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin = alin_kerros
        self.ylin = ylin_kerros
        self.nykyinen_kerros = alin_kerros

        def siirry_kerrokseen(self, kohde_kerros):
            pass
        def kerros_ylos(self,):
            self.nykyinen_kerros += 1
            print(f" Nykyinen kerros {self.nykyinen_kerros }")
        def kerros_alas(self):
            self.nykyinen_kerros -= 1
