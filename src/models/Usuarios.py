from config.bd import db, ma, app

class Usuario (db.Model):
    __tablename__ = "Usuario"

    id = db.Column(db.Integer, primary_key= True, autoincrement=True)
    Email = db.Column(db.String(50), unique = True)
    Password = db.Column(db.String(50))

    def __init__ (self, Email, Password):
        self.Email = Email
        self.Password = Password

with app.app_context():
    db.create_all()

class UsuarioSchema (ma.Schema):
    class Meta:
        fields = ("id", "Email", "Password")
