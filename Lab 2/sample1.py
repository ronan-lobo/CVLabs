import cv2
import numpy as np

img = cv2.imread('sample.png', 0)

cv2.imshow('input image', img)
cv2.waitKey(0)

c = 255 / (np.log(1 + np.max(img)))

log_transformed = c * np.log(1 + img)
log_transformed = np.array(log_transformed, dtype=np.uint8)

cv2.imshow('log transformed image', log_transformed)
cv2.waitKey(0)

cv2.destroyAllWindows()
