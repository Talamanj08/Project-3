#http://localhost:5000/

#################################################
# Import the dependencies.
#################################################
from sqlalchemy import create_engine, MetaData
from config import user, password, host, port, database
from flask import Flask, render_template
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import json


#################################################
# Create App and Create Engine and Base
#################################################
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{user}:{password}@{host}:{port}/{database}"
db = SQLAlchemy(app)

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

Base = db.Model

@app.route('/heatmap')
def heatmap():
    # Execute the query using SQLAlchemy's execute() method
    with engine.connect() as conn:
        query = "SELECT latitude, longitude, state FROM deaths_perstate_wCoords2021"
        result = conn.execute(query)
        data = result.fetchall()

    # Create a pandas DataFrame from the query result
    df = pd.DataFrame(data, columns=['latitude', 'longitude', 'state'])

    # Convert Decimal values to strings
    df['latitude'] = df['latitude'].apply(str)
    df['longitude'] = df['longitude'].apply(str)

    # Create a list of coordinates and values for the heatmap
    heatmap_data = df.to_dict(orient='records')

    # Convert the heatmap data to JSON string
    heatmap_json = json.dumps(heatmap_data)

    # Render the HTML template with the heatmap data
    return render_template('heatmap_d3.html', heatmap_data=heatmap_json)

if __name__ == '__main__':
    app.run()

#################################################
# Database Connection
#################################################
#################################################
# Create Classes(Tables)
#################################################
#class Death_byState_2021(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    #data = db.Column(db.String(255))

#class Death_byState_2022(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    #data = db.Column(db.String(255))

#class Death_byState_2023(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    #data = db.Column(db.String(255))



#Base.metadata.create_all()
#################################################
# Flask Routes
#################################################
##homepage 
#@app.route('/')
#def index():
   #return render_template('index.html')

#if __name__ == '__main__':
    #app.run()

##barchart
#@app.route('/bar_chart')
#def bar_chart():
    #try:
       # Session = create_session()
       # session = Session()

       # result = session.execute("SELECT category, COUNT(*) FROM your_table GROUP BY category")
       # data = result.fetchall()

       # labels = [row[0] for row in data]
       # values = [row[1] for row in data]

       # return render_template('bar_chart.html', labels=labels, values=values)

    #except SQLAlchemyError as ex:
       # print("Error occurred while querying the database:", ex)

   # finally:
   #     session.close()

#if __name__ == '__main__':
    #app.run()


##heatmap

#################################################
# Create Session
#################################################

#################################################
# Create Session
#################################################

#################################################
# Create Session
#################################################