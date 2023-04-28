class Zmogus:
    def __init__(self, vardas, amzius):
        self.amzius = amzius
        self.vardas = vardas


zmogus1 = Zmogus("Tomas", 17)
zmogus2 =  Zmogus("Jonas", 18)
zmones = [zmogus1, zmogus2]

def kriterijus(zmogus):
    return  zmogus.vardas
def kriterijus2(zmogus):
    return zmogus.amzius
metai = sorted(zmones, key=kriterijus2)
for zmogus in metai:
    print("Pagagl  metus:", zmogus.amzius)

isrikiuoti = sorted(zmones, key=kriterijus)

for zmogus in isrikiuoti:
    print("Pagal abecele vardai:", zmogus.vardas)


