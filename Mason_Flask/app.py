#http://localhost:5000/

#################################################
# Import the dependencies.
#################################################
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from config import user, password, host, port, database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import psycopg2
from psycopg2 import sql

app = Flask(__name__)

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="Project_3",
    user="postgres",
    password="postgres"
)

@app.route('/')
def pie_chart():
    # Retrieve data from the database
    cursor = conn.cursor()

    # Execute SQL query
    query = sql.SQL("SELECT category, value FROM your_table")
    cursor.execute(query)

    data = cursor.fetchall()
    cursor.close()

    # Format data for the pie chart
    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    # Pass data to the template
    return render_template('pie.html', labels_json=jsonify(labels), values_json=jsonify(values))

if __name__ == '__main__':
    app.run()