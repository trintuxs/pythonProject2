class Sakinys():
    def __init__(self, tekstas= "Zen of Python"):
        self.tekstas = tekstas

    def atbulai(self):
        return self.tekstas[::-1]

    def mazos_raides(self):
        return self.tekstas.lower()

    def dideles_raides(self):
        return self.tekstas.upper()

    def zodis(self,numeris):
        zodziai = self.tekstas.split()
        if numeris < len(zodziai):
            return zodziai[numeris]
        else:
            return None

    def kiekis(self, grazina):
        return self.tekstas.count(grazina)

    def pakeisti(self, grazina, pakeitimas):
        return self.tekstas.replace(grazina, pakeitimas)

    def savybės(self):
        kiek_zodziu = len(self.tekstas.split())
        kiek_skaiciu = sum(1 for kazkas in self.tekstas if kazkas.isdigit())
        didziosios = sum(1 for kazkas in self.tekstas if kazkas.isupper())
        mazosios = sum(1 for kazkas in self.tekstas if kazkas.islower())
        print( "zodziu suma:",kiek_zodziu)
        print("skaiciu suma:", kiek_skaiciu)
        print("didziuju raidziu suma:", didziosios)
        print("mazuju raidziu suma:", mazosios)

eilute = Sakinys("labas vakaras Ponas Aladinai 2023")

print(eilute.atbulai())
print(eilute.mazos_raides())
print(eilute.dideles_raides())
print(eilute.zodis(1))
print(eilute.kiekis("a"))
print(eilute.pakeisti("vakaras",  "rytas"))
eilute.savybės()
