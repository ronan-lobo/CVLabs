import cv2

img = cv2.imread('ex1.jpg', 0)

cv2.imshow('input image', img)

img = cv2.equalizeHist(img)

cv2.imshow('histogram equalized image', img)
cv2.imwrite('histogram_equalized_ex1.jpg', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
