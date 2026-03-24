equipos = {}

def mostrar_menu():
    print()
    print("1 - Agregar equipo")
    print("2 - Registrar resultado")
    print("3 - Mostrar tabla de posiciones")
    print("4 - Eliminar equipo")
    print("5 - Salir")
    print()

def agregar_equipo(equipos):
    nombre = input("Ingresá el nombre del equipo: ").strip()

    if nombre in equipos:
        print("Ese equipo ya existe.")
    else:
        equipos[nombre] = 0
        print("Equipo agregado correctamente.")

def marcador_valido(goles):
    partes = goles.split("-")

    if len(partes) != 2:
        return False

    izquierda = partes[0].strip()
    derecha = partes[1].strip()

    if not izquierda.isdigit() or not derecha.isdigit():
        return False

    return True

def registrar_resultado(equipos):
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