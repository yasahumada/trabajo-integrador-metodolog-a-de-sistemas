
class Estudiante:
    def __init__(self, id, nombre, legajo):
        self.id = id
        self.nombre = nombre
        self.legajo = legajo

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "legajo": self.legajo
        }


class Responsable:
    def __init__(self, id, nombre, area):
        self.id = id
        self.nombre = nombre
        self.area = area

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "area": self.area
        }


class Solicitud:
    def __init__(
        self, id, estudiante_id, tipo, prioridad,
        descripcion, estado="Pendiente", responsable_id=None
    ):
        self.id = id
        self.estudiante_id = estudiante_id
        self.tipo = tipo
        self.prioridad = prioridad
        self.descripcion = descripcion
        self.estado = estado
        self.responsable_id = responsable_id

    def to_dict(self):
        return {
            "id": self.id,
            "estudiante_id": self.estudiante_id,
            "tipo": self.tipo,
            "prioridad": self.prioridad,
            "descripcion": self.descripcion,
            "estado": self.estado,
            "responsable_id": self.responsable_id
        }
