import smtplib	# Library used to send mail to any Internet machine with an SMTP
from PIL import Image, ImageDraw, ImageFont  # Library used for image processing

FROMADDR = "SenderMail" #Sender Mail
LOGIN    = FROMADDR 
PASSWORD = "pass"	# Write password of your mail
TOADDRS  = ["receivermail"]	# Write receiver mail in list
SUBJECT  = "Test"

msg = "Whatever i wrote should be send" # Message you want to send

server = smtplib.SMTP('smtp.gmail.com:587')
server.set_debuglevel(1)
server.ehlo()	# Identify yourself to an ESMTP server using EHLO
server.starttls()	# To upgarde insecure connection to sceure connection
server.login(LOGIN, PASSWORD)	# To login 
server.sendmail(FROMADDR, TOADDRS, msg)
server.quit()