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


guessed = []
attempts = 6
puntos = 6

print("¡Bienvenido al Ahorcado!")
print()


seleccion = elegir_categoria(categorias)

word = random.choice(categorias[seleccion])

while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)
    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        print("¡Ganaste!")
        break

    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")

    letter = input("Ingresá una letra: ")
    
    if len(letter) != 1 or (letter < 'a' or letter > 'z'):
    # Verifico el caracter, si no es valido imprimo mensaje y continúo el juego en la siguiente iteración.
        print('Entrada no válida')
    else:
        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
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
    puntos = 0

print (f'Puntaje: {puntos}')