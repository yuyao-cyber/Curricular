# import Database.py
import smtplib 
import requests

# email constraints
sender = "422project1group3@gmail.com"
recipient = "recipient@gmail.com"
subject = "Congratulations on your Vaccination Appointment!"
message = "Dear, \n\tCongratulations! You have successfully made an appointment for Covid-19 vaccination. "
    
# format email
email = "Subject: {}\n\n{}".format(subject, message)

# get sender password
password_file = open("password.txt", "r")
password = password_file.readline()
password_file.close()

# creates SMTP session 
s = smtplib.SMTP("smtp.gmail.com", 587) 
    
# start TLS for security 
s.starttls() 
    
# authentication 
s.login(sender, password) 
    
# sending the mail 
s.sendmail(sender, recipient, email)
    
# terminating the session 
s.quit() 

# success message
print("\nSuccessfully sent a confirmation email to", recipient)
