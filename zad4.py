import cv2
import numpy as np
import imutils

img = cv2.imread("zdj.jpg")

(h, w) = img.shape[:2]

cv2.imshow("Oryginalny obraz", img)

M = np.float32([[1, 0, 100], [0, 1, 50]])

shifted = imutils.translate(img, 100, 50)
shifted2 = cv2.warpAffine(img, M, (w, h))

cv2.imshow("Po przesunieciu (imutils)", shifted)
cv2.imshow("Po przesunieciu (cv2.warpAffine)", shifted2)

cv2.waitKey(0)