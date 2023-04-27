"""Sąlyga [else] for ir while cikluose:"""
for skaicius in range(1, 5):
    if skaicius == 10:
        break
    print(skaicius)
else:
    print("Ciklas užbaigtas")



#programa kuri leidzia speti is saraso skaiciu.


sarasas = [2, 8, 45, 787, 45, 89, 45, 78, 78, 9, 4]
ieskomasis = int(input("Įveskite ieškomą skaičių"))

for x in sarasas:
    print(x)
    if x == ieskomasis:
        print("Skaičius rastas")
        break
else:
    print("Skaičius nerastas")

print("Programos pabaiga")



"""Ciklo nutraukimas (break):"""
sarasas = range(0, 10, 2)

for one in sarasas:
    print(one)
    if one == 4:
        print("Skaičius 4 yra šiame sąraše")
#         break
"""Pakartojimo praleidimas (continue):"""
for one in range(0, 6):
    if one == 3:
        continue
    print(one)

 for skaicius in range(6):
     print(skaicius)
# 0
# 1
## 2
 # 3
## 4
 # 5
# """pradzia 4 skaiciavimas iki 15. 2 pasako skaiciuoti tik kas antra"""
 for skaicius in range(4, 15, 2):
     print(skaicius)
 # 4
 # 6
 # 8
 # 10
 # 12
 # 14
 """While ciklai:
# Kol (while) [sąlyga], tol vykdyk ciklą"""
a = 5

while a < 100:
     a += 5
     print(a)
"""Begalinis ciklas (Infinite loop):"""
while True:
    print("dar kartą")
# dar kartą
# dar kartą
# dar kartą
# dar kartą
# dar kartą
# dar kartą
# dar kartą
