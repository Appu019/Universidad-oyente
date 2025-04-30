from modelo.universitario import Universitario


class UniversitarioController:
    def __init__(self):
        self.universitarios = []  # Lista para almacenar los universitarios

    def registrar_universitario(self, nombre, apellido, edad, sexo, cod_estudiante):
        """Agrega un nuevo universitario."""
        nuevo_universitario = Universitario(nombre, apellido, edad, sexo, cod_estudiante)
        self.universitarios.append(nuevo_universitario)
        return nuevo_universitario

    def obtener_universitarios(self):
        """Obtiene la lista de universitarios."""
        return self.universitarios