import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com', 587)

server.ehlo()

server.login('wex100.sec@gmail.com', 'Bunny7-Payable7-Material3-Clicker2')

msg = MIMEMultipart()
msg['From'] = 'WEX'
msg['To'] = 'fipas96656@hraifi.com'
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
server.sendmail('wex100.sec@gmail.com', 'fipas96656@hraifi.com', text)