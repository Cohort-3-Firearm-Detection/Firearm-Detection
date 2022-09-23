from send_mms_alert.send_mms import SendText
from Tensorflow.live_detect_app import *
from send_email_alert.smtp_alert import SendEmail

PATH = "Tensorflow/workspace/images/detection.png"
MSG = "A detection has been made with a confidence level of {}. See the attached image for more information".format(Detection.conf_lev)
REPS = ['jerewalker@teksystems.com', 'jhagerman@teksystems.com', 'mdave@teksystems.com', 'acovarrubio@teksystems.com', 'dchamness@teksystems.com']
NUM = '+12146051373'

Detection.live_detect()
if Detection.conf_lev >= 0.7:
    print('Detection made with a confidence level of {}'.format(Detection.conf_lev))
    SendText.image_upload(PATH)
    SendText.mms(NUM, MSG)
    SendEmail.send_email(PATH, MSG, REPS)