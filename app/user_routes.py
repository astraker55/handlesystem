# Здесь описаны роуты для
# человека-"под самолетом"
#
#
#
#
import json
import sys
# from .db_init import conn
from flask import request, jsonify, make_response, after_this_request, Blueprint
from flask_cors import cross_origin
from datetime import datetime
from psycopg2 import sql
from psycopg2.extras import RealDictCursor


users_api = Blueprint('users', __name__)

#@app.route('/api/user-<id: int>/showpossibleresourses', methods=["GET"])
# @app.login_required
#def show_resourses():
    #cursor = conn.cursor(cursor_factory=RealDictCursor)
    #query = sql.SQL("""SELECT * FROM category_table """)
    #cursor.excecute(query)
    #result = cursor.fetchall()
    #cursor.commit()
    #cursor.close()
    #return json.dumps(result, indent=4, ensure_ascii=False), 200


@users_api.route('/api/user/<userid>/create_request', methods=["POST"])
@cross_origin(methods=["POST"])
def create_request(userid):
    body = request.get_json()
    body["userid"] = userid
    body["request_time"] = datetime.now()
    resp = make_response(body)
    return resp, 200
