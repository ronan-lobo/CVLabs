import cv2
import numpy as np


def scale_image(img):
    img = (img - img.min()) / (img.max() - img.min()) * 255
    return img


image = cv2.imread('Resources/lena.png', 0)
cv2.imshow('Original Image', image)
image = np.array(image, np.float32)

image_x = cv2.Sobel(image, -1, 1, 0, ksize=3)
image_y = cv2.Sobel(image, -1, 0, 1, ksize=3)

grad_image = np.sqrt(image_x ** 2 + image_y ** 2)
sobel_unsharp = image + (image - scale_image(grad_image))
sobel_unsharp = np.array(scale_image(sobel_unsharp), np.uint8)

cv2.imshow('Sobel Sharpened Image', sobel_unsharp)
cv2.imwrite('Resources\\sobel_sharpening.jpg', sobel_unsharp)

laplacian_image = cv2.Laplacian(image, -1)
laplacian_unsharp = image + (image-laplacian_image)
laplacian_unsharp = scale_image(laplacian_unsharp)
laplacian_unsharp = np.array(laplacian_unsharp, np.uint8)

cv2.imshow('Laplacian Sharpened Image', laplacian_unsharp)
cv2.imwrite('Resources\\laplacian_sharpening.jpg', laplacian_unsharp)

cv2.waitKey(0)
cv2.destroyAllWindows()
