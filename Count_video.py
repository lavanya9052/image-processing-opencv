import numpy as np
import matplotlib.pyplot as plt
import cv2


from Date_time import font_style

video=cv2.VideoCapture('images/sample_video.mp4')
count=0
while True:
    status,pixels=video.read()
    if status==True:
        count=count+1
        text=str(count)
        font_style=cv2.FONT_HERSHEY_PLAIN
        cv2.putText(pixels,text,(50,50),font_style,1,(255,0,0),2)
        cv2.imshow('Frames',pixels)
        if cv2.waitKey(25)==ord('l'):
            break
    else:
        break
print(f'Number of frames in the video:{count}')
video.release()
cv2.destroyAllWindows()