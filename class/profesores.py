
class Profesor:
    def __init__(self, data):
        self.rut_profesor = data['rut_profesor']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.id_colegio = data['id_colegio']
