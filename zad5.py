import imutils
import cv2

image = cv2.imread("zdj.jpg")
cv2.imshow("Original", image)

resized = imutils.resize(image, width=500)

cv2.imshow("Resized", resized)

cv2.waitKey(0)