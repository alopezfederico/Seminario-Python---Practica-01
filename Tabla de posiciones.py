equipos = {}

def mostrar_menu():
    # Imprime en pantalla las opciones del menú disponibles
    print()
    print("1 - Agregar equipo")
    print("2 - Registrar resultado")
    print("3 - Mostrar tabla de posiciones")
    print("4 - Eliminar equipo")
    print("5 - Salir")
    print()

def agregar_equipo(equipos):
    # Agrega equipo al diccionario en caso de no existir
    nombre = input("Ingresá el nombre del equipo: ").strip()

    if nombre in equipos:
        print("Ese equipo ya existe.")
    else:
        equipos[nombre] = 0
        print(f"Equipo {nombre} agregado correctamente.")

def marcador_valido(goles):
    # Valida si el formato del marcador ingresado es correcto
    partes = goles.split("-")

    if len(partes) != 2:
        return False

    izquierda = partes[0].strip()
    derecha = partes[1].strip()

    if not izquierda.isdigit() or not derecha.isdigit():
        return False

    return True

def registrar_resultado(equipos):
    # Verifica si los equipos ingresados existen y si se ingresó dos veces el mismo.
    # En caso de haber ingresado los nombres correctamente, se suman puntos de manera correspondiente.
    local = input("Ingresá el equipo local: ").strip()
    visitante = input("Ingresá el equipo visitante: ").strip()

    if local not in equipos or visitante not in equipos:
        print("Uno o ambos equipos no existen.")
        return

    if local == visitante:
        print("Un equipo no puede jugar contra sí mismo.")
        return

    goles = input("Ingresá el marcador en formato 4 - 2: ").strip()

    if not marcador_valido(goles):
        print("Formato de marcador inválido.")
        return

    partes = goles.split("-")
    goles_local = int(partes[0].strip())
    goles_visitante = int(partes[1].strip())

    if goles_local > goles_visitante:
        equipos[local] += 3
    elif goles_local < goles_visitante:
        equipos[visitante] += 3
    else:
        equipos[local] += 1
        equipos[visitante] += 1

    print("Resultado registrado correctamente.")

def mostrar_tabla(equipos):
    # Imprime tabla de posiciones siempre y cuando haya equipos agregados.
    if len(equipos) == 0:
        print("No hay equipos cargados.")
        return

    tabla = list(equipos.items())
    tabla.sort(key=lambda item: item[1], reverse=True)

    print()
    print("TABLA DE POSICIONES")
    posicion = 1

    for equipo, puntos in tabla:
        print(posicion, "-", equipo, "-", puntos, "puntos")
        posicion += 1

def eliminar_equipo(equipos):
    # AL ingresar un equipo, si este equipo existe, se elimina.
    nombre = input("Ingresá el nombre del equipo a eliminar: ").strip()

    if nombre in equipos:
        del equipos[nombre]
        print("Equipo eliminado correctamente.")
    else:
        print("Ese equipo no existe.")

option = ""

while option != "5":
    mostrar_menu()
    option = input("Elegí una opción: ").strip()

    if option == "1":
        agregar_equipo(equipos)
    elif option == "2":
        registrar_resultado(equipos)
    elif option == "3":
        mostrar_tabla(equipos)
    elif option == "4":
        eliminar_equipo(equipos)
    elif option == "5":
        print("Fin del programa.")
    else:
        print("Opción inválida.")