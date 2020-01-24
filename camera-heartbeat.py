import cv2
import time
import math
import RPi.GPIO as GPIO

currently_processing = False #ignore button input during processing time
pin = 26 #digital input pin for button
heartbeat = 10 #wait this many seconds before affirming its existence
existence_affirmed = False
GPIO.setmode(GPIO.BCM)#sets the module to use GPIO numbers rather than port numbers
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)#GPIO 6, used as input, defaults to 0(off)

print('Waiting on input...')
while True:
    if not currently_processing and not existence_affirmed:
        if math.floor(time.time())%heartbeat == 0:
            print('still alive (system time:%s)'%time.strftime('%H:%M:%S'))
            existence_affirmed = True
    if not currently_processing and existence_affirmed:
        if math.floor(time.time())%heartbeat == 1:
            existence_affirmed = False
    if GPIO.input(pin) and not currently_processing:
        print('Received input from pin %s'%pin)
        currently_processing = True
        for i in range(0,7,2):
            image_no = math.floor(i/2)+1
            print('processing image %s'%(image_no))
            webcam = cv2.VideoCapture(i)
            check, frame = webcam.read()
            str_time = time.strftime('%m-%d-%y-%H%M%S.jpg')
            cv2.imwrite(filename=str_time, img=frame)
            print('successfully wrote image %s as %s'%(image_no,str_time))
            webcam.release()
        currently_processing = False
        print('Waiting on input...')

