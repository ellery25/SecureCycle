from flask import jsonify, request, blueprints, redirect, jsonify, json, session, render_template
from models.Post import Post, PostSchema, db
from datetime import datetime 

posts_routes = blueprints.Blueprint("posts", __name__)


#------------------GET----------------------
@posts_routes.route('/getPost', methods=['GET'])
def getPosts():
    try:
        posts = Post.query.all()
        return PostSchema(many=True).dump(posts), 200
    except Exception as e:
        return jsonify({"error": "Error al obtener los posts", "details": str(e)}), 500

#-----------------POST----------------------
@posts_routes.route('/addPost', methods=['POST'])
def addPost():
    try:
        # Obtiene los datos del formulario en lugar de JSON
        title = request.form['title']
        content = request.form['content']
        
        # Obtiene el user_id de la sesión
        user_id = session.get('user_id')

        # Obtiene la fecha actual
        date = datetime.now()

        # Crea una instancia del modelo Post con los datos obtenidos
        new_post = Post(user_id=user_id, title=title, content=content, date=date)

        # Agrega el nuevo post a la base de datos
        db.session.add(new_post)
        db.session.commit()

        return redirect('/mainPage')
    except Exception as e:
        return jsonify({"error": "Error al crear el comentario", "details": str(e)}), 400


#-------PUT-----------
@posts_routes.route('/put/<id>', methods=['PUT'])
def updatePost(id):
    try:
        post = Post.query.get(id)
        if not post:
                return jsonify({"error": "Comentario no encontrado"}), 404

        data = request.json
            
        for k, v in data.items():
            setattr(post, k, v)

        db.session.commit()

        return jsonify({"mensaje": "Comentario actualizado correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al actualizar el Comentario", "details": str(e)}), 500

#-------DELETE--------
@posts_routes.route('/delete/<id>', methods=['DELETE'])
def deletePost(id):
    try:
        post = Post.query.get(id)

        if not post:
            return jsonify({"error": "Comentario no encontrado"}), 404

        db.session.delete(post)
        db.session.commit()

        return jsonify({"mensaje": "Comentario eliminado correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al eliminar el Comentario", "details": str(e)}), 500