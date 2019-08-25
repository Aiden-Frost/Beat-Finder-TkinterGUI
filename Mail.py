import smtplib
import random
otp = random.randint(1000,9999)
message = "Welcome to the communtiy of Music lovers.\nYou are just one step away.\nYour One Time Password is"+' '+':'+' '+str(otp)
email_user = 'beat.finder.music@gmail.com'
email_send = 'rahulraman1604@gmail.com'
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,'beat@123')
server.sendmail(email_user,email_send,message)
server.quit()
