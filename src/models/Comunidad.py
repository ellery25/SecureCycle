from config.bd import db, ma, app

class Comunidad(db.Model):
    __tablename__ = "Comunidad"

    id_comunidad = db.Column(db.integer, primary_key = True)
    nombre = db.Column(db.String(20))
    
    def __init__ (self, nombre):
        self.nombre = nombre

with app.app_context():
    db.create_all()

class ComunidadSchema(ma.Schema):
    class Meta:
        fields = ['id_comunidad', 'nombre']