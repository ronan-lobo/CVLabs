import cv2

img = cv2.imread('C:\\Users\\OSLAB\\PycharmProjects\\pythonProject\\CVLab\\Lab1\\image1.jpg')

cv2.imshow('original img', img)

row, col, chn = img.shape

img = cv2.resize(img, (int(col/2), int(row/2)))

cv2.imshow('resized img', img)

cv2.waitKey(0)

cv2.destroyAllWindows()
