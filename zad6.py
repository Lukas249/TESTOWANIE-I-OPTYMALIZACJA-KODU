import cv2
import numpy as np

image = cv2.imread("opencv.png")

(B,G,R) = cv2.split(image)

merged1 = cv2.merge([R,G,B])

merged2 = cv2.merge([R, G, np.zeros(image.shape[:2], dtype="uint8")])

cv2.imshow("Original", image)
cv2.imshow("Logo RGB", merged1)
cv2.imshow("Logo RG0", merged2)

cv2.waitKey(0)
