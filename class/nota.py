
class Nota:
    def __init__(self, data):
        self.id_nota = data['id_nota']
        self.resultado = data['resultado']
        self.id_alumno = data['id_alumno']
        self.id_materia = data['id_materia']