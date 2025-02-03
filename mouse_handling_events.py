'''
In this whevever we click those x and y cordinates will be displayes with same image
'''

import numpy as np
import matplotlib.pyplot as plt
import cv2



def sample(EVENT,x,y,a,b):
    if EVENT==cv2.EVENT_LBUTTONDOWN:
        #print(x,y) wherever we click that x and y cordinates will be shown
        text_image=str(x)+" "+str(y)
        font_style=cv2.FONT_HERSHEY_PLAIN
        cv2.putText(lena_image,text_image,(x,y),font_style,1,(255,0,0),2)
        cv2.imshow('lena',lena_image)


lena_image=cv2.imread('images/lena_color_512.tif')

cv2.imshow('lena',lena_image)

cv2.setMouseCallback('lena',sample)

cv2.waitKey()
cv2.destroyAllWindows()