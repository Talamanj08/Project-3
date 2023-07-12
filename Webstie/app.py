from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from config import db_url
from sqlalchemy import create_engine


# connect to data base

engine = create_engine(db_url)
conncection = engine.connect()

app = Flask(__name__)

@app.route('/')