


import datetime

class Darbuotojas:
    def __init__(self, vardas,  valandos_ikainis, dirba_nuo):
        self.vardas = vardas
        self.valandos_ikainis = valandos_ikainis
        self.dirba_nuo = dirba_nuo
        print(f"Darbuotojas: {self.vardas}, {self.valandos_ikainis}, {self.dirba_nuo}")

    def _kiek_dienu(self):

        skirtumas  = datetime.date.today() - self.dirba_nuo
        return skirtumas.days

        print("kiek dienu praejo :", skirtumas)


    def atliginimas(self):
        alga = self._kiek_dienu() * self.valandos_ikainis
        return alga


class NormalusDarbuotojas:
    def __init__(self, dienos):
        super().__init__(vardas, valandos_ikainis, dirba_nuo)
        self.dienos = dienos


zmogus = Darbuotojas("juozas", 12, datetime.date (2023,4,15) )
print(zmogus._kiek_dienu())

print(zmogus.atliginimas())


