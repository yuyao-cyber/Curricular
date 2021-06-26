import Database #call Database.py for functionalities
import search # call search.py for functionalities

def schedule(matches, db):
    """
    matches is the user's chosen appointment:
    eg. 'Albertsons_Pharmacy, 311_Coburg_Rd_Eugene_OR_97401, Pfizer, Weekday, 11, NULL'
    open DataBase.txt -> find the line that matches the variable "matches" ->
    change the confirmation number by calling updateApp function in Database.py
    """
    #open DataBase.txt
    with open("DataBase.txt", 'r') as f:
        count = 0 #count the number of line in DataBase.txt from 0
        #matches = matches + "\n"
        for line in f: #for loop each line to find the string that matches the variable "matches"
            line = line.strip() #this get rid of the new line at the end of each string

            if matches == line: #if found that "matches" equals to the line
                break
            count += 1 #count the number of line

    db.updateApp(count,id(matches)) #call the function in Database.py to add a confirmation # for the appointment
    return id(matches) #return the confirmation number


# Running test example:
#schedule('Albertsons_Pharmacy, 311_Coburg_Rd_Eugene_OR_97401, Pfizer, Weekday, 11, NULL')
