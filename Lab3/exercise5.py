import numpy as np
import cv2


def non_max_suppression(magnitude, angles):
    r, c = magnitude.shape
    for i in range(1, r-1):
        for j in range(1, c-1):



def mycanny(image):
    image_np = np.array(image, dtype=np.float32)
    gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
    gaussian = cv2.GaussianBlur(gray, (3, 3), 0)
    sobel_x = cv2.Sobel(gaussian, -1, 1, 0)
    sobel_y = cv2.Sobel(gaussian, -1, 0, 1)
    magnitude = np.sqrt(np.power(sobel_x, 2) + np.power(sobel_y, 2))
    angles = np.arctan(np.divide(sobel_y, sobel_x))
    angles_quantized = np.round(angles * 4 / np.pi)




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
