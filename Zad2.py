import cv2

image = cv2.imread("zdj.jpg")

cv2.imshow("Before", image)

(h, w) = image.shape[:2]

image[h - 1, w - 1] = (0, 0, 255)

cv2.imshow("After", image)

cv2.waitKey(0)