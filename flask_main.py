"""
File: flask_main.py
Purpose: The backend server for the vaccine scheduling system
Authors: Max Hopkins
"""

import flask
import Database
from flask import request, redirect, url_for, session
from search import search
#import confirm_email 
import app_scheduling
###
# Globals
###

#The flask application 
app = flask.Flask(__name__)
#The secret key for the session dictionary
app.secret_key = "something random"
#The database used for storing and retrieving appointments
db = Database.database("DataBase.txt")
#Used by the confirmation screen to determine what appointments should be displayed
result = {}

###
# Pages
###


@app.route("/")
@app.route("/index")
def index():
    """The main page of the application"""
    return  flask.render_template('main.html')

@app.route("/schedule")
def schedule_appointment():
    """
    Retrieve session details and update the database given the selected appointment
    """
    #Information to update the database
    day = session.get('day', None)
    time = session.get('time', None)
    place = session.get('place', None)
    address = session.get('address', None)
    vaccine = session.get('vaccine', None)
    date = session.get('date', None)

    #Convert the address and the name of clinic into the database format
    place = place.replace(" ", "_")
    address = address.replace(" ", "_")

    #args concatenates the data received from the user and converts it into how it would show up
    #in the database
    args = place + ", " + address + ", " + vaccine + ", " + day + ", " + date + ", " + time + ", NULL"

    #code is the confirmation code generated from the schedule method
    code = app_scheduling.schedule(args, db)

    #confirm_email.email(email, fname, lname, code)

    #Render the confirmation code page and pass the confirmtion code to be displayed
    return flask.render_template("schedule.html", code=code)

@app.route("/confirmation", methods = ['GET', 'POST'])
def signup():
    """Display the available appointments based on search params"""
    return flask.render_template("confirmation.html")


@app.route("/cancel")
def cancel():
    """Load the cancel template, allows the user to cancel an appointment with a confirmation #"""
    return flask.render_template("cancel.html")



###############
# AJAX request handlers
#   These return JSON, rather than rendering pages.
###############

@app.route("/_cancel")
def cancel_appointment():
    """Cancel an appointment by changing the confirmation # to NULL"""

    #match will become true if the confirmation # exists in the database
    match = 'false'

    #get the confirmation code from the user
    code = request.args.get('code', "", type=str)

    #determines where to index into the database
    #updated in the for loop below
    count = 0

    #this will iterate through the database and check if the confirmation # exists
    #If the confirmation number does exist, match will be set to true
    for line in db._lines:
        line = line.split(",")
        if str(code) == str(line[6].strip()):
            db.updateApp(count, "NULL")
            match = 'true'
        count += 1
        
    #put the result for match into a JSON format
    result = {"match": match}

    return flask.jsonify(result=result)

@app.route("/_search")
def search_for_appointment():
    """Search for an appointment in the database based on the search params"""

    #Retrieve the information used to search
    vaccine = request.args.get('vaccine', "", type=str)
    distance = request.args.get('distance', "", type=str)
    time = request.args.get("time", "", type=str)
    address = request.args.get("address", "", type=str)

    #these are not used
    #fname = request.args.get("fname", "", type=str)
    #lname = request.args.get("lname", "", type=str)
    #email = request.args.get("email", "", type=str)

    #call the search module
    #matches is the list of appointments that meet the search requirements
    matches = search(vaccine, distance, time, address, db)

    #x is used to index in the JSON format 
    x = "0"

    #The amount of appointments returned by search
    length = len(matches)

    #This loop will JSONify the appointments into the result dictionary, which is global
    for i in range(length):
        #put the appointment into the result dictionary
        result[x] = matches[i]
        #add +1 to x variable and convert back to string
        x = int(x) + 1
        x = str(x)
        
    #return the length of the matches as a json variable
    result["length"] = length

    return flask.jsonify(result=result)

@app.route("/_retreive")
def retreive():
    """Called when the confirmation template is loaded, sends the matches to be displayed"""
    return flask.jsonify(result=result)


@app.route("/_schedule", methods = ['GET', 'POST'])
def schedule():
    """
    When a schedule button is pushed, this is called to store the appointment selected into
    session variables
    """
    if request.method == 'GET':
        #store the selected appointment into sessions details
        session['day'] = request.args.get("day", "", type=str)
        session['place'] = request.args.get("place", "", type=str)
        session['date'] = request.args.get("date", "", type=str)
        session['address'] = request.args.get("address", "", type=str)
        session['vaccine'] = request.args.get("vaccine", "", type=str)
        session['time'] = request.args.get("time", "", type=str)

        #sent back to the user as a test
        temp = 1
        
        return flask.jsonify(temp=temp)

    else: 
        return flask.render_template("schedule.html")



###################
#   Error handlers
###################


@app.errorhandler(404)
def error_404(e):
    app.logger.warning("++ 404 error: {}".format(e))
    return flask.render_template('404.html'), 404


@app.errorhandler(500)
def error_500(e):
    app.logger.warning("++ 500 error: {}".format(e))
    assert not True  # I want to invoke the debugger
    return flask.render_template('500.html'), 500


@app.errorhandler(403)
def error_403(e):
    app.logger.warning("++ 403 error: {}".format(e))
    return flask.render_template('403.html'), 403


####

if __name__ == "__main__":
        #Run the server on localhost:5000
        app.run(port=5000, host="0.0.0.0")
