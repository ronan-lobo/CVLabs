import cv2

video = cv2.VideoCapture('C:\\Users\\OSLAB\\PycharmProjects\\pythonProject\\CVLab\\Lab1\\video1.webm')

while video.isOpened():
    ret, frame = video.read()
    if ret:
        cv2.imshow('Frame', frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

video.release()
cv2.destroyAllWindows()
