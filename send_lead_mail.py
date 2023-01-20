import os
import smtplib
from email.message import EmailMessage
import email_content as mail_body

sender = os.environ["mail"]
password = os.environ["pass"]

def lead_magnet_sending(receiver_email):
    try:
        email_body = mail_body.content
        msg = EmailMessage()
        msg['Subject'] = 'Hi 👋 From Debmalya'
        msg['From'] = sender
        msg['To'] = receiver_email
        msg.set_content('This is a plain text email')

        msg.add_alternative(email_body, subtype='html')

        with open('documents/Essential Skills and Knowledge For Blockchain Mastery.pdf', 'rb') as content_file:
            content = content_file.read()
            msg.add_attachment(content, maintype='application', subtype='pdf', filename='Essential Skills and Knowledge For Blockchain Mastery.pdf')
        
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender, password)
            server.send_message(msg)
        return True
    except:
        return False