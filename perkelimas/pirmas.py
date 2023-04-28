from perkelimas.antras import kvadratu_suma
skaiciai = []

while True:
    ivesta = input("iveskite skaiciu. jei norite iseiti, spauskite q:")
    if ivesta == "q":
        print("pabaiga")
        break
    try:
        skaicius = int(ivesta)
    except ValueError:
        print("ivedete ne skaiciu!!!!!!")
        continue


    skaiciai.append(skaicius)


suma = kvadratu_suma(skaiciai)

print( suma)