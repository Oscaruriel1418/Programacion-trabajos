while True: 
    contraseña = input("Introduce una contraseña segura (minimo 8 caracteres): ")
    if len(contraseña) >= 8:
        print("Contraseña segura registrada.")
        break
    else:
        print("Error: La contraseña debe tener al menos 8 caracteres.")