import numpy as np
import matplotlib.pyplot as plt
import cv2

image=cv2.imread('images/dog.1.jpg')

fil_values=np.array([[0,1,0],[1,-4,1],[0,1,0]])

result=cv2.filter2D(image,-1,fil_values)

cv2.imshow('original_image',image)
cv2.imshow('kernal_outcome',result)

cv2.waitKey()
cv2.destroyAllWindows()