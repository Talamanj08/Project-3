from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from config import db_url
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError


engine = create_engine(db_url)
connection = engine.connect()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/barchart')
def barchart():

    # Execute query for 2021
    query_2021 = "SELECT total_dose_1_administered, total_series_completed, total_covid_19_deaths FROM total_vaxs_vs_deaths_2021"
    result_2021 = connection.execute(query_2021)
    total_dose_1_administered_2021, total_series_completed_2021, total_covid_19_deaths_2021 = result_2021.fetchone()

    # Execute query for 2022
    query_2022 = "SELECT total_dose_1_administered, total_series_completed, total_covid_19_deaths FROM total_vaxs_vs_deaths_2022"
    result_2022 = connection.execute(query_2022)
    total_dose_1_administered_2022, total_series_completed_2022, total_covid_19_deaths_2022 = result_2022.fetchone()

     # Prepare the data for the 2021 chart
    chart_data_2021 = [
        {'label': 'Dose 1 Administered', 'count': total_dose_1_administered_2021},
        {'label': 'Series Completed', 'count': total_series_completed_2021},
        {'label': 'COVID-19 Deaths', 'count':total_covid_19_deaths_2021}
    ]

    # Prepare the data for the 2022 chart
    chart_data_2022 = [
        {'label': 'Dose 1 Administered', 'count': total_dose_1_administered_2022},
        {'label': 'Series Completed', 'count': total_series_completed_2022},
        {'label': 'COVID-19 Deaths', 'count': total_covid_19_deaths_2022}
    ]
    # Pass the chart data to the template
    return render_template('barchart3.html', chart_data_2021=chart_data_2021, chart_data_2022=chart_data_2022)


if __name__ == '__main__':
     app.run()