import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com', 587)

server.ehlo()

server.login('mail@gmail.com', 'password')

msg = MIMEMultipart()
msg['From'] = 'WEX'
msg['To'] = 'mail@gmail.com'
msg['Subject'] = 'Just A Test'

with open('message.txt') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'image.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('mail@gmail.com', 'mail@gmail.com', text)