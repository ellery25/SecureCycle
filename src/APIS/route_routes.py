from flask import jsonify, request, blueprints, redirect, jsonify, json, session, render_template
from models.Route import Route, RouteSchema, db
import googlemaps
route_routes = blueprints.Blueprint("routes", __name__) 

#------------------GET----------------------
@route_routes.route('/getRoute', methods=['GET'])
def getRoute():
    routes = Route.query.all()
    return jsonify(RouteSchema(many=True).dump(routes))

#-----------------POST-----------------------
from datetime import datetime  # Asegúrate de importar datetime

@route_routes.route('/addRoute', methods=['POST'])
def addRoute():
    try:
        # Obtiene los datos del formulario
        user_id = session.get('user_id')  # Toma el user_id de la sesión
        initialLocation = request.form['initLocation']
        finalLocation = request.form['endLocation']
        title = request.form.get('titleRoute')
        description = request.form.get('description')
        
        # Obtiene la fecha del formulario
        creationDate = request.form.get('fecha')

        # Crea una instancia del modelo Route con los datos obtenidos
        new_route = Route(user_id=user_id, initialLocation=initialLocation, finalLocation=finalLocation, 
                          title=title, description=description, creationDate=creationDate)

        # Agrega la nueva ruta a la base de datos
        db.session.add(new_route)
        db.session.commit()

        return redirect('/mainPage')
    except Exception as e:
        return jsonify({"error": "Error al crear la ruta", "details": str(e)}), 400



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