from flask import jsonify, request, blueprints, redirect, jsonify, json, session, render_template
from models.Alert import Alert, AlertSchema, db

alert_routes = blueprints.Blueprint("alerts", __name__)

#------------------GET----------------------
@alert_routes.route('/getAlerts', methods=['GET'])
def getAlerts():
    alerts = Alert.query.all()
    return jsonify(AlertSchema.dump(alerts))

#-----------------POST-----------------------
@alert_routes.route('/addAlert', methods = ['POSt'])
def addAlert():
    try:
        data = request.get_json()
        db.session.add(Alert(**data))
        db.session.commit()

        return AlertSchema.jsonify(Alert(**data)), 201
    except Exception as e:
        return jsonify({"error": "Error al crear el comentario", "details": str(e)}), 400

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