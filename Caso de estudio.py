print("La tarifa normal es de $20 pesos")
edad = int(input("Ingresa la edad: "))
hora = int(input("Ingresa la hora (En formato de 24 hrs): "))
precio_normal = 20 
total = precio_normal - 6
if edad <= 5:
    print("Tu viaje es gratis")
elif edad >= 65:
    print("Tienes un descuento de $6 pesos, "
          f"No se te aplica ningun sobre cargo por lo que tu tarifa es de {total}.")
    
else:
   
  if (hora >= 7 and hora <= 9) or (hora >= 17 and hora <= 19):
    print("Se aplica un sobrecargo de $5 pesos.")
    total = precio_normal + 5 
    print(f"La tarifa total es de ${total} pesos")
  else: 
     print(f"No se aplica ningun sobrecargo, no son horas pico por que son las {hora}")