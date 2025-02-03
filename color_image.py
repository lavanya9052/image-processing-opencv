import numpy as np
import cv2

#read the data from the black and white image
#in opencv for black and white image use ->0

image_color=cv2.imread('images/lena_gray_512.tif', 1)

print(image_color)  #image pixels are present here

print(image_color.shape) #shape of image that is width and height

#now i am going to give those pixel values to imshow function in opencv
cv2.imshow('leno_black_image', image_color)

#to keep wait the pop up ->outcome
cv2.waitKey()

# closing the window from user end
cv2.destroyAllWindows()