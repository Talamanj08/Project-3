#http://localhost:5000/

#################################################
# Import the dependencies.
#################################################
from sqlalchemy import create_engine
from config import user, password, host, port, database
from flask import Flask
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text

#################################################
# Database Connection
#################################################
def get_connection():
    return create_engine(
        url="postgresql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        )
    )
 
if __name__ == '__main__':    
    try:
        engine = get_connection()
        print(
            f"Connection to the {host} for user {user} created successfully.")
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)

#################################################
# Create App and Create Session
#################################################
app=Flask(__name__)

def create_session():
    engine = get_connection()
    Session = sessionmaker(bind=engine)
    return Session()

#################################################
# Flask Routes
#################################################
##main 
@app.route('/')
def index():
    try:
        session=create_session()
        return 'Hello Flask'
    except SQLAlchemyError as ex:
        # Handle any database errors
        return 'Database error occurred: {}'.format(str(ex))

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