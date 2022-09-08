import os
import subprocess


#trigger set to send an email of .6 or higher, otherwise print no threat detected.
def detection(obj):
    if obj >.75:
        print( 'MAJOR TROUBLE! SEND TEXT MESSAGE!')
        subprocess.call(['python', 'send_mms_alert/send_mms.py'])
    if obj >= .6:
         print('Sending email')
         subprocess.call(['python', 'send_email_alert/send_email.py'])


if __name__ == '__main__':
    detection()