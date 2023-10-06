from flask import Flask, redirect, request, jsonify, json, session, render_template

from config.bd import app, db

from APIS.usuarios_routes import users_routes
from APIS.rutas_routes import rutas_routes
from APIS.comments_routes import comments_routes

app.register_blueprint(users_routes, url_prefix = '/usuarios')
app.register_blueprint(rutas_routes, url_prefix = '/rutas')
app.register_blueprint(comments_routes, url_prefix = '/comments')


app.static_url_path = '/static'
app.static_folder = 'static'

@app.route('/', methods=['GET'])
def index():
    return render_template("HomePage.html")

@app.route('/signUp')
def sign_up():
    return render_template('signUp.html')

@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)