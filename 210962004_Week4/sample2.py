import sys
import cv2
import numpy as np

image = cv2.imread('Resources/lena.png')

if image is None:
    print('Could not read image')
    sys.exit(1)

cv2.imshow('Original', image)

kernel1 = np.array([[0, 0, 0],
                    [0, 1, 0],
                    [0, 0, 0]])

identity = cv2.filter2D(image, -1, kernel1)
cv2.imshow('Identity', identity)
cv2.imwrite('Resources\\sample2_identity.jpg', identity)

kernel2 = np.ones((5, 5), np.float32) / 25

box_blur = cv2.filter2D(image, -1, kernel2)
cv2.imshow('Box Blur', box_blur)
cv2.imwrite('Resources\\sample2_box_blur.jpg', box_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
