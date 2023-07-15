from flask import Flask, g, render_template, json
import psycopg2
from config import user, password, host, port, database 
import configparser

# Set up the app
app = Flask(__name__)

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

@app.route('/pie')
def pie_chart():
    # Retrieve data from the database
    db, cursor = get_db()

    # Execute SQL query
    cursor.execute("SELECT COVID_19_Deaths, Total_Deaths, Pneumonia_Deaths, Pneumonia_and_COVID_19_Deaths, Influenza_Deaths, Pneumonia_Influenza_or_COVID_19_Deaths FROM cause_of_death")
    data = cursor.fetchall()

    # Format data for the pie chart
    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    # Close the cursor and connection
    cursor.close()
    db.close()

    # Pass data to the template
    return render_template('pie.html', labels_json=json.dumps(labels), values_json=json.dumps(values))


if __name__ == '__main__':
    app.run(debug=True)
