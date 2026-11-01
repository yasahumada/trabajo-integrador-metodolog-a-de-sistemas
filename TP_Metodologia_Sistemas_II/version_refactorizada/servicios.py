
from modelos import Estudiante, Responsable, Solicitud


class ServicioSolicitudes:
    def __init__(self, repositorio):
        self.repositorio = repositorio
        self.datos = self.repositorio.cargar()

        self.estudiantes = [
            Estudiante(**e) for e in self.datos["estudiantes"]
        ]

        self.responsables = [
            Responsable(**r) for r in self.datos["responsables"]
        ]

        self.solicitudes = [
            Solicitud(**s) for s in self.datos["solicitudes"]
        ]

    def _guardar_datos(self):
        datos = {
            "estudiantes": [e.to_dict() for e in self.estudiantes],
            "responsables": [r.to_dict() for r in self.responsables],
            "solicitudes": [s.to_dict() for s in self.solicitudes]
        }

        self.repositorio.guardar(datos)

    def registrar_estudiante(self, nombre, legajo):
        if not nombre.strip() or not legajo.strip():
            raise ValueError("El nombre y el legajo son obligatorios.")

        estudiante = Estudiante(
            id=self._siguiente_id(self.estudiantes),
            nombre=nombre.strip(),
            legajo=legajo.strip()
        )

        self.estudiantes.append(estudiante)
        self._guardar_datos()
        return estudiante

    def registrar_responsable(self, nombre, area):
        if not nombre.strip() or not area.strip():
            raise ValueError("El nombre y el área son obligatorios.")

        responsable = Responsable(
            id=self._siguiente_id(self.responsables),
            nombre=nombre.strip(),
            area=area.strip()
        )

        self.responsables.append(responsable)
        self._guardar_datos()
        return responsable

    def registrar_solicitud(
        self, estudiante_id, tipo, prioridad, descripcion
    ):
        estudiante = self._buscar_por_id(
            self.estudiantes, estudiante_id
        )

        if estudiante is None:
            raise ValueError("El estudiante no existe.")

        if not tipo.strip() or not descripcion.strip():
            raise ValueError("El tipo y la descripción son obligatorios.")

        prioridad = prioridad.capitalize()

        if prioridad not in ["Alta", "Media", "Baja"]:
            raise ValueError("La prioridad debe ser Alta, Media o Baja.")

        solicitud = Solicitud(
            id=self._siguiente_id(self.solicitudes),
            estudiante_id=estudiante_id,
            tipo=tipo.strip(),
            prioridad=prioridad,
            descripcion=descripcion.strip()
        )

        self.solicitudes.append(solicitud)
        self._guardar_datos()
        return solicitud

    def cambiar_estado(self, solicitud_id, nuevo_estado):
        solicitud = self._buscar_por_id(
            self.solicitudes, solicitud_id
        )

        if solicitud is None:
            raise ValueError("La solicitud no existe.")

        estados_validos = ["Pendiente", "En proceso", "Resuelta"]

        estado_normalizado = nuevo_estado.strip().lower()
        estados = {estado.lower(): estado for estado in estados_validos}

        if estado_normalizado not in estados:
            raise ValueError("El estado ingresado no es válido.")

        solicitud.estado = estados[estado_normalizado]
        self._guardar_datos()

    def asignar_responsable(self, solicitud_id, responsable_id):
        solicitud = self._buscar_por_id(
            self.solicitudes, solicitud_id
        )

        responsable = self._buscar_por_id(
            self.responsables, responsable_id
        )

        if solicitud is None:
            raise ValueError("La solicitud no existe.")

        if responsable is None:
            raise ValueError("El responsable no existe.")

        solicitud.responsable_id = responsable_id
        self._guardar_datos()

    def buscar_solicitudes(self, texto):
        texto = texto.strip().lower()

        if not texto:
            return self.solicitudes.copy()

        return [
            solicitud for solicitud in self.solicitudes
            if texto in solicitud.estado.lower()
            or texto in solicitud.tipo.lower()
        ]

    def generar_reporte(self):
        return {
            "total_estudiantes": len(self.estudiantes),
            "total_responsables": len(self.responsables),
            "total_solicitudes": len(self.solicitudes),
            "solicitudes": self.solicitudes.copy()
        }

    @staticmethod
    def _siguiente_id(elementos):
        return max((elemento.id for elemento in elementos), default=0) + 1

    @staticmethod
    def _buscar_por_id(elementos, identificador):
        return next(
            (elemento for elemento in elementos
             if elemento.id == identificador),
            None
        )
