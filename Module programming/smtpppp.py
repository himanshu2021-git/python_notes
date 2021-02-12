import smtplib as mailer
from getpass import getpass 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase


#visit to that website | connection
#enable the security
#login
#send the email
#logout | break the connection

server = mailer.SMTP(
    #smtp host
    "smtp.gmail.com"
    #port as well these are mandatory and also enabling less secure apps in gmail
    587
    )
server.starttls()
server.ehlo() #optional
server.login(
    #username
    "himmupuroit1998@gmail.com"
    #password install getpass3 using pip
    getpass(prompt="please confirm your password")
    )
#sendemail
email = MIMEMultipart() #making genuine
email["From"]=""
email["To"] =""
email["Subject"]=""
body="dfdsjfdsjfcdsjc"
email.attach(MIMEText(body,"plain"))#never can attach pythonstring with email

#attaching a file

#open the file
attachment_file = open(
    #absolute path to the file
    "rogh.py"
    #mode(purpose)
    "rb"#readbinary
    )

#making file attachable
temp = MIMEBase('application','octet-stream')

#load the attachment
temp.set_payload((rogh.py).read()) #give in tuple format something kind of typecasting
encoders.encode_base64(temp)
#adding temp in emails
#pin with the email
temp.add_header("Content-Disposition","attachment;filename=himanshu")
email.attach(temp)


text_email =email.as_string()
#can use for loop for sending multiuser but the main thinf =g is use which is known as mass email
for x in emaails:
    server.sendmail(
        #from email
        "himmupurohit1998@gmail.com"
        #to email
        "himanshur1998@gmail.com"
        #body
        text_email
        )
server.quit()


#IMAP in python read it.......
