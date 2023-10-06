from flask import blueprints, request, jsonify
from models.Rutas import Rutas, RutasSchema, db

rutas_routes = blueprints.Blueprint("rutas", __name__)

@rutas_routes.route('/get', methods=['GET'])
def get_rutas():
    resultall = Rutas.query.all()
    schema = RutasSchema(many=True)
    result = schema.dump(resultall)
    return jsonify(result)

@rutas_routes.route('/post', methods=['POST'])
def create_ruta():
    try:
        data = request.get_json()
        nueva_ruta = Rutas(**data)  

        db.session.add(nueva_ruta)
        db.session.commit()

        return RutasSchema().jsonify(nueva_ruta), 201  
    except Exception as e:
        return jsonify({"error": "Error al crear la ruta", "details": str(e)}), 400



@rutas_routes.route('/put/<int:id>', methods=['PUT'])  
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



@rutas_routes.route('/delete/<id>', methods=['DELETE'])
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