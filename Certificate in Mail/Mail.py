# Library used to send mail to any Internet machine with an SMTP
import email,smtplib,ssl 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders

# Library used for image processing
from PIL import Image, ImageDraw, ImageFont  

FROMADDR = "SenderMail" #Sender Mail
LOGIN    = FROMADDR 
PASSWORD = "pass"	# Write password of your mail
TOADDRS  = ["receivermail"]	# Write receiver mail in list
# List of names to be used in certificates
NAMES = ['Ankur', 'Akshit' ] 
# Font for name
FONT = "C:/Windows/Fonts/AdobeArabic-Bold.otf"

# instance of MIMEMultipart 
msg = MIMEMultipart() 

# storing the senders email address   
msg['From'] = FROMADDR 
  
# storing the receivers email address  
# Use join method if there is multiple people else directly ReceiverAdd
msg['To'] = ",".join(TOADDRS) 
  
# storing the subject  
msg['Subject'] = "Subject of the Mail"

# Body of the mail
body = "Certificates" 

server = smtplib.SMTP('smtp.gmail.com:587')
server.set_debuglevel(1)
server.ehlo()	# Identify yourself to an ESMTP server using EHLO
server.starttls()	# To upgarde insecure connection to sceure connection
server.login(LOGIN, PASSWORD)	# To login 
server.sendmail(FROMADDR, TOADDRS, msg)
server.quit()