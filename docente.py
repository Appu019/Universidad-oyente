from persona import Persona

class Docente(Persona):
    def __init__(self, nombre, apellido, edad, sexo, cod_docente):
        self.persona = Persona(nombre, apellido, edad, sexo)
        self.cod_docente = cod_docente
        self.especialidades = []#Lista de especialidades

    def agregar_especialidad(self, especialidad):
        if especialidad not in self.especialidades:
            self.especialidades.append(especialidad)
            especialidad.agregar_docente(self)

    def mostrar_especialidades(self):
        print(f"Docente: {self.persona.nombre} {self.persona.apellido} - Código: {self.cod_docente}")
        print("Especialidades:")
        for especialidad in self.especialidades:
            print(especialidad.nombre)

    def __str__(self):
        return f"{self.cod_docente} - {self.persona}, Especialidades: {', '.join([e.nombre for e in self.especialidades])}"