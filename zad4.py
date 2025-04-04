import cv2
import numpy as np

image = cv2.imread("zdj.jpg")

cv2.imshow("Original", image)

M1 = np.zeros(image.shape, dtype="uint8")
M2 = np.zeros(image.shape, dtype="uint8")

M1[:, :, 0] = 10
M1[:, :, 2] = 30

M2[:, :, 1] = 20

imageFilter = cv2.add(image, M1)
imageFilter = cv2.subtract(imageFilter, M2)

cv2.imshow("After", imageFilter)

cv2.waitKey(0)