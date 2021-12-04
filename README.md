# Vaccination Distribution System
1. This vaccination distribution system provides an interface that gives users the ability to search for and 'schedule' Covid-19 vaccine appointments based on three specific criteria: The
distance from the user to the vaccination clinic, the type of vaccine, and day/time the user wishes to receive the vaccine.

2. Authors: Joshua Fawcett, Max Hopkins,  Meghan Riehl, Yuyao Zhuge

3. The implementation of the system started on 4/12/2021 and finished on 4/26/2021

4. This system was created as the final submission for Project 1 in CIS 422, spring 2021, with Professor Anthony Hornof

5. In order to run the program, the user must run the python file "flask_main.py". This will create 
a server for the user to connect to, and allow the user to connect to the website via 
"localhost:5000" in their browser of choice.

6. If not downloaded, the user will need to install flask in order to host the server on their machine.

7. Software dependencies:
	- `JQUERY v1.11.3`
	- `Flask v1.1.2`
	- `Google maps API`

8. Directory Structure
	- The main directory houses all the modules such as searching, scheduling, the database,
	  and the user interface
	- The `templates` directory houses all of the html templates for the website, including error
	  handling templates such as a 404 event handler.
	- The `static` directory houses all the static, or unchanging components to the website,
	  such as images and CSS style sheets.
