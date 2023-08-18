import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('sample1.jpg')

B, G, R = cv2.split(img)

B_hist = np.histogram(np.array(B, dtype=np.uint8).ravel(), 255)[0]
G_hist = np.histogram(np.array(G, dtype=np.uint8).ravel(), 255)[0]
R_hist = np.histogram(np.array(R, dtype=np.uint8).ravel(), 255)[0]

fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

ax2.plot(B_hist, 'b', linewidth=1)
ax2.plot(G_hist, 'g', linewidth=1)
ax2.plot(R_hist, 'r', linewidth=1)
ax2.legend(['Blue', 'Green', 'Red'])
plt.show()
