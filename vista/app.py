import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, request, redirect, url_for
from controlador.persona_controller import PersonaController
from controlador.universitario_controller import UniversitarioController
from controlador.docente_controller import DocenteController
from controlador.asignatura_controller import AsignaturaController

app = Flask(__name__)

# Controladores
persona_controller = PersonaController()
universitario_controller = UniversitarioController()
docente_controller = DocenteController()
asignatura_controller = AsignaturaController()

# Rutas para Persona
@app.route('/')
def index():
    personas = persona_controller.obtener_personas()
    return render_template('index.html', personas=personas)

@app.route('/agregar', methods=['POST'])
def agregar_persona():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    edad = int(request.form['edad'])
    sexo = request.form['sexo']
    persona_controller.registrar_persona(nombre, apellido, edad, sexo)
    return redirect(url_for('index'))

# Rutas para Universitario
@app.route('/universitarios')
def listar_universitarios():
    universitarios = universitario_controller.obtener_universitarios()
    return render_template('universitarios.html', universitarios=universitarios)

@app.route('/universitarios/agregar', methods=['POST'])
def agregar_universitario():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    edad = int(request.form['edad'])
    sexo = request.form['sexo']
    cod_estudiante = request.form['cod_estudiante']
    universitario_controller.agregar_universitario(nombre, apellido, edad, sexo, cod_estudiante)
    return redirect(url_for('listar_universitarios'))

# Rutas para Docente
@app.route('/docentes')
def listar_docentes():
    docentes = docente_controller.listar_docentes()
    return render_template('docentes.html', docentes=docentes)

@app.route('/docentes/agregar', methods=['POST'])
def agregar_docente():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    edad = int(request.form['edad'])
    sexo = request.form['sexo']
    cod_docente = request.form['cod_docente']
    docente_controller.agregar_docente(nombre, apellido, edad, sexo, cod_docente)
    return redirect(url_for('listar_docentes'))


#Rutas para asignatura
@app.route('/asignatura/agregar', methods=['POST'])
def agregar_asignatura():
    nombre = request.form['nombre']
    sigla = request.form['sigla']
    plan_estudio = request.form['plan_estudio']
    docente = request.form['docente']
    asignatura_controller.registrar_asignatura(nombre, sigla, plan_estudio, docente)
    return redirect(url_for('listar_asignaturas'))

if __name__ == '__main__':
    app.run(debug=True)