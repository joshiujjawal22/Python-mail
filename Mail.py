import smtplib

FROMADDR = "SenderMail"
LOGIN    = FROMADDR
PASSWORD = "pass"
TOADDRS  = ["receivermail"]
SUBJECT  = "Test"

msg = "Whatever i wrote should be send"

server = smtplib.SMTP('smtp.gmail.com:587')
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(LOGIN, PASSWORD)
server.sendmail(FROMADDR, TOADDRS, msg)
server.quit()