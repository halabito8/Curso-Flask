from flask import Blueprint, render_template

formas = Blueprint('formas', __name__)

@formas.route('/forms')
def formularios():
    return render_template('formas.html')