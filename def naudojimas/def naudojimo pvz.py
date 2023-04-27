
def pasisveikinti(vardas):
    print("labas vakaras",vardas)
pasisveikinti("jonas")
pasisveikinti("vaidas")


def kvadratas(skaicius):
    skaicius_kvadratu = skaicius**2
    print(skaicius_kvadratu)
    return skaicius_kvadratu


kvadratas5 = kvadratas(5)
kvadratas9 = kvadratas(9)
kvadratas15 = kvadratas(15)
print(f"skaicius 5 kvadratas yra {kvadratas5}")
kvadratas_suma = kvadratas5 + kvadratas9
print(f"5 ir 9 kvadratu suma yra {kvadratas_suma}")

skaicius = None
if skaicius is None:
    print("skaicius nera")
