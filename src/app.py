from flask import Flask, redirect, request, jsonify, json, session, render_template

from config.bd import app, db

from models.Usuarios import Usuario, UsuarioSchema
from models.Rutas import Rutas, RutasSchema
from models.Comunidad import Comunidad, ComunidadSchema
from models.Comments import Comments, CommentsSchema

app.static_url_path = '/static'
app.static_folder = 'static'

usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many = True)

ruta_schema = RutasSchema()
rutas_schema = RutasSchema(many = True)

comunidad_schema = ComunidadSchema()
comunidades_schema = ComunidadSchema(many = True)

comment_schema = CommentsSchema()
comments_schema = CommentsSchema(many = True)

app.static_url_path = '/static'
app.static_folder = 'static'

@app.route('/', methods=['GET'])
def index():
    return render_template("HomePage.html")

@app.route('/signUp')
def sign_up():
    return render_template('signUp.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/ingresar', methods=['POST'])
def ingresar():
    email = request.form['email']
    password = request.form['password']
    user = db.session.query(Usuario.id).filter(Usuario.Email == email, Usuario.Password == password).all()
    resultado = usuarios_schema.dump(user)

    if len(resultado)>0:
        session['email'] = email
        return redirect('/')
    else:
        return 'Usuario no encontrado'
    
@app.route('/registrar', methods=['POST'])
def create_usuario():
    try:
        email = request.form['email']
        password = request.form['password']
        
        nuevo_usuario = Usuario(Email=email, Password=password)
        db.session.add(nuevo_usuario)
        db.session.commit()
        
        return render_template('HomePage.html', usuario=nuevo_usuario)
    except Exception as e:
        return jsonify({"error": "Error al crear el usuario", "details": str(e)}), 400
    
@app.route('/put/<id>', methods=['PUT'])
def update_usuario(id):
    try:
        usuario = Usuario.query.get(id)
        if not usuario:
                return jsonify({"error": "Usuario no encontrado"}), 404

        data = request.get_json()

        for k, v in data.items():
            setattr(usuario, k, v)

        db.session.commit()

        return jsonify({"mensaje": "Usuario actualizado correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al actualizar el usuario", "details": str(e)}), 500

@app.route('/delete/<id>', methods=['DELETE'])
def delete_usuario(id):
    try:
        usuario = Usuario.query.get(id)

        if not usuario:
            return jsonify({"error": "Usuario no encontrado"}), 404

        db.session.delete(usuario)
        db.session.commit()

        return jsonify({"mensaje": "Usuario eliminado correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al eliminar el usuario", "details": str(e)}), 500


#Rutas
@app.route('/get', methods=['GET'])
def get_rutas():
    ruta = Rutas.query.all()
    return jsonify(rutas_schema.dump(ruta))


@app.route('/post', methods=['POST'])
def create_ruta():
    try:
        data = request.get_json()
        db.session.add(Rutas(**data))
        db.session.commit()

        return ruta_schema.jsonify(Rutas(**data)), 201
    except Exception as e:
        return jsonify({"error": "Error al crear la ruta", "details": str(e)}), 400


@app.route('/put/<id>', methods=['PUT'])
def update_ruta(id):
    try:
        ruta = Rutas.query.get(id)
        if not ruta:
                return jsonify({"error": "Ruta no encontrada"}), 404

        data = request.json
            
        for k, v in data.items():
            setattr(ruta, k, v)

        db.session.commit()

        return jsonify({"mensaje": "Ruta actualizada correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al actualizar la ruta", "details": str(e)}), 500


@app.route('/delete/<id>', methods=['DELETE'])
def delete_reporte(id):
    try:
        ruta = Rutas.query.get(id)

        if not ruta:
            return jsonify({"error": "Ruta no encontrada"}), 404

        db.session.delete(ruta)
        db.session.commit()

        return jsonify({"mensaje": "Ruta eliminada correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al eliminar la ruta", "details": str(e)}), 500


#comentarios  
@app.route('/get', methods=['GET'])
def get_comments():
    comentarios = Comments.query.all()
    return jsonify(comments_schema.dump(comentarios))


@app.route('/post', methods=['POST'])
def create_comment():
    try:
        data = request.get_json()
        db.session.add(Comments(**data))
        db.session.commit()

        return comments_schema.jsonify(Comments(**data)), 201
    except Exception as e:
        return jsonify({"error": "Error al crear el comentario", "details": str(e)}), 400


@app.route('/put/<id>', methods=['PUT'])
def update_comment(id):
    try:
        comentario = Comments.query.get(id)
        if not comentario:
                return jsonify({"error": "Comentario no encontrado"}), 404

        data = request.json
            
        for k, v in data.items():
            setattr(comentario, k, v)

        db.session.commit()

        return jsonify({"mensaje": "Comentario actualizado correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al actualizar el Comentario", "details": str(e)}), 500


@app.route('/delete/<id>', methods=['DELETE'])
def delete_comment(id):
    try:
        comentario = Comments.query.get(id)

        if not comentario:
            return jsonify({"error": "Comentario no encontrado"}), 404

        db.session.delete(comentario)
        db.session.commit()

        return jsonify({"mensaje": "Comentario eliminado correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al eliminar el Comentario", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)