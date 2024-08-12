
class Alumno:
    def __init__(self, data):
        self.rut_alumno = data['rut_alumno']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.id_curso = data['id_curso']
