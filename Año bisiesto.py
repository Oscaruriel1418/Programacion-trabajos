año = int(input("Ingresa el año: "))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0 ):
    print(f"{año} es un año bisiesto.")
else: 
    print("El año no es bisiesto ")