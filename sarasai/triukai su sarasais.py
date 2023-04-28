
#
# def kvadratu( sarasas ):
#     rezultatas = []
#     for x in sarasas:
#         rezultatas.append( x ** 2 )
#         return rezultatas
# skaiciai = [ 1, 2, 3, 6, 8, 10 ]
# skaiciai_kv = kvadratu( skaiciai )
# print( skaiciai_kv )




# def kelti_kvadratu( x ):
#     return x ** 2
#
# skaiciai = [ 1, 2, 3, 6, 8, 10 ]
#
# skaiciai_kv = list(map(kelti_kvadratu, skaiciai))
# print(skaiciai_kv)




# skaiciai = [ 1, 2, 4, 5, 9, 11 ]
#
# skaiciai_kv = list(map(lambda  sk: sk **2, skaiciai))
# print( skaiciai_kv)


'''

sakinys = "The Zen Of Python".split()
print(sakinys)
pakeista = " ".join(list(map(lambda x: x+"!",sakinys  ) ))#cia " ".join pakeicia apatini
print(pakeista)
# " ".join(sakinys)
'''

# def ar_lyginis(skaiciai):
#     return skaiciai % 2 == 0
#
# skaiciai = [1, 2, 3, 4, 5, 7, 8, 9, 10]
#
# lyginiai = list(filter(ar_lyginis, skaiciai))
# print(lyginiai)
# print(skaiciai)

from statistics import mean, median
skaicius = []
a =  range(0, 51)

a1 = map(lambda x: x * 10, a)
print(list(a1))
a2 = [skaiciai for skaiciai in a if skaiciai % 7 == 0]
print(list(a2))


a3 = [x**2 for x in a]
print(list(a3))
b = sum(a3)
c = min(a3)
d = max(a3)
e = mean(a3)
f = median(a3)
atgal = a3[::-1]
print(b)
print(c)
print(d)
print(e)
print(f)
print(atgal)
