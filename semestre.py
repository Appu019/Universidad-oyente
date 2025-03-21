class Semestre:
    def __init__(self, numero):
        self.numero = numero
        self.asignaturas = []  # Lista para almacenar asignaturas

    def agregar_asignatura(self, asignatura):
        self.asignaturas.append(asignatura)

    def mostrar_asignaturas(self):
        print(f"Semestre: {self.numero}")
        for asignatura in self.asignaturas:
            asignatura.mostrar_estudiantes()