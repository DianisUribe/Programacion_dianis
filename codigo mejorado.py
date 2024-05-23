edad = int(input("vienvenido a viajamundo:3 \n \ningresa tu edad: "))
boleto= 200
vip= 650
h_pico= 80
if edad < 5: print("el nene pasa gratis")
elif edad >=65:
    viaje=(input("que paquete prefiere vip o normal: "))
    if viaje == 'nomarl':
        hora=int(input("ingresa la hora (formato 24h)"))
        if (hora >= 7 and hora <= 9) or (hora >= 17 and hora <= 19):
           totalb = boleto * .25
           total = boleto - totalb
           totala = total + h_pico 
           print(f"su total seria: ${totala} ")
        elif hora > 24:
           print("no valido")
        else:
           total = boleto * .25
           totala = boleto - total
           print(f"su total seria: ${totala}")                     
    elif viaje == "vip":
        hora=int(input("ingresa la hora (formato 24h)"))
        if (hora >= 7 and hora <= 9) or (hora >= 17 and hora <= 19):
           totalb = vip * .25
           total = vip - totalb
           totala = total + h_pico 
           print(f"su total seria: ${totala}")
        elif hora > 24:
           print("no valido")
        else:
           total = vip * .25
           totala = vip - total
           print(f"su total seria: ${totala}")  
    else :
        print("no existe este paquete ")
else:
   viaje=(input("que paquete prefiere vip o normal: "))
   if viaje =='normal':
        hora=int(input("ingresa la hora (formato 24h)"))
        if (hora >= 7 and hora <= 9) or (hora >= 17 and hora <= 19):
            total = boleto + h_pico
            print(f"su total seria: ${total}")
        elif hora > 24:
           print("no valido")
        else:
           print(f"su total seria: ${boleto}")
   elif viaje == "vip":
        hora=int(input("ingresa la hora (formato 24h)"))
        if (hora >= 7 and hora <= 9) or (hora >= 17 and hora <= 19):
            total = vip + h_pico
            print(f"su total seria: ${total}")
        elif hora > 24:
           print("no valido")
        else:
           print(f"su total seria: ${vip}")
   else :
      print("no existe este paquete")
   