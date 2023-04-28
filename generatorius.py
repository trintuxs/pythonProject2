# def generuok_skaicius( n ):
#     for i in range( n ):
#         yield i
#
# generatorius = generuok_skaicius( 10 )
# a = next(generatorius)
# print(a)
# try:
#     print(next(generatorius))
#     print(next(generatorius))
#     print(next(generatorius))
#     print(next(generatorius))
#     print(next(generatorius))
#     print(next(generatorius))
#     print(next(generatorius))
#     print(next(generatorius))
#     print(next(generatorius))
#     print(next(generatorius))
# except StopIteration:
#     print("baigesi skaiciai")
'''
..........................................................
'''

# def generuok_skaicius(n):
#     for i in range(n):
#         yield i
#
#
# generatorius = generuok_skaicius(5)
# print(next(generatorius))  #cia paima skaiciu is listo del to lieka maziau galutiniam
# print(next(generatorius))
# skaiciai = list(generatorius)
# print(skaiciai)

#.......................................................................



# def skaityti_faila(failo_pavadinimas):
#     with open(failo_pavadinimas, "r") as file:
#         print(file.readline())
#
# skaityti_faila("aga.txt")#cia reiktu imesti kazkoki doka ir nuskaitytu 1 eilute


# def skaityti_faila(failo_pavadinimas):
#     with open(failo_pavadinimas, "r") as file:
#         eilute = file.readline()
#         while eilute:
#             yield eilute #print(eilute) su yield galima pasirinkti kiek eiluciu skaityt
#             eilute = file.readline()
#
# skaitymas = skaityti_faila("aga.txt")
# print(next(skaitymas))
# print(next(skaitymas))
# print(next(skaitymas))

# def generuok_skaicius():
#     skaicius = 2
#     while True:
#         yield skaicius
#         skaicius += 2
#
# generatorius = generuok_skaicius()# galima dadeti ir antra ar trecia generatoriu kuris prades irgi nuo 2
# print(next(generatorius))
# print(next(generatorius))
# print(next(generatorius))
# print(next(generatorius))
# print(next(generatorius))


def fibonnaci():
    n1 = 0
    yield n1
    n2 = 1
    yield n2
    while True:
        n3 = n1 + n2
        yield n3
        n1 = n2
        n2 = n3

seka = fibonnaci()
for i in range( 20 ):
    print(next(seka))


print(next(seka))
print(next(seka))
print(next(seka))
print(next(seka))
print(next(seka))
print(next(seka))
print(next(seka))
print(next(seka))
print(next(seka))
print(next(seka))