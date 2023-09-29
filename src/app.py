from flask import Flask, redirect, request, jsonify, json, session, render_template

from config.bd import app, db

from models.Usuarios import Usuario, UsuarioSchema
from models.Rutas import Rutas, RutasSchema
from models.Comunidad import Comunidad, ComunidadSchema
from models.Comments import Comments, CommentsSchema

usuarios_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many = True)

rutas_schema = RutasSchema()
rutas_schema = RutasSchema(many = True)

comunidad_schema = ComunidadSchema()
comunidad_schema = ComunidadSchema(many = True)

comments_schema = CommentsSchema()
comments_schema = CommentsSchema(many = True)

@app.route('/', methods=['GET'])
def index():
    
    return render_template("login.html")

@app.route('/ingresar', methods=['POST'])
def ingresar():
    
    return 'algo'

if __name__ == "__main__":
    app.run(debug=True)