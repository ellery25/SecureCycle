from flask import jsonify, request, blueprints, redirect, jsonify, json, session, render_template
from models.Post import Post, PostSchema, db

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
        data = request.get_json()
        db.session.add(Post(**data))
        db.session.commit()

        return PostSchema.jsonify(Post(**data)), 201
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