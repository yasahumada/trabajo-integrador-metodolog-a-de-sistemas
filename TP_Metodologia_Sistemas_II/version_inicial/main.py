
import json
import os

# Datos generales del sistema
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARCHIVO = os.path.join(BASE_DIR, "datos", "solicitudes.json")

estudiantes = []
responsables = []
solicitudes = []


# Cargar datos guardados
def cargar_datos():
    global estudiantes, responsables, solicitudes

    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            estudiantes = datos.get("estudiantes", [])
            responsables = datos.get("responsables", [])
            solicitudes = datos.get("solicitudes", [])


# Guardar datos
def guardar_datos():
    datos = {
        "estudiantes": estudiantes,
        "responsables": responsables,
        "solicitudes": solicitudes
    }

    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


# Registrar estudiante
def registrar_estudiante():
    nombre = input("Nombre del estudiante: ")
    legajo = input("Legajo: ")

    estudiante = {
        "id": len(estudiantes) + 1,
        "nombre": nombre,
        "legajo": legajo
    }

    estudiantes.append(estudiante)
    guardar_datos()

    print("Estudiante registrado correctamente.")


# Registrar responsable
def registrar_responsable():
    nombre = input("Nombre del responsable: ")
    area = input("Área: ")

    responsable = {
        "id": len(responsables) + 1,
        "nombre": nombre,
        "area": area
    }

    responsables.append(responsable)
    guardar_datos()

    print("Responsable registrado correctamente.")


# Registrar solicitud
def registrar_solicitud():
    if len(estudiantes) == 0:
        print("Primero debe registrar un estudiante.")
        return

    print("\nEstudiantes registrados:")
    for estudiante in estudiantes:
        print(estudiante["id"], "-", estudiante["nombre"])

    estudiante_id = int(input("ID del estudiante: "))
    tipo = input("Tipo de solicitud: ")
    prioridad = input("Prioridad (Alta/Media/Baja): ")
    descripcion = input("Descripción: ")

    solicitud = {
        "id": len(solicitudes) + 1,
        "estudiante_id": estudiante_id,
        "tipo": tipo,
        "prioridad": prioridad,
        "descripcion": descripcion,
        "estado": "Pendiente",
        "responsable_id": None
    }

    solicitudes.append(solicitud)
    guardar_datos()

    print("Solicitud registrada correctamente.")


# Cambiar estado de solicitud
def cambiar_estado():
    id_solicitud = int(input("ID de la solicitud: "))

    for solicitud in solicitudes:
        if solicitud["id"] == id_solicitud:
            nuevo_estado = input("Nuevo estado (Pendiente/En proceso/Resuelta): ")
            solicitud["estado"] = nuevo_estado
            guardar_datos()
            print("Estado actualizado.")
            return

    print("Solicitud no encontrada.")


# Asignar responsable
def asignar_responsable():
    id_solicitud = int(input("ID de la solicitud: "))

    for solicitud in solicitudes:
        if solicitud["id"] == id_solicitud:

            if len(responsables) == 0:
                print("No hay responsables registrados.")
                return

            for responsable in responsables:
                print(responsable["id"], "-", responsable["nombre"])

            responsable_id = int(input("ID del responsable: "))
            solicitud["responsable_id"] = responsable_id

            guardar_datos()
            print("Responsable asignado.")
            return

    print("Solicitud no encontrada.")


# Buscar solicitudes
def buscar_solicitudes():
    texto = input("Ingrese el estado o tipo que desea buscar: ").lower()

    encontrados = []

    for solicitud in solicitudes:
        if texto in solicitud["estado"].lower() or texto in solicitud["tipo"].lower():
            encontrados.append(solicitud)

    if len(encontrados) == 0:
        print("No se encontraron solicitudes.")
    else:
        for solicitud in encontrados:
            print(solicitud)


# Mostrar reporte
def mostrar_reporte():
    print("\n--- REPORTE DE SOLICITUDES ---")
    print("Total de estudiantes:", len(estudiantes))
    print("Total de responsables:", len(responsables))
    print("Total de solicitudes:", len(solicitudes))

    for solicitud in solicitudes:
        print(
            "ID:", solicitud["id"],
            "| Tipo:", solicitud["tipo"],
            "| Prioridad:", solicitud["prioridad"],
            "| Estado:", solicitud["estado"]
        )


# Menú principal
def menu():
    cargar_datos()

    while True:
        print("\n===== GESTIÓN DE SOLICITUDES ACADÉMICAS =====")
        print("1. Registrar estudiante")
        print("2. Registrar responsable")
        print("3. Registrar solicitud")
        print("4. Cambiar estado")
        print("5. Asignar responsable")
        print("6. Buscar solicitudes")
        print("7. Mostrar reporte")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_estudiante()
        elif opcion == "2":
            registrar_responsable()
        elif opcion == "3":
            registrar_solicitud()
        elif opcion == "4":
            cambiar_estado()
        elif opcion == "5":
            asignar_responsable()
        elif opcion == "6":
            buscar_solicitudes()
        elif opcion == "7":
            mostrar_reporte()
        elif opcion == "8":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción incorrecta.")


if __name__ == "__main__":
    menu()
