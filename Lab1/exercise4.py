import numpy as np
import cv2

img = np.ones((400, 400, 3), dtype=np.uint8)
img = 255 * img

img = cv2.rectangle(img, (100, 100), (300, 300), (255, 0, 0), 2)

cv2.imshow('rectangle', img)

cv2.waitKey(0)

cv2.destroyAllWindows()