import random
numero_secreto = random.randint(1000,9999)

while True:
    
    intento = int(input("addivina el numero entre 1000 y 9999: "))
    
    if intento == numero_secreto:

        print (" haz acertado ")
        break
    else:
        print (" intenta de nuevo ")