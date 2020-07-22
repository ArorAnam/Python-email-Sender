# Sending emails with attachments using Python

# libraries to be imported
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "arora.nam21@gmail.com"
toaddr = "naman.arora2060@gmail.com"

# MIMEMultipart
msg = MIMEMultipart()

# senders email address
msg['From'] = fromaddr

# receivers email address
msg['To'] = toaddr

# the subject of mail
msg['Subject'] = "PASSWORD RECOVERY"

# the body of the mail
body = "Your passcode is :: 123456"

# attaching the body with the msg
msg.attach(MIMEText(body, 'plain'))

# open the file to be sent
# rb is a flag for readonly
filename = "sample.txt"
attachment = open("attachment.txt", "rb")

# MIMEBase
attac = MIMEBase('application', 'octet-stream')

# To change the payload into encoded form
attac.set_payload((attachment).read())

# encode into base64
encoders.encode_base64(attac)

attac.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# attach the instance 'p' to instance 'msg'
msg.attach(attac)

# creates SMTP session
email = smtplib.SMTP('smtp.gmail.com', 587)

# TLS for security
email.starttls()

# authentication
password = input ("enter password :: ")
email.login(fromaddr, password)

# Converts the Multipart msg into a string
message = msg.as_string()

# sending the mail
email.sendmail(fromaddr, toaddr, message)

# terminating the session
# s.quit()
