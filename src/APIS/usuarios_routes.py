from flask import jsonify, request, blueprints, redirect, jsonify, json, session, render_template
from models.User import User, UserSchema, db

users_routes = blueprints.Blueprint("users", __name__)


@users_routes.route('/get', methods = ['GET'])
def get_usuarios():
    resultall = User.query.all()
    schema = UserSchema(many=True)
    result = schema.dump(resultall)
    return jsonify(result)

@users_routes.route('/getUser', methods=['GET'])
def get_usuario():
    if 'user_id' in session:
        user_id = session['user_id']
        user = User.query.filter_by(user=user_id).first()

        if user is not None:
            schema = UserSchema()
            result = schema.dump(user)
            return jsonify(result)
        else:
            return jsonify({"error": "Usuario no encontrado"}), 404
    else:
        return jsonify({"error": "No hay usuario en sesión"}), 401


@users_routes.route('/ingresar', methods=['POST'])
def ingresar():
    # Verifica si ya hay una sesión iniciada
    if 'user_id' in session:
        # El usuario ya tiene una sesión activa, redirige a la página principal o a donde desees
        return redirect('/mainPage')
    
    # Si no hay una sesión iniciada, continúa con el proceso de inicio de sesión
    login = request.form['email']  # Puede ser un correo electrónico o un nombre de usuario
    password = request.form['password']
    
    user = db.session.query(User).filter((User.email == login) | (User.user == login)).first()

    if user is not None and user.password == password:
        session['user_id'] = user.user  # Guarda el ID del usuario en la sesión
        return redirect('/mainPage')
    else:
        error_message = 'Usuario no encontrado o contraseña incorrecta'
        return redirect('/login?error_message=' + error_message)




    
@users_routes.route('/registrar', methods=['POST'])
def create_usuario():
    try:
        user = request.form['user']
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Verifica si el correo electrónico o el nombre de usuario ya están en uso
        existing_email_user = User.query.filter((User.email == email) | (User.user == user)).first()
        if existing_email_user:
            return render_template('signUp.html', error_message='Usuario o correo ya en uso') 

        # Crea un nuevo usuario
        nuevo_usuario = User(user=user, name=name, email=email, password=password)
        db.session.add(nuevo_usuario)
        db.session.commit()
        session['user_id'] = user
        return redirect('/mainPage')  # Reemplaza 'mainPage.html' con tu plantilla principal
    except Exception as e:
        return redirect('/signUp')  # Reemplaza 'register.html' con tu plantilla de registro

@users_routes.route('/logout')
def logout():
    # Verifica si hay una sesión activa
    if 'user_id' in session:
        # Elimina la sesión
        session.pop('user_id', None)
    
    # Redirige al usuario a la página de inicio de sesión u otra página, como la principal
    return redirect('/login')  # Cambia '/login' por la página a la que desees redirigir

    
@users_routes.route('/put/<user>', methods=['PUT'])
def update_usuario(user):
    try:
        usuario = User.query.get(user)
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
        usuario = User.query.get(id)

        if not usuario:
            return jsonify({"error": "Usuario no encontrado"}), 404

        db.session.delete(usuario)
        db.session.commit()

        return jsonify({"mensaje": "Usuario eliminado correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al eliminar el usuario", "details": str(e)}), 500