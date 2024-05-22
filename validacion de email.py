while True:
    email = input("introduce tu email: ")
    if "@dianis.mx" in email and "." in email:
        print("email valido")
        break
    else:
        print("email no valido, intenta de nuevo ")