from persona import Persona

class Docente(Persona):
    def __init__(self, nombre, apellido, edad, sexo, cod_docente, especialidad):
        self.persona = Persona(nombre, apellido, edad, sexo)
        self.cod_docente = cod_docente
        self.especialidad = especialidad
    
    def __str__(self):
        return f"{self.cod_docente} - {self.persona}, Especialidad: {self.especialidad}"
