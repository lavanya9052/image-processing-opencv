import numpy as np
import cv2

image_data=cv2.imread('images/lena_color_512.tif')

#line

#cv2.line(image_data,(200,180),(340,400),(0,255,0),2)

#arrowed line in at the end of second point arrow will come

#cv2.arrowedLine(image_data,(200,180),(340,400),(0,255,0),2)

#rectangle
#cv2.rectangle(image_data,(200,180),(340,400),(0,255,0),2)

#circle

cv2.circle(image_data,(250,250),15,(255,0,0),2)

cv2.imshow('leno_color',image_data)

cv2.waitKey()
cv2.destroyAllWindows()

