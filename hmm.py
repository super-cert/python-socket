import smtplib
 
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
print(smtpserver.ehlo())
smtpserver.starttls()
print(smtpserver.ehlo())
print(smtpserver.login("kjh07df@gmail.com", "xkdtn6@@"))
