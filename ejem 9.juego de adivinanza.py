import random

# Genera una palabra secreta de 4 letras aleatorias
palabra_secreta = ''.join(random.choice('a, z') for _ in range(1))

while True:
    # Solicita al usuario que ingrese un intento para adivinar la palabra
    intento = input("Adivina la palabra de 4 letras: ")
    
    # Comprueba si el intento del usuario coincide con la palabra secreta
    if intento == palabra_secreta:
        print("¡Correcto! ¡Has adivinado!")
        break
    else:
        # Si el intento no coincide, solicita al usuario que lo intente de nuevo
        print("¡Ups! Intenta de nuevo.")
