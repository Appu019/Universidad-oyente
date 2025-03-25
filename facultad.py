class Facultad:
    def __init__(self, nombre, sigla, mision, vision):
        self.nombre = nombre
        self.sigla = sigla
        self.mision = mision
        self.vision = vision
        self.carreras = []  # Lista para almacenar carreras

    def agregar_carrera(self, carrera):
        self.carreras.append(carrera)

    def mostrar_carreras(self):
        print(f"Facultad: {self.nombre} ({self.sigla})")
        print("Carreras:")
        for carrera in self.carreras:
            print("------------------------------------")
            print(carrera)

    def __str__(self):
        return f"{self.nombre} {self.sigla}, Misión: {self.mision}, Visión: {self.vision}"