import cv2

webcam = cv2.VideoCapture(0)

while True:
    result, frame = webcam.read()

    if result is False:
        break

    frame = cv2.Canny(frame, 50, 150)

    cv2.imshow('Webcam Test', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
