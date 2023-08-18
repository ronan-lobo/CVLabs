import cv2
import numpy as np

img = cv2.imread('sample.png', 0)

cv2.imshow('input image', img)
cv2.waitKey(0)

for gamma in [0.1, 0.5, 1.2, 2.2]:
    gamma_corrected = np.array(255 * (img / 255) ** gamma, dtype=np.uint8)
    cv2.imshow(f'gamma transformed - {gamma}', gamma_corrected)
    cv2.waitKey(0)

cv2.destroyAllWindows()
