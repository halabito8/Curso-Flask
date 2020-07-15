from flask import Blueprint

usuarios = Blueprint('usuarios', __name__)

@usuarios.route('/')
def index():
    return 'En usuarios'