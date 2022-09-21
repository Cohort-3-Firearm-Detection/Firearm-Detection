# from send_mms_alert.send_mms import SendText
from send_email_alert.send_email import SendEmail

# PATH = "Tensorflow/workspace/images/guntest1.png"

# SendText.image_upload(PATH)
# SendText.mms(number = '+15022165263')

SendEmail.email(cls = SendEmail, recipients= 'acovarrubio@teksystems.com')
# SendEmail.recipients = 'jerewalker@teksystems.com', 'mdave@teksystems.com', 'jhagerman@teksystems.com', 'acovarrubio@teksystems.com', 'dchamness@teksystems.com'