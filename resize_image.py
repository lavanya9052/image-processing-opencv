import numpy as np
import cv2

image_data=cv2.imread('images/lena_color_512.tif',1)

print(f'original image shape:{image_data}')

#resize
resize_image=cv2.resize(image_data,(256,256))
print(f'resized image:{resize_image.shape}')


cv2.imshow('leno_original',image_data)
cv2.imshow('leno_resize_image',resize_image)
cv2.waitKey()
cv2.destroyAllWindows()
