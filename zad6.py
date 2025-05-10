import cv2
import numpy as np

img = cv2.imread("zdj2.jpg")

mask = np.zeros(img.shape[:2], dtype=np.uint8)

cv2.rectangle(mask, (215,200), (300,300), 255, -1)

blurred = cv2.GaussianBlur(img, (21, 21), 0)

result = np.where(mask[:, :, np.newaxis] == 255, img, blurred)

cv2.imshow("Original", img)
cv2.imshow("Mask", mask)
cv2.imshow("Result", result)
cv2.waitKey(0)
