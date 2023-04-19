class Irasas:
    def __init__(self, tipas, suma):
        self.tipas = tipas
        self.suma = suma

    def __str__(self):
        return f"{self.tipas}: {self.suma}"



class Biudzetas:
    def __init__(self):
        self.zurnalas = []


    def prideti_centu(self, suma):
        pajamos = Irasas("pajamos", suma)
        self.zurnalas.append(pajamos)



    def atimti_litus(self, suma):
        islaidos = Irasas("islaidos", suma)
        self.zurnalas.append(islaidos)


    def balansas(self):
        pajamos = 0
        islaidos = 0

        for Irasas in self.zurnalas:
            if Irasas.tipas == "pajamos":
                pajamos += Irasas.suma
            elif Irasas.tipas == "islaidos":
                islaidos += Irasas.suma
        return pajamos - islaidos

    def ataskaita(self):
        for Irasas in self.zurnalas:
            print(Irasas)


bankas = Biudzetas()


while True:
    pasirinkimas = int(input("1 - įvesti pajamas, \n2 - įvesti išlaidas, \n3 - gauti balansą, \n4 - parodyti ataskaitą, \n5. - išeiti iš programos"))

    if pasirinkimas == 1:
        suma = float(input())
        bankas.prideti_centu(suma)

    elif pasirinkimas == 2:
        suma = float(input())
        bankas.atimti_litus(suma)

    elif pasirinkimas == 3:
       bankas.balansas()

    elif pasirinkimas == 4:
       bankas.ataskaita()

    elif pasirinkimas == 5:
       break