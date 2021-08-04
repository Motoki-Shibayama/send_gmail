import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr, formatdate
import json
import ssl

with open("secret.json") as f:
    secret = json.load(f)

FROM_ADDRESS = secret["SEND_FROM"]
MY_PASSWORD = secret["PASSWORD"]
TO_ADDRESS = secret["SEND_TO"]
BCC = secret["BCC"]
SUBJECT = secret["SUBJECT"]
body_text = secret["BODY"]

def create_message(from_addr, to_addr, bcc_addr, subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = from_addr
    msg["To"] = to_addr
    msg["Bcc"] = bcc_addr
    msg["Date"] = formatdate()
    return msg

def send(from_addr, to_addr, msg):
    smtpobj = smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=10)
    smtpobj.login(FROM_ADDRESS, MY_PASSWORD)
    smtpobj.sendmail(from_addr, to_addr, msg.as_string())
    smtpobj.close()

if __name__ == "__main__":
    body = list(body_text)
    for text in reversed(body):
        msg = create_message(FROM_ADDRESS, TO_ADDRESS, BCC, SUBJECT, text)
        send(FROM_ADDRESS, TO_ADDRESS, msg)
