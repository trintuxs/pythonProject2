?
import datetime
class Sukaktis:
    def __init__(self, data="1986-3-11"):
        self.data = datetime.datetime.strptime( data, "%Y-%m-%d")


    def praejo(self):
        dabar = datetime.datetime.now()
        skirtumas = dabar - self.data
        metai = skirtumas.days // 365
        menesis = skirtumas.days % 365 // 30
        diena = skirtumas.days
        valanda = skirtumas.seconds // 3600
        minute = skirtumas.seconds % 3600 // 60
        sekunde = skirtumas.seconds % 60
        print("kiek metu praejo:", metai)
        print("kiek menesiu prejo:", menesis)
        print("kiek dienu praejo:", diena)
        print("kiek valandu praejo:", valanda)
        print("kiek minuciu praejo:", minute)
        print("kiek sekundziu praejo:", sekunde)

    def ar_keliamieji(self):
        if self.data.year % 4 == 0:
            return True


    def atimti(self, diena):
        atimta = self.data - datetime.timedelta(days=diena)
        return atimta

    def prideti(self, diena):
        prideta = self.data + datetime.timedelta(days=diena)
        return prideta



gimtadienis = Sukaktis()
print(gimtadienis.atimti(5))