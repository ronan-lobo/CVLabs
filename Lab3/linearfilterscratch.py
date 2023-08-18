import cv2
import numpy as np


def convolve(image, kernel):
    k_h, k_w = kernel.shape
    i_h, i_w = image.shape

    k_ch, k_cw = k_h // 2, k_w // 2

    new_image = np.zeros_like(image)

    padded_img = np.zeros((i_h + k_ch * 2, i_w + k_cw * 2))
    padded_img[k_ch: -k_ch, k_cw: -k_cw] = image

    for i in range(i_h):
        for j in range(i_w):
            subimage = padded_img[i: i+k_h, j: j+k_w]

            new_image[i, j] = np.sum(np.multiply(subimage, kernel))

    return new_image


img = cv2.imread('sample.jpg', 0)
img = np.array(img)

kernel = np.ones((5, 5)) / 25.0

new_img = convolve(img, kernel)

cv2.imshow('original image', img)
cv2.imshow('filtered image', new_img)

cv2.imwrite('blur_sample.jpg', new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
