edad = int(input("Ingresa tu edad: "))
tiene_licencia = (input("Tienes licencia: "))

if edad >= 18:
    if tiene_licencia == "si": 
        print("Puedes conducir")
    else: 
        print("No puedes conducir sin licencia.")
else: 
    print("Eres demasiado joven para conducir.")