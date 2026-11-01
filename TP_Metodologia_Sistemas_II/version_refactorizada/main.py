
import os

from repositorio import RepositorioSolicitudes
from servicios import ServicioSolicitudes


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUTA_DATOS = os.path.join(BASE_DIR, "datos", "solicitudes.json")


class Aplicacion:

    def __init__(self):
        self.repositorio = RepositorioSolicitudes(RUTA_DATOS)
        self.servicio = ServicioSolicitudes(self.repositorio)

    def mostrar_menu(self):
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

            opcion = input("Seleccione una opción: ").strip()

            try:
                if opcion == "1":
                    self.registrar_estudiante()

                elif opcion == "2":
                    self.registrar_responsable()

                elif opcion == "3":
                    self.registrar_solicitud()

                elif opcion == "4":
                    self.cambiar_estado()

                elif opcion == "5":
                    self.asignar_responsable()

                elif opcion == "6":
                    self.buscar_solicitudes()

                elif opcion == "7":
                    self.mostrar_reporte()

                elif opcion == "8":
                    print("Saliendo del sistema...")
                    break

                else:
                    print("Opción incorrecta.")

            except ValueError as error:
                print("Error:", error)

            except Exception as error:
                print("Ocurrió un error:", error)

    def registrar_estudiante(self):
        nombre = input("Nombre del estudiante: ")
        legajo = input("Legajo: ")

        estudiante = self.servicio.registrar_estudiante(
            nombre, legajo
        )

        print("Estudiante registrado:", estudiante.nombre)

    def registrar_responsable(self):
        nombre = input("Nombre del responsable: ")
        area = input("Área: ")

        responsable = self.servicio.registrar_responsable(
            nombre, area
        )

        print("Responsable registrado:", responsable.nombre)

    def registrar_solicitud(self):
        for estudiante in self.servicio.estudiantes:
            print(estudiante.id, "-", estudiante.nombre)

        estudiante_id = int(input("ID del estudiante: "))
        tipo = input("Tipo de solicitud: ")
        prioridad = input("Prioridad (Alta/Media/Baja): ")
        descripcion = input("Descripción: ")

        solicitud = self.servicio.registrar_solicitud(
            estudiante_id,
            tipo,
            prioridad,
            descripcion
        )

        print("Solicitud registrada con ID:", solicitud.id)

    def cambiar_estado(self):
        solicitud_id = int(input("ID de la solicitud: "))

        nuevo_estado = input(
            "Nuevo estado (Pendiente/En proceso/Resuelta): "
        )

        self.servicio.cambiar_estado(
            solicitud_id, nuevo_estado
        )

        print("Estado actualizado correctamente.")

    def asignar_responsable(self):
        solicitud_id = int(input("ID de la solicitud: "))

        for responsable in self.servicio.responsables:
            print(responsable.id, "-", responsable.nombre)

        responsable_id = int(input("ID del responsable: "))

        self.servicio.asignar_responsable(
            solicitud_id, responsable_id
        )

        print("Responsable asignado correctamente.")

    def buscar_solicitudes(self):
        texto = input(
            "Ingrese el estado o tipo que desea buscar: "
        )

        resultados = self.servicio.buscar_solicitudes(texto)

        if not resultados:
            print("No se encontraron solicitudes.")
            return

        for solicitud in resultados:
            print(solicitud.to_dict())

    def mostrar_reporte(self):
        reporte = self.servicio.generar_reporte()

        print("\n--- REPORTE DE SOLICITUDES ---")
        print("Total de estudiantes:", reporte["total_estudiantes"])
        print("Total de responsables:", reporte["total_responsables"])
        print("Total de solicitudes:", reporte["total_solicitudes"])

        for solicitud in reporte["solicitudes"]:
            print(
                "ID:", solicitud.id,
                "| Tipo:", solicitud.tipo,
                "| Prioridad:", solicitud.prioridad,
                "| Estado:", solicitud.estado
            )


if __name__ == "__main__":
    aplicacion = Aplicacion()
    aplicacion.mostrar_menu()
