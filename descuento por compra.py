monto_compra = float (input("ingresa el monnto de la compra en pesos: "))
if monto_compra >= 100:
    descuento = monto_compra* (float(input("ingresa el porcentaje de descuento: "))/100)
    print (f"se aplica el descuento de $",descuento)
else:
    print("no se aplica el descuento")