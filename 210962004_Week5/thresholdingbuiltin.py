import cv2
import matplotlib.pyplot as plt

image = cv2.imread('Resources/eyesketch.jpg', 0)

thresholds = [('Binary Thresholding', cv2.THRESH_BINARY),
              ('Binary Inverted Thresholding', cv2.THRESH_BINARY_INV),
              ('Truncated Thresholding', cv2.THRESH_TRUNC),
              ('Set to 0 Thresholding', cv2.THRESH_TOZERO),
              ('Set to 0 inverted Thresholding', cv2.THRESH_TOZERO_INV)]

plt.figure(figsize=(10, 10))

plt.subplot(2, 3, 1)
plt.imshow(image, cmap='gray')
plt.xticks([])
plt.yticks([])
plt.title('Original Image')

for i, (name, threshold) in enumerate(thresholds):
    ret, threshold_image = cv2.threshold(image, 127, 255, threshold)
    plt.subplot(2, 3, i + 2)
    plt.imshow(threshold_image, cmap='gray')
    plt.xticks([])
    plt.yticks([])
    plt.title(name)

plt.tight_layout()
plt.savefig('Resources/thresholdingbuiltin.png')
plt.show()
