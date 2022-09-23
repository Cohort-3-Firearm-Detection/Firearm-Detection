from send_mms_alert.send_mms import SendText
# # from send_email_alert.send_email import SendEmail
from Tensorflow.live_detect_app import *
from smtp_alert import SendEmail

PATH = "Tensorflow/workspace/images/detection.png"
MSG = "A detection has been made with a confidence level of {}. See the attached image for more information".format(Detection.conf_lev)


Detection.live_detect()
if Detection.conf_lev >= 0.7:
    print('Detection made with a confidence level of {}'.format(Detection.conf_lev))
    SendText.image_upload(PATH)
    SendText.mms(number = '+12146051373', MSG= MSG)
    
# SendEmail.email()
# 'jerewalker@teksystems.com', 'mdave@teksystems.com', 'jhagerman@teksystems.com', 'acovarrubio@teksystems.com', 'dchamness@teksystems.com'


from smtp_alert import SendEmail

PATH = "Tensorflow/workspace/images/detection.png"
MSG = 'this is a test'

SendEmail.send_email(PATH, MSG)