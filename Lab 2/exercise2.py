import cv2
import numpy as np
import matplotlib.pyplot as plt

inp_img = cv2.imread('inp_image.webp', 0)
ref_img = cv2.imread('ref_image.webp', 0)

inp_hist = cv2.calcHist([inp_img], [0], None, [256], [0, 255])
ref_hist = cv2.calcHist([ref_img], [0], None, [256], [0, 255])

cv2.imshow('input image', inp_img)
cv2.imshow('reference image', ref_img)
cv2.waitKey(0)

cv2.destroyAllWindows()
