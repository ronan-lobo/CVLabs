import cv2
import numpy as np

image = cv2.imread('Resources/lena.png')
cv2.imshow('Original Image', image)

gaussian = cv2.GaussianBlur(image, (7, 7), 0)
cv2.imshow('Gaussian Blurring', gaussian)

median = cv2.medianBlur(image, 5)
cv2.imshow('Median Blurring', median)

bilateral = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow('Bilateral Blurring', bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()
