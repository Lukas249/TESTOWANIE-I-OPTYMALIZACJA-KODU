import cv2
import numpy as np

img = cv2.imread("zdj.jpg")

(h, w) = img.shape[:2]

cv2.imshow("Oryginalny obraz", img)

M = np.float32([[1, 0, 30], [0, 1, 40]])

shifted = cv2.warpAffine(img, M, (w, h))

cv2.imshow("Po przesunieciu", shifted)

cv2.waitKey(0)