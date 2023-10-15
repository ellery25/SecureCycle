from flask import jsonify, request, blueprints, redirect, jsonify, json, session, render_template
from models.User import User, UserSchema, db

users_routes = blueprints.Blueprint("users", __name__)


@users_routes.route('/get', methods = ['GET'])
def get_usuarios():
    resultall = User.query.all()
    schema = UserSchema(many=True)
    result = schema.dump(resultall)
    return jsonify(result)


from flask import render_template

@users_routes.route('/ingresar', methods=['POST'])
def ingresar():
    # Obtén las credenciales del usuario desde la solicitud
    login = request.form['email']  # Puede ser un correo electrónico o un nombre de usuario
    password = request.form['password']

    # Busca al usuario por correo electrónico o nombre de usuario
    user = db.session.query(User).filter((User.email == login) | (User.user == login)).first()

    if user is not None and user.password == password:
        session['user_id'] = user.user  # Guarda el ID del usuario en la sesión
        return redirect('/mainPage', usuario = user)
    else:
        return redirect('/login', error_message='Usuario no encontrado o contraseña incorrecta')


    
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

        return redirect('/mainPage', usuario = nuevo_usuario)  # Reemplaza 'mainPage.html' con tu plantilla principal
    except Exception as e:
        return redirect('/signUp')  # Reemplaza 'register.html' con tu plantilla de registro



    
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