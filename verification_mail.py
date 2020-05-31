import smtplib

s = smtplib.SMTP("smtp.gmail.com" , 587)

s.starttls()

s.login("kanishkavyas74@gmail.com","password")

message = "your model has achieved desired accuracy"

s.sendmail("kanishkavyas74@gmail.com","kanishkavyas74@gmail.com" , message)

s.quit()
