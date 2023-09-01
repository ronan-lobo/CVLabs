import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('Resources/lena.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

fig, ax = plt.subplots(1, 5, figsize=(15, 4))
fig.suptitle('Gaussian Blurring at Various Kernel Sizes')

ax[0].imshow(image)
ax[0].set_xticks([])
ax[0].set_yticks([])
ax[0].set_title(f'Original Image')

for i in range(3, 10, 2):
    gaussian = cv2.GaussianBlur(image, (i, i), 0)
    ax[i//2].imshow(gaussian)
    ax[i//2].set_xticks([])
    ax[i//2].set_yticks([])
    ax[i//2].set_title(f'Kernel Size - ({i} {i})')

plt.tight_layout()
plt.savefig('Resources/gaussian_blurring.png')
plt.show()
