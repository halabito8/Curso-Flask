from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, BooleanField, DecimalField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from wtforms.widgets import TextArea
from wtforms.widgets.html5 import NumberInput

# Cada clase va a ser un formulario, tiene herencia de FlaskForm
class Prueba(FlaskForm):
    usuario = StringField('Usuario')
    nombre = StringField('Nombre', validators=[DataRequired(message="nombre requerido")])
    descripcion = StringField('Descripcion', widget=TextArea())
    cantidad = DecimalField('Cantidad', widget=NumberInput())
    submit = SubmitField('Ok')