from persona import Persona

class Universitario(Persona):
    def __init__(self, nombre, apellido, edad, sexo, cod_estudiante):
        self.persona = Persona(nombre, apellido, edad, sexo)
        self.cod_estudiante = cod_estudiante
    
    def __str__(self):
        return f"{self.cod_estudiante} - {self.persona}"
