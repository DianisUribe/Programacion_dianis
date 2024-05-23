edad =int(input("ingresa tu edad: "))
if edad >= 18:
    licencia =input("cuentas con licencia? ")
    if licencia == "si"  :
        print ("puedes conducir")
    else:
        print("no puedes conducir sin licencia")
else:
    print("eres demasiado joven para conducir")
