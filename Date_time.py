'''
to display  current date and time on top of image based on cordinates
'''

import numpy as np
import matplotlib.pyplot as plt
import cv2
import time
import datetime

lena_image=cv2.imread('images/lena_color_512.tif')

# print(datetime.datetime.now())  it will print on normal

# to display date time  on top of image  based on cordinates

d_t=datetime.datetime.now()
text_image=str(d_t)
font_style=cv2.FONT_HERSHEY_PLAIN
cv2.putText(lena_image,text_image,(70,70),font_style,1,(0,255,0),2)



cv2.imshow('lena image',lena_image)

cv2.waitKey()
cv2.destroyAllWindows()
