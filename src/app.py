from flask import Flask, redirect, request, jsonify, json, session, render_template

from config.bd import app, db
import googlemaps
import os

from APIS.usuarios_routes import users_routes
from APIS.alert_routes import alert_routes
from APIS.post_routes import posts_routes
from APIS.route_routes import route_routes


app.register_blueprint(users_routes, url_prefix = '/usuarios')
app.register_blueprint(alert_routes, url_prefix = '/alerts')
app.register_blueprint(posts_routes, url_prefix = '/posts')
app.register_blueprint(route_routes, url_prefix = '/routes')


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

@app.route('/mainPage')
def main():
    return render_template('mainPage.html')


if __name__ == "__main__":
    app.run(debug=True)