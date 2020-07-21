from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sql3354595:7Haz6Ng1fm@sql3.freemysqlhosting.net/sql3354595'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecret'

db = SQLAlchemy(app)
Migrate(app, db)
from Aplicacion.models import *

from Aplicacion.core.views import core
from Aplicacion.usuarios.views import usuarios
from Aplicacion.bases.views import bases
from Aplicacion.formas.views import formas


app.register_blueprint(core)
app.register_blueprint(bases)
app.register_blueprint(usuarios, url_prefix='/usuarios')
app.register_blueprint(formas)