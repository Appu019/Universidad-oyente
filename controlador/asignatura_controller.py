from modelo.asignatura import Asignatura

class AsignaturaController:
    def __init__(self):
        self.asignaturas = []  # Lista para almacenar las asignaturas

    def registrar_asignatura(self, nombre, sigla, plan_estudio, docente):
        """Registra una nueva asignatura."""
        nueva_asignatura = Asignatura(nombre, sigla, plan_estudio, docente)
        self.asignaturas.append(nueva_asignatura)
        return nueva_asignatura

    def obtener_asignatura(self, sigla):
        """Obtiene una asignatura por su sigla."""
        for asignatura in self.asignaturas:
            if asignatura.sigla == sigla:
                return asignatura
        return None

    def listar_asignaturas(self):
        """Lista todas las asignaturas registradas."""
        return self.asignaturas

    def buscar_asignaturas_por_docente(self, docente):
        """Busca asignaturas asociadas a un docente específico."""
        return [asignatura for asignatura in self.asignaturas if asignatura.docente == docente]