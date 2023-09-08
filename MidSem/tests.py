import cv2
import numpy as np
import matplotlib.pyplot as plt

def on_change(value):
    ret, mask = cv2.threshold(gray_img, value, 255, cv2.THRESH_BINARY)
    mask = np.array(mask)
    mask[y-75: y+75, x-75: x+75] = 0
    out_img = np.array(img)
    mask_coords = np.where(mask == 255)
    for i, j in zip(mask_coords[0], mask_coords[1]):
        out_img[i, j, :] = [255, 127, 0]
    cv2.imshow(windowName, out_img)


img = cv2.imread('Resources\\image (19).jpg')
gauss = cv2.GaussianBlur(img, (21, 21), 0)

minval, maxval, mincoord, maxcoord = cv2.minMaxLoc(cv2.cvtColor(gauss, cv2.COLOR_BGR2GRAY))
x, y = maxcoord

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

windowName = 'Thresholded Image'

cv2.imshow(windowName, img)
cv2.createTrackbar('slider', windowName, 0, 255, on_change)

cv2.waitKey(0)
cv2.destroyAllWindows()
