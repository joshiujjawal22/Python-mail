import email,smtplib,ssl 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
   
SenderAdd = "ujjawal1291.cse18@chitkara.edu.in"
ReceiverAdd = ["joshiujjawal22@gmail.com","joshiujjawal22@rediffmail.com"]	
   
# instance of MIMEMultipart 
msg = MIMEMultipart() 
  
# storing the senders email address   
msg['From'] = SenderAdd 
  
# storing the receivers email address  
msg['To'] = ReceiverAdd 
  
# storing the subject  
msg['Subject'] = "Subject of the Mail"
  
# string to store the body of the mail 
body = "Write whatever you want to send"
  
# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain')) 
  
# open the file to be sent  
filename = "python_book.pdf"
attachment = open("Attachment/python_book.pdf", "rb") 
  
# instance of MIMEBase and named as p 
p = MIMEBase('application', 'octet-stream') 
  
# To change the payload into encoded form 
p.set_payload((attachment).read()) 
  
# encode into base64 
encoders.encode_base64(p) 
   
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
  
# attach the instance 'p' to instance 'msg' 
msg.attach(p) 

# To Convert the Multipart msg into a string 
text = msg.as_string()
  
# creates SMTP session 
server = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
server.starttls() 
  
# Authentication 
server.login(SenderAdd, "Joshi@2000")  
  
# sending the mail 
server.sendmail(SenderAdd, ReceiverAdd, text) 
  
# terminating the session 
server.quit() 