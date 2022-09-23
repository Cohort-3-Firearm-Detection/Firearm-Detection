import os 
import smtplib
import imghdr 
from email.message import EmailMessage

class SendEmail:
    EMAIL_ADDRESS='fva_alert@outlook.com'
    EMAIL_PASSWORD='FVA@22ml'

    @classmethod
    def send_email(cls, PATH, MSG, REPS):
        msg = EmailMessage()
        msg['Subject'] = 'FVA Detection'
        msg['From'] = cls.EMAIL_ADDRESS
        msg['To'] = REPS
        msg.set_content(MSG)    

        with open(PATH, 'rb') as f:
            file_data = f.read()
            file_type = imghdr.what(f.name)
            file_name = f.name

        msg.add_attachment(file_data, maintype = 'image', subtype = file_type, filename = file_name)

        with smtplib.SMTP('smtp.office365.com', 587) as smtp:
            smtp.starttls()
            smtp.login(cls.EMAIL_ADDRESS, cls.EMAIL_PASSWORD)
            smtp.send_message(msg)