#http://localhost:5000/

from flask import Flask, g, render_template, jsonify
import psycopg2
from config import user, password, host, port, database 
import configparser

# Set up the app
app= Flask(__name__)

# Load configuration
app.config.from_mapping(
    DATABASE_HOST=host,
    DATABASE_PORT=port,
    DATABASE_NAME=database,
    DATABASE_USER=user,
    DATABASE_PASSWORD=password
)

# Reusable connection to PostgreSQL
def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(
            host=app.config['DATABASE_HOST'],
            port=app.config['DATABASE_PORT'],
            database=app.config['DATABASE_NAME'],
            user=app.config['DATABASE_USER'],
            password=app.config['DATABASE_PASSWORD']
        )
        g.cursor = g.db.cursor()
    return g.db, g.cursor

@app.teardown_appcontext
def teardown_appcontext(error):
    db = g.pop('db', None)
    if db is not None:
        db.close()

## home - right now just displays state coords table 
@app.route('/')
def home():
    db, cursor = get_db()
    cursor.execute("SELECT * FROM capital_coords")
    rows = cursor.fetchall()
    table_html = "<table>"
    table_html += "<tr><th>State</th><th>Longitude</th><th>Latitude</th></tr>"
    for row in rows:
        table_html += "<tr>"
        for value in row:
            table_html += f"<td>{value}</td>"
        table_html += "</tr>"
    table_html += "</table>"
    return table_html

@app.route('/map')
def map():
    db, cursor = get_db()
    cursor.execute("SELECT state, latitude, longitude, deaths_per_capita_2021 FROM deaths_perstate_wcoords2021")
    rows = cursor.fetchall()
    data = [{'state': row[0], 'latitude': row[1], 'longitude': row[2], 'deaths_per_capita_2021': row[3]} for row in rows]
    return render_template('map.html', data=data)

@app.route('/map-data-2021')
def map_data_2021():
    db, cursor = get_db()
    cursor.execute("SELECT state, latitude, longitude, deaths_per_capita_2021 FROM deaths_perstate_wcoords2021")
    rows = cursor.fetchall()
    data = [
        {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [row[2], row[1]]
            },
            'properties': {
                'state': row[0],
                'deaths_per_capita_2021': row[3]
            }
        }
        for row in rows
    ]
    feature_collection = {
        'type': 'FeatureCollection',
        'features': data
    }
    return jsonify(feature_collection)

@app.route('/map-data-2022')
def map_data_2022():
    db, cursor = get_db()
    cursor.execute("SELECT state, latitude, longitude, deaths_per_capita_2022 FROM deaths_perstate_wcoords2022")
    rows = cursor.fetchall()
    data = [
        {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [row[2], row[1]]
            },
            'properties': {
                'state': row[0],
                'deaths_per_capita_2022': row[3]
            }
        }
        for row in rows
    ]
    feature_collection = {
        'type': 'FeatureCollection',
        'features': data
    }
    return jsonify(feature_collection)


if __name__ == '__main__':
    app.run()