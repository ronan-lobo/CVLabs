import cv2


def on_change(value):
    ret, out_img = cv2.threshold(img, value, 255, cv2.THRESH_TOZERO)
    cv2.imshow(windowName, out_img)


img = cv2.imread('Resources\\eyesketch.jpg', 0)

windowName = 'image'

cv2.imshow(windowName, img)
cv2.createTrackbar('slider', windowName, 0, 255, on_change)

cv2.waitKey(0)
cv2.destroyAllWindows()
