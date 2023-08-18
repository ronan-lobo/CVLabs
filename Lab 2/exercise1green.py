import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('sample1.jpg')

b, g, r = cv2.split(img)

g_eq = cv2.equalizeHist(g)

hist_orig = cv2.calcHist([g], [0], None, [256], [0, 255])
hist_eq = cv2.calcHist([g_eq], [0], None, [256], [0, 255])

zeros = np.zeros(g.shape, dtype=np.uint8)

g = cv2.merge((zeros, g, zeros))
g_eq = cv2.merge((zeros, g_eq, zeros))

fig, ax = plt.subplots(2, 2, figsize=(6, 6))

ax[0, 0].imshow(cv2.cvtColor(g, cv2.COLOR_BGR2RGB))
ax[0, 0].set_title('Original Image')
ax[0, 0].set_xticks([])
ax[0, 0].set_yticks([])
ax[0, 1].plot(hist_orig, color='green')
ax[0, 1].set_title('Histogram(Original)')
ax[0, 1].set_xlim([0, 255])

ax[1, 0].imshow(cv2.cvtColor(g_eq, cv2.COLOR_BGR2RGB))
ax[1, 0].set_title('Histogram Equalized Image')
ax[1, 0].set_xticks([])
ax[1, 0].set_yticks([])
ax[1, 1].plot(hist_eq, color='green')
ax[1, 1].set_title('Histogram(Equalized)')
ax[1, 1].set_xlim([0, 255])

plt.tight_layout()
plt.show()
