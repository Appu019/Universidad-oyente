class Asignatura:
    def __init__(self, nombre, sigla, plan_estudio, docente):
        self.nombre = nombre
        self.sigla = sigla
        self.plan_estudio = plan_estudio
        self.docente = docente
        self.estudiantes = []  # Lista para almacenar estudiantes

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def mostrar_estudiantes(self):
        print(f"Asignatura: {self.nombre} ({self.sigla}) - Plan de Estudio: {self.plan_estudio}")
        print(f"Docente: {self.docente}")
        print("Estudiantes Inscritos:")
        for estudiante in self.estudiantes:
            print(estudiante)
