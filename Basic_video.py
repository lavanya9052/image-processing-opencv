import numpy as np
import matplotlib.pyplot as plt
import cv2

video=cv2.VideoCapture('images/sample_video.mp4')
count=0
while True:
    status,pixels=video.read()
    if status==True:
        count=count+1
        cv2.imshow('video',pixels)
        if cv2.waitKey(20)==ord('l'):
            break
    else:
        break

print(f'how many frames are present in video:{count}')
video.release()
cv2.destroyAllWindows()

