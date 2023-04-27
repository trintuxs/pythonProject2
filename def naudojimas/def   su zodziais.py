
def zodziai(kazkas):
    raktas = kazkas[::-1]
    return raktas

atsakymas = zodziai("Malunas, Kiemas, Automobilis")
#zodzius printina atbulai. nuo paskutines raides iki pirmos

print(atsakymas)



def skaiciuok_info(stringas):
    zodziu_skaicius = 0
    didziosios_raides = 0
    mazosios_raides = 0
    skaiciai = 0
    zodziai = stringas.split()
    zodziu_skaicius = len(zodziai)
    for simbolis in stringas:
        if simbolis.isupper():
            didziosios_raides += 1
        elif simbolis.islower():
            mazosios_raides += 1
        elif simbolis.isdigit():
            skaiciai += 1
    print(f"Žodžių skaičius : {zodziu_skaicius}")  #skaiciai irgi isiskaiciuoja
    print(f"Didžiųjų raidžių skaičius: {didziosios_raides}")
    print(f"Mažųjų raidžių skaičius: {mazosios_raides}")
    print(f"Skaičių skaičius: {skaiciai}")
tekstas = "Šiandien yra gegužės 6 diena"
skaiciuok_info(tekstas)


