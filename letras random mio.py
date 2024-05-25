import random

def contar_coincidencias(palabra1, palabra2):
    """Cuenta el número de coincidencias de caracteres en las mismas posiciones."""
    return sum(1 for a, b in zip(palabra1, palabra2) if a == b)

def seleccionar_palabras_similares(lista_palabras, num_palabras):
    """Selecciona un subconjunto de palabras de una lista."""
    return random.sample(lista_palabras, num_palabras)

def juego_hackeo():
    print("¡Bienvenido al mini-juego de hackeo de Fallout 4!")

    # Definición de niveles de dificultad
    niveles = {
        'principiante': {'num_palabras': 10, 'intentos': 5},
        'avanzado': {'num_palabras': 15, 'intentos': 4},
        'experto': {'num_palabras': 20, 'intentos': 4},
        'maestro': {'num_palabras': 25, 'intentos': 3}
    }

    # Lista de palabras posibles
    lista_palabras = [
        "puede", "arbol", "tigre", "cielo", "rueda",
        "pluma", "gordo", "verde", "blusa", "botas",
        "piano", "banco", "hojas", "carga", "raton",
        "perro", "gatoo", "vacas", "grito", "letra",
        "computadora", "armadura", "robot", "mangeta", "casco", "protector"
    ]

    # Determinar la longitud de la palabra máxima en la lista
    longitud_palabra_max = max(len(palabra) for palabra in lista_palabras)

    # Selección del nivel de dificultad
    while True:
        nivel = input("Selecciona un nivel de dificultad (principiante, avanzado, experto, maestro): ").strip().lower()
        if nivel in niveles:
            break
        print("Nivel no válido. Inténtalo de nuevo.")

    parametros = niveles[nivel]
    num_palabras = parametros['num_palabras']
    intentos = parametros['intentos']

    # Seleccionar palabras y asegurarse de que la palabra secreta esté en la lista
    palabra_secreta = random.choice(lista_palabras)
    palabras = seleccionar_palabras_similares(lista_palabras, num_palabras)
    if palabra_secreta not in palabras:
        palabras[random.randint(0, num_palabras - 1)] = palabra_secreta

    print(f"\nNivel seleccionado: {nivel.capitalize()}")
    print(f"Palabras disponibles ({len(palabras)}):")
    for palabra in palabras:
        print(palabra)
    
    while intentos > 0:
        intento = input("\nIntroduce tu palabra: ").strip().lower()
        
        if intento not in palabras:
            print("Palabra no válida. Inténtalo de nuevo.")
            continue
        
        if intento == palabra_secreta:
            print("¡Has adivinado la palabra correcta! ¡Felicidades!")
            break
        else:
            coincidencias = contar_coincidencias(intento, palabra_secreta)
            print(f"Coincidencias: {coincidencias}")
            intentos -= 1
            print(f"Intentos restantes: {intentos}")
    
    if intentos == 0:
        print(f"¡Has perdido! La palabra correcta era '{palabra_secreta}'.")

if __name__ == "__main__":
    juego_hackeo()
