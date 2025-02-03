import numpy as np
import matplotlib.pyplot as plt
import cv2

# to select coordinates

# def sample(EVENT,x,y,a,b):
#     if EVENT==cv2.EVENT_LBUTTONDOWN:
#         text_image=str(x)+" "+str(y)
#         font_style=cv2.FONT_HERSHEY_PLAIN
#         cv2.putText(ronaldo_image,text_image,(x,y),font_style,1,(56,78,200),2)
#         cv2.imshow('ronaldo',ronaldo_image)


ronaldo_image=cv2.imread('images/img.png')
cv2.imshow('ronaldo',ronaldo_image)

roi_pixels=ronaldo_image[459:565, 311:428]
ronaldo_image[50:156,50:167]=roi_pixels
cv2.imshow('reimage',ronaldo_image)

# cv2.setMouseCallback('ronaldo',sample)

cv2.waitKey()
cv2.destroyAllWindows()