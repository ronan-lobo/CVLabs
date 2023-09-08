import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Resources\\image (95).jpg')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_mean = np.array(gray_img)
r, c = img_mean.shape
mean = np.median(img_mean.ravel())
for i in range(r):
    for j in range(c):
        if gray_img[i, j] <= 35:
            img_mean[i, j] = mean

windowName = 'Gray Image'

cv2.imshow(windowName, img_mean)

ret, out_img = cv2.threshold(img_mean, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow('Otsu', out_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
