import subprocess


def detection(object):
    if object == True:
        subprocess.call(['python', 'alert.py'])
    print( 'Need help')


if __name__ == '__main__':
    detection()
