from send_mms_alert.send_mms import SendText
from Tensorflow.live_detect_app import *
from send_email_alert.smtp_alert import SendEmail

PATH = "Tensorflow/workspace/images/detection.png"
REPS = [ 'jhagerman@teksystems.com','acovarrubio@teksystems.com','jerewalker@teksystems.com','mdave@teksystems.com','dchamness@teksystems.com']
NUM = '+15022165263'

Detection.live_detect()
if Detection.conf_lev >= 0.7:
    conf_round = '{:.2f}'.format(Detection.conf_lev)

    MSG = "A detection has been made with a confidence level of {}. See the attached image for more information".format(conf_round)
    print('Detection made with a confidence level of {}'.format(conf_round))
    SendText.image_upload(PATH)
    SendText.mms(NUM, MSG)
    SendEmail.send_email(PATH, MSG, REPS) 