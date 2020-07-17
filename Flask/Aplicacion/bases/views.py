from flask import Blueprint, render_template

bases = Blueprint('bases', __name__)

@bases.route('/venv')
def venv():
    return render_template('venv.html')

@bases.route('/rutas/<string:nombre>')
def rutas(nombre):
    return render_template('rutas.html', nombre=nombre)