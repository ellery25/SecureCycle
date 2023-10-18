from config.bd import db, ma, app
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Route(db.Model):
    __tablename__ = "Route"

    id_route = db.Column(db.Integer, primary_key = True, autoincrement=True)
    user_id = db.Column(db.String(30), ForeignKey('User.user'))
    initialLocation = db.Column(db.String(255)) #Asume que estás almacenando coordenadas como texto (p.ej. "lat,lng")
    finalLocation = db.Column(db.String(255))
    creationDate = db.Column(db.DateTime)
    title = db.Column(db.String(180))
    description = db.Column(db.String(255))

    user = relationship('User', back_populates='routes')

    def __init__(self, user_id, initialLocation, finalLocation, creationDate, title, description):
        self.user_id = user_id
        self.initialLocation = initialLocation
        self.finalLocation = finalLocation
        self.creationDate = creationDate
        self.title = title
        self.description = description

with app.app_context():
    db.create_all()

class RouteSchema(ma.Schema):
    class Meta:
        fields = ('user_id', 'initialLocation', 'finalLocation', 'creationDate', 'title', 'description')