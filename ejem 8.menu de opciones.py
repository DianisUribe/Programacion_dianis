while True:
    print("\n1.-Saludar \n2.-despedir \n3.-terminamos")
    opción =input ("elije una opción: ")
    if opción == "1" :
        print("hello macacos")
    elif opción == "2" :
        print("adios!")
    elif opción == "3" :
        print("saliendo del menu")
        break
    else:
        print("opcion no valida")
