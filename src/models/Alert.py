from config.bd import db, ma, app
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Alert(db.Model):
    __tablename__ = "Alert"

    id_alert = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(30), ForeignKey('User.user'))
    latitude = db.Column(db.Float)  
    longitude = db.Column(db.Float)  
    type = db.Column(db.String(40))
    description = db.Column(db.String(255))
    date = db.Column(db.DateTime)

    user = relationship('User', back_populates='alerts')

    def __init__(self, user_id, latitude, longitude, type, description, date):
        self.user_id = user_id
        self.latitude = latitude
        self.longitude = longitude
        self.type = type
        self.description = description
        self.date = date

with app.app_context():
    db.create_all()

class AlertSchema(ma.Schema):
    class Meta:
        fields = ('user_id', 'latitude', 'longitude', 'type', 'description', 'date')
