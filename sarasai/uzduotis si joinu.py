
sarasas = [2.5, 2, "Labas", True, 5, False, True, 7, 8, 2.8, "Vakaras"]

kiekis = sum(filter(lambda x: type(x) is int or type(x) is float, sarasas))
print(kiekis)

zodziai = list(filter(lambda x: type(x) is str == str, sarasas))
print(" ".join(zodziai))

bool_kiekis = list(filter(lambda sk: type(sk) == bool, sarasas))
print(bool_kiekis)