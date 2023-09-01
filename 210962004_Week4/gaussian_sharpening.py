import cv2
import numpy as np

image = cv2.imread('Resources/lena.png', 0)
cv2.imshow('Original Image', image)
image = np.array(image)

gaussian = cv2.GaussianBlur(image, (5, 5), 0)
gaussian = np.array(gaussian)

unsharp_img = image + (image - gaussian)
cv2.imshow('Unsharp Masked Image', unsharp_img)
cv2.imwrite('Resources\\gaussian_sharpening.jpg', unsharp_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
