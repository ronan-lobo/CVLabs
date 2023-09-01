import numpy as np
import cv2


def my_canny(image):
    image_np = np.array(image, dtype=np.float32)
    gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
    gaussian = cv2.GaussianBlur(gray, (3, 3), 0)
    sobel_x = cv2.Sobel(gaussian, -1, 1, 0)
    sobel_y = cv2.Sobel(gaussian, -1, 0, 1)
    print(sobel_x[:5, :5])
    print(sobel_y[:5, :5])
    magnitude = np.sqrt(np.power(sobel_x, 2) + np.power(sobel_y, 2))
    angles = np.arctan(np.divide(sobel_y, sobel_x))
    print(angles[:5, :5])
    angles_quantized = np.round(angles * 4 / np.pi)
    print(angles_quantized[:5, :5])


img = cv2.imread('Resources/house.webp')

my_canny(img)

cv2.destroyAllWindows()
