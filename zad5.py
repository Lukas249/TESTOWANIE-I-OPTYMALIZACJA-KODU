import cv2
import numpy as np

image = cv2.imread("car.jpg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_red1 = np.array([0, 30, 30])
upper_red1 = np.array([10, 255, 255])

lower_red2 = np.array([170, 30, 30])
upper_red2 = np.array([180, 255, 255])

mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

mask = cv2.bitwise_or(mask1, mask2)

result = cv2.bitwise_and(image, image, mask=mask)

result = cv2.add(result, np.array([0,0,255], dtype=np.uint8), mask=mask)

cv2.imshow("Image", image)
cv2.imshow("Maska", mask)
cv2.imshow("Result", result)
cv2.waitKey(0)
