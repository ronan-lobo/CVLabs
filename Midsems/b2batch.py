import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

source_dir = 'Resources\\'

filenames = os.listdir('Resources')
n = len(filenames)

plt.figure(figsize=(8, 10))

for i, name in enumerate(filenames):
    im = cv2.imread(source_dir + name)

    gray_im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(gray_im, 127, 1, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    thresh = cv2.merge([thresh, thresh, thresh])

    output_im = cv2.multiply(im, thresh)

    plt.subplot(n, 2, i*2 + 1)
    plt.imshow(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
    plt.xticks([])
    plt.yticks([])
    plt.title('Original - ' + name)

    plt.subplot(n, 2, i*2 + 2)
    plt.imshow(cv2.cvtColor(output_im, cv2.COLOR_BGR2RGB))
    plt.xticks([])
    plt.yticks([])
    plt.title('Segmented - ' + name)

plt.savefig('Resources\\output.png')
plt.show()
