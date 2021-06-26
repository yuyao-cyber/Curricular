'''
search.py

    Search function for vaccine appointment scheduler

    -Appointment scheduler allowes users to search local clinics for 
     available appointments based off:
        +vaccine type
        +distance from user
        +weekend or weekday
        +time (9AM - 4:30PM)
     user can then select from available appointments and reserve their 
     appointment slot.

     -Search function filters through a database of all appointments 
      returns any matching appointments that are not already reserved.

    Authors: Meghan Riehl, Max Hopkins

'''
#Database of all appointments
    #Clinic Name, Clinic Address, Vaccine Offered, Day Type, Date, Time Type, Reserved
    #Lines will be split so search can compare directly with indexed parameters
import Database
#Google API function to determine distance of clinic from user input address
from api import getDistance

def search(vaccine, distance, date, location, data):
    '''
    The searching function for the system:

    vaccine = user selected vaccine type (Moderna, Pfizer, J&J, any)
    distance = user selected distance from location (10, 15, 20, 25, 30, any)
    date = user input day/ time (weekend/weekday, am/pm)
    location = user input address (street, city, zip)
    data = database to be filtered
    '''
    #End returned list of all matching appointments
    matches = []
    #Setting distance variable so it's useable by Google API
    distance = int(distance)
    #check if we have am, pm, or both
    day_time = date.split()

    #Looking for am or pm: time will either be set to all options, am times, or pm times
    if day_time[0] == "any":
        time = ['9', '930', '10', '1030', '11', '1130', '12', '1230', '1', '130', '2', '230', '3', '330', '4', '430']
    elif day_time[1] == 'am':
        time = ['9', '930', '10', '1030', '11', '1130']
    else:
        time = ['12', '1230', '1', '130', '2', '230', '3', '330', '4', '430']


    #storing parameters 
    '''
        parameters_lists for those that have multiple options based off user input (any)
        parameters for those that only have the one option (specified)
    '''
    parameters_lists = [(5, time)]
    #NULL value at the 6th index means the appointment is not reserved
    parameters = [(6, 'NULL')]

    #Looking for weekend or weekday
    if day_time[0] == "any":
        day = ["Weekend", "Weekday"]
        #adding both options to parameters_lists
        parameters_lists.append((3, day))
    else:
        #adding specified option to parameters
        parameters.append((3, day_time[0]))
    
    #Looking for specified vaccine type
    if vaccine == 'any':
        vaccine = ['Moderna', 'Pfizer', 'J&J', 'AstroZenica']
        #adding all options to parameters_lists
        parameters_lists.append((2, vaccine))
    else:
        #adding specified option to parameters
        parameters.append((2, vaccine))
    
    #looking through file
        #data.getLines() '''testing'''
    for line in data._lines:
        #how many parameters are met (if not all pass):
        count = 0
        #splitting data line into appointment details
        appointment = line.split(',')
        #print(appointment) '''testing'''

        #remove whitespace
        for i in range(len(appointment)):
            appointment[i] = appointment[i].strip()

        #print(appointment[1]) '''testing'''
        appointment[1] = appointment[1].replace("_", " ")
        dist = getDistance(location, appointment[1]) 
        dist = dist.replace(",", "") 
        dist = dist.split(" ") 
        dist = float(dist[0]) 

        #Iterating though specified parameters
        for item in parameters:
            if appointment[item[0]] == item[1]:
                #adding match to counter
                count += 1

        #Iterating through option parameters
        for item in parameters_lists:
            if appointment[item[0]] in item[1]:
                #adding match to counter
                count += 1

        if dist <= distance:
            count += 1

        #If all parameters are met
        if count == 5:
            appointment[0] = appointment[0].replace("_", " ")
            #Combine appointment details into one line and add to matches list
            matches.append(','.join(appointment))

    return matches

#db = Database.database("DataBase.txt") '''testing'''
#matches = search("Moderna", "25", "any", "address", db) '''testing'''

#print(matches) '''testing''''''
