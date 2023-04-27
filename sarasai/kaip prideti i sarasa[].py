sarasas = [5, 2, 6]
sarasas.append(13)
print(sarasas)
# [5, 2, 6, 13]

'''
kaip pakeisti sarase esanti elementa
'''
sarasas = [5, 2, 6]
sarasas[1] = 64
print(sarasas)
'''
istrinti elementa
'''
sarasas2 = [5, 64, 6]
sarasas2.pop(1)
print(sarasas2)

# [5, 6]

'''
kaip suzinoti saraso dydi
'''
sarasas = [6, 98, 159, "zodziai", 5.55, True]
print(len(sarasas))
# 6
ilgiausias_zodis = "nebeprisikiškiakopūsteliaujantiesiems"
print(len(ilgiausias_zodis))
# 37
pats_ilgiausias_zodis = "Nebeprisivaizdotinklaraštininkaujantiesiems"
print (len(pats_ilgiausias_zodis))
# 43