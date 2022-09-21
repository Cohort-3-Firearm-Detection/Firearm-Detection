import os
from twilio.rest import Client
from flask import send_from_directory
from flask import Flask
import pyimgur



class SendText:
    CLIENT_ID = "a779a15bf8a2b82"
    # PATH = "../Tensorflow/workspace/images/guntest1.png"
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    @classmethod
    def image_upload(cls, PATH):
        img = pyimgur.Imgur(cls.CLIENT_ID)
        uploaded_image = img.upload_image(PATH, title="Uploaded with PyImgur")
        print(uploaded_image.title)
        print(uploaded_image.link)
        print(uploaded_image.size)
        print(uploaded_image.type)

    @classmethod
    def mms(cls, number):
        numbers_to_message = []
        numbers_to_message = numbers_to_message.append(number)
        for number in numbers_to_message:
            message = cls.client.messages.create(
                body='A detection has made, see attached image!',
                media_url=[cls.uploaded_image.link],
                from_='+12517664504',
                to=number
            )
        print(message.status)
        print(message.account_sid)
        print(message.sid)
        print(message.body)


# CLIENT_ID = "a779a15bf8a2b82"
# PATH = "../Tensorflow/workspace/images/detection.png"

# im = pyimgur.Imgur(CLIENT_ID)
# uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur")
# # print(uploaded_image.title)
# # print(uploaded_image.link)
# # print(uploaded_image.size)
# # print(uploaded_image.type)

# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']
# client = Client(account_sid, auth_token)

# numbers_to_message = []
# for number in numbers_to_message:
#     message = client.messages.create(
#         body='A detection has made, see attached image!',
#         media_url=[uploaded_image.link],
#         from_='+12517664504',
#         to=number
#     )

# print(message.status)
# print(message.account_sid)
# print(message.sid)
# print(message.body)


# send_email.twilio()