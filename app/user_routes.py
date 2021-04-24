# Здесь описаны роуты для
# человека-"под самолетом"
#
#
#
#
import json
from app import app
# from .db_init import conn
from flask import request, jsonify
from datetime import datetime
from psycopg2 import sql
from psycopg2.extras import RealDictCursor


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


@app.route('/api/user/<userid>/create_request', methods=["POST"])
def create_request(userid):
    body = json.loads(request.data)
    body["userid"] = userid
    body["request_time"] = datetime.now()
    
    return body, 200
