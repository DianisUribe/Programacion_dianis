año = int(input("ingresa el año en número: "))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print (f"{año} es año bisiesto.")
else:
    print("el año no es bisiesto.")