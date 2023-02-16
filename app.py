from typing import List, Dict
from flask import Flask
import mysql.connector
import json
import os

app = Flask(__name__)

"""
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'knights'
"""

def favorite_colors() -> List[Dict]:
    config = {
        'user': os.environ['MYSQL_USER'],
        'password': os.environ['MYSQL_PWD'],
        'host': os.environ['MYSQL_URL'],
        'port': os.environ['MYSQL_PORT'],
        'database': os.environ['MYSQL_DATABASE']
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM favorite_colors')
    results = [{name: color} for (name, color) in cursor]
    cursor.close()
    connection.close()

    return results


@app.route('/')
def index() -> str:
    return json.dumps({'favorite_colors': favorite_colors()})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
