from flask import jsonify, request, Blueprint
import sys
from . import app


app_routes = Blueprint('app_bp', __name__)


@app_routes.route('/')
@app_routes.route('/<name>')
def index(name=None):
    return jsonify({"msg":"Hello, Aviahackathon 2021"})
