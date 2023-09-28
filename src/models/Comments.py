from config.bd import db, ma, app

class Comments(db.Model):
    __tablename__ = "Comments"

    id_comments = db.Column(db.Integer, primary_key = True)
    id_usuario = db.Column(db.Integer, unique = True)
    id_comunidad = db.Column(db.Integer, unique = True)
    title = db.Column(db.String(50))
    content = db.Column(db.String(180))

    def __init__ (self, id_usuario, id_comunidad, title, content):
        self.id_usuario = id_usuario
        self.id_comunidad = id_comunidad
        self.title = title
        self.content = content

with app.app_context():
    db.create_all()

class CommentsSchema(ma.Schema):
    class Meta:
        fields = ['id_comments', 'id_usuario', 'id_comunidad', 'title', 'content']