import cv2
import imutils

image = cv2.imread("zdj.jpg")

cv2.imshow("Przed", image)

rotated = imutils.rotate_bound(image, -33)

cv2.imshow("Po", rotated)

cv2.waitKey(0)