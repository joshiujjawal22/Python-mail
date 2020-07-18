## Mail with attachment:

### AIM:
**To send mail with attachment to all the receivers without using GUI of ```gmail```**.

## Getting Started

### Requirements:
- Two factor authentication of sender's gmail account should be turned off.
- `Less Secure apps` setting should be enabled. 

### Libraries used:
- smtplib
- from email.mime.multipart import MIMEMultipart
- from email.mime.text import MIMEText
- from email.mime.base import MIMEBase
- from email import encoders

### Reference:
**SMTP Library** : [SMTP](https://docs.python.org/3/library/smtplib.html) 
<br>
**Less Secure apps** : [Less secure Apps](https://support.google.com/accounts/answer/6010255?hl=en)

### Issue Fixed:
[x] ``as_string()`` function started functioning properly.

**Note**:***No need to install any libraryu externally as it is already installed in python package.***
  