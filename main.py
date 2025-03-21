from carrera import Carrera
from semestre import Semestre
from asignatura import Asignatura
from universitario import Universitario
from docente import Docente

def main():
    # Crear un docente
    docente1 = Docente("Juan", "Martínez", 45, "M", "RD1233123", "Programación")
    docente2 = Docente("Pedro", "Gomez", 45, "M", "RD412331", "Redes")
    
    # Crear asignaturas
    asignatura1 = Asignatura("Programación 3", "SIS-133", "2018", docente1)
    asignatura2 = Asignatura("Redes", "SIS-111", "2018", docente2)
    
    # Crear estudiantes
    estudiante1 = Universitario("Juanito", "Perez", 22, "M", "RU202301")
    estudiante2 = Universitario("Ana", "Perez", 21, "F", "RU202302")
    estudiante3 = Universitario("Carlos", "Ruiz", 23, "M", "RU202303")

    # Agregar estudiantes a las asignaturas
    asignatura1.agregar_estudiante(estudiante1)
    asignatura1.agregar_estudiante(estudiante2)
    asignatura1.agregar_estudiante(estudiante3)

    asignatura2.agregar_estudiante(estudiante2)
    asignatura2.agregar_estudiante(estudiante3)
    
    # Crear semestres y agregar asignaturas
    print ("Creando semestres")
    semestre1 = Semestre(1)
    semestre1.agregar_asignatura(asignatura1)
    
    semestre2 = Semestre(2)
    semestre2.agregar_asignatura(asignatura2)
    
    # Crear carrera y agregar semestres
    carrera = Carrera("Ingeniería de Sistemas")
    carrera.agregar_semestre(semestre1)
    carrera.agregar_semestre(semestre2)
    
    # Mostrar información de la carrera
    carrera.mostrar_semestres()

if __name__ == "__main__":
    main()