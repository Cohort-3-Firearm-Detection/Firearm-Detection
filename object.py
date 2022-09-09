from trigger import detection
from Tensorflow.live_detect_app import obj


print ("Gun detected at confidence level:", obj)


detection(obj)