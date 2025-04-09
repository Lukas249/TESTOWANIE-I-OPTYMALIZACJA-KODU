import cv2
import numpy as np

image1 = cv2.imread("zdj.jpg")

(B, G, R) = cv2.split(image1)

merged1 = cv2.merge([R, B, G])

cv2.imshow("RBG", merged1)

merged2 = cv2.merge([R, np.zeros(image1.shape[:2], dtype="uint8"), G])

cv2.imshow("R0G", merged2)

cv2.waitKey(0)
