import datetime as dt
import numpy as np
import pandas as pd

#access our data in the SQLite database
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#add the code to import the Flask dependencies 
from flask import Flask, jsonify

# Set up the Database engine for the Flask app to access and query SQLite db file
engine = create_engine('sqlite:///hawaii.sqlite')
# reflect teh database into our classes
Base = automap_base()
#Python functin to reflect the tables
Base.prepare(engine, reflect=True)

# Save our references to each table  2 tables below 
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link from python to our database
session = Session(engine)

# Define our app for our Flask app. 
# Set Up Flask      
app = Flask(__name__)

# Set up the flask route
@app.route('/')
def welcome():
    return( """Welcome to the Climate Analysis API!
              Available Routes:
              /api/v1.0/precipitation
              /api/v1.0/stations
              /api/v1.0/tobs
              /api/v1.0/temp/start/end""")

@app.route('/api/v1.0/precipitation')
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

#Listed the stations by unraveling results into a one-dimensional array by using the function  np.ravel() with (results) as parameter
# to return list as JSON  added stations-stations
@app.route('/api/v1.0/stations')
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)


#return the temperature observations for the previous year. define route and created function called temp_monthly()
@app.route('/api/v1.0/tobs')
def temp_monthly():
    prev_year = dt.date(2017, 8, 3) - dt.timedelta(days=365)
    resutls = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(resutls))
    return jsonify(temps=temps)

# last route will report min, average adn max temps. Will require start and end date
# create a list called sel
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)   

    #  /api/v1.0/temp/start/end route
    # /api/v1.0/temp/2017-06-01/2017-06-30
    # flask run at command line
    if __name__ == "__main__":
	    app.run(debug=True)