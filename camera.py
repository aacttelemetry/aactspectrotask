import cv2
import time
import math
'''
index = 0
arr = []
while index<5:
    cap = cv2.VideoCapture(index)
    if not cap.read()[0]:
        continue
    else:
        arr.append(index)
    cap.release()
    index += 1
'''
for i in range(0,7,2):
    image_no = math.floor(i/2)+1
    print('processing image %s'%(image_no))
    webcam = cv2.VideoCapture(i)
    check, frame = webcam.read()
    str_time = time.strftime('%m-%d-%y-%H%M%S.jpg')
    cv2.imwrite(filename=str_time, img=frame)
    print('successfully wrote image %s as %s'%(image_no,str_time))
    webcam.release()
