import smtplib
from email.mime.text import MIMEText

body = "This is a test email. How are you?"

msg = MIMEText(body)
msg["from"] = "101mehta101@gmail.com"
msg['to'] = "101mehta101@gmail.com"
msg['Subject'] = "hello"

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('101mehta101','eagleview123')

server.send_message(msg)
print("Mail sent")

server.quit()
