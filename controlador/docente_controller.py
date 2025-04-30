from modelo.docente import Docente
class DocenteController:
    def __init__(self):
        self.docentes = []  # Lista para almacenar los docentes

    def agregar_docente(self, nombre, apellido, edad, sexo, cod_docente):
        """Registra un nuevo docente."""
        nuevo_docente = Docente(nombre, apellido, edad, sexo, cod_docente)
        self.docentes.append(nuevo_docente)
        return nuevo_docente

    # def obtener_docente(self, cod_docente):
    #     """Obtiene un docente por su código."""
    #     for docente in self.docentes:
    #         if docente.cod_docente == cod_docente:
    #             return docente
    #     return None

    def listar_docentes(self):
        """Lista todos los docentes registrados."""
        return self.docentes