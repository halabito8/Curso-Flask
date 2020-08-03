from flask import Blueprint, render_template, request
from Aplicacion.formularios.forms import Prueba

formularios = Blueprint('formularios', __name__)

@formularios.route('/formularios', methods=['GET','POST'])
def formulario():
    form = Prueba()
    if request.method == "POST" and form.validate_on_submit():
        return "Muy bien campeon"
    return render_template('formularios.html', form=form)