class Carrera:
    def __init__(self, nombre):
        self.nombre = nombre
        self.semestres = []  # Lista para almacenar semestres

    def agregar_semestre(self, semestre):
        self.semestres.append(semestre)

    def mostrar_semestres(self):
        print(f"Carrera: {self.nombre}")
        for semestre in self.semestres:
            print("-------------------------------------------------")
            semestre.mostrar_asignaturas()
            