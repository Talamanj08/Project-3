from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from config import db_url
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError



# connect to data base

engine = create_engine(db_url)
connection = engine.connect()

app = Flask(__name__)


def create_session():
     engine = connection()
     Session = sessionmaker(bind=engine)
     return Session()
    

@app.route('/')
def index():
     try:
        # session=create_session()
        data=engine.execute("select * from death_byage_2021")
        for record in data:
            print(record)
        #print(data)
        return 'Hello Flask'
     except SQLAlchemyError as ex:
         # Handle any database errors
         return 'Database error occurred: {}'.format(str(ex))

# creat bar chart view

@app.route('/barchart')
def barchart():
    # Establish a connection to the database
    connection = engine.connect()
    ##cursor = connection.cursor()

    # Execute a query to fetch the data
    query = "SELECT total_dose_1_administered, total_series_completed, total_covid_19_deaths FROM total_vaxs_vs_deaths_2021"
    result = connection.execute(query)

    # Fetch the results
    ##results = cursor.fetchall()
    data = result.fetchone()
    total_dose_1_administered, total_series_completed, total_covid_19_deaths = data

    # Close the cursor and the database connection
    ##cursor.close()
    connection.close()

    # Convert the results to JSON format
    ##chart_data = [{'category': row[0], 'count': row[1]} for row in results]
    chart_data = [
        {'label': 'Dose 1 Administered', 'count': total_dose_1_administered},
        {'label': 'Series Completed', 'count': total_series_completed},
        {'label': 'COVID-19 Deaths', 'count': total_covid_19_deaths}
    ]
    # Pass the chart data to the template
    return render_template('barchart.html', chart_data=chart_data)




if __name__ == '__main__':
     app.run()