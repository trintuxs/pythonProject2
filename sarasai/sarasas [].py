sarasas = []
skaiciai = [4, 5, 45, 95]
zodziai = ["Labas ", "vakaras, ", "Lietuva"]
visko_po_truputi = [5, 5.6, "Lietuva", [5, 6, 15], True]
print(zodziai)
# ['Labas ', 'vakaras, ', 'Lietuva']
"""
Kaip pasiekti atskirus sąrašo įrašus:
"""
zodziai = ["Labas ", "vakaras, ", "Lietuva"]
print(zodziai[0])
print(zodziai[2])
# Labas
# Lietuva
zodis = "Laba diena"
print(zodis[5])
# d
visko_po_truputi = [5, 5.6, "Lietuva", [5, 6, 15], True]
print(visko_po_truputi[3][1]) #0=5, 1=5.6, 2=Lietuva, 3=zodynas viduje,  antrame zodyne 0=5, 1=6. stai ka reiksia [3][1]
# 6
