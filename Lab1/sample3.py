import cv2
import numpy as np

img = cv2.imread('C:\\Users\\OSLAB\\PycharmProjects\\pythonProject\\CVLab\\Lab1\\image1.jpg')

cv2.imshow('original image', img)
cv2.waitKey(0)

b, g, r = cv2.split(img)
zeros = np.zeros(b.shape, dtype=np.uint8)

b = cv2.merge((b, zeros, zeros))
g = cv2.merge((zeros, g, zeros))
r = cv2.merge((zeros, zeros, r))

cv2.imshow('blue channel', b)
cv2.waitKey(0)
cv2.imshow('green channel', g)
cv2.waitKey(0)
cv2.imshow('red channel', r)
cv2.waitKey(0)

cv2.destroyAllWindows()
