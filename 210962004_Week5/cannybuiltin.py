import cv2
import matplotlib.pyplot as plt

img = cv2.imread('Resources/house.webp')

canny = cv2.Canny(img, 100, 200)

plt.figure(figsize=(14, 4))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.xticks([])
plt.yticks([])
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(canny, cv2.COLOR_BGR2RGB))
plt.xticks([])
plt.yticks([])
plt.title('Edges Detected Using Canny Edge Detector')

plt.tight_layout()
plt.savefig('Resources/canny_edges.png')
plt.show()

