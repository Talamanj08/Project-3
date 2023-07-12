#http://localhost:5000/

#################################################
# Import the dependencies.
#################################################
from sqlalchemy import create_engine
from config import user, password, host, port, database
from flask import Flask, render_template
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from . import db
from flask_sqlalchemy import SQLAlchemy

#################################################
# Create App and Create Engine and Base
#################################################
app = Flask(__name__)
db = SQLAlchemy(app)

engine = create_engine(
    f"postgresql://{user}:{password}@{host}:{port}/{database}"
)
Base = declarative_base(bind=engine)

#################################################
# Database Connection
#################################################
def get_connection():
    return engine

if __name__ == '__main__':
    try:
        engine = get_connection()
        print("Connection to the database created successfully.")
    except Exception as ex:
        print("Connection could not be made due to the following error:\n", ex)


#################################################
# Create Classes(Tables)
#################################################
class Example(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(255))

class Example(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(255))

Base.metadata.create_all()
#################################################
# Flask Routes
#################################################
##homepage 
@app.route('/')
def home():
   return render_template('home.html')

if __name__ == '__main__':
    app.run()


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
@app.route('/heatmap')
def heatmap():
    try: 
        session= create_session()
        query= text("SELECT latitude, longitude, name FROM capital_coords")

        with session.begin():
            result= session.execute(query)
            data= result.fetchall()

            return "Heatmap Generated Successfully"
    except SQLAlchemyError as ex:
        return 'Database error occurred: {}'.format(str(ex))
#################################################
# Create Session
#################################################

#################################################
# Create Session
#################################################

#################################################
# Create Session
#################################################