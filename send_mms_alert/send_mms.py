import os
from twilio.rest import Client
from flask import send_from_directory
from flask import Flask

# app = Flask(__name__)
# UPLOAD_FOLDER = 'Firearm-Detection/results/'

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

numbers_to_message = ['+15022165263']
for number in numbers_to_message:
    message = client.messages.create(
        body='This is the ship that made the Kessel Run in fourteen parsecs.',
        media_url=['https://c1.staticflickr.com/3/2899/14341091933_1e92e62d12_b.jpg'],
        from_='+12517664504',
        to=number
    )



# @app.route('Firearm-Detection/results/detection.png', methods=['GET', 'POST'])
# def uploaded_file(filename):
#     return send_from_directory(UPLOAD_FOLDER,filename)

# if __name__ == "__main__":
#     app.run()


print(message.status)
print(message.account_sid)
print(message.sid)
print(message.body)
 
