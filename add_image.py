'''
In this file we are going to add 2 images with equal weightage(50% 1st image and 50% to second image
'''

import numpy as np
import matplotlib.pyplot as plt
import cv2

lena_image=cv2.imread('images/lena_color_512.tif')
mandir_image=cv2.imread('images/mandril_color.tif')

#add ->both images shape should be same

#new_image=cv2.add(lena_image,mandir_image)

#addweighted -> we can give the priority for image what we need

new_image=cv2.addWeighted(lena_image,0.3,mandir_image,0.7,1)

cv2.imshow('lena image',lena_image)
cv2.imshow('mandir image',mandir_image)

cv2.imshow('added image',new_image)

cv2.waitKey()
cv2.destroyAllWindows()
