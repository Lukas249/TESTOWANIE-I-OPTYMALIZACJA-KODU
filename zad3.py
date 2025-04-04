import cv2
import numpy as np

image = cv2.imread("zdj.jpg")

cv2.imshow("Original", image)

M = np.ones(image.shape, dtype="uint8") * 80

lighter_cv2 = cv2.subtract(image, M)

lighter_np = image - M

cv2.imshow("Lighter (OpenCV)", lighter_cv2)

cv2.imshow("Lighter (NumPy)", lighter_np)

cv2.waitKey(0)
