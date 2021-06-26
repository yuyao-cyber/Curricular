""" Database.py

    This module is in charge of managing the database.txt file. It provides a class called 'database'
    which stores the database.txt file name and a list of each line in the database.txt file. The databse
    class has methods that give it the ability to add appointments to the database, delete appointments
    from the database, and update appointments in the database. The result of calling each method
    (addApp, deleteApp, updateApp) will modify the database.txt file

    Created: 4/18/2021

    Initial Author: Joshua Fawcett

 """

# ===============================================================================================================================================================
# ============================================================= Start Database Class Implementation =============================================================

class database:
# ============================================ Constructor ==============================================
    def __init__(self, filename):
        # self.fName stores the name of the database.txt file for future access
        self._fName = filename
        
        # self._lines is used to store each line in the file for easy access to the contents. This
        # is especially useful for the addApp, deleteApp, and updateApp methods which would need to
        # open the database.txt file 2 times (1 for reading and 1 for writing) every time they're called. 
        self._lines = []

        # open the database with read access
        with open(self._fName, 'r') as f:
            # iterate through each line in the file
            for line in f:
                # store the line in self._lines
                self._lines.append(line)

    """
    def getLines(self):
        self._lines = []
        with open(self._fName, 'r') as f:
            for line in f:
                self._lines.append(line)
    """

# ============================================ Adding an appointment ====================================
    def addApp(self, cName, cLoc, aType, aDay, aDate, aTime, cNumber):
        """ Add an appointment to the database
                - cName: clinic Name
                - cLoc: clinic Location
                - aType: appointment type (moderna, pfizer, etc)
                - aDay: day of the week the appointment occurs (weekday, weekend)
                - aDate: The date of the appointment (day/month/year)
                - aTime: appointment time
                - cNumber: confirmation number
        """
        # Correctly format the appointment to be added
        app = "\n{}, {}, {}, {}, {}, {}, {}".format(cName, cLoc, aType, aDay, aDate, aTime, cNumber)

        # Open the file with append access to write the new line to the very end of the file
        with open(self._fName, 'a+') as f:
            # write the new appointment to the file
            f.write(app)

        # Update self._lines to reflect the changes to the file
        self._lines.append(app)
        return None

# ============================================ Deleting an appointment ==================================
    def deleteApp(self, ind):
        """ This method deletes an appointment from the database

            - ind: The index of the appointment into self._lines (The line number of the appointment - 1)
        """
        # numLines stores the number of lines in the file. It is used for error checking
        # to make sure that an invalid index is not being provided. It is also used to iterate
        # through self._lines
        numLines = len(self._lines)

        # Error handling: Make sure a valid index is given for the appointment
        if ((ind >= numLines) or (ind < 0)):
            return -1

        # Open self._fName with write access
        with open(self._fName, 'w') as f:
            # Iterate through each line in self._lines
            for i in range(numLines):
                # If the current line is not the line to delete
                if i != ind:
                    # Write the line to the file
                    f.write(self._lines[i])
                    
        # Update self._lines by splicing out the entry located at 'ind'
        self._lines = self._lines[:ind] + self._lines[(ind+1):]
        return None

# ============================================ Updating an appointment ==================================
    def updateApp(self, appIndex, data, field = 6):
        """ This method updates a specific field of an appointment at the specified
            line number.

            - appIndex: The index of the appointment into self._lines (The line number of the appointment - 1)
            - data: The new data to be written to the file
            - field: The part of the appointment that is being updated (clinic name, location, vaccine type, etc.)

            If 'field' is not specified when calling this method, then it will default to updating field #7
            in the database.txt file (at index 6 in self._lines), which is the confirmation number
        """
        # Error handling: Make sure a valid index is given for the appointment
        if ((appIndex >= len(self._lines)) or (appIndex < 0)):
            return -1

        # split the appointment from a string to a list of fields, i.e:
        # "cname, loc, vtype, day, date, time, cnumber" -> ["cname", "loc", "vtype", ...]
        fields_list = self._lines[appIndex].split(" ")

        # Error handling: Make sure a valid field is specified
        if ((field >= len(fields_list)) or (field < 0)):
            return -1

        # Write the new data to the specified field
        fields_list[field] = "{}\n".format(data)

        # Join the fields list together to make it a single string, i.e:
        # ["cname", "loc", "vtype", "day", "date", "time", "cnumber"] -> "cname, loc, vtype, ..."
        # and store the result back in self._lines
        self._lines[appIndex] = " ".join(fields_list)

        #print(self._lines[appIndex])

        # Open self._fName with write access
        with open(self._fName, 'w+') as f:
            # Iterate through each line in self._lines
            for line in self._lines:
                # Write the line to the file
                f.write(line)   
        return None

# ================================================================ End Database Class Implementation ============================================================
# ===============================================================================================================================================================

#db = database("DataBase.txt")
#a = 1
#for i in range(51):
    #test = db.updateApp(i,id(a))
    #test = db.updateApp(i,"NULL")
    

