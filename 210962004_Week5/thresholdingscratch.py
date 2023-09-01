import cv2
import numpy as np
import matplotlib.pyplot as plt


def binary_thresholding(image, val):
    image = np.array(image)
    out_img = np.zeros(image.shape)
    r, c = image.shape
    for i in range(r):
        for j in range(c):
            if image[i, j] >= val:
                out_img[i, j] = 255
    return out_img


def inv_binary_thresholding(image, val):
    out_img = binary_thresholding(image, val)
    out_img = 255 - out_img
    return out_img


def truncated_thresholding(image, val):
    out_img = np.copy(image)
    r, c = image.shape
    for i in range(r):
        for j in range(c):
            if image[i, j] >= val:
                out_img[i, j] = val
    return out_img


def thresh_to_zero(image, val):
    out_img = np.copy(image)
    r, c = image.shape
    for i in range(r):
        for j in range(c):
            if image[i, j] < val:
                out_img[i, j] = 0
    return out_img

def thresh_to_zero_inv(image, val):
    out_img = np.copy(image)
    r, c = image.shape
    for i in range(r):
        for j in range(c):
            if image[i, j] >= val:
                out_img[i, j] = 0
    return out_img


image = cv2.imread('Resources/eyesketch.jpg', 0)

thresholds = [('Binary Thresholding', binary_thresholding),
              ('Binary Inverted Thresholding', inv_binary_thresholding),
              ('Truncated Thresholding', truncated_thresholding),
              ('Set to 0 Thresholding', thresh_to_zero),
              ('Set to 0 inverted Thresholding', thresh_to_zero_inv)]

plt.figure(figsize=(10, 10))

plt.subplot(2, 3, 1)
plt.imshow(image, cmap='gray')
plt.xticks([])
plt.yticks([])
plt.title('Original Image')

for i, (name, threshold) in enumerate(thresholds):
    threshold_image = threshold(image, 127)
    plt.subplot(2, 3, i + 2)
    plt.imshow(threshold_image, cmap='gray')
    plt.xticks([])
    plt.yticks([])
    plt.title(name)

plt.tight_layout()
plt.savefig('Resources/thresholdingscratch.png')
plt.show()
