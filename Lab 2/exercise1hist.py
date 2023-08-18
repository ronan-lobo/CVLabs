import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('sampleboy.jpg', 0)

img_eq = cv2.equalizeHist(img)

hist_orig = cv2.calcHist([img], [0], None, [256], [0, 255])
hist_eq = cv2.calcHist([img_eq], [0], None, [256], [0, 255])

fig, ax = plt.subplots(2, 2, figsize=(6, 6))

ax[0, 0].imshow(img, cmap='gray')
ax[0, 0].set_title('Original Image')
ax[0, 0].set_xticks([])
ax[0, 0].set_yticks([])
ax[0, 1].plot(hist_orig, color='black')
ax[0, 1].set_title('Histogram(Original)')
ax[0, 1].set_xlim([0, 255])

ax[1, 0].imshow(img_eq, cmap='gray')
ax[1, 0].set_title('Histogram Equalized Image')
ax[1, 0].set_xticks([])
ax[1, 0].set_yticks([])
ax[1, 1].plot(hist_eq, color='black')
ax[1, 1].set_title('Histogram(Equalized)')
ax[1, 1].set_xlim([0, 255])

plt.tight_layout()
plt.show()
