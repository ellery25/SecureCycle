from config.bd import db, ma, app

class Rutas(db.Model):
    __tablename__ = "Rutas"

    id_ruta = db.Column(db.Integer, primary_key = True)
    id_user = db.Column(db.Integer, unique = True)
    latitud = db.Column(db.Integer)
    longitud = db.Column(db.Integer)

    def init(self, id_user, latitud, longitud):
        self.id_user = id_user
        self.latitud = latitud
        self.longitud = longitud

with app.app_context:
    db.create_all()

class RutasSchema(ma.Schema):
    class Meta:
        fields = ('id_ruta', 'id_user', 'latitud', 'longitud')