from flask import Flask, redirect, request, jsonify, json, session, render_template

from config.bd import app, db

@app.route('/', methods=['GET'])
def index():
    
    return "Hola Ellery"

if __name__ == "__main__":
    app.run(debug=True)