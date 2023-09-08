import numpy as np
import cv2
import matplotlib.pyplot as plt

im = cv2.imread('Resources\\image (19).jpg')
gauss = cv2.GaussianBlur(im, (21, 21), 0)

minval, maxval, mincoord, maxcoord = cv2.minMaxLoc(cv2.cvtColor(gauss, cv2.COLOR_BGR2GRAY))

gray_img = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

windowName = 'Thresholded Image'

hist = np.histogram(np.array(im).ravel(), bins=256, range=[0, 256])
x, y = hist[1][:-1], hist[0]
y = y / np.sum(y)
y = np.cumsum(y)

vals = np.where(y > 0.8)
value = vals[0][0]

ret, mask = cv2.threshold(gray_img, value, 255, cv2.THRESH_BINARY)
mask = np.array(mask)
x, y = maxcoord
mask[y-75: y+75, x-75: x+75] = 0
out_img = np.array(im)
mask_coords = np.where(mask == 255)
for i, j in zip(mask_coords[0], mask_coords[1]):
    out_img[i, j, :] = [255, 127, 0]
cv2.imshow(windowName, out_img)

cv2.waitKey(0)
cv2.destroyAllWindows()


