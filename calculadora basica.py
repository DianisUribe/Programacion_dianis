a = float(input("ingresa el primer número: "))
b = float(input("ingresa el siguiente numero: "))
operación=input("elije la operación(+ - * / )")
if operación =='+':
    resultado = a + b
elif operación == '-':
    resultado = a - b 
elif operación == '*':
    resultado = a * b
else:
    operación == '/'
    resultado = a / b
print("resultado: ",resultado)