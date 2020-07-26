### Generate and e-mail certificate:

### AIM:
***To generate and send certificate in their corresponding mail without using GUI of ```gmail```***.

## Getting Started

### Requirements:
- Two factor authentication of sender's gmail account should be turned off.
- `Less Secure apps` setting should be enabled. 

### Libraries used:

**For image processing**
- PILLOW

**For e-mail**
- smtplib
- from email.mime.multipart import MIMEMultipart
- from email.mime.text import MIMEText
- from email.mime.base import MIMEBase
- from email import encoders

### Reference:

**Pillow** : [Pillow](https://pillow.readthedocs.io/en/stable/installation.html)
<br>
**SMTP Library** : [SMTP](https://docs.python.org/3/library/smtplib.html) 
<br>
**Less Secure apps** : [Less secure Apps](https://support.google.com/accounts/answer/6010255?hl=en)

> **Note**:***No need to install any e-mail library externally as it is already installed in python package.***
