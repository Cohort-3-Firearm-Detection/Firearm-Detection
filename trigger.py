import subprocess


def detection(object):
    if object == True:
        subprocess.call(['python', 'alert.py'])
    print( 'No object detected.')


if __name__ == '__main__':
    detection()
