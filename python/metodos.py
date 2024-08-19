class Colegios:
    def __init__(self, data):
        self.id_colegio = data["id_colegio"]
        self.nombre = data["nombre"]
        self.direccion = data["direccion"]

    @classmethod
    def seleccionar(cls):
        query = "SELECT * FROM colegios"
        return query

    @classmethod
    def seleccionar_id(cls, id):
        query = f"SELECT * FROM colegios WHERE id_colegio = {id}"
        return query

    @classmethod
    def insert_values(cls, nombre, direccion):
        query = f"INSERT INTO colegios (nombre, direccion) VALUES ('{nombre}', '{direccion}')"
        return query

    @classmethod
    def delete_id(cls, id):
        query = f"DELETE FROM colegios WHERE id_colegio = {id}"
        return query


class Cursos:
    def __init__(self, data):
        self.id_curso = data["id_curso"]
        self.nombre = data["nombre"]
        self.id_colegio = data["id_colegio"]

    @classmethod
    def seleccionar(cls):
        query = "SELECT * FROM cursos"
        return query

    @classmethod
    def select_id(cls, id):
        query = f"SELECT * FROM cursos WHERE id_curso = {id}"
        return query

    @classmethod
    def insert(cls, nombre, id_colegio):
        query = f"INSERT INTO cursos (nombre, id_colegio) VALUES ('{nombre}', {id_colegio})"
        return query

    @classmethod
    def delete(cls, id):
        query = f"DELETE FROM cursos WHERE id_curso = {id}"
        return query


class CursosMaterias:
    def __init__(self, data):
        self.id_curso_materia = data["id_curso_materia"]
        self.id_curso = data["id_curso"]
        self.id_materia = data["id_materia"]

    @classmethod
    def selecvionar(cls):
        query = "SELECT * FROM cursos_materias"
        return query

    @classmethod
    def select_id(cls, id):
        query = f"SELECT * FROM cursos_materias WHERE id_curso_materia = {id}"
        return query

    @classmethod
    def insert(cls, id_curso, id_materia):
        query = f"INSERT INTO cursos_materias (id_curso, id_materia) VALUES ({id_curso}, {id_materia})"
        return query

    @classmethod
    def delete(cls, id):
        query = f"DELETE FROM cursos_materias WHERE id_curso_materia = {id}"
        return query


class Alumnos:
    def __init__(self, data):
        self.rut_alumno = data["rut_alumno"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.id_curso = data["id_curso"]

    @classmethod
    def seleccionar(cls):
        query = "SELECT * FROM alumnos"
        return query

    @classmethod
    def select_id(cls, id):
        query = f"SELECT * FROM alumnos WHERE rut_alumno = {id}"
        return query

    @classmethod
    def insert(cls, rut_alumno, nombre, apellido, id_curso):
        query = f"INSERT INTO alumnos (rut_alumno, nombre, apellido, id_curso) VALUES ({rut_alumno}, '{nombre}', '{apellido}', {id_curso})"
        return query

    @classmethod
    def delete(cls, id):
        query = f"DELETE FROM alumnos WHERE rut_alumno = {id}"
        return query


class Profesores:
    def __init__(self, data):
        self.rut_profesor = data["rut_profesor"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.id_colegio = data["id_colegio"]

    @classmethod
    def seleccionar(cls):
        query = "SELECT * FROM profesores"
        return query

    @classmethod
    def select_id(cls, id):
        query = f"SELECT * FROM profesores WHERE rut_profesor = {id}"
        return query

    @classmethod
    def insert(cls, rut_profesor, nombre, apellido, id_colegio):
        query = f"INSERT INTO profesores (rut_profesor, nombre, apellido, id_colegio) VALUES ({rut_profesor}, '{nombre}', '{apellido}', {id_colegio})"
        return query

    @classmethod
    def delete(cls, id):
        query = f"DELETE FROM profesores WHERE rut_profesor = {id}"
        return query
    
class Materias:
    def __init__(self, data):
        self.id_materia = data["id_materia"]
        self.nombre = data["nombre"]

    @classmethod
    def seleccionar(cls):
        query = "SELECT * FROM materias"
        return query

    @classmethod
    def select_id(cls, id):
        query = f"SELECT * FROM materias WHERE id_materia = {id}"
        return query

    @classmethod
    def insert(cls, nombre):
        query = f"INSERT INTO materias (nombre) VALUES ('{nombre}')"
        return query

    @classmethod
    def delete(cls, id):
        query = f"DELETE FROM materias WHERE id_materia = {id}"
        return query


class ProfesoresMaterias:
    def __init__(self, data):
        self.id_profesor_materia = data["id_profesor_materia"]
        self.rut_profesor = data["rut_profesor"]
        self.id_materia = data["id_materia"]

    @classmethod
    def seleccionar(cls):
        query = "SELECT * FROM profesores_materias"
        return query

    @classmethod
    def select_id(cls, id):
        query = f"SELECT * FROM profesores_materias WHERE id_profesor_materia = {id}"
        return query

    @classmethod
    def insert(cls, rut_profesor, id_materia):
        query = f"INSERT INTO profesores_materias (rut_profesor, id_materia) VALUES ({rut_profesor}, {id_materia})"
        return query

    @classmethod
    def delete(cls, id):
        query = f"DELETE FROM profesores_materias WHERE id_profesor_materia = {id}"
        return query


class Notas:
    def __init__(self, data):
        self.id_nota = data["id_nota"]
        self.resultado = data["resultado"]
        self.rut_alumno = data["rut_alumno"]
        self.id_materia = data["id_materia"]

    @classmethod
    def seleccionar(cls):
        query = "SELECT * FROM notas"
        return query

    @classmethod
    def select_id(cls, id):
        query = f"SELECT * FROM notas WHERE id_nota = {id}"
        return query

    @classmethod
    def insert(cls, resultado, rut_alumno, id_materia):
        query = f"INSERT INTO notas (resultado, rut_alumno, id_materia) VALUES ({resultado}, {rut_alumno}, {id_materia})"
        return query

    @classmethod
    def delete(cls, id):
        query = f"DELETE FROM notas WHERE id_nota = {id}"
        return query