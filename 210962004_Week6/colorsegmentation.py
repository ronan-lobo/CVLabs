import cv2
import numpy as np

cap = cv2.VideoCapture('Resources\\sample.mp4')

while cap.isOpened():
    ret, frame = cap.read()

    if ret is False:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([60, 35, 140])
    upper_blue = np.array([180, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
