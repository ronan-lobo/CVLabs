import cv2
import numpy as np

image = cv2.imread('Resources/lena.png', 0)
cv2.imshow('Original', image)
image = np.array(image, np.float32)

image_x = cv2.Sobel(image, -1, 1, 0, ksize=5)
image_y = cv2.Sobel(image, -1, 0, 1, ksize=5)

grad_image = (image_x ** 2 + image_y ** 2) ** 0.5
grad_image = ((grad_image - grad_image.min()) / (grad_image.max() - grad_image.min())) * 255
grad_image = np.array(grad_image, np.uint8)

cv2.imshow('Image Gradient', grad_image)
cv2.imwrite('Resources\\image_gradient.jpg', grad_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
