amzius = {"Rokas": 20, "Andrius": 34, "Laura": 25}
for irasas in amzius:
    print(irasas)
# Rokas
# Andrius
# Laura
for irasas in amzius.values():
    print(irasas)
# 20
# 34
# 25
for raktas, reiksme in amzius.items():
    print(raktas, reiksme)
# Rokas 20
# Andrius 34
# Laura 25