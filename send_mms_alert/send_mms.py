import os
from twilio.rest import Client
import pyimgur


class SendText:
    CLIENT_ID = "a779a15bf8a2b82"
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    url = None

    @classmethod
    def image_upload(cls, PATH):
        img = pyimgur.Imgur(cls.CLIENT_ID)
        uploaded_image = img.upload_image(PATH, title="FVA Detection")
        print(uploaded_image.title)
        print(uploaded_image.link)
        print(uploaded_image.size)
        print(uploaded_image.type)
        setattr(SendText, 'url', uploaded_image.link)

    @classmethod
    def mms(cls, NUM , MSG):
        numbers_to_message = [NUM]
        for number in numbers_to_message:
            message = cls.client.messages.create(
                body= MSG,
                media_url=[cls.url],
                from_='+12517664504',
                to=NUM
            )
        print(message.status)
        print(message.account_sid)
        print(message.sid)
        print(message.body)
        