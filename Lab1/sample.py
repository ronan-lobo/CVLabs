import cv2

img = cv2.imread('C:\\Users\\OSLAB\\PycharmProjects\\pythonProject\\CVLab\\Lab1\\image1.jpg', 0)

cv2.imshow('image', img)

cv2.waitKey(0)

cv2.destroyAllWindows()

cv2.imwrite('C:\\Users\\OSLAB\\PycharmProjects\\pythonProject\\CVLab\\Lab1\\image2.jpg', img)
