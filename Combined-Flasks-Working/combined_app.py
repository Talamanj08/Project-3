#http://localhost:5000/

from flask import Flask, g, render_template, jsonify, json
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
    return render_template('home.html')

@app.route('/pie')
def pie_chart():
    # Retrieve data from the database
    db, cursor = get_db()

    # Execute SQL query to select the required columns from the cause_of_death table
    cursor.execute("""
        SELECT COVID_19_Deaths, Total_Deaths, Pneumonia_Deaths,
               Pneumonia_and_COVID_19_Deaths, Influenza_Deaths
        FROM cause_of_death
    """)
    data = cursor.fetchone()  # Assuming the query returns a single row

    # Extract the cause of deaths values
    covid_deaths, total_deaths, pneumonia_deaths, pneumonia_covid_deaths, influenza_deaths = data

    # Calculate the value for "Other_Deaths"
    other_deaths = total_deaths - covid_deaths - pneumonia_deaths - pneumonia_covid_deaths - influenza_deaths

    # Create an updated values array including "Other_Deaths"
    values = [covid_deaths, pneumonia_deaths, pneumonia_covid_deaths, influenza_deaths, other_deaths]

    # Close the cursor and connection
    cursor.close()
    db.close()

    # Pass data to the template
    return render_template('pie.html', values_json=json.dumps(values))

@app.route('/barchart')
def barchart():
    # Retrieve a database connection
    db, cursor = get_db()

    # Execute query for 2021
    query_2021 = "SELECT total_dose_1_administered, total_series_completed, total_covid_19_deaths FROM total_vaxs_vs_deaths_2021"
    cursor.execute(query_2021)
    total_dose_1_administered_2021, total_series_completed_2021, total_covid_19_deaths_2021 = cursor.fetchone()

    # Execute query for 2022
    query_2022 = "SELECT total_dose_1_administered, total_series_completed, total_covid_19_deaths FROM total_vaxs_vs_deaths_2022"
    cursor.execute(query_2022)
    total_dose_1_administered_2022, total_series_completed_2022, total_covid_19_deaths_2022 = cursor.fetchone()

    # Close the cursor and connection
    cursor.close()
    db.close()

    # Prepare the data for the 2021 chart
    chart_data_2021 = {
        'labels': ['Total Dose 1 Administered', 'Total Series Completed', 'Total COVID-19 Deaths'],
        'counts': [total_dose_1_administered_2021, total_series_completed_2021, total_covid_19_deaths_2021]
    }

    # Prepare the data for the 2022 chart
    chart_data_2022 = {
        'labels': ['Total Dose 1 Administered', 'Total Series Completed', 'Total COVID-19 Deaths'],
        'counts': [total_dose_1_administered_2022, total_series_completed_2022, total_covid_19_deaths_2022]
    }

    # Pass the chart data to the template
    return render_template('barchart.html', chart_data_2021=json.dumps(chart_data_2021), chart_data_2022=json.dumps(chart_data_2022))


@app.route('/map')
def map():
    # Retrieve a database connection
    db, cursor = get_db()
    # Execute query
    cursor.execute("SELECT state, latitude, longitude, deaths_per_capita_2021 FROM deaths_perstate_wcoords2021")
    rows = cursor.fetchall()
    data = [{'state': row[0], 'latitude': row[1], 'longitude': row[2], 'deaths_per_capita_2021': row[3]} for row in rows]
    # Pass the map data to the template
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