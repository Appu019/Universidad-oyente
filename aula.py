class Aula:
    def __init__(self, nombre, capacidad, ubicacion):
        self. nombre = nombre
        self.capacidad = capacidad
        self.ubicacion = ubicacion
        self.asignaturas = []#lista de asignaturas
        self.docentes = []
        self.estudiantes = []

    def agregar_asignatura(self, asignatura):
        if asignatura not in self.asignaturas:
            self.asignaturas.append(asignatura)
            asignatura.agregar_aula(self)

    def mostrar_asignaturas(self):
        print(f"Aula: {self.nombre} ({self.capacidad}) - Ubicación: {self.ubicacion}")
        print("Asignaturas:")
        for asignatura in self.asignaturas:
            print(asignatura.nombre)
    
   
