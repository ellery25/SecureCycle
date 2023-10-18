from flask import jsonify, request, blueprints, redirect, jsonify, json, session, render_template
from models.Route import Route, RouteSchema, db
import googlemaps
route_routes = blueprints.Blueprint("routes", __name__) 

#------------------GET----------------------
@route_routes.route('/getRoute', methods=['GET'])
def getRoute():
    routes = Route.query.all()
    return jsonify(RouteSchema.dump(routes))

#-----------------POST-----------------------
@route_routes.route('/addRoute', methods = ['POSt'])
def addRoute():
    try:
        data = request.get_json()
        db.session.add(Route(**data))
        db.session.commit()

        return RouteSchema.jsonify(Route(**data)), 201
    except Exception as e:
        return jsonify({"error": "Error al crear el comentario", "details": str(e)}), 400

@route_routes.route('/get_directions', methods=['POST'])
def get_directions():
    origin = request.form['origin']
    destination = request.form['destination']

    directions = googlemaps.directions(origin, destination)

    return jsonify(directions)


#-------PUT-----------
@route_routes.route('/put/<id>', methods=['PUT'])
def updatePost(id):
    try:
        routes = Route.query.get(id)
        if not routes:
                return jsonify({"error": "Comentario no encontrado"}), 404

        data = request.json
            
        for k, v in data.items():
            setattr(routes, k, v)

        db.session.commit()

        return jsonify({"mensaje": "Comentario actualizado correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al actualizar el Comentario", "details": str(e)}), 500

#-------DELETE--------
@route_routes.route('/delete/<id>', methods=['DELETE'])
def deletePost(id):
    try:
        routes = Route.query.get(id)

        if not routes:
            return jsonify({"error": "Comentario no encontrado"}), 404

        db.session.delete(routes)
        db.session.commit()

        return jsonify({"mensaje": "Comentario eliminado correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al eliminar el Comentario", "details": str(e)}), 500