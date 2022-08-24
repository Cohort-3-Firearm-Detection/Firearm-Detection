
import subprocess

#trigger set to send an email of .6 or higher, otherwise print no threat detected.
def detection(obj):
    if obj >= .6:
        subprocess.call(['python', 'send_email.py'])
    else: 
        print( 'No threat detected')


if __name__ == '__main__':
    detection()