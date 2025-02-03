import numpy as np
import matplotlib.pyplot as plt
import cv2

#read the data using matplotlib ->show the data using opencv

image_data=plt.imread('images/lena_color_512.tif') # read the image using matplotlib

#plt ->will read data in the form of RGB
#opencv ->will read the data in the form of BGR
# For that in opencv we reverse the read image data

cv2.imshow('lena_image',image_data[:,:,::-1])
cv2.waitKey()
cv2.destroyAllWindows()