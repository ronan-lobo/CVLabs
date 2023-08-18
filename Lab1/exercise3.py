import numpy as np
import cv2

img = cv2.imread('C:\\Users\\OSLAB\\PycharmProjects\\pythonProject\\CVLab\\Lab1\\image1.jpg')

img = np.array(img)

row, col, depth = img.shape
i, j = int(row/2), int(col/2)

print(f'RGB values at ({i}, {j})')
print(f'B: {img[i, j, 0]}')
print(f'G: {img[i, j, 1]}')
print(f'R: {img[i, j, 2]}')
