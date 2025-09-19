#import all neccesary lib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
#configuration 
SMTP_SERVER ="smtp.gmail.com" 
SMTP_PORT=587
SENDER_EMAIL="enter your gmail here"
SENDER_PASSKEY="use your generated passkey"   #TOget this passkey we have to follow some steps
#go to email-settings-manageac-security-two step authentication-turn on it-next search by google-enter name smtp and create
#your paaskey is created
   


   #CREATE single email sender
def single_email_send(to_email:str,subject:str,body:str):
    msg=MIMEMultipart() #method usd to connect all
    msg['To']=to_email
    msg['Subject']=subject
    msg['From']=SENDER_EMAIL
    msg.attach(MIMEText(body,'plain'))

    #start server
    server=smtplib.SMTP(SMTP_SERVER,SMTP_PORT)
    server.starttls() #Create sequere connection
    server.login(SENDER_EMAIL,SENDER_PASSKEY) #LOGIN WITh email anspassword
    server.sendmail(SENDER_EMAIL,to_email,msg.as_string()) #email send
    server.quit()

    print(f"succesfully email sent to {to_email}")
