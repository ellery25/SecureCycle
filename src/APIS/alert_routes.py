from flask import jsonify, request, blueprints, redirect, jsonify, json, session, render_template
from models.Alert import Alert, AlertSchema, db
from datetime import datetime
from flask import request, jsonify, session


alert_routes = blueprints.Blueprint("alerts", __name__)

#------------------GET----------------------
@alert_routes.route('/getAlerts', methods=['GET'])
def getAlerts():
    alerts = Alert.query.all()
    return jsonify(AlertSchema(many=True).dump(alerts))

#-----------------POST-----------------------


@alert_routes.route('/addAlert', methods=['POST'])
def addAlert():
    try:
        # Obtiene los datos del formulario
        type = request.form['type']
        direction = request.form['direction']
        description = request.form['description']

        # Obtiene el user_id de la sesión
        user_id = session.get('user_id')

        # Obtiene la fecha actual
        date = datetime.now()

        # Crea una instancia del modelo Alert con los datos obtenidos
        new_alert = Alert(user_id=user_id, type=type, direction=direction, description=description, date=date)

        # Agrega el nuevo alert a la base de datos
        db.session.add(new_alert)
        db.session.commit()

        return redirect('/mainPage')
    except Exception as e:
        return jsonify({"error": "Error al crear la alerta", "details": str(e)}), 400


#-------PUT-----------
@alert_routes.route('/put/<id>', methods=['PUT'])
def updatePost(id):
    try:
        alert = Alert.query.get(id)
        if not alert:
                return jsonify({"error": "Comentario no encontrado"}), 404

        data = request.json
            
        for k, v in data.items():
            setattr(alert, k, v)

        db.session.commit()

        return jsonify({"mensaje": "Comentario actualizado correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al actualizar el Comentario", "details": str(e)}), 500

#-------DELETE--------
@alert_routes.route('/delete/<id>', methods=['DELETE'])
def deletePost(id):
    try:
        alert = Alert.query.get(id)

        if not alert:
            return jsonify({"error": "Comentario no encontrado"}), 404

        db.session.delete(alert)
        db.session.commit()

        return jsonify({"mensaje": "Comentario eliminado correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al eliminar el Comentario", "details": str(e)}), 500