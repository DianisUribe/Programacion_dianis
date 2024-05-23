hora = float(input("ingresa la hora(formato 24h): "))
if 6 <= hora <= 9 or 16 <= hora <= 19:
    print("La tarifa es alta y el boleto es de $50")
else:
    print ("La tarifa es baja y el boleto es de $25")