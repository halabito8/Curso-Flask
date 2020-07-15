from Aplicacion import db

class TipoUsuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    tipo = db.Column(db.String(100), nullable=False)

    usuarios = db.relationship('Usuarios', backref='tipo', lazy='dynamic')

    def __init__(self, tipo):
        self.tipo = tipo


class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nombre = db.Column(db.String(50))
    passwrd = db.Column(db.String(50))
    tipoID = db.Column(db.Integer, db.ForeignKey('tipo_usuarios.id'))

    cursos = db.relationship('Cursos', secondary='cursos_usuarios', backref='usuarios', lazy='dynamic')

    def __init__(self, nombre, email, passwrd):
        self.nombre = nombre
        self.email = email
        self.passwrd = passwrd

    def __repr__(self):
        return f"id {self.id} nombre {self.nombre} email {self.email}"

class Cursos(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    curso = db.Column(db.String(50))

    def __init__(self, curso):
        self.curso = curso

    def __repr__(self):
        return f"id {self.id} curso {self.curso}"

db.Table('cursos_usuarios',
    db.Column('usuarioID', db.Integer, db.ForeignKey('usuarios.id')),
    db.Column('cursoID', db.Integer, db.ForeignKey('cursos.id'))
)