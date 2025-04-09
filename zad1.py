import cv2
import numpy as np

image = cv2.imread("osoba.jpg")

mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.circle(mask, (420, 100), 55, 255, -1)

result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Maska", mask)
cv2.imshow("Rezultat", result)
cv2.waitKey(0)