class Irasas:
    def __init__(self, suma):
        self.suma = suma

class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas, papildoma_informacija):
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.papildoma_informacija = papildoma_informacija
    def parodyti_info(self):
        print(f"Pajamos: + {self.siuntejas}, {self.papildoma_informacija}")
class IslaiduIrasas(Irasas):
    def __init__(self,suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        super().__init__(suma)
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.isigyta_preke_paslauga = isigyta_preke_paslauga

class Biudzetas:
    def __init__(self):
        self.irasai = []

    def prideti_irasa(self, irasas):
        self.irasai.append(irasas)

    def gauti_balansa(self):
        galutine_suma = 0

        for irasas in self.irasai:
            if isinstance(irasas, PajamuIrasas) == True:
                galutine_suma += irasas.suma
            elif isinstance(irasas, IslaiduIrasas) == False:
                galutine_suma -= irasas.suma

        return galutine_suma
    def parodyti_ataskaita(self):
        for irasas in self.irasai:
            irasas.parodyti_informacija()


bankas = Biudzetas()


while True:
    pasirinkimas = int(input("1 - įvesti pajamas, \n2 - įvesti išlaidas, \n3 - gauti balansą, \n4 - parodyti ataskaitą, \n0. - išeiti iš programos"))

    if pasirinkimas == 1:
        suma = float(input())
        siuntejas = input("iveskite savo varda")
        papildoma_informacija = input("isvekite papildoma info")
        irasas = PajamuIrasas(suma, siuntejas, papildoma_informacija)
        bankas.prideti_irasa(irasas)

    elif pasirinkimas == 2:
        suma = float(input())
        atsiskaitymo_budas = input("kaip mokesi?")
        isigyta_preke_paslauga = input("ka pirksi?")
        irasas = IslaiduIrasas(suma,atsiskaitymo_budas, isigyta_preke_paslauga)
        bankas.prideti_irasa(irasas)
    elif pasirinkimas == 3:
       print(bankas.gauti_balansa())

    elif pasirinkimas == 4:
       bankas.parodyti_ataskaita()

    elif pasirinkimas == 0:
       break