from config.bd import db, ma, app
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Post(db.Model):
    __tablename__ = "Post"

    id_post = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    user_id = db.Column(db.String(30), ForeignKey('User.user'))
    title = db.Column(db.String(50))
    content = db.Column(db.String(255))
    image = db.Column(db.LargeBinary)
    date = db.Column(db.DateTime)

    user = relationship('User', back_populates='posts')

    def __init__(self, user_id, title, content, image, date):
        self.user_id = user_id
        self.title = title
        self.content = content
        self.image = image
        self.date = date

with app.app_context():
    db.create_all()

class PostSchema(ma.Schema):
    class Meta:
        fields = ('user_id', 'title', 'content', 'image', 'date')

