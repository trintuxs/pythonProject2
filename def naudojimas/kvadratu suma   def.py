def kvadratu_suma(sarasas):
    suma = 0
    for skaicius in sarasas:
        suma += skaicius**2
    return suma

sarasas1 = [1, 2, 5, 6]
sarasas2 = [8, 9, 6, 5]
sarasas3 = [8, 6, 7, 2]
suma1 = kvadratu_suma(sarasas1)
suma2 = kvadratu_suma(sarasas2)
suma3 = kvadratu_suma(sarasas3)
print(f"suma1: {suma1}, suma2: {suma2}, suma3{suma3}")

def suma_sandauga(skaicius1, skaicius2, skaicius3):
    suma = skaicius1 + skaicius2
    daugyba = suma * skaicius3
    return daugyba    #(printina tik paskutini veiksma)
#skaicius vienas atitinka 5,,skaicius2 9,,,skaicius3  4......
rezultatas = suma_sandauga(5, 9, 4)

print(rezultatas)

def sarasas(skaicius1, skaicius2, skaicius3):
    suma = skaicius1 + skaicius2 +skaicius3
    return  suma


print(sarasas(5, 8, 9))


def kubas(skaicius):
    skaicius_kubas = skaicius**3
    return skaicius_kubas

a = kubas(3)

print(a)

