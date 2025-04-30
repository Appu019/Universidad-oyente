class Universidad:
    def __init__(self, nombre, sigla, mision, vision):
        self.nombre = nombre
        self.sigla = sigla
        self.mision = mision
        self.vision = vision
        self.facultades = []  # Lista para almacenar facultades

    def agregar_facultad(self, facultad):
        self.facultades.append(facultad)

    def mostrar_facultades(self):
        print(f"Universidad: {self.nombre} ({self.sigla})")
        print("Facultades:")
        for facultad in self.facultades:
            print("------------------------------------")
            print(facultad)

    def __str__(self):
        return f"{self.nombre} {self.sigla}, Misión: {self.mision}, Visión: {self.vision}"