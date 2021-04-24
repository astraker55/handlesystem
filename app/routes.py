from app import app
from flask import jsonify


@app.route('/')
@app.route('/<name>')
def index(name=None):
    return jsonify({"msg":"Hello, Aviahackathon 2021"})
    
