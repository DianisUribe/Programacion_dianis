while True:
    contraseña = input("introduce una contraseña segura (minimo 8 caracteres): ")
    if len (contraseña) >= 8:
        print("contraseña segura registrada")
        break
    else:
        print("error: la contraseña debe tener 8 caracteres")