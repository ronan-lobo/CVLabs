import numpy as np
import cv2
import matplotlib.pyplot as plt

im1 = cv2.imread('Resources\\image (19).jpg', 0)

plt.subplot(2, 3, 1)
plt.imshow(cv2.cvtColor(im1, cv2.COLOR_BGR2RGB))
plt.subplot(2, 3, 4)
hist = np.histogram(np.array(im1).ravel(), bins=256, range=[0, 256])
x, y = hist[1][:-1], hist[0]
y = y / np.sum(y)
y = np.cumsum(y)
plt.bar(x, y)

im2 = cv2.imread('Resources\\image (87).jpg', 0)

plt.subplot(2, 3, 2)
plt.imshow(cv2.cvtColor(im2, cv2.COLOR_BGR2RGB))
plt.subplot(2, 3, 5)
hist = np.histogram(np.array(im2).ravel(), bins=256, range=[0, 256])
x, y = hist[1][:-1], hist[0]
y = y / np.sum(y)
y = np.cumsum(y)
plt.bar(x, y)


im3 = cv2.imread('Resources\\image (95).jpg', 0)

plt.subplot(2, 3, 3)
plt.imshow(cv2.cvtColor(im3, cv2.COLOR_BGR2RGB))
plt.subplot(2, 3, 6)
hist = np.histogram(np.array(im3).ravel(), bins=256, range=[0, 256])
x, y = hist[1][:-1], hist[0]
y = y / np.sum(y)
y = np.cumsum(y)
plt.bar(x, y)
plt.show()

