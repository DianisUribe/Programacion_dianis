import random
import string

def generar_palabra_aleatoria():
    letras = string.ascii_lowercase
    palabra = ''.join(random.choice(letras) for _ in range(3))
    return palabra

def comparar_palabras(palabra, adivinanza):
    correctas = sum(1 for p, a in zip(palabra, adivinanza) if p == a)
    return correctas

def jugar():
    palabra_secreta = generar_palabra_aleatoria()
    intentos = 7
    
    print("adivina la palabra ")
    print("Debes adivinar una palabra de 3 letras.")
    print("Tienes", intentos, "intentos.\n ")

    while intentos > 0:
        adivinanza = input("Introduce tus letras: ").lower()
        
        if len(adivinanza) != 3 or not adivinanza.isalpha():
            print("Por favor, introduce una palabra válida de tres letras.")
            continue
        
        correctas = comparar_palabras(palabra_secreta, adivinanza)
        
        if correctas == 3:
            print("¡Felicidades! Adivinaste la palabra:", palabra_secreta)
            break
        else:
            intentos -= 1
            print("Te quedan", intentos, "intentos.")

    if intentos == 0:
        print("Lo siento, te quedaste sin intentos. La palabra era:", palabra_secreta)

jugar()
