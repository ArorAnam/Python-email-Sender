# Sending emails without attachments using python
# importing the required library library
import smtplib

# creates SMTP session
email = smtplib.SMTP('smtp.gmail.com', 587)

# TLS for security
email.starttls()

# authentication
# compiler gives an error for wrong credential.
email.login("arora.nam21@gmail.com", "psswd")

# message to be sent
message = "Your Passcode is :: 123456"

# sending the mail
email.sendmail("arora.nam21@gmail.com", "naman.arora2060@gmail.com", message)

# terminating the session
email.quit()
