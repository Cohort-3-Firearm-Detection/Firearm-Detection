from flask import Flask
from flask_mail import Mail, Message

class SendEmail:
    app = Flask(__name__)
    mail = Mail(app)
    app.config['MAIL_SERVER']='smtp.office365.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USERNAME'] = 'fva_alert@outlook.com'
    app.config['MAIL_PASSWORD'] = 'FVA@22ml'
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_ASCII_ATTACHMENTS'] = False


    @app.route("/")
    def email(cls, recipients):
        msg = Message(
				    'Hello',
				    sender ='fva_alert@outlook.com',
				    recipients = [recipients] 
			    )
        msg.body = 'Hello a threat was detected with a confidence level of. See attached image. Flask message sent from Flask-Mail. Do not respond to this message.'
        with cls.app.open_resource('../Tensorflow/workspace/images/guntest1.png') as detect:
            msg.attach('detection.png', 'image/png', detect.read())
        cls.mail.send(msg)
        return('Sent')
    if __name__ == '__main__':
        app.run(debug = True)


# class SendEmail:
    
#     @classmethod
#     def email(self):
#         app = Flask(__name__)
#         mail = Mail(app)
#         app.config['MAIL_SERVER']='smtp.office365.com'
#         app.config['MAIL_PORT'] = 587
#         app.config['MAIL_USERNAME'] = 'abcovarrubio@outlook.com'
#         app.config['MAIL_PASSWORD'] = 'OUTLOOK!T4nC4yd'
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