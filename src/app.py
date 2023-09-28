from flask import Flask, redirect, request, jsonify, json, session, render_template

from config.bd import app, db

from models.Usuarios import Usuario, UsuarioSchema
from models.Rutas import Rutas, RutasSchema

usuarios_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many = True)

rutas_schema = RutasSchema()
rutas_schema = RutasSchema(many = True)

@app.route('/', methods=['GET'])
def index():
    
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)