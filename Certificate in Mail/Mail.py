# Library used to send mail to any Internet machine with an SMTP
import email,smtplib,ssl 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders

# Library used for image processing
from PIL import Image, ImageDraw, ImageFont 

# Login and Sender Information
FROMADDR = "ujjawal1291.cse18@chitkara.edu.in" #Sender Mail
PASSWORD = input("Enter Password")	# Write password of your mail
TOADDRS  = ["joshiujjawal22@gmail.com","joshiujjawal22@rediffmail.com"]	# Write receiver mail in list

# To login into the server
server = smtplib.SMTP('smtp.gmail.com:587')
server.set_debuglevel(1)
server.ehlo()	# Identify yourself to an ESMTP server using EHLO
server.starttls()	# To upgarde insecure connection to sceure connection
server.login(FROMADDR, PASSWORD)

# List of names to be used in certificates
names = ['Ankur', 
		 'Akshit'] 

# Font address
font_path = "C:/Windows/Fonts/AdobeArabic-Bold.otf"
       
# Certificate location
certificate = "template/Certificate.png" 

# To send mail and generate certificate
for i in range(len(TOADDRS)): 
          
    # Position of text
    text_vert_position = 900 

    # opens the image 
    img = Image.open(certificate, mode ='r') 
      
    # gets the image width 
    image_width = img.width  

    draw = ImageDraw.Draw(img) 

    font = ImageFont.truetype( 
        font_path, 
        200 
    ) 

    # To get the text Width or Height
    text_width, _ = draw.textsize(names[i], font = font)

    draw.text( 
        (   
            # To center the image
            (image_width - text_width) / 2 , 
            text_vert_position 
        ), 
        names[i], 
        fill=150,
        font = font,
          ) 

     # Saves the image in png format 
    img.save("GeneratedStuff/{}.png".format(names[i]))

    # instance of MIMEMultipart 
    msg=MIMEMultipart()

	# storing the senders email address   
    msg['From']=FROMADDR 
	  
	# storing the receivers email address  
	# Use join method if there is multiple people else directly ReceiverAdd
    msg['To'] = TOADDRS[i]
	  
	# storing the subject  
    msg['Subject'] = "Subject of the Mail"

	# Body of the mail
    body = "Certificates" 

	# attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 
	  
	# open the file to be sent  
    filename = "{}.png".format(names[i])
    attachment = open("GeneratedStuff/{}.png".format(names[i]), "rb") 
	  
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


    server.sendmail(FROMADDR, TOADDRS[i], text)

server.quit()