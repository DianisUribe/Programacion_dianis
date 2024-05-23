x = float(input("ingresa el primer numero"))
y = float (input("ingresa el segundo numero"))
z = float(input("ingresa el tercer numero "))
if x > y and x > z:
    print(f"El mayor es{x}")
elif y > z :
    print(f"el mayor es {y}")
else:
    print(f"El mayor es {z}")