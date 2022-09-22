#### SendGrid Email###
import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content, Attachment, FileContent, FileType, FileName, Disposition, HtmlContent
import base64

class SendEmail:
    @classmethod
    def email(self):
        sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
        from_email = Email("fva_alert@outlook.com")  # Change to your verified sender
        to_email = [To('jerewalker@teksystems.com'), To('acovarrubio@teksystems.com')]  # Change to your recipient
        subject = "Detection Found"
         
        content = Content("text/plain", "A detection has been made. See image.")
        html_content = HtmlContent('<html><body><img class "fit-picture" src="../Tensorflow/workspace/images/guntest1.png"/></body></html>')
        
        mail = Mail(from_email, to_email, subject, content, html_content)

        # Get a JSON-ready representation of the Mail object
        mail_json = mail.get()

        # Send an HTTP POST request to /mail/send
        response = sg.client.mail.send.post(request_body=mail_json)
        print(response.status_code)
        print(response.headers)
































# from flask import Flask
# from flask_mail import Mail, Message



# app = Flask(__name__)
# app.config.update(
#     DEBUG = True,
#     MAIL_SERVER='smtp.office365.com',
#     MAIL_PORT = 587,
#     MAIL_USERNAME = 'abcovarrubio@outlook.com',
#     MAIL_PASSWORD = 'OUTLOOK!T4nC4yd',
#     MAIL_USE_TLS = True,
#     MAIL_USE_SSL = False,
#     MAIL_ASCII_ATTACHMENTS = False
#     )
# mail = Mail(app)


# ######## Live stuff ############
# @app.route('/')
# def email(recipients):
#     try:
#         msg = Message('Hello',
# 			sender ='abcovarrubio@outlook.com',
# 			recipients = [recipients] )
#         msg.body = 'Hello a threat was detected with a confidence level of. See attached image. Flask message sent from Flask-Mail. Do not respond to this message.'
#         # with cls.app.open_resource('../Tensorflow/workspace/images/guntest1.png') as detect:
#         #     msg.attach('detection.png', 'image/png', detect.read())
#         mail.send(msg)
#         return "Sent"
    
#     except Exception as e:
#         return str(e)











# class SendEmail:
#     @classmethod
#     @app.route("/")
#         def email(cls, recipients):

    
#         msg = Message(
# 		    	'Hello',
# 			        sender ='abcovarrubio@outlook.com',
# 				    recipients = [recipients] 
# 			     )
#         msg.body = 'Hello a threat was detected with a confidence level of. See attached image. Flask message sent from Flask-Mail. Do not respond to this message.'
#         # with cls.app.open_resource('../Tensorflow/workspace/images/guntest1.png') as detect:
#         #     msg.attach('detection.png', 'image/png', detect.read())
#         mail.send(msg)
#         return "Sent"




# class SendEmail:
    
#     @classmethod
#     def email(self):
#         app = Flask(__name__)
#         mail = Mail(app)
#         app.config['MAIL_SERVER']='smtp.office365.com'
#         app.config['MAIL_PORT'] = 587
#         app.config['MAIL_USERNAME'] = 'fva_alert@outlook.com'
#         app.config['MAIL_PASSWORD'] = 'FVA@22ml'
#         app.config['MAIL_USE_TLS'] = True
#         app.config['MAIL_USE_SSL'] = False
#         app.config['MAIL_ASCII_ATTACHMENTS'] = False


#         @app.route("/")
#         def index():
#             recipients = ['acovarrubio@teksystems.com']
#             # recipients.append(recipient)
#             msg = Message(
#                     'Hello',
#                     sender ='fva_alert@outlook.com',
#                     recipients = recipients 
#                 )
#             msg.body = 'Hello a threat was detected with a confidence level of. See attached image. Flask message sent from Flask-Mail. Do not respond to this message.'

#       #attach image, needs to be in same location as app or include path    
#             with app.open_resource('../Tensorflow/workspace/images/guntest1.png') as detect:
#                 msg.attach('Detection.png', 'image/png', detect.read())

#     # send email    
#             mail.send(msg)
        
#     # proof app ran properly    
#             return('Sent')

#         if __name__ == '__main__':
#             app.run(debug = True)