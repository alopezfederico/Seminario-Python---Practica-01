import random

categorias = {
'Programación':["python",
    "programa",
    "variable",
    "funcion",
    "bucle",
    "cadena",
    "entero",
    "lista"
],
'Marcas':[
    'Nike',
    'Adidas',
    'Amazon',
    'Google',
    'Microsoft',
    'Samsung',
    'Oracle'
],
'Equipos de futbol':[
    'Boca',
    'Estudiantes',
    'River',
    'Gimnasia',
    'Independiente',
    'Racing',
    'Barcelona'
    ],
'Colores':[
    'Amarillo',
    'Azul',
    'Violeta',
    'Naranja',
    'Verde',
    'Celeste',
    ]
}

puntos = 6

def mostrar_categorias(categorias):
    print("Categorías disponibles:")
    opciones = list(categorias.keys())
    for i in range(len(opciones)):
        print(i + 1, "-", opciones[i])
    return opciones

def elegir_categoria(categorias):
    opciones = mostrar_categorias(categorias)
    seleccion = input("Elegí una categoría: ")

    while not seleccion.isdigit() or int(seleccion) < 1 or int(seleccion) > len(opciones):
        seleccion = input("Selección inválida. Elegí una opción válida: ")

    return opciones[int(seleccion) - 1]

def letra_valida(letter):
    return len(letter) == 1 and 'a' <= letter <= 'z'

def elegir_palabra(categorias, categoria, palabras_usadas):
    palabras_disponibles = []

    for palabra in categorias[categoria]:
        if palabra not in palabras_usadas:
            palabras_disponibles.append(palabra)

    if len(palabras_disponibles) == 0:
        return None

    palabra = random.sample(palabras_disponibles, 1)[0]
    palabras_usadas.append(palabra)
    return palabra

def quedan_palabras(categorias, palabras_usadas):
    for categoria in categorias:
        for palabra in categorias[categoria]:
            if palabra not in palabras_usadas:
                return True
    return False

palabras_usadas = []

print("¡Bienvenido al Ahorcado!")
print()

seguir_jugando = "s"

while seguir_jugando == "s":

    if not quedan_palabras(categorias, palabras_usadas):
        print("Ya no quedan palabras disponibles en ninguna categoría.")
        break

    while True:
        seleccion = elegir_categoria(categorias)
        word = elegir_palabra(categorias, seleccion, palabras_usadas)

        if word is None:
            print("Ya no quedan palabras disponibles en esa categoría. Elegí otra.")
        else:
            break

    guessed = []
    attempts = 6

    while attempts > 0:
        progress = ""

        for letter in word:
            if letter.lower() in guessed:
                progress += letter + " "
            else:
                progress += "_ "

        print(progress)

        if "_" not in progress:
            print("¡Ganaste!")
            puntos += 6
            break

        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")

        letter = input("Ingresá una letra: ").lower()

        if not letra_valida(letter):
            print("Entrada no válida")
        else:
            if letter in guessed:
                print("Ya usaste esa letra.")
            elif letter in word.lower():
                guessed.append(letter)
                print("¡Bien! Esa letra está en la palabra.")
            else:
                guessed.append(letter)
                attempts -= 1
                puntos -= 1
                print("Esa letra no está en la palabra.")
        print()
    else:
        print(f"¡Perdiste! La palabra era: {word}")

    print(f"Puntaje: {puntos}")
    print()

    seguir_jugando = input("¿Querés jugar otra ronda? (s/n): ").lower()

    while seguir_jugando != "s" and seguir_jugando != "n":
        seguir_jugando = input("Respuesta inválida. Ingresá s o n: ").lower()

print("Gracias por jugar.")
print(f"Puntaje final: {puntos}")