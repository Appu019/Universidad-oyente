from carrera import Carrera
from semestre import Semestre
from asignatura import Asignatura
from universitario import Universitario
from docente import Docente
from especialidad import Especialidad
from universidad import Universidad
from facultad import Facultad
from aula import Aula

def main():
    # --- 1. CREAR UNIVERSIDAD ---
    print("\n--- Creando Universidad ---")
    universidad = Universidad(
        "Universidad Amazonica De Pando",
        "UAP",
        "Formar profesionales competentes",
        "Ser líder en educación superior"
    )
    print(f"Universidad creada: {universidad.nombre} ({universidad.sigla})")

    # --- 2. CREAR FACULTADES ---
    print("\n--- Creando Facultades ---")
    facultad_ingenieria = Facultad(
        "Facultad de Ingeniería y Tecnologia",
        "FIT",
        "Formar ingenieros",
        "Ser líder en ingeniería"
    )
    facultad_marketing = Facultad(
        "Facultad De Marketin Digital",
        "FMD",
        "Formar profesionales para las nuevas tecnologias",
        "Ser líder en marketing digital"
    )
    universidad.agregar_facultad(facultad_ingenieria)
    universidad.agregar_facultad(facultad_marketing)
    print(f"Facultades agregadas: {facultad_ingenieria.nombre}, {facultad_marketing.nombre}")

    # --- 3. CREAR CARRERAS ---
    print("\n--- Creando Carreras ---")
    carrera_sistemas = Carrera("Ingeniería de Sistemas")
    carrera_marketing = Carrera("Marketing Digital")
    facultad_ingenieria.agregar_carrera(carrera_sistemas)
    facultad_marketing.agregar_carrera(carrera_marketing)
    print(f"Carreras creadas: {carrera_sistemas.nombre}, {carrera_marketing.nombre}")

    # --- 4. CREAR SEMESTRES ---
    print("\n--- Creando Semestres ---")
    semestre1 = Semestre(1)
    semestre2 = Semestre(2)
    semestre3 = Semestre(3)
    carrera_sistemas.agregar_semestre(semestre1)
    carrera_sistemas.agregar_semestre(semestre2)
    carrera_marketing.agregar_semestre(semestre3)
    print(f"Semestres creados: 1, 2, 3")

    # --- 5. CREAR DOCENTES ---
    print("\n--- Creando Docentes ---")
    docente1 = Docente("Juan", "Martínez", 45, "M", "RD1233123")
    docente2 = Docente("Pedro", "Gomez", 45, "M", "RD412331")
    docente3 = Docente("Maria", "Perez", 45, "F", "RD412331")
    docente4 = Docente("Cristian", "Coaquira", 45, "M", "RD412331")
    print(f"Docentes creados: {docente1.persona.nombre}, {docente2.persona.nombre}, {docente3.persona.nombre}, {docente4.persona.nombre}")

    # --- 6. CREAR ESPECIALIDADES ---
    programacion = Especialidad("Programación III", "Desarollo de aplicaciones")
    redes1 = Especialidad("Redes", "Conexiones de redes y telecomunicaciones")
    
    docente1.agregar_especialidad(programacion)
    docente2.agregar_especialidad(redes1)
    
    labIII = Aula("Laboratorio de Computación", 20, "Edificio de Tecnología")
    labRedes = Aula("Laboratorio de Redes", 20, "Edificio de Tecnología")
    
    labIII.agregar_asignatura(asignatura1)
    labRedes.agregar_asignatura(asignatura2)
    
    
    especialidad1.agregar_docente(docente1)
    especialidad2.agregar_docente(docente2)
    especialidad3.agregar_docente(docente3)
    especialidad4.agregar_docente(docente4)
    print(f"Especialidades creadas: {especialidad1.nombre}, {especialidad2.nombre}, {especialidad3.nombre}, {especialidad4.nombre}")

    # --- 7. CREAR ASIGNATURAS ---
    print("\n--- Creando Asignaturas ---")
    asignatura1 = Asignatura("Programación 3", "SIS-133", "2018", docente1)
    asignatura2 = Asignatura("Redes", "SIS-111", "2018", docente2)
    asignatura3 = Asignatura("Marketing", "SIS-111", "2018", docente3)

    semestre1.agregar_asignatura(asignatura1)
    semestre2.agregar_asignatura(asignatura2)
    semestre3.agregar_asignatura(asignatura3)
    print(f"Asignaturas creadas: {asignatura1.nombre}, {asignatura2.nombre}, {asignatura3.nombre}")

    # --- 8. CREAR ESTUDIANTES ---
    print("\n--- Creando Estudiantes ---")
    estudiante1 = Universitario("Juanito", "Perez", 22, "M", "RU202301")
    estudiante2 = Universitario("Ana", "Perez", 21, "F", "RU202302")
    estudiante3 = Universitario("Carlos", "Ruiz", 23, "M", "RU202303")
    estudiante4 = Universitario("Cristopher", "Coaquira", 21, "M", "RU38203")

    asignatura1.agregar_estudiante(estudiante1)
    asignatura1.agregar_estudiante(estudiante2)
    asignatura1.agregar_estudiante(estudiante3)
    asignatura2.agregar_estudiante(estudiante2)
    asignatura2.agregar_estudiante(estudiante3)
    asignatura3.agregar_estudiante(estudiante2)
    asignatura3.agregar_estudiante(estudiante3)
    asignatura3.agregar_estudiante(estudiante4)
    print(f"Estudiantes matriculados: {estudiante1.persona.nombre}, {estudiante2.persona.nombre}, {estudiante3.persona.nombre}, {estudiante4.persona.nombre}")

    # --- 9. CREAR AULAS ---
    print("\n--- Creando Aulas ---")
    aula1 = Aula("Aula 101", 30, "Edificio Principal", "A101")
    aula2 = Aula("Aula 202", 25, "Edificio Secundario", "A202")
    aula3 = Aula("Laboratorio de Computación", 20, "Edificio de Tecnología", "LAB1")
    
    #en un aula se puede dictar mas de una asignatura
    aula1.agregar_asignatura(asignatura1)
    aula2.agregar_asignatura(asignatura2)
    aula3.agregar_asignatura(asignatura3)

    # asignatura1.agregar_aula(aula1)
    # asignatura1.agregar_aula(aula3)
    # asignatura2.agregar_aula(aula2)
    # asignatura3.agregar_aula(aula3)
    print(f"Aulas creadas: {aula1.nombre}, {aula2.nombre}, {aula3.nombre}")

    # --- 10. MOSTRAR INFORMACIÓN COMPLETA ---
    print("\n--- Información Completa de la Universidad ---")
    universidad.mostrar_facultades()
    facultad_ingenieria.mostrar_carreras()
    carrera_sistemas.mostrar_semestres()

    # print("\n--- Detalles de Asignaturas y Aulas ---")
    # aula1.mostrar_asignaturas()
    # aula2.mostrar_asignaturas()
    # aula3.mostrar_asignaturas()

if __name__ == "__main__":
    main()
