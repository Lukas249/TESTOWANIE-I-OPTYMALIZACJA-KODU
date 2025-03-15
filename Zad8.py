import cv2

image = cv2.imread("zdj.jpg")

(h, w) = image.shape[:2]

cv2.imshow("Before", image)

image[100, 0:w] = (0, 255, 0)

cv2.imshow("After", image)

cv2.waitKey(0)