import os
from twilio.rest import Client
import pyimgur
from send_mms import SendText

SendText.image_upload(PATH = "../Tensorflow/workspace/images/guntest1.png")
SendText.mms(number = '')