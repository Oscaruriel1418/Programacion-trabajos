hora = float(input("Ingresa la hora (formato 24 hrs): "))
if 6 <= hora <= 9 or 16 <= hora <= 19: 
    print("La tarifa es alta y se de es $15.50")
else: 
    print("La Tarifa es baja y se de $7.50")