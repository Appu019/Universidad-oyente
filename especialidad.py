class Especialidad:
    def __init__(self, nombre, area_de_especialidad, nivel_academico, asignaturas):
        self.nombre = nombre
        self.area_de_especialidad = area_de_especialidad
        self.nivel_academico = nivel_academico
        self.asignaturas = []
        self.docentes = []

    def agregar_docente(self, docente):
        if docente not in self.docentes:
            self.docentes.append(docente)
            docente.agregar_especialidad(self)

    def mostrar_docentes(self):
        print(f"Especialidad: {self.nombre} - Área: {self.area_de_especialidad} - Nivel: {self.nivel_academico}")
        print("Docentes:")
        for docente in self.docentes:
            print(docente.persona.nombre)
