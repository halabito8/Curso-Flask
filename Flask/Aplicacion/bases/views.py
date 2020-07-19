from flask import Blueprint, render_template

bases = Blueprint('bases', __name__)

@bases.route('/venv')
def venv():
    return render_template('venv.html')

@bases.route('/rutas/<string:nombre>')
def rutas(nombre):
    return render_template('rutas.html', nombre=nombre)

@bases.route('/debug')
def debug():
    return render_template('debug.html')

@bases.route('/blueprints')
def blueprints():
    return render_template('blueprints.html')