import cv2
import numpy as np

image = cv2.imread("osoba.jpg")

mask = np.ones(image.shape[:2], dtype="uint8") * 255

cv2.rectangle(mask, (390, 90), (420, 100), 0, -1)
cv2.rectangle(mask, (420, 100), (450, 110), 0, -1)

result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Maska", mask)
cv2.imshow("Rezultat", result)
cv2.waitKey(0)