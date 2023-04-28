#
# import logging
# print( "Pasirinkite log lygi: 0 : DEBUG, 1: INFO, 2: WARNING" )

# pasirinkimas = input( "> " )
# if pasirinkimas == "0":
#     logging.basicConfig(level=logging.DEBUG)
# elif pasirinkimas == "1":
#     logging.basicConfig(level=logging.INFO)
# elif pasirinkimas == "2":
#     logging.basicConfig(level=logging.WARNING)
#
# logging.warning( "Memory low" )
# logging.info( "Gavom uzklausa" )
# logging.debug( "Gavom uzklausa")
#
# import logging
# logging.basicConfig(
#     filename="veiksmai.log", encoding="UTF-8",
#     level=logging.DEBUG,
#     format='%(asctime)s:%(levelname)s:%(module)s:%(lineno)d:%(message)s' )
# logging.warning( "Memory low" )
# logging.info( "Gavom uzklausa" )
# logging.debug( "Gavom uzklausa" )

import logging

logging.basicConfig(
    filename="skaiciuotuvas.log",
    encoding="UTF-8",
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s [%(module)s line %(lineno)d] : %(message)s'
)


print("1: sudetis")
print("2: atimtis")
print("3: daugyba")
print("4: dalyba")
pasirinkimas = input(">")
logging.debug(f"zmogus pasirinko {pasirinkimas}")

try:
    a = int(input("a:"))
    b = int(input("b:"))
except ValueError:
    print("ivedete ne skaiciu")
    logging.critical("zmogus ivede raide ne skaiciu")
res = 0

if pasirinkimas == "1":
    res = a + b
elif pasirinkimas == "2":
    res = a - b
elif pasirinkimas == "3":
    res = a * b
elif pasirinkimas == "4":
    res = a / b
else:
    print("tokio pasirinkimo nera")

print(pasirinkimas)