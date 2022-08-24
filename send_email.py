# importing libraries
from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app) # instantiate the mail class

# configuration of mail
# info needed for sender, each email host has different server and possibly different port. Current set up for outlook."
app.config['MAIL_SERVER']='smtp.office365.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = '*******************'
app.config['MAIL_PASSWORD'] = '******************'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_ASCII_ATTACHMENTS'] = False

mail = Mail(app)

# message object mapped to a particular URL ‘/’
@app.route("/")
def index():
    msg = Message(
				'Hello',
				sender ='*********************',
				recipients = ['*********************']
			)
    msg.body = 'Hello a threat was detected. See attached image. Flask message sent from Flask-Mail. Do not respond to this message.'

# attach image, needs to be in same location as app or include path    
    with app.open_resource('puppy.jpg') as pup:
        msg.attach('puppy.jpg', 'image/jpeg', pup.read())

# send email    
    mail.send(msg)
    
# proof app ran properly    
    return 'Sent'

if __name__ == '__main__':
    app.run(debug = True)
