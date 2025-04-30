from modelo.persona import Persona
import sys
import os

class PersonaController:
    def __init__(self):
        self.personas = []
    
    def registrar_persona(self, nombre, apellido, edad, sexo):
        nueva_persona = Persona(nombre, apellido, edad, sexo)
        self.personas.append(nueva_persona)
        return nueva_persona
    
    
    def obtener_personas(self):
        for persona in self.personas:
            if persona.edad < 18:
                print(f"Persona menor de edad: {persona.nombre} {persona.apellido}, {persona.edad} años")
        return None
    
    def listar_personas(self):
        """Lista todas las personas registradas."""
        for persona in self.personas:
            print(f"Nombre: {persona.nombre}, Apellido: {persona.apellido}, Edad: {persona.edad}, Sexo: {persona.sexo}")
        return self.personas
    
    def buscar_persona(self, nombre):
        return[persona for persona in self.personas if persona.nombre == nombre]