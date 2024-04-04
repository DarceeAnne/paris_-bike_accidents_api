
from flask import Flask, render_template
from flask_basicauth import BasicAuth
import pymysql
import os
from flask import abort
from flask import request
import json
import math

app = Flask(__name__)
app.config.from_file("accident_velo_config.json", load=json.load)

auth = BasicAuth(app)

from flask_swagger_ui import get_swaggerui_blueprint
from xlwings import App
swaggerui_blueprint = get_swaggerui_blueprint(
    base_url='/docs',
    api_url='/static/openapi.yaml',
)
app.register_blueprint(swaggerui_blueprint)

MAX_PAGE_SIZE = 100

@app.route("/accidents_velo")
@auth.required
def accidents():
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', MAX_PAGE_SIZE))
    page_size = min(page_size, MAX_PAGE_SIZE)
    db_conn = pymysql.connect(host="localhost", 
                              user="root", 
                              password=os.getenv('sql_password'), 
                              database="paris_bike_traffic",
                              cursorclass=pymysql.cursors.DictCursor)
    try:
        with db_conn.cursor() as cursor:
            cursor.execute(u"""
                        SELECT 
                        av.date, 
                        av.an,
                        av.mois,
                        av.jour,
                        av.dep as department,
                        s.value as sexe,
                        si.value as position,
                        t.value as trajet
                        FROM accidents_velo av
                        JOIN dim_sex s ON av.sexe = s.id 
                        JOIN dim_situ si ON av.situ = si.id
                        JOIN dim_trajet t ON av.trajet = t.id
                        ORDER BY av.date
                        LIMIT %s
                        OFFSET %s
                        """, (page_size, (page-1) * page_size))
            accidents = cursor.fetchall()
        
        with db_conn.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) AS total FROM accidents_velo")
            total = cursor.fetchone()
            last_page = math.ceil(total['total'] / page_size)

    finally: db_conn.close()

    return {
        'accidents':accidents,
        'last_page': f'/accidents_velo?page={last_page}&page_size={page_size}',
        'next_page': f'/accidents_velo?page={page+1}&page_size={page_size}',  
    }

