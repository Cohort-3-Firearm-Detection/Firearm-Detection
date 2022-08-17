import subprocess


def detection(object):
    if object == True:
        subprocess.call(['python', 'alert.py'])
    else:
        subprocess.call(['python', 'test.py'])
    return 'Need help'


if __name__ == '__main__':
    detection()
