from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from config import db_url
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError


#connect to data base
engine = create_engine(db_url)
connection = engine.connect()

app = Flask(__name__)


def create_session():
     engine = connection()
     Session = sessionmaker(bind=engine)
     return Session()
<<<<<<< Updated upstream
    
=======

>>>>>>> Stashed changes

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

<<<<<<< Updated upstream
if __name__ == '__main__':
=======
if __name__ == 'main':
>>>>>>> Stashed changes
     app.run()