
import json
import os


class RepositorioSolicitudes:
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
        self._crear_archivo()

    def _crear_archivo(self):
        carpeta = os.path.dirname(self.ruta_archivo)

        if carpeta:
            os.makedirs(carpeta, exist_ok=True)

        if not os.path.exists(self.ruta_archivo):
            self.guardar({
                "estudiantes": [],
                "responsables": [],
                "solicitudes": []
            })

    def cargar(self):
        try:
            with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        except (json.JSONDecodeError, OSError):
            return {
                "estudiantes": [],
                "responsables": [],
                "solicitudes": []
            }

    def guardar(self, datos):
        with open(self.ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
