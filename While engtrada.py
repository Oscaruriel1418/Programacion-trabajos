while True: 
    entrada = input("Introduce un numero entero: ")
    if entrada . isdigit():
        numero = int(entrada)
        print(f"El numero entero es {numero}")
        break
    else: 
        print("Error: entrda no valida, por favor introduce en numero entero.")