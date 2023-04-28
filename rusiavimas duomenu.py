sarasas = [4, 3, 2, 1, 5, 6, 7, 10, 9, 8]
sarasas.sort()
print(sarasas)
#sorten = sukuria nauja sarasa kuri padaro pagal eile
#sort(reverse=True) padaro is gali pagal eile




# skaiciai = [11, 16, 21, 24, 95, 91, 69, 79]
# def pagal_kriteriju(skaicius):
#     print(f"kriterijus {skaicius}")
#     return  skaicius % 10
# rusiuoti_skaiciai = sorted(skaiciai, key=pagal_kriteriju)
# print(rusiuoti_skaiciai)


zodziai = [ "Tevas", "Mama", "Bobute"]
def paieska(zodis):
    return zodis.count( "a")

rasta = sorted(zodziai, key=paieska)
print(rasta)
#zodis .count("a") tai key reiksme kuri iesko sarase a raidziu.
# atspausdina pagal ju kieki,nuo maziausiai turincio iki daugiausiai