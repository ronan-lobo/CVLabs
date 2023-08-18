import cv2

img = cv2.imread('C:\\Users\\OSLAB\\PycharmProjects\\pythonProject\\CVLab\\Lab1\\image1.jpg')

cv2.imshow('original img', img)

img = cv2.rotate(img, cv2.ROTATE_180)

cv2.imshow('rotated img', img)

cv2.waitKey(0)

cv2.destroyAllWindows()
