from flask import jsonify, request, blueprints, redirect, jsonify, json, session, render_template
from models.Usuarios import Usuario, UsuarioSchema, db

users_routes = blueprints.Blueprint("usuarios", __name__)


@users_routes.route('/get', methods = ['GET'])
def get_usuarios():
    resultall = Usuario.query.all()
    schema = UsuarioSchema(many=True)
    result = schema.dump(resultall)
    return jsonify(result)


@users_routes.route('/ingresar', methods=['POST'])
def ingresar():
    email = request.form['email']
    password = request.form['password']
    user = db.session.query(Usuario.id).filter(Usuario.Email == email, Usuario.Password == password).all()
    resultado = UsuarioSchema.dump(user)

    if len(resultado)>0:
        session['email'] = email
        return redirect('/')
    else:
        return 'Usuario no encontrado'
    
@users_routes.route('/registrar', methods=['POST'])
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
    
@users_routes.route('/put/<id>', methods=['PUT'])
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

@users_routes.route('/delete/<id>', methods=['DELETE'])
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