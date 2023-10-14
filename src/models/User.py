from config.bd import db, ma, app
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__ = "User"

    user = db.Column(db.String(30), primary_key=True)  
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))


    def __init__(self, user, name, email, password):  
        self.user = user
        self.name = name
        self.email = email
        self.password = password

with app.app_context():
    db.create_all()

class UserSchema(ma.Schema):
    class Meta:
        fields = ("user", "name", "email", "password")  


