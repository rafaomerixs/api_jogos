from db import db

class Jogos(db.Model):

    _tablename_ = 'jogos'

    titulo= db.Column(db.Integer, primary_key=True)
    genero= db.Column(db.String(80), nullable=False)
    desenvolvedor= db.Column(db.String(80), nullable=False)
    plataforma= db.Column(db.Integer, nullable=False)

    def json(self):
        return {
            'titulo': self.titulo,
            'genero': self.genero,
            'desenvolvedor': self.desenvolvedor,
            'plataforna': self.plataforma
        }